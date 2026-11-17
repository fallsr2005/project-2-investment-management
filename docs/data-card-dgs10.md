# DGS10 point-in-time data card

**AI used:** ChatGPT/Codex helped organize this record from the completed Lab 17 evidence; I reviewed the source treatment and own the decision use.

**Education only — not investment advice.**

| Field | Record |
|---|---|
| Series and source | Federal Reserve Bank of St. Louis, [DGS10 — 10-Year Treasury Constant Maturity Rate](https://fred.stlouisfed.org/series/DGS10) |
| Measure and units | Daily 10-year Treasury constant-maturity rate, percent, not seasonally adjusted |
| Saved decision vintage | As known on 2026-09-30: latest observation was 2026-09-29 at 5.26% |
| Publication timing | The saved ALFRED vintage showed a one-business-day lag; weekends and holidays can create longer calendar gaps |
| Revisions | The application compares the ALFRED vintage to current FRED data. A nonzero same-date revision count requires a reassessment rather than substitution of today's history. |
| Download/source check | Completed Lab 17 checked 2026-10-23 = 5.00, 2026-10-26 = 5.00, and 2026-10-27 = 4.99 against FRED. |
| Project 2 use | A monitoring signal for the SCHR Treasury sleeve. It is **not** a price return, allocation optimizer input, or return forecast. |

## Point-in-time rule

For each committee decision, use only the ALFRED vintage available on that decision date. If that vintage is absent, its date is stale beyond the expected publication lag, or revisions are material to the decision, pause the process and re-run the review. Do not replace an old vintage with the current FRED series.

## Why it matters

A current series may contain observations or revisions unavailable when a historical decision supposedly occurred. Separating the measured date from the publication date avoids treating later information as if it had been actionable. DGS10 can help monitor interest-rate conditions relevant to SCHR; it does not establish future fund returns.
