AI used: ChatGPT/Codex assisted with code structure, tests, documentation, and this disclosure; I must review the analysis and own the decision.

Education only — not investment advice.

# Validation and AI use

## Scope and as-of boundaries

| Item | Record |
|---|---|
| Portfolio-price source | Yahoo Finance monthly adjusted-close history for SGOV, SCHR, USIG, and ACWI; downloaded 2026-10-22 in the completed Lab 14/15 work |
| Price history used | 60 monthly observations from 2021-10-01 through 2026-09-01; 59 adjacent monthly simple returns |
| Estimation method | Arithmetic mean monthly return × 12; sample standard deviation × √12; correlations from the same return series |
| Signal source | Federal Reserve Bank of St. Louis DGS10, saved ALFRED vintage as known on 2026-09-30; see [data-card-dgs10.md](data-card-dgs10.md) |
| Decision boundary | DGS10's latest saved observation was 2026-09-29 at 5.26%; it is a monitoring signal, not a return forecast or portfolio optimizer input |

## Tests and results

Run from the repository root:

```powershell
python -m unittest discover -s tests -v
```

| Test | Result |
|---|---|
| CSV accepts the fixed four-ticker universe and 60 saved dates | Pass |
| All-history estimate uses 59 returns; short window uses 36 returns | Pass |
| Base constrained portfolio is feasible and its weights sum to 100% | Pass |
| Equal-weight and 60/40 benchmark both return explicit mandate verdicts | Pass |
| Weight-change function identifies a 20-percentage-point difference | Pass |
| Manual source check from Lab 17: three DGS10 observations matched the FRED page | Recorded in the DGS10 data card |

The standard app stress suite changes the ACWI estimate, historical window, annual cost, and SGOV constraint. Its results are saved in [visible_output.json](../visible_output.json). A failure to find a feasible allocation, or a weight move greater than 20 percentage points from base, is the stop condition. The observed 20-point all-history/last-36 difference is escalated for committee review.

## Material AI use and disposition

| Interaction date | Tool/model | Material use | Disposition and human responsibility |
|---|---|---|---|
| 2026-11-16 | ChatGPT/Codex | Created the standalone Streamlit structure, reusable portfolio engine, tests, documentation drafts, and recording guides using the student's Lab 13–19 files | Code and claims require student review. The student must verify every source, choose the recommendation, write the AI-off prediction, record the videos, and submit the work. |
| Earlier labs | AI assistance documented in the saved lab files | Helped develop lab code and explanations | Prior work is retained as project evidence; it does not substitute for this project's validation record. |

## Locked Changed-Input Record — not yet complete

**Status: pending required student action.** This record cannot be truthfully completed by an AI because the prediction must be human-authored with AI off and committed before the selected test is run. Do not submit this template as a completed record.

1. Close generative-AI tools. Choose a **new material input change that has not already been run or discussed with AI**.
2. In the fields below, write the prediction yourself, commit this Markdown file, and record the immutable commit ID.
3. Only then run the app once with the exact old/new values. Paste the app's before/after result, state the actual decision effect, and explain any divergence from the prediction.

| Required field | Student entry before the run |
|---|---|
| Timestamp and immutable Git commit | **PENDING** |
| Exact input and units | **PENDING** |
| Old value → new value | **PENDING** |
| Human-authored AI-off prediction of output direction | **PENDING** |
| Predicted decision effect | **PENDING** |

| Required field | Student entry after the run |
|---|---|
| Exact output before → after, with units | **PENDING** |
| Actual decision effect | **PENDING** |
| Prediction reconciliation and failure diagnosis, if different | **PENDING** |
| Preserved evidence location | **PENDING** |

## Limitations

- Historical mean returns, volatility, and correlations are uncertain and are not forecasts.
- Yahoo adjusted closes can be revised; the saved data does not prove it was available at a particular historical trading time.
- The 5-point grid is not a continuous optimizer.
- The model does not cover taxes, turnover, bid-ask spreads, drawdown, investor-specific cash needs, or realized performance.
- A passing mandate calculation does not establish that the 6.0% hurdle or reserve floor is appropriate.
