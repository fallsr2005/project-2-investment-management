# DGS10 point-in-time data card

**AI used:** ChatGPT/Codex helped organize this record from the completed Lab 17 evidence; I reviewed the source treatment and own the decision use.

**Education only — not investment advice.**

| Field | Record |
|---|---|
| Series and source | Federal Reserve Bank of St. Louis, [DGS10 — 10-Year Treasury Constant Maturity Rate](https://fred.stlouisfed.org/series/DGS10) |
| Measure and units | Daily 10-year Treasury constant-maturity rate, percent, not seasonally adjusted |
| Reported decision vintage | Lab 17 notes report 2026-09-29 at 5.26% as known on 2026-09-30. Original response absent; not independently verified in this audit. |
| Publication timing | Lab notes report one business day of lag for this vintage; weekends and holidays can create longer gaps. Source response is required to substantiate this instance. |
| Revisions | The earlier Lab 17 application compared ALFRED to current FRED data. This Project 2 app displays the reported snapshot only; it does not download or count revisions. Do not infer zero revisions. |
| Download/source check | Lab 17 reports checking three values on 2026-10-29. This repository contains no raw response or independent capture proving those checks. |
| Project 2 use | A monitoring signal for the SCHR Treasury sleeve. It is **not** a price return, allocation optimizer input, or return forecast. |

## Point-in-time rule

**Audit status, 2026-11-19: unresolved source evidence.** Retrieval of the ALFRED CSV timed out. Preserve a successful response from [this exact vintage endpoint](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=DGS10&vintage_date=2026-09-30), retrieval timestamp, and hash, then verify the date/value against the app. If the source contradicts the note, correct the app and all current documents with a dated explanation. Do not manufacture a source response from the reported number. Until resolved, the monitoring signal is quarantined and adoption is paused.

For each committee decision, use only the ALFRED vintage available on that decision date. If that vintage is absent, its date is stale beyond the expected publication lag, or revisions are material to the decision, pause the process and re-run the review. Do not replace an old vintage with the current FRED series.

## Why it matters

A current series may contain observations or revisions unavailable when a historical decision supposedly occurred. Separating the measured date from the publication date avoids treating later information as if it had been actionable. DGS10 can help monitor interest-rate conditions relevant to SCHR; it does not establish future fund returns.
