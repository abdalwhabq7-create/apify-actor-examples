# Coverage reporting repairs — 12 November 2026

Previously, certain bounded runs could finish successfully while their application report failed to reflect unread source pages. The following hosted builds correct that distinction. A platform `SUCCEEDED` means the process finished; inspect `RUN_REPORT.status` before treating the output as complete.

| Actor | Build | New behavior |
|---|---|---|
| [Mostaql](https://apify.com/abdulwhab95/mostaql-projects-monitor) | 0.1.7 | Explicit status; maxPages, maxProjects and spending stops are LIMIT_REACHED. Source errors take precedence. Valid unchanged output remains SUCCEEDED. |
| [World Bank](https://apify.com/abdulwhab95/world-bank-country-indicator-monitor) | 1.0.3 | Unread indicator pages at maxPages set limitReached. |
| [WooCommerce](https://apify.com/abdulwhab95/woocommerce-public-catalog-scraper) | 1.0.7 | The 50-page source cutoff propagates to LIMIT_REACHED. |
| [ATS Jobs](https://apify.com/abdulwhab95/public-ats-jobs-change-feed) | 1.0.6 | Lever's 5,000-job source cap propagates to LIMIT_REACHED. |
| [PDF](https://apify.com/abdulwhab95/pdf-tables-text-to-json-csv) | 1.0.6 | Skipped image-only pages are PARTIAL. A selected page range that omits document pages is LIMIT_REACHED. OCR remains unsupported. |

The focused regressions run during each cloud build. World Bank also returned one Kuwait GDP observation for 2023 in live run `Qfmciuzk9rEwmORf8`, with status SUCCEEDED and zero reported errors. The other four changes used offline fixtures; this release makes no fresh live-source coverage claim for them.

Prices, data-delivery logic, configured collection limits, access controls, privacy and default run settings were preserved. A cap is reported more honestly, not automatically increased. The historical four failed customer runs visible in public aggregate statistics have no established cause from this verification.

The old [Zid page scraper](../actors/zid-public-product-scraper/README.md) is deprecated. Review the [Zid catalog alternative](../actors/zid-store-catalog-scraper/README.md) for new work; the input contracts differ.
