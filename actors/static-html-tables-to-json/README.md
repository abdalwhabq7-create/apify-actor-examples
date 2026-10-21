# Static HTML Tables to JSON — Bounded Extraction

Extract rows and headers from supplied static HTML or an authorized public HTTPS page. Reject unsupported nested and spanned tables instead of guessing columns.

## Working example

These are synthetic demonstration inputs, not scraped customer data.

```json
{
  "payload": {
    "html": "<table><tr><th>Product</th><th>Price</th></tr><tr><td>Sample A</td><td>12.50</td></tr></table>"
  }
}
```

Expected dataset example (computed by the included implementation):

```json
[
  {
    "tableIndex": 0,
    "rowIndex": 1,
    "headers": [
      "Product",
      "Price"
    ],
    "cells": [
      "Sample A",
      "12.50"
    ]
  }
]
```

## Scope and limitations

Up to 2 MB HTML and 5,000 rows. Static HTML only; no scripts execute. Explicit closing tags required. Nested tables and row/column spans greater than one are rejected. First header row becomes the headers array. JSON preserves array structure; CSV exports contain arrays as serialized fields, not a flattened worksheet. Empty pages can produce zero rows.

Input is bounded to 2 MB in serialized form, and work/output to 5,000 records/findings. HTML table output is additionally capped at 8 MB before delivery. Async I/O has a 60-second budget; the configured platform timeout is 90 seconds for the entire run. The async timer alone cannot interrupt synchronous parsing, which is bounded by byte/row limits. Format failures are not billed as result records. RUN_REPORT distinguishes computed and delivered rows, billing-limit truncation and source/input failures. A successful run with zero output is possible for an unchanged comparison or empty input collection.

## Optional public source

Only the sitemap, header and table tools accept sourceUrl. Provide an HTTPS URL without query/fragment/credentials and set authorizedSource=true only if you have the necessary rights. The supplied source replaces currentXml, headers or html respectively. Only a 200 response is accepted; no page redirects, login, CAPTCHA or access-control bypass. DNS is pinned to a validated public address and private/reserved networks are blocked. Robots rules are checked; fetch limits are 8 requests, 2 MB per response, and no external credentials are forwarded. Source terms still apply; robots permission is not a legal conclusion. Other tools work entirely on supplied data and make no source requests.

## Price

$2 per 1,000 successfully delivered result rows, plus $0.001 per run start at supported memory. For headers a full audit emits six result rows; OpenAPI bills findings, sitemap bills changes, normalization bills retained records and tables bills data rows. Empty runs still have the start charge. Set Apify Maximum cost per run. Platform pricing/terms prevail. No source API key, external AI subscription or recurring schedule is created.

## Privacy and appropriate use

Use data you own or are permitted to process. Do not upload secrets, personal/sensitive information or copyrighted datasets without the required rights. Inputs and results are stored in your Apify account under its retention settings; delete those stores when no longer needed. This Actor does not send your input to an AI service. Public listings/examples contain only synthetic data. This tool is not legal, security or compatibility certification.

## Export and troubleshooting

Use Dataset JSON for full fidelity. CSV/Excel export may serialize nested arrays and objects. Treat spreadsheet cells as text when opening untrusted data; source content is not rewritten to neutralize formulas. A FAILED report means input/source processing did not complete. LIMIT_REACHED means fewer rows were delivered than computed. Keep your original input and inspect RUN_REPORT before using the output downstream.

Reference: https://docs.python.org/3/library/html.parser.html

## عربي

أداة محدودة وواضحة النطاق: أدخل بيانات عندك حق استخدامها، وراجع تقرير التشغيل والحدود قبل الاعتماد على النتائج. الأمثلة تجريبية ومعلّمة بذلك، ولا يوجد ضمان أمان أو توافق أو دخل. لا تتجاوز الأداة تسجيل الدخول أو قيود الوصول.

## Verified hosted example

Verified 2026-10-21, Apify build 1.0.2; 1 synthetic rows, matched against expected output; charged result count matched delivered rows. This tests supplied-data mode, not all external websites.

[Run on Apify](https://apify.com/abdulwhab95/static-html-tables-to-json)
