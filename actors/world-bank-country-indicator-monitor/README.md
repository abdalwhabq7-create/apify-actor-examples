# World Bank Indicators — Country Data & Revisions

<img src="icon.png" alt="" width="64" height="64">

Give country and indicator codes plus years and export annual values with source attribution.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/world-bank-country-indicator-monitor) · [All tools](../../README.md) · مؤشرات البنك الدولي**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "countries": [
    "KW"
  ],
  "indicators": [
    "NY.GDP.MKTP.CD"
  ],
  "startYear": 2023,
  "endYear": 2024,
  "maxResults": 3,
  "maxPages": 1,
  "onlyChanges": false,
  "includeMissing": false,
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py world-bank-country-indicator-monitor
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:56:07.637Z UTC, build `1.0.1`, run `NoxRMLiWkcyX0U9Q8`. 2 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| country | indicator | year | value | source | license |
| --- | --- | --- | --- | --- | --- |
| Kuwait | GDP (current US$) | 2024 | 160903106639.233 | World Bank, World Development Indicators | CC BY 4.0 |
| Kuwait | GDP (current US$) | 2023 | 165462656226.772 | World Bank, World Development Indicators | CC BY 4.0 |

## Limits and pricing

Source: World Bank World Development Indicators. Follow the source license supplied with each series; this is not real-time economic data.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/world-bank-country-indicator-monitor) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
