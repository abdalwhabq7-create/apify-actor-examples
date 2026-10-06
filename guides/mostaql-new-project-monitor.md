# Build a shortlist of unseen Mostaql projects

Use [Mostaql Projects Monitor](https://apify.com/abdulwhab95/mostaql-projects-monitor) to check public project listings, apply your filters and export project links, budgets and dates for review. Turn on `onlyNew` to avoid returning project IDs that this monitor has already processed.

This guide is maintained by the Actor's developer. It is an independent paid tool, not an official Mostaql or Hsoub product. Check the [current price](https://apify.com/abdulwhab95/mostaql-projects-monitor/pricing), the source's current rules and your permitted use before running. Public availability does not establish permission to republish client content.

## 1. Try one listing page

Open the Actor in Apify Console and paste [this small input](mostaql-monitor-input.json):

```json
{
  "categories": [],
  "skills": [],
  "keywords": [],
  "maxProjects": 3,
  "maxPages": 1,
  "onlyNew": true,
  "stateStoreName": "my-mostaql-monitor-demo"
}
```

Set **Maximum cost per run**, then start. This reads at most one listing page and returns at most three matching projects. It does not claim to find every open project.

On the first run, matching projects returned from that page are marked `NEW`. The Actor remembers project IDs in the named key-value store. Keep the same state name, filters and Apify account when repeating the monitor. Use a separate name for independent monitors, and avoid overlapping runs that write to the same state.

## 2. Understand what “new” means

`onlyNew` means **not previously processed by this monitor**, not necessarily published since your previous run. For example, after a run returns its first three projects, the next run can return older, previously unseen projects from the same page. That is backfill, not proof that three projects were just published.

It also does **not** monitor edits to a known project's budget, title, status or description. IDs are remembered after successful delivery or after being checked and rejected by the filters. Failed or undelivered projects can be tried again later. State retention is bounded; do not treat this as a permanent archive of every ID.

If you only want projects published after a particular moment, add `publishedSince`. Use an ISO date such as `2026-10-07` (midnight UTC), or a date-time with an explicit timezone, such as `2026-10-07T09:00:00+03:00`. Replace that example date with your actual cutoff. A saved fixed date does not move forward automatically each day.

## 3. Choose useful filters

| Input | What it does |
|---|---|
| `categories` | Select categories such as `development` or `design`; empty means all. Use the options shown in the Actor's input form. |
| `skills` | Accepts skill slugs or supported Mostaql skill-listing links. |
| `keywords` | Keeps matches to at least one supplied Arabic or English term across the project's searchable text. |
| `minBudget` | Compares with the **top** of the stated budget range. A range of $100–$250 can match `250`; this is not a promised payout. |
| `publishedSince` | Excludes projects before your fixed cutoff and projects with no usable publish time. |
| `maxProjects` / `maxPages` | Bound returned projects and listing pages read. They also bound coverage. |

Changing the categories, skills, keywords, budget threshold or publication cutoff creates a separate comparison scope. Previously seen projects can therefore appear again under the new filters. Review the first result before scheduling that configuration.

## 4. Check the report before interpreting an empty result

Open the run's key-value store record **`RUN_REPORT`** as well as its status and Dataset:

| Check | Interpretation |
|---|---|
| `alreadySeen` / `filteredOut` | Help explain why a read produced few or no new rows. |
| `pagesRead` / `projectsRead` | Show how much of the source was actually checked. |
| `unreadable` / `failedPages` | Identify gaps from source failures. |
| `robotsDisallowed` / `blocked` | Identify access restrictions; do not bypass them. |
| `stoppedAtSpendingLimit` | The configured cost ceiling stopped delivery. |
| `stoppedAtMaxProjects` | The return limit was reached; later runs may backfill unseen projects. |
| `incomplete` | Flags certain access/read failures. A false value does not mean every source page was scanned; `maxPages` still limits the run. |

Zero rows can be normal when the projects in the scanned pages were already seen or did not match your filters. It is not proof that Mostaql has no new work. Treat results as a shortlist and open each original project to confirm its current details.

## 5. Export a small review list and schedule it

For your shortlist, export only `projectId`, `url`, `budgetMin`, `budgetMax`, `currency` and `publishedAt`. This guide deliberately avoids republishing client titles, descriptions or contact information. The Actor's complete dataset can contain user-written text with personal data; selecting a few export columns does not remove that text from the stored dataset. Review and restrict access to your datasets before sharing anything.

After a successful manual test, use **Save as a new task** in Console. Keep the state name stable, set its run limits, and add the task to a daily schedule with your timezone. Check **Next runs** before enabling it. See Apify's [task guide](https://docs.apify.com/actors/running/tasks) and [schedule guide](https://docs.apify.com/actors/running/schedules). Neither this guide nor the example runner creates a recurring schedule for you.

You can run the small example once with the existing client after [setting your own token](../README.md#run-an-example):

```sh
python run.py mostaql-projects-monitor --input guides/mostaql-monitor-input.json --max-charge 0.10
```

Run it from the repository root. The client downloads the complete returned rows to your local `results/` directory, including any source text. Keep those files private and create a selected-column export for sharing. It starts a paid run; a zero-row result can still incur start or platform charges.

The tool does not submit proposals or contact clients. Review and respond through Mostaql's own workflow and current rules.

## Verified small read

Run `TFvxneMCWmYxpoD2a`, build `0.1.3`, was checked **7 October 2026 in Kuwait** (`2026-10-06T23:10:01.516Z`). With `maxProjects: 5`, `maxPages: 1`, empty keywords and `onlyNew: false`, it returned five projects. Its report recorded zero unreadable projects or failed listing pages and `stoppedAtMaxProjects: true`.

The [selected metadata excerpt](mostaql-sample-20261007.json) contains only identifiers, links, stated budget limits and publication dates. Two rows from that actual result:

| Project ID | Original project | Stated budget (USD) | Published (UTC) |
|---|---|---:|---|
| 1283464 | https://mostaql.com/project/1283464 | 50–100 | 2026-10-06T21:43:13Z |
| 1283461 | https://mostaql.com/project/1283461 | 100–250 | 2026-10-06T21:41:49Z |

This was a bounded read, not a proof of full coverage, current availability or deduplication across runs. The budgets are source-stated ranges, not promised earnings.

### Two-run check of unseen IDs

We also tested `onlyNew: true` twice using build `0.1.3`, the same test state name, no filters and one listing page. **These checks used `maxProjects: 5`; the downloadable introductory example above uses 3.** [Selected run evidence](monitor-checks-20261007.json):

| Check time (UTC) | Run ID | Rows returned | Already seen | Remembered IDs |
|---|---|---:|---:|---:|
| 2026-10-06 23:13:38 | `FyrtlxmhcRykt1a1S` | 5 | 0 | 5 |
| 2026-10-06 23:14:18 | `idQhh5h5GkOQciZvV` | 5 | 5 | 10 |

Both runs succeeded without failed or unreadable pages, blocked requests or a spending-limit stop. The second result contained five different IDs: **older, previously unseen projects from the same listing page**, not five projects newly posted between the checks. This demonstrates deduplication and backfill with a return cap. It does not verify ongoing project availability or edit detection. These UTC timestamps correspond to 7 October in Kuwait.

[Actor reference and dated output example](../actors/mostaql-projects-monitor/README.md) · [All examples](../README.md)
