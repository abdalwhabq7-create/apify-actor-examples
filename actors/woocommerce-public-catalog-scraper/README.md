# WooCommerce Public Catalog — Prices & Stock

<img src="icon.png" alt="" width="64" height="64">

Give a WooCommerce store URL and export public Store API products with prices, currency and stock status.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/woocommerce-public-catalog-scraper) · [All tools](../../README.md) · منتجات WooCommerce**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "storeUrls": [
    "https://scrapeme.live/shop/"
  ],
  "maxResults": 3,
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py woocommerce-public-catalog-scraper
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:09.592Z UTC, build `1.0.6`, run `2MJIKVeXRgcRzqHey`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| name | price | currency | inStock | url |
| --- | --- | --- | --- | --- |
| Blacephalon | 149 | GBP | True | https://scrapeme.live/shop/Blacephalon/ |
| Stakataka | 190 | GBP | True | https://scrapeme.live/shop/Stakataka/ |

## Limits and pricing

Requires an accessible public WooCommerce Store API. It does not access private merchant data.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/woocommerce-public-catalog-scraper) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
