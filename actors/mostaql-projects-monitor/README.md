# Mostaql Projects Monitor

<img src="icon.png" alt="" width="64" height="64">

Read public Mostaql project listings and export titles, skills, budgets and project links.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/mostaql-projects-monitor) · [All tools](../../README.md) · مشاريع مستقل**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "maxProjects": 3,
  "minBudget": 25,
  "categories": [],
  "skills": [],
  "keywords": [],
  "maxPages": 5,
  "onlyNew": false
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py mostaql-projects-monitor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:38.807Z UTC, build `0.1.2`, run `ruJC5Hn6KrftNjvEV`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| title | budgetMin | budgetMax | currency | url |
| --- | --- | --- | --- | --- |
| إنتاج فيديوهات قصيرة (YouTube Shorts / Reels) مخصصة لأغاني ومحتوى الأطفال | 250 | 500 | USD | https://mostaql.com/project/1280013 |
| مطلوب خبير نشر علمي لمجلة سكوبس (Scopus) في تخصص تقويم الأسنان | 250 | 500 | USD | https://mostaql.com/project/1280004 |

## Limits and pricing

Listings and budgets change. This tool does not submit proposals or obtain client contact information.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/mostaql-projects-monitor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
