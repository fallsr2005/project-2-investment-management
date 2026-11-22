# Monthly adjusted-price lineage

## Source boundary

The saved `data/prices.csv` was supplied in the completed Lab 14/15 work. Those records report a Yahoo Finance chart-endpoint download on 2026-10-22. The [original downloader](../data/source-evidence/lab-price-lineage/original-download_prices.py), [Lab 14 source excerpt](../data/source-evidence/lab-price-lineage/lab-14-source-excerpt.md), and [Lab 15 source excerpt](../data/source-evidence/lab-price-lineage/lab-15-source-excerpt.md) are now bundled for inspection. These are copies of the current workspace evidence, not authenticated October captures. Do not execute the original downloader in the repository root: it writes `prices.csv` in its working directory. The app uses `data/prices.csv` and needs no network access.

The [workspace comparison](../data/source-evidence/lab-price-lineage/workspace-comparison.json) records source-file hashes and verifies that the lab CSV and project CSV have identical parsed rows and identical bytes after newline normalization. Their different original byte hashes are explained by line endings. No original October vendor JSON response was found, so the reported download date remains supported by the lab records only.

| Input | Source link | Meaning |
|---|---|---|
| SGOV | https://finance.yahoo.com/quote/SGOV/history/ | Monthly adjusted close of Treasury-bill ETF |
| SCHR | https://finance.yahoo.com/quote/SCHR/history/ | Monthly adjusted close of intermediate Treasury ETF |
| USIG | https://finance.yahoo.com/quote/USIG/history/ | Monthly adjusted close of investment-grade corporate-bond ETF |
| ACWI | https://finance.yahoo.com/quote/ACWI/history/ | Monthly adjusted close of global-equity ETF |

Reported original request pattern: `https://query1.finance.yahoo.com/v8/finance/chart/TICKER?period1=1633046400&period2=1790812800&interval=1mo&events=history`. A later download can differ because vendor adjustments can revise history. Do not overwrite the submitted snapshot with a fresh download.

## Independent current-source comparison — November 22, 2026

All four public chart responses were retrieved on November 22 at 23:38 UTC and preserved in [the dated capture folder](../data/source-evidence/prices-20261122T233854Z/). The [metadata](../data/source-evidence/prices-20261122T233854Z/metadata.json) records each request URL, actual retrieval time, and raw-response SHA-256. The [comparison report](../data/source-evidence/prices-20261122T233854Z/comparison-report.json) verifies hashes, ticker identities, and exact alignment of all 60 months; null, nonpositive, nonfinite, missing, or duplicate observations are rejected rather than repaired silently.

| Ticker | Months | Maximum absolute adjusted-price difference, USD | Maximum relative price difference | Annual mean-return difference, percentage points |
|---|---:|---:|---:|---:|
| SGOV | 60 | 0.328849 | 0.327657% | +0.00000987 |
| SCHR | 60 | 0.090156 | 0.364424% | -0.00000033 |
| USIG | 60 | 0.213905 | 0.421857% | -0.00000180 |
| ACWI | 60 | 0.000023 | 0.000025% | +0.00000188 |

These are observed differences, not proof of a particular revision cause. Adjusted price levels differ, while adjacent-return estimates remain very close. The capture selects the same 70% SGOV / 30% ACWI base mix; estimated return and volatility still display 6.02% and 4.56%. Both baseline mandate verdicts are unchanged. This supports retaining the existing input snapshot for reproducibility; it does not authenticate the original October retrieval, verify all historical corporate actions, or establish historical information availability. The raw source and six-decimal comparison CSV remain separate from the app's original CSV.

Recompute the complete report offline and check it against the preserved report and reconstructed CSV:

```powershell
python audit_price_sources.py --snapshot data/source-evidence/prices-20261122T233854Z
```

Optional later capture, requiring source access: `python audit_price_sources.py --capture`. Each capture creates a new timestamped folder and never overwrites the app input. This endpoint is an observed source interface, not a guarantee of future vendor availability.

## Transformations, exclusions, and reproduction

- Four fixed ticker columns; 60 matching, consecutive month labels, October 2021–September 2026; oldest first. Six-decimal adjusted prices are retained as supplied.
- First-of-month dates label the represented month's completed price, not when that price became available. Treat the price sample as completed through September 30, 2026, not September 1.
- Returns are adjacent simple ratios minus one: 60 prices produce 59 returns. Last-36 mode uses 37 prices for 36 returns.
- Raw JSON selection uses `chart.result[0].indicators.adjclose[0].adjclose`, aligned to UTC timestamp month labels. It uses adjusted prices, not the unadjusted quote close, and rounds prices to six decimals before estimating returns. Dollar levels are per-share adjusted values, not executable historical quotes. Yahoo's [adjusted-close definition](https://help.yahoo.com/kb/SLN28256.html) explains its split and distribution adjustments.
- Annual arithmetic mean = monthly mean ×12. Annual sample standard deviation = monthly sample standard deviation ×sqrt(12). Sample covariance and correlation use the same aligned returns.
- No forward filling, winsorizing, dropping individual asset months, or converting missing values to zero. Invalid, nonpositive, nonfinite or misaligned inputs are rejected. The parser requires the fixed universe and at least 37 prices.
- Costs are explicit additional annual implementation-cost assumptions, subtracted from arithmetic return estimates. They are not inferred trading costs or an extra deduction of the funds' expense ratios.
- Saved price SHA-256: `b8b78ad16aaef542fbcd266e65b2ff7502ff76a7a9fb1747869d31de9f8cc260`.
- `python reproduce.py` records the exact price SHA-256, estimates, correlations, baseline checks, scenario results, and run timestamp in `outputs/reproduced-results.json`.

## Revision, rights, and privacy limits

This is not a point-in-time price-vintage database or a backtest. Adjusted prices may reflect later vendor revisions. The later raw-response comparison corroborates the current source without authenticating the reported October retrieval. The user's portfolio roles and the 6%/10% rules are classroom choices, not client facts.

Vendor access is not itself permission for unrestricted republication. The [Yahoo historical-download help](https://help.yahoo.com/kb/finance-app-for-ios/download-historical-data-yahoo-finance-sln2311.html) identifies licensing restrictions for some instruments; [Yahoo's terms](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html) govern source use. No redistribution license was independently established by this audit, and classroom purpose alone is not a license determination. The general-terms page could not be retrieved in full during this audit, so no claim that its conditions were fully reviewed is made. Reuse outside the course or broader distribution requires appropriate rights confirmation or a suitably licensed replacement source. This remains an explicit rubric limitation.

The capture stores public response bodies and retrieval metadata only; it needs no login, cookies, credentials, personal portfolio, or personal account information. No new license grant over third-party data is asserted here.
