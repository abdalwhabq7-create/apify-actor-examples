# GitHub Release Monitor — Versions & Asset Downloads

<img src="icon.png" alt="" width="64" height="64">

Give public owner/repository names and export release tags, dates and asset download counts.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/github-release-change-monitor) · [All tools](../../README.md) · إصدارات GitHub**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "repositories": [
    "psf/requests"
  ],
  "maxResults": 3,
  "maxPages": 1,
  "includePrereleases": false,
  "maxRequests": 100,
  "onlyChanges": false
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py github-release-change-monitor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:54:09.028Z UTC, build `1.0.2`, run `6044kkkc5xcQ0gFRz`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| repository | tag | publishedAt | totalAssetDownloads | url |
| --- | --- | --- | --- | --- |
| psf/requests | v2.34.2 | 2026-05-14T19:27:15Z | 959 | https://github.com/psf/requests/releases/tag/v2.34.2 |
| psf/requests | v2.34.1 | 2026-05-13T19:23:51Z | 129 | https://github.com/psf/requests/releases/tag/v2.34.1 |

## Limits and pricing

Public GitHub API rate limits apply. Asset downloads are not repository clone counts.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/github-release-change-monitor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
