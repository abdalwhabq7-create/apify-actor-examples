# Product JSON-LD & Structured Data Auditor

<img src="icon.png" alt="" width="64" height="64">

Give product page URLs and get JSON-LD syntax and Product offer diagnostics with structured issue codes.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/product-jsonld-schema-auditor) · [All tools](../../README.md) · فحص JSON-LD**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "urls": [
    "https://oav.zid.store/products/jade"
  ],
  "maxResults": 3,
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py product-jsonld-schema-auditor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:54.413Z UTC, build `1.0.5`, run `CghhGLE2KztuQydzb`. 1 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| url | validJsonLd | scriptCount | entityCount | types |
| --- | --- | --- | --- | --- |
| https://oav.zid.store/products/jade | True | 3 | 4 | ["BreadcrumbList", "Organization", "Product", "WebSite"] |

## Limits and pricing

An audit result may report missing or invalid markup. It does not guarantee Google rich-result eligibility.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/product-jsonld-schema-auditor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
