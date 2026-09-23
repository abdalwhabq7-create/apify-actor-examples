# YouCan Store Catalog & Price Scraper

<img src="icon.png" alt="" width="64" height="64">

Give a YouCan store URL and export its public product feed, including prices and available variant metadata.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/youcan-store-catalog-scraper) · [All tools](../../README.md) · منتجات YouCan**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "stores": [
    "https://youcan.supply"
  ],
  "maxProductsPerStore": 1,
  "onlyOnSale": false,
  "includeVariants": false,
  "includeVariantStock": false,
  "onlyChanges": false
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py youcan-store-catalog-scraper
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:20.014Z UTC, build `0.1.8`, run `KDCwvUSgBGSh8Kw6O`. 1 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| name | price | currency | hasVariants | productUrl |
| --- | --- | --- | --- | --- |
| NO TIME TO WASTE T-SHIRT | 249 | MAD | True | https://youcan.supply/products/no-time-to-waste |

## Limits and pricing

Variant and inventory details depend on what the store publishes; missing stock is not proof that a product is out of stock.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/youcan-store-catalog-scraper) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
