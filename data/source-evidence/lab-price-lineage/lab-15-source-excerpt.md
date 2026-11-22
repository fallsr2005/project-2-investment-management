## R — Inputs and mandate

| Input | Meridian training case | Project 2 working universe |
|---|---|---|
| Assets | Treasury bills, Treasury 10-year note, investment-grade bond fund, global equity index fund | SGOV, SCHR, USIG, ACWI (roles below) |
| Returns, volatilities, correlations | Lab 14's course-authored assumptions in `portfolio.py` | To be estimated from monthly adjusted closes in `prices.csv`; historical estimates, not forecasts |
| Expected-return objective | 6.5% | At least 6.0% annual expected return |
| Hard constraint | At least 3% in reserve-eligible bills and 10-year Treasury note | At least 10% in SGOV |

The Project 2 selection covers the four roles in the [Project 2 mandate](Project%202%20-%20Investment%20Mandate.md). Its target and constraint are classroom choices, created for this project rather than drawn from the Meridian case.

| Ticker | Fund | Working role | Monthly adjusted-price source | Download date |
|---|---|---|---|---|
| SGOV | iShares 0–3 Month Treasury Bond ETF | Cash and reserve proxy | [Yahoo Finance](https://finance.yahoo.com/quote/SGOV/history/) | 2026-10-22 |
| SCHR | Schwab Intermediate-Term U.S. Treasury ETF | Government bonds | [Yahoo Finance](https://finance.yahoo.com/quote/SCHR/history/) | 2026-10-22 |
| USIG | iShares Broad USD Investment Grade Corporate Bond ETF | Investment-grade fixed income | [Yahoo Finance](https://finance.yahoo.com/quote/USIG/history/) | 2026-10-22 |
| ACWI | iShares MSCI ACWI ETF | Broad global equity | [Yahoo Finance](https://finance.yahoo.com/quote/ACWI/history/) | 2026-10-22 |

`prices.csv` contains 60 consecutive monthly observations, October 2021 through September 2026, with date first and oldest month first. The date labels the first of each month; the value is the source's monthly adjusted close, not a price observed on the first. Sixty prices yield 59 monthly returns. Adjusted closes incorporate distributions and splits and may be revised by Yahoo.
