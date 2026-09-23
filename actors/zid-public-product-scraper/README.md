# Zid Product Scraper — Arabic Prices & Availability

<img src="icon.png" alt="" width="64" height="64">

Give Zid product or catalog URLs and extract Product JSON-LD into product names, prices, currency and stock fields.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/zid-public-product-scraper) · [All tools](../../README.md) · صفحات منتجات زد**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "urls": [
    "https://oav.zid.store/products/jade"
  ],
  "discoverProducts": false,
  "maxPages": 3,
  "maxResults": 3,
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py zid-public-product-scraper
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:17.489Z UTC, build `1.0.2`, run `bH8d214jA8OuOufdc`. 1 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| name | price | currency | inStock | url |
| --- | --- | --- | --- | --- |
| Jade  | 490 | SAR | True | https://oav.zid.store/products/jade |

## Limits and pricing

Requires Product JSON-LD on accessible pages. This page-oriented tool is separate from the sitemap-based Zid catalog tool.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/zid-public-product-scraper) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
