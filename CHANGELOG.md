# Changelog

## 1.1.0 — 2026-10-21 — five new utilities and safer result handling

### Added

- Five published, paid Apify tools: sitemap snapshot changes, HTTP security-header presence, limited OpenAPI structural differences, CSV/JSON deduplication, and static HTML tables to JSON. Examples are synthetic and executed on build 1.0.2; result billing counters matched delivered rows.
- Added the previously omitted Greenhouse/Lever/Ashby Jobs API to the catalog, bringing it to 30 public tools. Its example was not freshly executed in this release.
- Result-verification guide linked from all 25 existing public tool pages.

### Fixed

- Client saves RUN_REPORT with downloaded data, warns about partial/unverified results and the 1,000-row download cap; never retries a paid start automatically.
- Mostaql hosted build 0.1.5 no longer falls back to stale robots rules when current rules cannot be fetched. Verified by local regression tests and successful cloud build, not a new live crawl.
- World Bank hosted build 1.0.2 accepts explicitly empty response pages. Seven regression tests and a bounded live Kuwait GDP example passed. This is not a confirmed explanation for earlier customer failures.

### Scope

A private read-only checker and per-Actor runbooks cover the original 27-tool fleet. Only the two runtimes named above changed; other improvements are shared client, documentation and operational tooling. No existing prices, private visibility, schedules or account limits were changed. New tools cost $2 per 1,000 result rows plus $0.001/run start at supported memory; check current Store pricing. No profit, uptime, full coverage or certification guarantee.

21 new-utility tests, 9 client/catalog tests, 3 health-check tests, 2 Mostaql tests and 7 World Bank tests passed. Optional external fetch paths were tested with mocks; live utility smoke tests used supplied synthetic data.

Implementation and this announcement were prepared with AI assistance. The real local Claude Code was unavailable in this environment; this is not presented as Claude's work.
