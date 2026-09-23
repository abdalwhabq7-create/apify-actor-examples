# Website Screenshots & Visual Changes — Static HTML

<img src="icon.png" alt="" width="64" height="64">

Give static page URLs and viewport dimensions to capture screenshots and compare later captures against a saved baseline.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/static-website-visual-change-monitor) · [All tools](../../README.md) · صور صفحات المواقع**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "urls": [
    "https://example.com"
  ],
  "width": 1280,
  "height": 800,
  "maxResults": 3,
  "pixelThreshold": 20,
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py static-website-visual-change-monitor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:54:00.190Z UTC, build `1.0.6`, run `8mkAtvF6QxfMJLuY2`. 1 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| url | width | height | comparison | renderMode |
| --- | --- | --- | --- | --- |
| https://example.com | 1280 | 800 | no-baseline | static-html-javascript-disabled |

## Limits and pricing

JavaScript is disabled. The first capture has no comparison baseline; this is not full browser testing of interactive applications.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/static-website-visual-change-monitor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
