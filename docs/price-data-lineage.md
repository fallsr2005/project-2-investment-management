# Monthly adjusted-price lineage

## Source boundary

The saved `data/prices.csv` was supplied in the completed Lab 14/15 work. Those records report a Yahoo Finance download on 2026-10-22. The original lab downloader remains at `../download_prices.py` in the course workspace; this standalone repository reproduces results from the saved CSV and does not require that parent file. An original vendor JSON response is not present, so the claimed download date is lab-record evidence rather than an independently authenticated timestamp.

| Input | Source link | Meaning |
|---|---|---|
| SGOV | https://finance.yahoo.com/quote/SGOV/history/ | Monthly adjusted close of Treasury-bill ETF |
| SCHR | https://finance.yahoo.com/quote/SCHR/history/ | Monthly adjusted close of intermediate Treasury ETF |
| USIG | https://finance.yahoo.com/quote/USIG/history/ | Monthly adjusted close of investment-grade corporate-bond ETF |
| ACWI | https://finance.yahoo.com/quote/ACWI/history/ | Monthly adjusted close of global-equity ETF |

Reported original request pattern: `https://query1.finance.yahoo.com/v8/finance/chart/TICKER?period1=1633046400&period2=1790812800&interval=1mo&events=history`. A later download can differ because vendor adjustments can revise history. Do not overwrite the submitted snapshot with a fresh download.

## Transformations, exclusions, and reproduction

- Four fixed ticker columns; 60 matching, consecutive month labels, October 2021–September 2026; oldest first. Six-decimal adjusted prices are retained as supplied.
- First-of-month dates label the represented month's completed price, not when that price became available. Treat the price sample as completed through September 30, 2026, not September 1.
- Returns are adjacent simple ratios minus one: 60 prices produce 59 returns. Last-36 mode uses 37 prices for 36 returns.
- Annual arithmetic mean = monthly mean ×12. Annual sample standard deviation = monthly sample standard deviation ×sqrt(12). Sample covariance and correlation use the same aligned returns.
- No forward filling, winsorizing, dropping individual asset months, or converting missing values to zero. Invalid, nonpositive, nonfinite or misaligned inputs are rejected. The parser requires the fixed universe and at least 37 prices.
- Costs are explicit additional annual implementation-cost assumptions, subtracted from arithmetic return estimates. They are not inferred trading costs or an extra deduction of the funds' expense ratios.
- Saved price SHA-256: `b8b78ad16aaef542fbcd266e65b2ff7502ff76a7a9fb1747869d31de9f8cc260`.
- `python reproduce.py` records the exact price SHA-256, estimates, correlations, baseline checks, scenario results, and run timestamp in `outputs/reproduced-results.json`.

## Revision, rights, and privacy limits

This is not a point-in-time price-vintage database or a backtest. Adjusted prices may reflect later vendor revisions. No authenticity claim stronger than the saved lab evidence is made. The user's portfolio roles and the 6%/10% rules are classroom choices, not client facts.

Vendor access is not itself permission for unrestricted republication. Confirm that the course repository's distribution of this small classroom dataset complies with the applicable Yahoo/source terms before expanding or commercially redistributing it. No secrets or personal account data are needed to run this app. No new license grant over third-party data is asserted here.
