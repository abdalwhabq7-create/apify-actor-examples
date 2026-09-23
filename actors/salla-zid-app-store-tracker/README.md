# Salla & Zid App Store Tracker

<img src="icon.png" alt="" width="64" height="64">

Choose Salla or Zid app directories and export app names, categories, ratings and published pricing fields.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/salla-zid-app-store-tracker) · [All tools](../../README.md) · تطبيقات سلة وزد**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "platforms": [
    "salla"
  ],
  "maxAppsPerPlatform": 3,
  "includeCategories": false,
  "language": "en",
  "onlyChanges": false
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py salla-zid-app-store-tracker
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:25.617Z UTC, build `0.1.3`, run `N2F2CY4qyUPKpsnq9`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| platform | name | rating | pricingText | url |
| --- | --- | --- | --- | --- |
| salla | Ai Product Backgrounds | null | Start From 299 SAR / Monthly | https://apps.salla.sa/en/app/71684259 |
| salla | Thikaa Bot | null | 110 SAR / Monthly (Free Trial 7 Days) | https://apps.salla.sa/en/app/345824228 |

## Limits and pricing

Directory pages and pricing text can change. Not every app exposes a numeric price or rating.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/salla-zid-app-store-tracker) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
