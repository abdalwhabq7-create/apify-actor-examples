# RSS & Atom Feed Aggregator — New or Updated Items

<img src="icon.png" alt="" width="64" height="64">

Give RSS or Atom feed URLs and export deduplicated items with titles, dates and links.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/rss-atom-new-items-feed) · [All tools](../../README.md) · تغذيات RSS وAtom**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "feedUrls": [
    "https://feeds.bbci.co.uk/news/rss.xml"
  ],
  "maxResults": 3,
  "onlyChanges": false,
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py rss-atom-new-items-feed
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:54:03.523Z UTC, build `1.0.4`, run `cC8MvN0La3UZrMdxH`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| title | url | publishedAt | sourceFeed |
| --- | --- | --- | --- |
| Blood tests find high level of cancer-causing forever chemical in residents near factory | https://www.bbc.co.uk/news/articles/cjly4rv0q3l0o?at_medium=RSS&at_campaign=rss | 2026-09-23T21:01:06Z | https://feeds.bbci.co.uk/news/rss.xml |
| UK military jamming other nations' satellites to defend itself, BBC told | https://www.bbc.co.uk/news/articles/c32l8y8kygdvo?at_medium=RSS&at_campaign=rss | 2026-09-23T17:01:11Z | https://feeds.bbci.co.uk/news/rss.xml |

## Limits and pricing

A feed may contain only recent items. Scheduling is configured separately; the Actor is not always running.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/rss-atom-new-items-feed) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
