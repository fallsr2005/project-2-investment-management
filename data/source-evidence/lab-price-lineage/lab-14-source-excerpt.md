## Thursday preparation: selected fund universe

The following working selection covers the four roles in the course instructions. The personal Project 2 mandate has not been supplied, so the selection must be checked against its actual roles and constraints. These are practice funds, not recommendations.

| Ticker | Fund | Role | Adjusted-price source |
|---|---|---|---|
| SGOV | iShares 0-3 Month Treasury Bond ETF | Cash and reserve proxy | [Yahoo Finance history](https://finance.yahoo.com/quote/SGOV/history/) |
| SCHR | Schwab Intermediate-Term U.S. Treasury ETF | Government bonds | [Yahoo Finance history](https://finance.yahoo.com/quote/SCHR/history/) |
| USIG | iShares Broad USD Investment Grade Corporate Bond ETF | Investment-grade fixed income | [Yahoo Finance history](https://finance.yahoo.com/quote/USIG/history/) |
| ACWI | iShares MSCI ACWI ETF | Broad global equity | [Yahoo Finance history](https://finance.yahoo.com/quote/ACWI/history/) |

The managers describe [SGOV's Treasury-bill exposure](https://www.ishares.com/us/products/314116/ishares-0-3-month-treasury-bond-etf-sgov), [SCHR's intermediate-term Treasury exposure](https://www.schwabassetmanagement.com/products/schr), [USIG's investment-grade corporate bonds](https://www.ishares.com/us/literature/fact-sheet/usig-ishares-broad-usd-investment-grade-corporate-bond-etf-fund-fact-sheet-en-us.pdf), and [ACWI's developed and emerging market stocks](https://www.ishares.com/us/products/239600/ishares-msci-acwi-etf?qt=ACWI).

`prices.csv` contains 60 monthly adjusted close observations per ticker, October 2021–September 2026, downloaded October 22, 2026 from Yahoo Finance's chart endpoint by `download_prices.py`. The date is the first day of the labeled month; the value is Yahoo's monthly adjusted close for that month, not a price observed on that date. Adjusted closes incorporate distribution and split adjustments and may be revised by the provider. Months are oldest first, with matching observations and no missing values. The 60 observations produce 59 adjacent monthly returns; a full 60-month return series would require an additional preceding price.
