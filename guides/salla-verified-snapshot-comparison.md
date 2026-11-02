# Compare two complete Salla snapshots with a price threshold

The [Salla catalog Actor](https://apify.com/abdulwhab95/salla-catalog-scraper) already supports `onlyChanges`, previous prices and stock changes. Use the [existing monitoring guide](salla-daily-price-stock-monitor.md) when that is enough.

Use this workflow when you have **two complete snapshots of the same store** and want [Dataset Change Detector](https://apify.com/abdulwhab95/dataset-change-detector) to suppress small price-only changes, while keeping stock and currency changes. Both tools are maintained by this repository's developer. They are independent of Salla.

## 1. Obtain two eligible source runs

Run the Salla catalog Actor at two different times with the same single store input, `onlyChanges: false`, `onlyOnSale: false` and `emitRemoved: false`. Choose a product limit and spend ceiling appropriate for that store. This helper does **not** start or pay for those source runs.

The source report must show a full catalog read: `exhaustiveRead: true`, `truncated: false`, no unresolved stores, skipped or duplicate products, or spending-limit interruption. Its delivered and read counts must agree with the dataset. A run that merely says `SUCCEEDED` is insufficient.

This bounded example supports one nonempty store with at most **1,000 products and 5 MB of selected fields per snapshot**. It refuses larger datasets rather than silently truncating them. The three- and five-product demos elsewhere in this repository generally **do not qualify**: they intentionally sample a catalog. Do not raise their completeness flags manually.

Copy the two completed run IDs from Apify Console. Keep their inputs, reports and datasets unchanged. Use runs you own or are authorized to read. The current run must start after the previous one finishes.

## 2. Verify and prepare, without starting an Actor

Set `APIFY_TOKEN` as described in the [Python setup](../README.md#run-an-example), then run from the repository root. Replace the two uppercase placeholders with the actual 17-character IDs:

```sh
python salla_compare.py PREVIOUS_RUN_ID CURRENT_RUN_ID --threshold 5
```

The helper reads the source runs' metadata, `INPUT`, `RUN_REPORT` and full datasets through the Apify API. It checks source identity, unfiltered coverage, stable dataset metadata, counts, keys and matching store scope. It saves a prepared `.input.json` under ignored `results/`. No Actor starts in this mode. API reads/storage can still count toward platform usage.

Only `store`, `productId`, `price`, `currency`, `isAvailable` and `isOutOfStock` are copied. The generated input embeds the verified rows; later edits to a remote dataset cannot change what that comparison receives. These are consistency checks on the Actor's report, **not an independent audit of the source website**.

## 3. Optionally execute the existing detector

Review the generated input and the detector's [live pricing](https://apify.com/abdulwhab95/dataset-change-detector/pricing). To start exactly one detector run, repeat the command with `--run` and a charge ceiling you choose:

```sh
python salla_compare.py PREVIOUS_RUN_ID CURRENT_RUN_ID --threshold 5 --run --max-charge 0.10
```

This uses the existing client runner's 180-second Actor timeout and approximately five-minute client wait. A lost start response is **not retried automatically**; inspect Console before starting another run. The charge ceiling follows Apify's billing semantics and is separate from the costs of the two source runs. A ceiling of $0.10 is a safety choice, not a promise that every comparison fits that amount.

The script saves the comparison report with its unique run ID. It writes `.changes.json` only when the report confirms every selected change was delivered and downloaded. A spend-limited or otherwise partial comparison fails clearly; it does not become an alert feed. Previously successful result files have different run IDs.

## What the results mean

- `NEW`: a product exists in the current snapshot but not the previous one.
- `UPDATED`: a watched price, currency or stock field changed. A 5% threshold suppresses price-only movement below 5% relative to the previous price. It is not a cumulative threshold across many runs.
- Stock or currency changes still pass the filter. Unknown or zero prior prices are handled conservatively by the detector.
- Zero delivered rows, with a complete successful report and zero selected changes, is a valid quiet result.
- Removal events are deliberately disabled in this small example. It does not report products missing from the current snapshot.

No saved baseline, schedule, notification or store-price modification is created. For a daily sampled monitor, prefer Salla's built-in `onlyChanges` workflow. For this complete-snapshot workflow, reuse the helper only after the two source runs finish; do not point it at a run still writing data.

## Verification

The helper is covered by offline tests for complete matching snapshots, capped/filtered/partial runs, mismatched counts and scopes, duplicate or missing keys, changing datasets, invalid identifiers and partial comparison output. These tests do not claim a new live full-catalog comparison. Existing source and detector implementations were inspected at Salla build `0.1.10` and detector build `1.0.7` when this guide was written.

On 3 November 2026, two live catalog samples each reached their 1,000-product cap with `exhaustiveRead: false`, despite the Actor runs succeeding. The helper was run against the capped output and rejected it. No full-catalog comparison or notification was produced from these samples. Use an eligible complete snapshot to exercise the comparison end to end.

API references: [run metadata](https://docs.apify.com/api/v2/actor-run-get), [dataset metadata](https://docs.apify.com/api/v2/dataset-get), [dataset items](https://docs.apify.com/api/v2/dataset-items-get).

## بالعربي

هذا المثال يقارن تشغيلين كاملين لنفس متجر سلة، ويستبعد تغيّر السعر الأقل من النسبة اللي تختارها. يرفض العينة الناقصة حتى لو التشغيل ناجح. بدون `--run` يفحص ويجهّز ملف الإدخال فقط؛ ومعه يشغّل أداة المقارنة المدفوعة بحد تكلفة. النتيجة الفارغة صحيحة إذا تقرير المقارنة يؤكد اكتمالها. ما يفعّل جدول أو تنبيهات تلقائيًا.
