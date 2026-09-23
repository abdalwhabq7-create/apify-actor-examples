# Crossref Research Monitor — DOI, Journals & Citations

<img src="icon.png" alt="" width="64" height="64">

Give a research query and export DOI metadata, publication titles, dates and citation counts.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/crossref-research-doi-monitor) · [All tools](../../README.md) · أبحاث Crossref**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "query": "machine learning",
  "maxResults": 3,
  "maxPages": 1,
  "workType": "any",
  "maxRequests": 100,
  "onlyChanges": false
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py crossref-research-doi-monitor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:54:21.252Z UTC, build `1.0.1`, run `mcX7QTHqO6mVn93Cq`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| doi | title | publishedDate | citationCount | url |
| --- | --- | --- | --- | --- |
| 10.1067/msy.2099.99951b | Learning sentinel node biopsy: Results of a prospective randomized trial of two techniques | 1999-10 | 5 | https://doi.org/10.1067/msy.2099.99951b |
| 10.1067/men.2001.113061 | ED learning units: An innovative teaching method | 2001-04 | 1 | https://doi.org/10.1067/men.2001.113061 |

## Limits and pricing

Metadata only, not full-text papers. Search relevance and citation coverage depend on Crossref.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/crossref-research-doi-monitor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
