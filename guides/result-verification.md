# Verify results before using them

The client starts one run and never automatically retries the paid start request. If submission times out, check Apify Console before starting another.

A platform status of SUCCEEDED means the Actor process completed. It does not establish complete source coverage. The updated runner downloads RUN_REPORT when available and saves a sibling .report.json file. PARTIAL, FAILED, LIMIT_REACHED or missing/unknown reports are warnings. Missing reports are marked UNVERIFIED, not inferred successful.

Downloads are capped at 1,000 rows. mayBeTruncated=true at the cap means more data may exist; export the full dataset using Apify Console or the documented pagination API. A missing optional report returns UNVERIFIED only for HTTP 404; authentication and service errors are not suppressed.

## Troubleshooting

1. Compare platform status, RUN_REPORT and row count. Inspect the run log in your own account; do not post credentials or customer records publicly.
2. For zero rows: check filters, source availability, limits and change-only state. A first-run baseline and an unchanged repeat can legitimately produce different counts.
3. For blocked sources: stop. Confirm permission and current site terms; do not bypass login, robots restrictions, CAPTCHA or rate limits.
4. For monitors: keep a separate named state store per configuration and avoid overlapping runs. No schedule is created by this repository.
5. For billing: review live Store prices and the Maximum cost per run setting. A client timeout is not a remote abort. Inspect Console before manually cancelling or retrying.

Inputs/results may contain sensitive information. Keep result files private, follow the original source license and attribution, and delete retained stores when no longer needed. Treat untrusted spreadsheet values as text.

This is a shared client/documentation upgrade for the existing public catalog, not a claim that every hosted implementation was changed or freshly crawled.
