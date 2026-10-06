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

### Two-run check on 7 October 2026

We ran the three-product monitor twice with build `0.1.9`, the same store and a separate test state name. [Selected run evidence](monitor-checks-20261007.json):

| Check time (UTC) | Run ID | Products checked | Rows returned |
|---|---|---:|---:|
| 2026-10-06 23:13:32 | `LodNkPQlfV2xOmPJF` | 3 | 3, all `NEW` |
| 2026-10-06 23:13:52 | `0oW3Xfc1JhrUsDNZJ` | 3 | 0 |

Both runs succeeded, resolved the store, reported zero skipped or duplicate products, and did not stop at a spending limit. Both had `exhaustiveRead: false`. This confirms that the sampled baseline persisted and unchanged sampled products were not returned again. It does not test a real price change, a removed product or full-catalog coverage. The dates above are UTC; these checks occurred on 7 October in Kuwait.

## 3. Turn the sample into a daily task

1. Choose the stores and coverage you actually need. Increase `maxProductsPerStore` only after reviewing their sizes, run time and price. The input accepts up to 6,000 products per store. Check `exhaustiveRead` rather than assuming a large limit means full coverage.
2. Give the production monitor its own stable state name, such as `my-salla-daily-prices`. Its first run creates a new baseline and returns the products it reads as `NEW`.
3. Use **Save as a new task** in Apify Console to keep this configuration. Set an appropriate maximum cost and timeout in its run options, then run the task manually and inspect its report.
4. In **Schedules**, create a daily schedule, choose your timezone and add the tested task. Review **Next runs**, then enable it. The schedule uses your account and budget; saving a task alone does not schedule it or make it a public Store listing.
5. Check the next run's status, report and output. Keep prices and availability as data for review; this Actor does not automatically change your shop's prices or send a customer message.

These steps follow Apify's [task guide](https://docs.apify.com/actors/running/tasks) and [schedule guide](https://docs.apify.com/actors/running/schedules). A changed-only run still reads source data, and a quiet run can still have start or platform charges. Review actual run charges before choosing a recurring budget.

## 4. Export the useful columns

In the run's Dataset, export CSV or JSON. Start with `productId`, `productUrl`, `name`, `price`, `regularPrice`, `currency`, `isAvailable`, `isOutOfStock`, `changeType`, `changedFields` and `previousValues`. JSON preserves nested previous values; a spreadsheet is useful for reviewing prices.

The [latest small sample](salla-sample-20261007.json) was checked **7 October 2026 in Kuwait** (`2026-10-06T23:09:59.924Z`), run `UNnqswydfejTDG2nh`, build `0.1.9`. It returned five products from `salla.sa/coffee_souq` with `maxProductsPerStore: 5` and `onlyChanges: false`:

| Product ID | Product URL | Price | Currency | Available |
|---|---|---:|---|---|
| 1589226865 | https://coffeesouq1.com/QzqVKzw | 60 | SAR | true |
| 1301644920 | https://coffeesouq1.com/YzPVloE | 30 | SAR | true |

Its report recorded no unresolved stores, skipped products or duplicate products, and `exhaustiveRead: false`. These rows demonstrate a successful bounded read and the output shape, not full coverage or a verified change between two monitoring runs. Prices and availability can change after the recorded check.

## Optional: report products missing from the catalog

Keep `emitRemoved: false` while learning the workflow. To use removals, enable both `onlyChanges` and `emitRemoved`, leave `onlyOnSale: false`, and establish a complete baseline first. Subsequent removal checks require another complete read without skipped products or limits cutting it short. A missing product in a small sample is **not** evidence that it was removed from the store.

`REMOVED` rows are charged like other returned rows. Read `removalNote` whenever expected removals are absent. If you only need price and stock changes, leave removal detection off.

[Actor reference and small output example](../actors/salla-catalog-scraper/README.md) · [All examples](../README.md)
