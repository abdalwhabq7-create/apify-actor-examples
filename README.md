# Apify Actor examples — catalogs, monitoring and data extraction

**24 hosted data tools. Pick a task, inspect a real output sample, and run a small example.**

[جميع الأدوات بالعربي](README.ar.md) · [Apify Store](https://apify.com/abdulwhab95)

Maintained by the developer of these Actors. The examples run the hosted tools on Apify; this repository contains client examples and documentation, not the private Actor implementations.

## Choose a tool

### Commerce

| Tool | What you get |
|---|---|
| [Salla Store Catalog & Price Scraper](actors/salla-catalog-scraper/README.md) | Give a Salla store URL and export product prices, availability and identifiers. Use the data for catalog analysis or price monitoring. |
| [Shopify Product Price & Catalog Scraper](actors/shopify-catalog-scraper/README.md) | Give a Shopify store domain and export public product variants with SKU, price and availability. |
| [WooCommerce Public Catalog — Prices & Stock](actors/woocommerce-public-catalog-scraper/README.md) | Give a WooCommerce store URL and export public Store API products with prices, currency and stock status. |
| [Zid Store Catalog & Price Scraper](actors/zid-store-catalog-scraper/README.md) | Give a Zid store URL and collect product pages through its sitemap, with prices, discounts and availability. |
| [Zid Product Scraper — Arabic Prices & Availability](actors/zid-public-product-scraper/README.md) | Give Zid product or catalog URLs and extract Product JSON-LD into product names, prices, currency and stock fields. |
| [YouCan Store Catalog & Price Scraper](actors/youcan-store-catalog-scraper/README.md) | Give a YouCan store URL and export its public product feed, including prices and available variant metadata. |
| [Salla & Zid App Store Tracker](actors/salla-zid-app-store-tracker/README.md) | Choose Salla or Zid app directories and export app names, categories, ratings and published pricing fields. |

### Data quality

| Tool | What you get |
|---|---|
| [Product Catalog Quality Checker — CSV, SKU & Prices](actors/catalog-product-data-quality-checker/README.md) | Supply CSV text or product records and get per-record validation issues, normalized values and preserved originals. |
| [Dataset Change Detector — Prices, Stock & Records](actors/dataset-change-detector/README.md) | Supply previous and current JSON snapshots and get NEW, UPDATED or optional REMOVED events with before/after values. |

### Business opportunities

| Tool | What you get |
|---|---|
| [Building Permits Scraper - Multi-City Construction Leads](actors/building-permits-multi-city/README.md) | Select city open-data sources and export building permits with dates, types and declared values. |
| [Mostaql Projects Monitor](actors/mostaql-projects-monitor/README.md) | Read public Mostaql project listings and export titles, skills, budgets and project links. |
| [Development Project Tenders & Procurement Notices Monitor](actors/development-tenders-monitor/README.md) | Filter World Bank procurement notices by country, time or keyword and export titles, notice types, deadlines and source links. |
| [ATS Job Feed — Greenhouse, Lever & Ashby Changes](actors/public-ats-jobs-change-feed/README.md) | Give public Greenhouse, Lever or Ashby board identifiers and export jobs in a common schema. |

### Web and documents

| Tool | What you get |
|---|---|
| [Website to Markdown — RAG Content & Change Feed](actors/website-markdown-change-feed/README.md) | Give public page URLs and export clean Markdown with content hashes and source URLs for document or RAG pipelines. |
| [Website SEO & Broken Link Audit](actors/website-seo-broken-link-audit/README.md) | Give public page URLs and get title, heading and metadata diagnostics plus a bounded set of link checks. |
| [Product JSON-LD & Structured Data Auditor](actors/product-jsonld-schema-auditor/README.md) | Give product page URLs and get JSON-LD syntax and Product offer diagnostics with structured issue codes. |
| [PDF Tables & Text to JSON and CSV](actors/pdf-tables-text-to-json-csv/README.md) | Give public text-based PDF URLs and export page text, table arrays and CSV strings. |
| [Website Screenshots & Visual Changes — Static HTML](actors/static-website-visual-change-monitor/README.md) | Give static page URLs and viewport dimensions to capture screenshots and compare later captures against a saved baseline. |
| [RSS & Atom Feed Aggregator — New or Updated Items](actors/rss-atom-new-items-feed/README.md) | Give RSS or Atom feed URLs and export deduplicated items with titles, dates and links. |

### Developer and research

| Tool | What you get |
|---|---|
| [GitHub Release Monitor — Versions & Asset Downloads](actors/github-release-change-monitor/README.md) | Give public owner/repository names and export release tags, dates and asset download counts. |
| [npm Package Monitor — Versions, Downloads & Deprecation](actors/npm-package-version-download-monitor/README.md) | Give npm package names and export versions, weekly download counts, licenses and deprecation metadata. |
| [Hacker News Topic Monitor — Stories & Engagement](actors/hacker-news-topic-change-monitor/README.md) | Give a keyword and export matching Hacker News stories, links, points and comment counts. |
| [Crossref Research Monitor — DOI, Journals & Citations](actors/crossref-research-doi-monitor/README.md) | Give a research query and export DOI metadata, publication titles, dates and citation counts. |
| [World Bank Indicators — Country Data & Revisions](actors/world-bank-country-indicator-monitor/README.md) | Give country and indicator codes plus years and export annual values with source attribution. |

## Run an example

Requires Python 3.10+ and an Apify account. No Python packages are needed. Read the selected Actor page and pricing first.

```sh
git clone https://github.com/abdalwhabq7-create/apify-actor-examples.git
cd apify-actor-examples
```

Set your own token in your current shell. Do not put it in a repository or shared script.

**PowerShell:**

```powershell
$env:APIFY_TOKEN = Read-Host 'Apify token' -MaskInput
python run.py salla-catalog-scraper
```

The masked prompt above requires PowerShell 7. On Windows PowerShell 5.1, set `APIFY_TOKEN` through Windows user environment settings and reopen your terminal.

**Bash:**

```bash
read -rs -p 'Apify token: ' APIFY_TOKEN; export APIFY_TOKEN; echo
python run.py github-release-change-monitor
```

To use your own JSON input file:

```sh
python run.py salla-catalog-scraper --input my-input.json --max-charge 0.10
```

The runner starts one run, prints its ID, checks the outcome, and downloads up to 1,000 dataset rows to `results/`. It never retries a start request automatically. A connection failure after submission may leave a run running: check Apify Console before trying again.

## Billing and scope

These are paid hosted Actors. The sample runner passes `maxTotalChargeUsd=0.10` and `timeout=180` by default. The charge ceiling follows Apify billing semantics; confirm what your account and Actor pricing cover. The client stops waiting after about five minutes but does not abort a remote run. Review [Apify run parameters](https://docs.apify.com/api/v2/actors-runs-post) and each live Store price.

Inputs are deliberately small and change-only modes are disabled for first-run examples. For recurring monitoring, configure persistent state and an Apify schedule separately. No schedule is created by these examples.

## Verification

All 24 examples were executed against the published Actors. Verification window (UTC): 2026-09-23T21:53:03.613Z to 2026-09-23T21:56:07.637Z. Each page records its actual run timestamp and build. Samples demonstrate output shape; they do not establish full source coverage, guaranteed uptime, or future results. Dataset comparison and catalog validation use explicitly synthetic input fixtures.

Third-party text excerpts are limited to short identifying metadata. Source datasets, artwork and trademarks retain their own rights. Check the Actor and original source for licenses and attribution.

## Help

Use the issue/support section on the relevant Apify Store page for Actor-specific questions. Never share API keys, personal records or private datasets in public discussions.

## Check the example runner

```sh
python -m unittest discover -s tests
```
