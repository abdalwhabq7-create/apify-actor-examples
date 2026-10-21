# Greenhouse, Lever & Ashby Jobs API

[Hosted tool](https://apify.com/abdulwhab95/greenhouse-lever-ashby-jobs)

Provide exact public job-board URLs and optionally filter by title keywords and location. Exact URLs are preferable to guessed company names. Full descriptions are off by default; keep limits low for your first test. Only use sources and data you have permission to process.

The attached input is illustrative and was not freshly executed during the 2026-10-21 release. This page closes a catalog omission; it does not announce a new Actor or a runtime rewrite. Do not treat absence of a RUN_REPORT as proof of complete output.

Run: `python run.py greenhouse-lever-ashby-jobs --max-charge 0.10`

See [result verification and troubleshooting](../../guides/result-verification.md).

## Result checks (2026-10-21 client update)

The shared Python runner now saves a separate run report and warns about partial/unknown quality and the 1,000-row download cap. See [result verification](../../guides/result-verification.md). This documentation/client update alone does not imply a new hosted implementation or a fresh live-source test.
