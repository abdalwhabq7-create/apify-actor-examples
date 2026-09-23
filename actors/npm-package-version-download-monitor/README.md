# npm Package Monitor — Versions, Downloads & Deprecation

<img src="icon.png" alt="" width="64" height="64">

Give npm package names and export versions, weekly download counts, licenses and deprecation metadata.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/npm-package-version-download-monitor) · [All tools](../../README.md) · إصدارات وتحميلات npm**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "packages": [
    "express",
    "apify"
  ],
  "maxResults": 3,
  "maxRequests": 100,
  "onlyChanges": false
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py npm-package-version-download-monitor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:54:14.233Z UTC, build `1.0.2`, run `sE54X6Oo4i1jwml8V`. 2 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| name | version | weeklyDownloads | license | url |
| --- | --- | --- | --- | --- |
| express | 5.2.1 | 101489586 | MIT | https://www.npmjs.com/package/express |
| apify | 3.7.2 | 38619 | Apache-2.0 | https://www.npmjs.com/package/apify |

## Limits and pricing

Download counts are not unique users. This tool does not install packages or perform a security audit.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/npm-package-version-download-monitor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
