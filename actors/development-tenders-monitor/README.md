# Development Project Tenders & Procurement Notices Monitor

<img src="icon.png" alt="" width="64" height="64">

Filter World Bank procurement notices by country, time or keyword and export titles, notice types, deadlines and source links.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/development-tenders-monitor) · [All tools](../../README.md) · مناقصات البنك الدولي**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "countryCodes": [],
  "daysBack": 30,
  "maxResults": 3,
  "onlyNew": false,
  "includeDescription": true
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py development-tenders-monitor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:41.136Z UTC, build `0.1.2`, run `jkKpr5bmt6GXQfptx`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| title | country | noticeType | deadline | url |
| --- | --- | --- | --- | --- |
| Hiring of an Environmental Specialist | Liberia | Request for Expression of Interest | 2026-10-02T04:00 | https://projects.worldbank.org/en/projects-operations/procurement-detail/OP00423255 |
| Rebidding- Construction of 120 mtr. Span Pedestrian Bridge over Mainagaad in Pipalkoti-Math-Syun-Bemru Bridle road district Chamol | India | Contract Award | null | https://projects.worldbank.org/en/projects-operations/procurement-detail/OP00470191 |

## Limits and pricing

Source: World Bank Procurement Notices, CC BY 4.0. Not affiliated with the World Bank. Check the original notice before making a bid.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/development-tenders-monitor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
