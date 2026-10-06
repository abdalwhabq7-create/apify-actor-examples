# Salla Store Catalog & Price Scraper

<img src="icon.png" alt="" width="64" height="64">

Give a Salla store URL and export product prices, availability and identifiers. Use the data for catalog analysis or price monitoring.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/salla-catalog-scraper) · [All tools](../../README.md) · منتجات سلة**

**[Practical guide: monitor prices and stock daily](../../guides/salla-daily-price-stock-monitor.md)** — keep a baseline, understand empty change output, and schedule a tested configuration.

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "stores": [
    "salla.sa/coffee_souq",
    "otor200sa.com"
  ],
  "maxProductsPerStore": 3,
  "onlyChanges": false,
  "onlyOnSale": false,
  "includeEndedDiscounts": false,
  "requestDelayMs": 200,
  "respectRobots": true
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py salla-catalog-scraper
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:03.613Z UTC, build `0.1.8`, run `kYIFgUru6yeHEShlZ`. 6 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| name | price | currency | isAvailable | productUrl |
| --- | --- | --- | --- | --- |
| قهوة اوثا مورينا البرازيل مجففة | 41.74 | SAR | True | https://coffeesouq1.com/oZOQwNv |
| قمع قهوة MHW-3BOMBER Meteorite – قاعدة مسطّحة بزاوية 73° | 125 | SAR | True | https://coffeesouq1.com/qGYYvqZ |

## Limits and pricing

Store access and available fields vary. Change monitoring needs saved state and repeated scheduled runs.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/salla-catalog-scraper) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
