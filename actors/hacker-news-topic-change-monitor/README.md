# Hacker News Topic Monitor — Stories & Engagement

<img src="icon.png" alt="" width="64" height="64">

Give a keyword and export matching Hacker News stories, links, points and comment counts.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/hacker-news-topic-change-monitor) · [All tools](../../README.md) · مواضيع Hacker News**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "query": "automation",
  "sortBy": "relevance",
  "maxResults": 3,
  "maxPages": 1,
  "minPoints": 0,
  "minComments": 0,
  "maxRequests": 100,
  "onlyChanges": false
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py hacker-news-topic-change-monitor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:54:19.973Z UTC, build `1.0.2`, run `riOPgetgm5UngqK9k`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| title | points | comments | discussionUrl |
| --- | --- | --- | --- |
| Open-Source Home Automation | 869 | 231 | https://news.ycombinator.com/item?id=21665125 |
| Do-nothing scripting: the key to gradual automation (2019) | 804 | 230 | https://news.ycombinator.com/item?id=29083367 |

## Limits and pricing

Relevance searches may return older stories. It does not post comments or promote products on Hacker News.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/hacker-news-topic-change-monitor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
