import copy
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import salla_compare


def source():
    return {
        'run': {'id': 'A' * 17, 'actId': salla_compare.SALLA_ID, 'status': 'SUCCEEDED',
                'startedAt': '2026-11-01T10:00:00Z', 'finishedAt': '2026-11-01T10:01:00Z',
                'defaultDatasetId': 'D' * 17, 'defaultKeyValueStoreId': 'K' * 17},
        'input': {'stores': ['salla.sa/example'], 'onlyChanges': False, 'onlyOnSale': False},
        'report': {'items': 1, 'storesTried': 1, 'storesReached': 1, 'unresolved': [],
                   'skippedProducts': 0, 'stoppedAtSpendingLimit': False,
                   'stores': [{'store': 'salla.sa/example', 'identifier': 'example',
                               'products': 1, 'duplicateProducts': 0, 'truncated': False,
                               'exhaustiveRead': True, 'catalog': {'productsRead': 1}}]},
        'dataset': {'itemCount': 1, 'modifiedAt': '2026-11-01T10:00:59Z'},
        'rows': [{'store': 'example', 'productId': 123, 'price': 10, 'currency': 'SAR',
                  'isAvailable': True, 'isOutOfStock': False}],
    }


class SallaCompareTests(unittest.TestCase):
    def test_complete_matching_snapshots_keep_salla_keys_and_price_stock_fields(self):
        old = source()
        new = source()
        new['run'].update(id='B' * 17, startedAt='2026-11-02T10:00:00Z',
                          finishedAt='2026-11-02T10:01:00Z')
        new['rows'][0]['price'] = 12
        before = salla_compare.validate_snapshot(**old)
        after = salla_compare.validate_snapshot(**new)
        data = salla_compare.comparison_input(before, after, 5)
        self.assertEqual(data['keyFields'], ['store', 'productId'])
        self.assertEqual(data['stockFields'], ['isAvailable', 'isOutOfStock'])
        self.assertEqual(data['previous'][0]['price'], 10)
        self.assertEqual(data['current'][0]['price'], 12)
        self.assertEqual(data['maxResults'], 1)
        self.assertFalse(data['allowRemoved'])
        self.assertNotIn('currentSnapshotComplete', data)

    def test_successful_capped_filtered_or_partial_run_is_rejected(self):
        variants = []
        for key in ('onlyChanges', 'onlyOnSale'):
            item = source(); item['input'][key] = True; variants.append(item)
        for key, value in [('exhaustiveRead', False), ('truncated', True), ('duplicateProducts', 1)]:
            item = source(); item['report']['stores'][0][key] = value; variants.append(item)
        for key, value in [('unresolved', ['other']), ('skippedProducts', 1),
                           ('stoppedAtSpendingLimit', True), ('items', 2)]:
            item = source(); item['report'][key] = value; variants.append(item)
        item = source(); del item['report']['stoppedAtSpendingLimit']; variants.append(item)
        for item in variants:
            with self.subTest(item=item), self.assertRaises(ValueError):
                salla_compare.validate_snapshot(**item)

    def test_rejects_wrong_actor_count_duplicates_and_missing_fields(self):
        variants = []
        item = source(); item['run']['actId'] = 'other'; variants.append(item)
        item = source(); item['dataset']['itemCount'] = 2; variants.append(item)
        item = source(); item['rows'] *= 2; variants.append(item)
        item = source(); del item['rows'][0]['productId']; variants.append(item)
        item = source(); item['rows'][0]['productId'] = None; variants.append(item)
        item = source(); item['rows'][0]['price'] = float('nan'); variants.append(item)
        for item in variants:
            with self.subTest(item=item), self.assertRaises(ValueError):
                salla_compare.validate_snapshot(**item)

    def test_rejects_scope_change_overlapping_runs_and_bad_threshold(self):
        old = salla_compare.validate_snapshot(**source())
        changed = copy.deepcopy(old); changed['scope'] = ('other', 'other', 'other')
        changed['startedAt'] = '2026-11-02T10:00:00+00:00'
        with self.assertRaisesRegex(ValueError, 'scope'):
            salla_compare.comparison_input(old, changed, 5)
        with self.assertRaisesRegex(ValueError, 'later'):
            salla_compare.comparison_input(old, old, 5)
        for value in (-1, float('nan'), float('inf')):
            with self.assertRaises(ValueError):
                salla_compare.comparison_input(old, changed, value)

    def test_read_rejects_dataset_changed_during_download(self):
        item = source()
        responses = [item['run'], item['input'], item['report'], item['dataset'],
                     item['rows'], {**item['dataset'], 'modifiedAt': '2026-11-02T00:00:00Z'}]
        with patch.object(salla_compare, 'request', side_effect=responses):
            with self.assertRaisesRegex(ValueError, 'changed'):
                salla_compare.load_snapshot('A' * 17, 'test-token')

    def test_no_changes_is_a_complete_result_but_charge_cutoff_is_not(self):
        result = {'runReport': {'status': 'SUCCEEDED', 'results': 0,
                               'selectedChangeCount': 0, 'errors': [], 'limitReached': False}}
        salla_compare.check_comparison(result, [])
        result['runReport']['selectedChangeCount'] = 1
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            salla_compare.check_comparison(result, [])

    def test_bad_ids_fail_before_network(self):
        with patch.object(salla_compare, 'request') as api:
            for run_id in ('../private', 'https://example.com', 'A' * 16):
                with self.assertRaises(ValueError):
                    salla_compare.load_snapshot(run_id, 'test-token')
        api.assert_not_called()

    def test_default_cli_only_prepares_verified_input_without_paid_run(self):
        before = salla_compare.validate_snapshot(**source())
        after = copy.deepcopy(before)
        after.update(runId='B' * 17, startedAt='2026-11-02T10:00:00+00:00',
                     finishedAt='2026-11-02T10:01:00+00:00')
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(salla_compare, 'ROOT', Path(directory)), \
                    patch.object(salla_compare, 'load_snapshot', side_effect=[before, after]), \
                    patch.object(salla_compare, 'run') as paid_run, \
                    patch('sys.argv', ['salla_compare.py', 'A' * 17, 'B' * 17]), \
                    contextlib.redirect_stdout(io.StringIO()):
                salla_compare.main()
            paid_run.assert_not_called()
            prepared = list((Path(directory) / 'results').glob('*.input.json'))
            self.assertEqual(len(prepared), 1)
            data = json.loads(prepared[0].read_text(encoding='utf-8'))
            self.assertEqual(data['previous'], data['current'])
            self.assertEqual(data['minPriceChangePercent'], 5)


if __name__ == '__main__':
    unittest.main()
