# PDF Tables & Text to JSON and CSV

<img src="icon.png" alt="" width="64" height="64">

Give public text-based PDF URLs and export page text, table arrays and CSV strings.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/pdf-tables-text-to-json-csv) · [All tools](../../README.md) · جداول ونصوص PDF**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "urls": [
    "https://www.irs.gov/pub/irs-pdf/f1040.pdf"
  ],
  "startPage": 2,
  "maxPagesPerPdf": 1,
  "maxResults": 1,
  "tableStrategy": "lines",
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py pdf-tables-text-to-json-csv
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:57.767Z UTC, build `1.0.5`, run `wct6fSpqVc8ZAQF2C`. 1 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| url | page | documentPages | tableCount |
| --- | --- | --- | --- |
| https://www.irs.gov/pub/irs-pdf/f1040.pdf | 2 | 2 | 6 |

## Limits and pricing

No OCR: scanned image-only PDFs need a different workflow. Table quality depends on the document layout.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/pdf-tables-text-to-json-csv) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
