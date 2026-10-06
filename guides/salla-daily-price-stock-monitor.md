# Monitor Salla prices and stock with a saved baseline

Give [Salla Store Catalog & Price Scraper](https://apify.com/abdulwhab95/salla-catalog-scraper) a store URL. Save its product snapshot, then run the same input again to receive only new products and changed prices or stock status. You can export those rows to CSV or JSON.

This guide is maintained by the Actor's developer. The hosted Actor is paid; check its [current price](https://apify.com/abdulwhab95/salla-catalog-scraper/pricing) and your Apify plan before running. It is an independent tool, not an official Salla service.

## 1. Try a small monitor

Open the Actor in Apify Console and paste [this input](salla-monitor-input.json) into its JSON input editor:

```json
{
  "stores": ["salla.sa/coffee_souq"],
  "maxProductsPerStore": 3,
  "onlyChanges": true,
  "stateStoreName": "my-salla-monitor-demo",
  "onlyOnSale": false,
  "emitRemoved": false,
  "includeEndedDiscounts": false,
  "requestDelayMs": 200,
  "respectRobots": true
}
```

The store is a public example. For your own workflow, choose a store you are permitted to access. Use a different `stateStoreName` for each independent monitor. Keep the same name when rerunning that monitor in the same Apify account; a new name starts a fresh baseline. Avoid overlapping runs that write to the same state store.

Set **Maximum cost per run** before starting. The three-product limit makes this a small sample, not a scan of the whole catalog. In `onlyChanges` mode, this limit counts products **checked**, including unchanged products, rather than just rows returned.

If you prefer Python, use the existing repository runner after [setting your own token](../README.md#run-an-example):

```sh
python run.py salla-catalog-scraper --input guides/salla-monitor-input.json --max-charge 0.10
```

Run that command from the repository root. It starts one paid run and saves up to 1,000 output rows in `results/`. It does not create a schedule. The charge ceiling follows Apify billing rules and may not include every platform charge.

## 2. Run the same input again

On the first successful read, products not already in this monitor's state appear as `NEW`. On later reads, `UPDATED` means at least one watched field changed: `price`, `regularPrice`, `isAvailable` or `isOutOfStock`. Inspect `changedFields` and `previousValues` to see what moved.

**Zero rows is normal when the products checked have not changed.** It does not prove the entire store stayed unchanged. A three-product sample can miss changes elsewhere, and the first three products can change as a store reorders its catalog.

Before treating an empty dataset as a quiet result, check the run status and open the run's key-value store record **`RUN_REPORT`**:

| Check | Why it matters |
|---|---|
| `unresolved` | A store that could not be resolved is not an unchanged store. |
| `skippedProducts` | A skipped product leaves a gap in what was checked. |
| `stoppedAtSpendingLimit` | A cost-capped run may leave products unchecked. |
| Each store's `truncated` | An interrupted read needs investigation. |
| Each store's `exhaustiveRead` | `true` indicates a complete catalog read; a capped sample is not complete. |
| Each store's `removalNote` | Explains why removal detection did not run, when requested. |

A successful capped sample can merge the products it checked into saved state. An error or spending-limit interruption keeps the prior comparison state, so a retry may report the same changes again. Review the report before using the output for alerts.

The report's `verdict` can say `NO DATA - zero rows produced` on a quiet changed-only run. Interpret it together with the status and coverage fields above; it does not by itself establish a source failure.

## 3. Turn the sample into a daily task

1. Choose the stores and coverage you actually need. Increase `maxProductsPerStore` only after reviewing their sizes, run time and price. The input accepts up to 6,000 products per store. Check `exhaustiveRead` rather than assuming a large limit means full coverage.
2. Give the production monitor its own stable state name, such as `my-salla-daily-prices`. Its first run creates a new baseline and returns the products it reads as `NEW`.
3. Use **Save as a new task** in Apify Console to keep this configuration. Set an appropriate maximum cost and timeout in its run options, then run the task manually and inspect its report.
4. In **Schedules**, create a daily schedule, choose your timezone and add the tested task. Review **Next runs**, then enable it. The schedule uses your account and budget; saving a task alone does not schedule it or make it a public Store listing.
5. Check the next run's status, report and output. Keep prices and availability as data for review; this Actor does not automatically change your shop's prices or send a customer message.

These steps follow Apify's [task guide](https://docs.apify.com/actors/running/tasks) and [schedule guide](https://docs.apify.com/actors/running/schedules). A changed-only run still reads source data, and a quiet run can still have start or platform charges. Review actual run charges before choosing a recurring budget.

## 4. Export the useful columns

In the run's Dataset, export CSV or JSON. Start with `productId`, `productUrl`, `name`, `price`, `regularPrice`, `currency`, `isAvailable`, `isOutOfStock`, `changeType`, `changedFields` and `previousValues`. JSON preserves nested previous values; a spreadsheet is useful for reviewing prices.

For an output-shape example, the existing [verified sample](../actors/salla-catalog-scraper/sample-output.json) contains these real rows from **23 September 2026**, run `kYIFgUru6yeHEShlZ`, build `0.1.8`:

| Product URL | Price | Currency | Available |
|---|---:|---|---|
| https://coffeesouq1.com/oZOQwNv | 41.74 | SAR | true |
| https://coffeesouq1.com/qGYYvqZ | 125 | SAR | true |

That historical run used `onlyChanges: false`, read three products from each of two stores and returned six rows. It demonstrates output shape, not today's prices, full coverage or a verified change between two monitoring runs.

## Optional: report products missing from the catalog

Keep `emitRemoved: false` while learning the workflow. To use removals, enable both `onlyChanges` and `emitRemoved`, leave `onlyOnSale: false`, and establish a complete baseline first. Subsequent removal checks require another complete read without skipped products or limits cutting it short. A missing product in a small sample is **not** evidence that it was removed from the store.

`REMOVED` rows are charged like other returned rows. Read `removalNote` whenever expected removals are absent. If you only need price and stock changes, leave removal detection off.

[Actor reference and small output example](../actors/salla-catalog-scraper/README.md) · [All examples](../README.md)
