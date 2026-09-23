# ATS Job Feed — Greenhouse, Lever & Ashby Changes

<img src="icon.png" alt="" width="64" height="64">

Give public Greenhouse, Lever or Ashby board identifiers and export jobs in a common schema.

**[Open the Actor on Apify](https://apify.com/abdulwhab95/public-ats-jobs-change-feed) · [All tools](../../README.md) · وظائف ATS**

## Try it without code

Open the Actor, sign in to Apify, paste the JSON below into the input editor and review the current price before running. Download results from the run's Dataset as JSON or CSV.

The small example uses public source data (or an explicitly synthetic fixture). For your own workflow, substitute a source you are permitted to access. A source appearing in a demo is not an endorsement.

## Example input

```json
{
  "boards": [
    {
      "provider": "greenhouse",
      "board": "greenhouse"
    }
  ],
  "maxResults": 3,
  "includeDescriptions": true,
  "onlyChanges": false,
  "maxRequests": 100
}
```

## Run with Python

From the repository root, after setting your own `APIFY_TOKEN` ([setup](../../README.md#run-an-example)):

```sh
python run.py public-ats-jobs-change-feed
```

This starts one paid Actor run with a default $0.10 pay-per-event charge ceiling and a 180-second Actor timeout. That parameter does not cap every pricing model; review current pricing first. See the root README for billing and timeout details. Results are saved under `results/`.

## Actual output excerpt

Verified 2026-09-23T21:53:46.540Z UTC, build `1.0.5`, run `JbXYpF8KY2utrLDLE`. 3 rows returned. This is a small functional check, not a completeness or availability guarantee. Selected fields only; no values are fabricated. See [JSON excerpt](sample-output.json).

| title | provider | location | url |
| --- | --- | --- | --- |
| Commercial Counsel | greenhouse | Eastern Timezone | https://job-boards.greenhouse.io/greenhouse/jobs/8126988?gh_jid=8126988 |
| Engineering Manager, Cloud Platform | greenhouse | Ontario | https://job-boards.greenhouse.io/greenhouse/jobs/8021661?gh_jid=8021661 |

## Limits and pricing

Only supported public job boards are covered. Salary data appears only when the employer publishes it.

The Actor and source may change after this sample. Refer to the [current Store listing](https://apify.com/abdulwhab95/public-ats-jobs-change-feed) for full input options and pricing, including any start fee. An Apify token is required for API use even where no source-site API key is required.

Published by the tool's developer. Source names identify compatibility and data provenance, not endorsement. You are responsible for permitted use and source attribution. Sample third-party data retains its original rights.
