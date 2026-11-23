# DGS10 point-in-time monitoring data card

AI used: Codex assisted with source capture, verification code, and documentation; the student must review the analysis and owns the decision.

Education only — not investment advice.

| Field | Frozen demonstration record |
|---|---|
| Source / ID | Federal Reserve Bank of St. Louis [ALFRED DGS10](https://alfred.stlouisfed.org/series?seid=DGS10); underlying source Board of Governors, H.15 |
| Definition | Market yield on US Treasury securities at 10-year constant maturity, quoted on an investment basis |
| Units / frequency | Percent per year; daily; not seasonally adjusted |
| Observation | 2026-11-18 = 5.07% |
| Source update time | 2026-11-19 at 15:16 CST, stated in the saved page's dataset metadata |
| Capture boundary | 2026-11-20 at 06:08:22 UTC (01:08:22 Eastern); no claim that this capture was available before that timestamp |
| Raw evidence | [Saved source page](../data/source-evidence/dgs10-20261120T060822Z.html) and [retrieval metadata](../data/source-evidence/dgs10-20261120T060822Z.html.json) |
| SHA-256 | `9a2017ca4195f97c8246fa92112cdff6c3fac4a94d06c72177b5d73f31da80e1` |
| Transformation | Parse the latest observation date/value from the captured HTML; retain percent units without annualizing or treating yield as fund return |
| Publication timing | The saved page's update is one day after the measured observation. At capture time the measured date was two calendar days earlier. This instance does not establish a universal publication lag. |
| Revisions | One captured page does not establish whether an observation was revised. Freeze this capture for this review; use archived vintages for any historical decisions. |
| Exclusions | No current-history substitution for historical vintages; no rate-to-return conversion; no missing-value imputation |
| Decision use | Monitoring information for Treasury-rate conditions relevant to SCHR; not an optimizer input, trading rule, or performance forecast |

## Admission and stop rule

Admit the observation only for the dated demonstration review at or after the capture boundary. `verify_signal_evidence()` checks the stored SHA-256 and the actual parsed date/value. Missing, altered, or inconsistent evidence stops the operational recommendation. A later committee decision must preserve a new admissible snapshot and inspect publication timing and any revision issue before use. The app does not automatically refresh, check freshness, compare revision histories, or establish that this snapshot is live/latest. A successful hash/date/value check is not a freshness certification.

## Earlier claim and correction

The reviewed Lab 17 record also reports a manual source check on October 29: October 23 = 5.00%, October 26 = 5.00%, and October 27 = 4.99%. These are preserved lab-reported checks, not independently authenticated raw responses or checks of the November observation. They support the documented checking process without replacing the dated capture above. Lab 16's fictional training table illustrates publication-date/vintage filtering; its values are not Project 2 market inputs.

Lab 17 prose reported 2026-09-29 at 5.26% as known on September 30, but its original vintage response was not preserved here. Attempts to retrieve that historical CSV failed. The original Lab 20 screenshots remain historical evidence, but their displayed DGS10 claim is not independently validated. The current Project 2 app uses the newly captured observation above instead. This is a dated source correction, not proof of the September vintage, and does not change the portfolio arithmetic because DGS10 is monitoring-only.

## Rights and privacy

The ALFRED page identifies the underlying series as public domain with citation requested. Attribute the Board of Governors and Federal Reserve Bank of St. Louis. The source page contains ordinary public web markup; no account credentials or personal account information are needed. `capture_signal.py` records a new response and timestamp; it cannot recreate an old vintage.
