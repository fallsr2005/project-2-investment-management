AI used: ChatGPT/Codex assisted with code structure, tests, documentation, and this disclosure; I must review the analysis and own the decision.

Education only — not investment advice.

# Validation and AI use

## Additional ACWI changed-input evidence — 2026-11-22

The student supplied a new ACWI annual-return-adjustment prediction (0.00 to -3.00 percentage points), followed by before/after screenshots, their own comparison, explanation, actual decision effect, and screenshots proving restoration to base. See the [unchanged pre-run prediction](changed-input-prediction-acwi.md) and [results, provenance, and nine evidence screenshots](changed-input-results-acwi.md). The prediction was committed and pushed at `054f0d3a82d62a772c13f495ccc084646d1df2af` before the changed-run screenshots were supplied. The selected result was 50% SGOV / 50% ACWI, 6.01% estimated net return, 7.50% volatility, PASS mandate verdict, and REVIEW numerical decision; restoration returned to 70% SGOV / 30% ACWI and PILOT.

The student states the prediction and after-run wording are their own. Codex formatted and committed the prediction at the student's request, acknowledged evidence during the chat, and assembled the linked results report after restoration. This is evidence of student-supplied work and preserved execution, not a certification that the AI-off requirement was met. Instructor interpretation remains unresolved. The original cost prediction and historical evidence below remain unchanged.

## Scope and as-of boundaries

| Item | Record |
|---|---|
| Portfolio-price source | Yahoo Finance monthly adjusted-close history for SGOV, SCHR, USIG, and ACWI; downloaded 2026-10-22 in the completed Lab 14/15 work |
| Price history used | 60 monthly observations from 2021-10-01 through 2026-09-01; 59 adjacent monthly simple returns |
| Estimation method | Arithmetic mean monthly return × 12; sample standard deviation × √12; correlations from the same return series |
| Signal source | Federal Reserve Bank of St. Louis DGS10; current source-page response captured 2026-11-20 at 06:08 UTC; see [data-card-dgs10.md](data-card-dgs10.md) |
| Decision boundary | Current review uses November 18 at 5.07%, supported only at or after the capture timestamp. The old September claim remains unverified in historical records. DGS10 is monitoring-only. |

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

## Locked Changed-Input Record — prediction and observed result

**Status: prediction committed before the selected run; screenshots and after-run reconciliation recorded.** The student supplied the prediction below and confirmed the terms “net return” and “more than 20 percentage points.” Codex transcribed it into this record. The cost scenario and prediction reasoning were discussed in this chat before the prediction commit. The student reports an instructor-approved exception; compliance with the AI-off requirement remains for instructor determination. No AI-off attestation is made here.

After this prediction is committed and pushed, close AI tools, preserve the base output, run the 0.45% annual-cost scenario, and preserve its output. Complete the after-run table using the actual results. Retain this prediction unchanged.

| Required field | Student entry before the run |
|---|---|
| Timestamp and immutable Git commit | Recorded 2026-11-17 at 17:10 Eastern; the commit titled `Record student cost prediction before run` locks this text. Its hash will be recorded separately after committing. |
| Exact input and units | Annual implementation-cost stress, percent per year; all 59 monthly returns, 10% minimum SGOV reserve, and zero ACWI return adjustment held fixed. |
| Old value → new value | 0.00% → 0.45% annually (45 basis points). |
| Student-supplied prediction of output direction | “I think that the net return estimate is going to decrease because the costs are taken away/subtracted from the gross return estimate. My app may select a different allocation to meet the 6.0% net return target which could maybe increase volatility. If no allocation qualifies, it should report no feasible portfolio.” |
| Predicted decision effect | “Probably keep the pilot suggestion if the calculated portfolio stays feasible and between the stability limit. If no portfolio qualifies, I would stop, pause and reassess if that happened or if the allocation weight changes by more than 20 percentage points from the base case.” |

| Required field | Student entry after the run |
|---|---|
| Exact output before → after, with units | User-supplied screenshots show annual cost 0.00% → 0.45%; SGOV 70% → 60%; ACWI 30% → 40%; SCHR and USIG remain 0%. Gross annual return estimate 6.02% → 6.77%; net annual return estimate 6.02% → 6.32%; annual volatility 4.56% → 6.03%. Mandate verdict remains PASS. Largest allocation change: 10 percentage points. |
| Actual decision effect | Student-confirmed judgment, adopting wording proposed by Codex after the run: “I would keep the pilot recommendation, subject to committee review. The portfolio still meets the 6% net-return target, and its weights changed by 10 percentage points, below the 20-point stability limit. However, the higher volatility and 60% SGOV / 40% ACWI allocation fall outside my original pilot range, so I would reassess before implementing the new allocation.” The allocation is outside the memo's 65–75% SGOV range; volatility is higher (the memo specifies no separate volatility range). The 45-basis-point cost also exceeds its 25-basis-point cost review trigger. |
| Prediction reconciliation and failure diagnosis, if different | Allocation changed and volatility increased as anticipated. The optimized net estimate increased rather than decreased: the search moved more weight into ACWI to meet the net target. Holding the original allocation fixed would instead reduce its net estimate from about 6.02% to 5.57%, failing the 6.0% hurdle. The 5-point grid then selected a higher-gross-return allocation, which cleared the target after costs. This distinguishes cost drag on fixed weights from the result after optimization. The standard stress suite is fixed and does not change with the sidebar cost control; the selected scenario is shown in the top portfolio table. |
| Preserved evidence location | [Before screenshot](evidence/cost-45bp/before.png) and [after screenshot](evidence/cost-45bp/after.png), supplied by the student after prediction commit `d49857a2c5e4b70b2493a2a5d837896d79b0a4c7` was pushed. This after-run interpretation was documented with Codex assistance. |

## Audit addendum — 2026-11-19

The audit leaves the original pre-run prediction and screenshots preserved in their commits. It adds 12 passing calculation/regression tests, including agreement with the original base output, cost reoptimization, and STOP/REVIEW boundaries. `reproduce.py` creates `outputs/reproduced-results.json` with the price-file SHA-256, input estimates/correlations, baseline checks, selected scenarios, and run timestamp. This is a later verification run, not a replacement for the student's protected execution.

The app previously always displayed pilot even under infeasible selected settings; the current app applies STOP/REVIEW/PILOT numerical rules and separately pauses adoption for the missing DGS10 source response. The SGOV constraint control can now tighten from the mandate's 10% floor to 100%, without silently relaxing it. The memo now distinguishes a candidate review band from the subset meeting the return hurdle.

DGS10 provenance is unresolved: the original ALFRED response is not in the repository and the audit download timed out. The 5.26% observation is inherited from Lab 17 prose, not independently verified. The app does not perform live vintage comparisons. See the data card before relying on it. Likewise, the price download date is inherited from the lab record; the saved-price hash establishes which input was used, not independent vendor authenticity.

AI use in this audit: Codex (exposed model gpt-6.1-sol) reviewed official course requirements, inspected code/documents, proposed and implemented corrections, wrote regression tests and reproduction tooling, and prepared the requirement audit. Earlier model/version details are not available in the preserved record and are not inferred. Student review remains required.

The public assignment references a 300-point analytic rubric. Both attempted rubric paths returned 404 and the current GitHub file tree contained no rubric file. The submission architecture's six categories were inspected, but precise point levels could not be verified. Check the Brightspace rubric before final submission.

Streamlit's app test exercised the base case (PILOT numerical status), 0.45% annual cost (REVIEW), and 100% SGOV floor (STOP), with no application exceptions. The test harness reported a Windows permission error while cleaning up its own temporary folder after completion; this does not establish a clean fresh-environment installation. The partner cold-run note remains the available independent setup evidence.

## Limitations

## Completion addendum — 2026-11-20

The current ALFRED page download succeeded on retry and is preserved in `data/source-evidence/` with UTC retrieval metadata and SHA-256 `9a2017ca4195f97c8246fa92112cdff6c3fac4a94d06c72177b5d73f31da80e1`. The source response reports November 18 at 5.07% and source update November 19 at 15:16 CST. `verify_signal_evidence()` verifies the response hash and parses the displayed observation; failure stops operational use. This closes the current-review snapshot evidence gap but does not validate the old September claim or establish a historical backtest. The dated November 19 addendum above records the earlier unresolved state.

The supplied Brightspace rubric is now mapped in `rubric-evidence-map.md`: maximum 300; six maxima 45/45/60/45/75/30. The model exposed for this work is gpt-6.1-sol. Codex assisted with the source capture, new source-verification check, recording scripts, and rubric mapping. The proposed three-month pilot and monthly cadence are explicit classroom assumptions requiring student/committee review.

The original prediction is locked at `d49857a2c5e4b70b2493a2a5d837896d79b0a4c7`. No after-run wording or source correction rewrites that historical commit. Source-verification and corrupted-source rejection bring the suite to 14 tests. Current results are reproduced in `outputs/reproduced-results.json`; the original November 16 output is a historical snapshot with superseded signal provenance. Price-data transformations and remaining vendor-source limitations are documented in `price-data-lineage.md`.

### Remaining financial limitations

Student approval recorded November 20, 2026 at 07:52 UTC: after discussing the recommendation with Codex, the student confirmed agreement with a three-month classroom pilot, monthly reviews, the base allocation and candidate range, and review/stop triggers. The student understands that this period evaluates the process and cannot validate an annual return promise. This approval does not resolve the separate instructor ruling on the protected prediction or certify independent verification of every source.

Package verification: the committed source was exported using `git archive` and extracted into a separate local folder. All 14 tests passed there, including the exact raw-source hash check. This verifies tracked-file completeness with the existing Python environment; it is not a new dependency installation or a replacement for the partner cold run. The final app test also verified the source-success banner, REVIEW at 45bp, and STOP at a 100% SGOV floor without app exceptions. Streamlit's test harness again emitted a temporary-directory cleanup permission error after completion; no Windows security setting was changed.

- Historical mean returns, volatility, and correlations are uncertain and are not forecasts.
- Yahoo adjusted closes can be revised; the saved data does not prove it was available at a particular historical trading time.
- The 5-point grid is not a continuous optimizer.
- The model does not cover taxes, turnover, bid-ask spreads, drawdown, investor-specific cash needs, or realized performance.
- A passing mandate calculation does not establish that the 6.0% hurdle or reserve floor is appropriate.
