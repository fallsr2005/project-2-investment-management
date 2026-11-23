AI used: ChatGPT/Codex assisted with code, tests, source capture, and documentation. I am responsible for reviewing the analysis and owning the decision. Prediction authorship and later formatting assistance are distinguished below.

Education only — not investment advice.

# Validation and AI use

## Submission record

The primary Locked Changed-Input Record is the student's **ACWI adjustment from 0.00 to -3.00 percentage points**. Its prediction, results, diagnosis, decision effect, and restoration evidence are indexed below. The earlier 45-basis-point cost exercise is supporting sensitivity evidence, not a substitute for the ACWI record.

The [historical validation record](validation-history-2026-11-22.md) preserves the preceding document verbatim, including the older cost prediction and dated audit states. Its obsolete instructions, smaller test counts, missing-source findings, and reported exception are historical. This document presents the submission's current evidence and limitations.

## Sources and timing

| Input | Evidence and boundary |
|---|---|
| ETF prices | `data/prices.csv`: SGOV, SCHR, USIG, ACWI; 60 completed monthly adjusted-price observations, October 2021–September 2026; 59 adjacent returns. First-of-month labels identify the month, not availability on that day. |
| Original retrieval | Lab 14/15 prose reports October 22, 2026. Bundled downloader/excerpts and the unchanged CSV in initial commit bea2f9e (November 17) support the lineage and preservation record; no original October raw response or authenticated retrieval timestamp was found. |
| Later price check | Four raw Yahoo chart responses captured November 22 at 23:38 UTC; exact months, ticker identities, source URLs, retrieval times, hashes, six-decimal reconstruction, and numerical comparison are preserved in the [price lineage](price-data-lineage.md). This verifies the later comparison, not the October vintage. |
| DGS10 | November 18 observation, 5.07%, in the ALFRED page captured November 20 at 06:08:22 UTC. The [data card](data-card-dgs10.md) defines admissibility and source verification. This is a frozen demonstration snapshot, not a live/latest value or proof of the earlier September claim. |
| Rights and privacy | DGS10 is tagged public domain with citation requested. Yahoo access/redistribution permission is not independently established, including for the existing public repository. No account data, credentials, or personal portfolios are needed. See the [source-limitation review](source-limitations-review.md). |

Adjusted-price returns are simple adjacent ratios minus one. Annual arithmetic mean is monthly mean × 12; annual sample volatility is monthly sample standard deviation × √12; covariance and correlations use the same aligned returns. The last-36-return option uses 37 prices. Implementation cost is an additional annual assumption subtracted from gross estimated return, not a second fund-expense deduction. Historical estimates do not establish future returns or investor suitability.

Labs 14–19 were inspected for supporting evidence. Labs 14–15 document the fund/source choices, arithmetic conventions, base/window results and earlier sensitivity reasoning. Lab 16 supplies the publication/vintage-filtering method; Lab 17 records three manual DGS10 checks, retained as lab-reported history in the data card. The labs supply no additional original October response or Yahoo permission evidence. The separate SEC company-screening exercises in Labs 18–19 do not establish ETF price provenance.

## Existing verification evidence

The last executed suite passed **17 tests**, including in an exported repository using the existing Python environment. This document review did not rerun the suite or app. It does not establish a fresh dependency installation. The [partner cold-run record](lab-20-project-2-readiness.md) reports a separate successful README-only run.

| Checks | Evidence and conclusion |
|---|---|
| Inputs and calculations | Invalid prices/dates rejected; correct 59/36-return windows; original saved results reproduced; single-asset volatility matches its input. |
| Mandate and baselines | Long-only, full investment, minimum SGOV, and net-return checks; both baselines carry failed-rule labels. |
| Cost sensitivity | Fixed base weights lose 0.45 percentage points under 45bp cost; reoptimization selects 60% SGOV / 40% ACWI, 6.32% net return and 6.03% volatility. The higher optimized net return does not contradict fixed-weight cost drag. |
| Governance and failure | Exactly 20 points produces selected-scenario REVIEW; more than 20 points produces STOP. A 100% SGOV floor is infeasible. Corrupted DGS10 evidence fails verification. |
| Price-source evidence | Raw hashes and exact month alignment checked; altered responses, wrong symbols, missing months, and null prices rejected. Later-source base weights and baseline verdicts are unchanged. |
| Packaging | Export checking exposed CSV line-ending conversion that changed its hash. `.gitattributes` now preserves input/source bytes; the subsequent exported copy passed all 17 tests. |

Reproduction commands, when a new run is wanted:

```powershell
python -m unittest discover -s tests -v
python audit_price_sources.py --snapshot data/source-evidence/prices-20261122T233854Z
python reproduce.py --output outputs/reproduced-results.json
```

The [November 20 reproduced report](../outputs/reproduced-results.json) records its own run timestamp, input hash, base/baselines, and standard/additional scenarios. The [original November 16 output](../visible_output.json) is historical and has superseded DGS10 provenance. Neither is presented as a newly executed report. ACWI -3pp execution is evidenced by the student's screenshots below.

## Locked Changed-Input Record: ACWI -3 percentage points

| Required item | Preserved evidence |
|---|---|
| Human authorship | The student states the prediction was independently written with AI off and that the comparison, explanation, and decision effect are their own words. |
| Immutable prediction | [Original prediction file](changed-input-prediction-acwi.md), locked at [commit 054f0d3](https://github.com/fallsr2005/project-2-investment-management/commit/054f0d3a82d62a772c13f495ccc084646d1df2af), November 22, 2026 at 17:54:09 Eastern. The commit was pushed before the student supplied changed-run screenshots. No original prediction wording has been edited. |
| Exact input/units | ACWI annual-return adjustment, 0.00 → -3.00 percentage points. All 59 returns, 10% minimum SGOV, zero implementation cost, and the saved CSV held unchanged. |
| Expected direction/magnitude | ACWI 45–55%, SGOV 45–55%, SCHR/USIG near zero; volatility approximately 7–9%; net return approximately 6.00–6.40%, conditional on feasibility. See the original file for the student's full reasoning and expected decision effect. |
| Actual output | ACWI 30% → 50%; SGOV 70% → 50%; SCHR/USIG remain zero. Net estimate 6.02% → 6.01%; volatility 4.56% → 7.50%; largest weight change 20 percentage points. Mandate PASS; selected-scenario decision PILOT → REVIEW. |
| Diagnosis and actual decision effect | The student's [comparison, explanation, and decision effect](changed-input-results-acwi.md) distinguish feasibility from governance approval: weights/volatility were within predicted ranges, but the app explicitly requires REVIEW at exactly 20 points and outside the 65–75% SGOV candidate band. Committee reassessment is required before using the changed allocation. |
| Before/after/reset proof | [Nine original screenshots](changed-input-results-acwi.md#evidence-index) cover all three stages. Reset returns ACWI adjustment to 0.00, allocation to 70/30 SGOV/ACWI, net estimate to 6.02%, volatility to 4.56%, and numerical status to PILOT. |
| Later assistance | After the student supplied their wording, Codex formatted headings/bullets, saved and pushed the prediction, acknowledged screenshots/section structure, and assembled the results report. The student supplied the reasoning; this assistance is disclosed rather than attributed to independent authorship. Screenshot capture times and the AI-off working conditions are not independently authenticated by this repository. |

The older cost exercise and its prior AI discussion remain in the historical validation record and Git history. No instructor exception is claimed for the new ACWI exercise, and no new instructor-approval requirement is introduced here. The instructor assesses the submitted evidence under the course rule.

## Material AI use and disposition

| Date | Tool/model information | Material use and disposition |
|---|---|---|
| Earlier labs / November 16 | ChatGPT/Codex; exact versions unavailable in the preserved initial record | Assisted with lab calculations, standalone app structure, tests, and documentation drafts. These contributions require student understanding; the student's recommendation remains their responsibility. |
| November 19–20 | Codex; historical log reports exposed model `gpt-6.1-sol` | Audited requirements and corrected unconditional pilot messaging, stop/review boundaries, candidate-range wording, and DGS10 provenance. Historical test/cleanup limitations are retained in the archive. |
| November 22: student exercise | ChatGPT/Codex; exact model/version not exposed in this session | Mechanical formatting and Git assistance after student-supplied prediction; later assembly of student-supplied interpretation and screenshots. No prediction evaluation or changed-input execution was performed in that exchange. |
| November 22: source/package audit | ChatGPT/Codex; exact model/version not exposed in this session | Captured later vendor evidence, wrote the lineage audit and three failure/evidence tests, fixed byte preservation, and aligned documentation and recording guides. This review used existing artifacts rather than rerunning tests. |
| November 22: Video 1 preparation | ChatGPT/Codex; exact model/version not exposed in this session | Prepared a timed spoken rehearsal script and exact screen actions using existing memo history and student experiment evidence; added recording/upload/caption instructions. The script is disclosed AI assistance, not an actual transcript or evidence of a completed recording. |
| November 23: Video 1 captions | ChatGPT/Codex; exact model/version not exposed in this session | Reviewed student-supplied SRT files and saved 23 timestamped cues as the Video 1 text transcript, normalizing whitespace only. Corrected-range captions and a complete ending were supplied by the student. The student confirmed saying “restoration advice”; that spoken wording is retained. The student subsequently confirmed successful audio/visual/access/duration checks; these checks were not independently observed by Codex. No script wording was substituted for speech. |

Specific AI-assisted outputs corrected or qualified during review:

- **Unconditional PILOT:** infeasibility and material changes must produce STOP/REVIEW; source-code branches and recorded app states support the correction.
- **All candidates in a 65–75% SGOV band are feasible:** the 75/25 endpoint estimates only 5.65% before cost. The base-feasible grid subset is 65–70% SGOV paired with 30–35% ACWI.
- **A later DGS10 capture proves the September vintage:** it proves only what was captured at its actual retrieval boundary. The unsupported historical claim remains explicitly qualified.

An additional evidence boundary is explicit: an input hash identifies bytes; the later raw-response comparison supplies separate, dated corroboration. This is a validation principle, not a claim that the student independently rejected a specific earlier AI answer.

These are documented review dispositions, not a claim that the student independently performed each AI-assisted audit.

## Decision limits and remaining deliverables

The recommendation remains a conditional three-month classroom process pilot, reviewed monthly, centered on 70% SGOV / 30% ACWI. The selected ACWI stress requires REVIEW. A mandate PASS is not committee authorization. Exactly 20 points in the fixed window stress remains a sensitivity requiring human reassessment; the base selected scenario still displays PILOT.

The historical sample is short; estimates, adjusted prices, and correlations can change. Taxes, turnover, bid-ask spreads, drawdown, personal liquidity needs, and realized performance are omitted. The 5-point grid is discrete. The 6% hurdle and 10% SGOV floor are classroom assumptions. Original-vintage and third-party-rights gaps remain open and restrict claims; disclosure does not cure them. DGS10 evidence must be refreshed and preserved for a later decision, and its timestamp check does not automatically test freshness or revision history.

Video 1's YouTube link and complete student-supplied captions are recorded in the manifest; its text transcript is saved. The student confirmed the spoken “restoration advice” wording and successful audio/visual/access checks, and reported a YouTube runtime of **2:42**, within the 3:00 limit. These are student-reported checks; Codex did not independently view the recording. The last supplied caption ends at **2:44.080**, exceeding that reported runtime; caption timing must be reconciled with the final upload before freeze. No spoken wording or caption timing was silently changed to conceal the mismatch. Videos 2–3 and their corrected actual transcripts/captions, remaining manifest fields, final repository access/freeze checks, and Brightspace submission remain outstanding. See the [submission checklist](submission-checklist.md). Recording guides are preparation materials, not actual transcripts.
