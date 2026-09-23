# Website to Markdown — RAG Content & Change Feed

<img src="icon.png" alt="" width="64" height="64">

Give public page URLs and export clean Markdown with content hashes and source URLs for document or RAG pipelines.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/website-markdown-change-feed) · [All tools](../../README.md) · المواقع إلى Markdown**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "urls": [
    "https://docs.python.org/3/library/json.html"
  ],
  "maxResults": 1,
  "maxPages": 1,
  "crawlLinks": false,
  "onlyChanges": false,
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py website-markdown-change-feed
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:48.211Z UTC, build `1.0.5`, run `sPr26oMmQD55OM0LH`. 1 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| url | title | language | wordCount |
| --- | --- | --- | --- |
| https://docs.python.org/3/library/json.html | json — JSON encoder and decoder — Python 3.14.7 documentation | en | 4375 |

## Limits and pricing

Static HTML extraction; it does not run a website application or supply an LLM answer.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/website-markdown-change-feed) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
