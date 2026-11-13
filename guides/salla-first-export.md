# Your first Salla catalog export

Start with one store and five products. Check the output before expanding the run or scheduling it.

**[Open Salla Store Catalog & Price Scraper](https://apify.com/abdulwhab95/salla-catalog-scraper)** � [Current pricing](https://apify.com/abdulwhab95/salla-catalog-scraper/pricing)

## 1. Choose a public store

Use a Salla store you are permitted to access. The example below uses a public demo source; it is not an endorsement or a promise that the source will always be available.

In Apify Console, open the Actor's JSON input editor and paste:

```json
{
  "stores": ["salla.sa/coffee_souq"],
  "maxProductsPerStore": 5,
  "onlyChanges": false,
  "onlyOnSale": false,
  "includeEndedDiscounts": false,
  "requestDelayMs": 200,
  "respectRobots": true
}
```

Review the current price and set a maximum cost and timeout before starting. This is a paid hosted tool. An Apify account is required; no source-store API key is needed for this public-source example.

## 2. Inspect the result

Open the run's Dataset. Compare a few returned products against their source pages:

- `productUrl` and `name`: is this the intended product?
- `price`, `regularPrice` and `currency`: does the source page agree?
- `isAvailable` and `isOutOfStock`: are they consistent with what the source displays?

Prices can change between extraction and inspection. Treat missing or unclear fields as unknown, not as proof that a product is free or available.

Download JSON for nested fields or CSV for spreadsheet review.

## 3. Check coverage before using the data

A successful run or five returned rows is not proof of a complete catalog. Open the run's key-value store and inspect `RUN_REPORT`, including unresolved stores, skipped products, spending-limit status and each store's `exhaustiveRead`.

- **No rows:** check the report and source access. Do not assume the shop has no products.
- **Only five rows:** expected for this sample. Do not report missing products as removed.
- **More coverage needed:** review the source size and costs before raising the product limit, then verify `exhaustiveRead` rather than relying on the limit alone.

## Choose your next step

| Goal | Guide |
|---|---|
| Export a small catalog sample | [Actor example and dated output](../actors/salla-catalog-scraper/README.md) |
| Track sampled price or stock changes | [Saved-baseline monitoring](salla-daily-price-stock-monitor.md) |
| Compare complete snapshots | [Coverage-checked snapshot comparison](salla-verified-snapshot-comparison.md) |
| Understand partial or capped downloads | [Result verification](result-verification.md) |

## Verification and support

This walkthrough is documentation, not a claim of a new live test. The linked examples state their original test dates and limits. Source behavior and pricing can change.

Published by the Actor's developer; this is an independent tool, not an official Salla service. For help, use the Actor's Apify support page with the run ID and a description of the issue. Never post tokens, private data or account credentials.

