# Track Salla and Zid app listings, ratings and displayed prices

إذا تطور تطبيقات لسلة أو زد، هذا الشرح يساعدك تتابع التطبيقات المنشورة وتغيّر تقييماتها وأسعارها المعروضة. المقصود متاجر التطبيقات؛ متابعة منتجات التجار لها أدوات أخرى.

**Disclosure:** I develop [Salla & Zid App Store Tracker](https://apify.com/abdulwhab95/salla-zid-app-store-tracker) under the Apify username `abdulwhab95`. This is a tutorial for my own paid Actor, independent of Salla and Zid.

**AI disclosure:** This article was drafted by an AI assistant using the Actor's documentation and input schema. The illustrative records below are synthetic.

An app developer can use a repeatable listing export to decide which changes deserve a closer look. Ratings and displayed prices are observable signals; they do not establish installations, paying customers or revenue.

**1. Inspect a small sample.** Open the Actor's JSON input editor and use:

```json
{
  "platforms": ["salla", "zid"],
  "language": "en",
  "maxAppsPerPlatform": 5,
  "includeCategories": false,
  "onlyChanges": false
}
```

Set Apify's maximum charge per run, start the run and inspect Output. This checks at most five apps per platform. `includeCategories: false` avoids Salla's separate category-list traversal; its category fields will be `null`, meaning they were not looked up. Zid category data is unaffected. Turning this option off is an existing feature. [Input schema](https://apify.com/abdulwhab95/salla-zid-app-store-tracker/input-schema).

**Live sample verified on 3 November 2026:** build `0.1.4`, run `bfgnzoEGd1YieXBgc`, returned ten rows (five per platform). Its `RUN_REPORT` recorded two requests, zero failed requests, `status: SUCCEEDED` and `incomplete: false`. This proves that the bounded sample completed; it does not establish complete marketplace coverage or customer demand.

This **synthetic excerpt is an illustration, not a captured app listing or a measured run**:

| platform | name | rating | ratingCount | price | currency |
| --- | --- | ---: | ---: | ---: | --- |
| salla | Demo reporting app | 4.5 | 12 | 49 | SAR |
| zid | Demo inventory app | null | 0 | 79 | null |

The second row illustrates two distinct unknowns. An unrated app should not be treated as a five-star app. A number without a known currency should not be ranked against SAR prices. Preserve `pricingText` when reviewing an offer: a headline amount alone does not describe every billing condition. [Output and interpretation](https://apify.com/abdulwhab95/salla-zid-app-store-tracker).

**2. Save a consistent tracking task.** After inspecting the sample, this example expands the checked window to 100 apps per platform:

```json
{
  "platforms": ["salla", "zid"],
  "language": "en",
  "maxAppsPerPlatform": 100,
  "includeCategories": false,
  "onlyChanges": true,
  "stateStoreName": "gulf-app-market-review"
}
```

The limit counts apps checked, not changes delivered. This is a bounded window in each platform's listing order, not a complete marketplace census. Increase it deliberately if you need wider coverage; the schema allows up to 5,000 per platform. [Input limits](https://apify.com/abdulwhab95/salla-zid-app-store-tracker/input-schema).

The first tracking run emits observed apps as `NEW`. Later runs can emit `UPDATED` when rating, rating count, price or pricing text differs. Review `changedFields` and the provided previous values. Removed apps are not reported. Keep the state name and language stable; changing language starts another snapshot, and switching Salla category enrichment also uses a separate snapshot. [Tracking semantics](https://apify.com/abdulwhab95/salla-zid-app-store-tracker).

Run the saved task again, then inspect its `RUN_REPORT`. An empty dataset can mean no watched differences; `listingComplete: false` means a platform listing was not fully read. A quiet result is useful only alongside its coverage report. [Run reports](https://apify.com/abdulwhab95/salla-zid-app-store-tracker).

**3. Add a schedule after the repeat check.** In Apify Console, create a schedule, add the saved task, choose the timezone and frequency, then enable it. An output dataset is the result of this workflow. Sending alerts into email or chat requires an additional integration. [Scheduling documentation](https://docs.apify.com/actors/running/schedules).

The public pricing checked on 3 November 2026 is **$2 per 1,000 delivered apps**, plus an **Actor Start event of $0.00005**; platform usage is shown as included. Ten delivered sample rows therefore have a listed event charge of **$0.02005**. The 200-row tracking window would be **$0.40005** if all 200 apps are delivered. A no-change run still has the start event. Recheck the [current pricing](https://apify.com/abdulwhab95/salla-zid-app-store-tracker/pricing) before running.

Try the [small Salla/Zid app-listing sample](https://apify.com/abdulwhab95/salla-zid-app-store-tracker) and inspect the data before increasing coverage or enabling repeat runs.
