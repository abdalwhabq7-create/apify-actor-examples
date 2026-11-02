"""Verify two complete Salla runs, then prepare an optional paid price/stock comparison."""
import argparse
import json
import math
import os
import re
import sys
from datetime import datetime, timezone

from run import ROOT, request, run

SALLA_ID = 'ABcDcvTPvTao7a6pV'
FIELDS = ['store', 'productId', 'price', 'currency', 'isAvailable', 'isOutOfStock']
MAX_ROWS = 1000


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if parsed.tzinfo is None:
            raise ValueError()
        return parsed.astimezone(timezone.utc).isoformat()
    except (ValueError, AttributeError, TypeError):
        raise ValueError('Source run needs valid start/finish timestamps with timezone.') from None


def validate_snapshot(run, input, report, dataset, rows):
    """Check the Salla 0.1.10 report contract, not just platform SUCCEEDED."""
    if any(not isinstance(x, dict) for x in (run, input, report, dataset)):
        raise ValueError('Source metadata, input or completion report is missing.')
    if run.get('actId') != SALLA_ID or run.get('status') != 'SUCCEEDED':
        raise ValueError('Source must be a successful run of the Salla catalog Actor.')
    stores = input.get('stores')
    if not isinstance(stores, list) or len(stores) != 1 or not isinstance(stores[0], str):
        raise ValueError('Use one store per comparison; multi-store snapshots are not supported here.')
    if any(input.get(k, False) is not False for k in ('onlyChanges', 'onlyOnSale', 'emitRemoved')):
        raise ValueError('Source must return the full unfiltered snapshot, not changes or sale-only rows.')
    if (report.get('unresolved') != [] or report.get('skippedProducts') != 0
            or report.get('stoppedAtSpendingLimit') is not False
            or report.get('storesTried') != 1 or report.get('storesReached') != 1):
        raise ValueError('Source coverage is incomplete or unverifiable; no comparison was prepared.')
    details = report.get('stores')
    if not isinstance(details, list) or len(details) != 1 or not isinstance(details[0], dict):
        raise ValueError('Source needs one complete per-store report.')
    store = details[0]
    if (store.get('store') != stores[0] or not store.get('identifier')
            or store.get('exhaustiveRead') is not True or store.get('truncated') is not False
            or store.get('duplicateProducts') != 0):
        raise ValueError('Source store is incomplete, capped or ambiguous; no comparison was prepared.')
    count = dataset.get('itemCount')
    if (type(count) is not int or not 1 <= count <= MAX_ROWS or not isinstance(rows, list)
            or len(rows) != count or report.get('items') != count or store.get('products') != count
            or (store.get('catalog') or {}).get('productsRead') != count):
        raise ValueError('Source counts disagree, are empty, or exceed this example\'s 1,000-row limit.')
    checked = []
    keys = set()
    labels = set()
    for row in rows:
        if not isinstance(row, dict) or any(k not in row for k in FIELDS):
            raise ValueError('Source row is missing a product key or watched field.')
        if (not isinstance(row['store'], str) or not row['store']
                or type(row['productId']) not in (str, int) or not str(row['productId']).strip()):
            raise ValueError('Source row needs a store and a stable product ID.')
        key = (row['store'], type(row['productId']).__name__, row['productId'])
        if key in keys:
            raise ValueError('Duplicate product keys cannot define a complete comparison.')
        keys.add(key); labels.add(row['store'])
        checked.append({k: row[k] for k in FIELDS})
    if len(labels) != 1 or len(json.dumps(checked, allow_nan=False).encode()) > 5_000_000:
        raise ValueError('Source has ambiguous store labels or exceeds the 5 MB snapshot limit.')
    started = timestamp(run.get('startedAt')); finished = timestamp(run.get('finishedAt'))
    if finished < started:
        raise ValueError('Source finish timestamp precedes its start.')
    return {'runId': run['id'], 'startedAt': started, 'finishedAt': finished,
            'scope': (stores[0], str(store['identifier']), next(iter(labels))), 'rows': checked}


def load_snapshot(run_id, token):
    if not token or not re.fullmatch(r'[A-Za-z0-9]{17}', run_id):
        raise ValueError('Set APIFY_TOKEN and supply a 17-character Apify run ID, not a URL.')
    result = request('actor-runs/' + run_id, token)
    if result.get('actId') != SALLA_ID or result.get('status') != 'SUCCEEDED':
        raise ValueError('Source must be a successful run of the Salla catalog Actor.')
    kv = result.get('defaultKeyValueStoreId', ''); did = result.get('defaultDatasetId', '')
    if not all(re.fullmatch(r'[A-Za-z0-9]{17}', value) for value in (kv, did)):
        raise ValueError('Source run has no valid report store or dataset.')
    source_input = request('key-value-stores/' + kv + '/records/INPUT', token)
    report = request('key-value-stores/' + kv + '/records/RUN_REPORT', token)
    before = request('datasets/' + did, token)
    count = before.get('itemCount')
    if type(count) is not int or not 1 <= count <= MAX_ROWS:
        raise ValueError('Source dataset must contain 1–1,000 rows; it will never be truncated to fit.')
    rows = request('datasets/' + did + '/items', token, limit=count, clean='false')
    after = request('datasets/' + did, token)
    if (before.get('modifiedAt') is None or before.get('modifiedAt') != after.get('modifiedAt')
            or before.get('itemCount') != after.get('itemCount')):
        raise ValueError('Source dataset changed during download; keep completed snapshots unchanged.')
    return validate_snapshot(result, source_input, report, before, rows)


def comparison_input(previous, current, threshold):
    if not math.isfinite(threshold) or not 0 <= threshold <= 100000:
        raise ValueError('Price threshold must be a finite percentage from 0 to 100000.')
    if previous['scope'] != current['scope']:
        raise ValueError('Source scope changed; use the same store input, resolved ID and product labels.')
    if current['startedAt'] <= previous['finishedAt']:
        raise ValueError('Current snapshot must start later than the previous completed run.')
    # Embed verified rows: subsequent source dataset changes cannot affect the comparison.
    return {'previous': previous['rows'], 'current': current['rows'],
            'keyFields': ['store', 'productId'], 'compareFields': FIELDS[2:],
            'allowRemoved': False, 'maxResults': len(current['rows']),
            'minPriceChangePercent': threshold, 'onlyPriceOrStockChanges': True,
            'priceField': 'price', 'currencyField': 'currency',
            'stockFields': ['isAvailable', 'isOutOfStock']}


def check_comparison(result, rows):
    report = result.get('runReport') or {}
    if (report.get('status') != 'SUCCEEDED' or report.get('errors') != []
            or report.get('limitReached') is not False
            or report.get('results') != len(rows) or report.get('selectedChangeCount') != len(rows)):
        raise ValueError('Comparison is incomplete or unverified. Inspect its saved report; do not use it as an alert feed.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('previous_run'); parser.add_argument('current_run')
    parser.add_argument('--threshold', type=float, default=5, help='Minimum price-only change percentage.')
    parser.add_argument('--run', action='store_true', help='Start one paid detector run after verification.')
    parser.add_argument('--max-charge', type=float, default=0.10, help='Detector run charge ceiling; review live pricing.')
    args = parser.parse_args()
    token = os.environ.get('APIFY_TOKEN', '')
    previous = load_snapshot(args.previous_run, token)
    current = load_snapshot(args.current_run, token)
    data = comparison_input(previous, current, args.threshold)
    folder = ROOT / 'results'; folder.mkdir(exist_ok=True)
    name = 'salla-comparison-' + args.previous_run + '-' + args.current_run
    path = folder / (name + '.input.json')
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(f'Verified {len(previous["rows"])} previous / {len(current["rows"])} current products. Saved {path}')
    if not args.run:
        print('No Actor started. Review the input and live pricing, then add --run to compare.')
        return
    result, rows = run('dataset-change-detector', data, token, args.max_charge)
    name += '-' + result['id']
    (folder / (name + '.report.json')).write_text(json.dumps({
        'runId': result['id'], 'runReport': result.get('runReport'),
        'sourceRuns': [args.previous_run, args.current_run], 'rowsDownloaded': len(rows),
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    check_comparison(result, rows)
    output = folder / (name + '.changes.json')
    output.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Complete comparison: {len(rows)} changes. Saved {output}')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, RuntimeError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
