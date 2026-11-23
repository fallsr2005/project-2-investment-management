# Lab 20 — Project 2 Readiness

Current status: this file retains the student-reported partner work and earlier preflight history. The primary locked exercise is now the [ACWI record](validation-and-ai-use.md), with before/after/restoration evidence; the earlier cost exercise is supporting history. The current submission audit is [project-2-requirement-audit.md](project-2-requirement-audit.md). Historical partner DGS10 claims do not replace the later corrected data card.

**Decision question:** Could a committee member who has never met me reach the Project 2 decision from this repository, and does that decision survive one changed input?

## Repository readiness

| Lab 20 requirement | Repository evidence | Status |
|---|---|---|
| Tool | `app.py` provides one interactive control set, mandate verdicts, two baselines, the constrained portfolio, and stress results | Locally verified |
| One-command run instructions | `README.md` contains the Streamlit command | Locally verified |
| Visible output | `outputs/reproduced-results.json` is the November 20 corrected-source report; `visible_output.json` is the historical November 16 report | Preserved; timestamps identify each run |
| Decision memo | `docs/decision-memo.md` agrees with the visible-output base result: 70% SGOV / 30% ACWI, 6.02% estimate, 4.56% volatility, and pilot recommendation | Locally checked |
| Validation and AI use | `docs/validation-and-ai-use.md` indexes the primary ACWI prediction, student explanation, decision effect, nine screenshots and reset proof | Evidence assembled; student authorship and later assistance distinguished |
| Videos and transcripts | Recording guides and transcript placeholders exist in `docs/` | Pending recording, caption review, and upload |

## Cold run — recorded partner report

The student reported the partner run below from the published repository. This is the preserved report, not a newly observed independent run of the final package.

**Partner protocol:** send only the repository URL. The partner clones it into their own folder, follows only `README.md`, and then enters the following facts.

| Required fact | Partner entry |
|---|---|
| Repository URL tested | `https://github.com/fallsr2005/project-2-investment-management` |
| Exact command used | `cd project-2-investment-management`; `python -m venv .venv`; `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`; `.\.venv\Scripts\python.exe -m streamlit run app.py` |
| First failure, or `none` | None |
| Elapsed time | 3 minutes 22 seconds from opening the repository to the running app |
| Where the visible decision result appeared | Streamlit in the browser at `http://localhost:8504`; it displayed the constrained 70% SGOV / 30% ACWI allocation, baseline verdicts, DGS10 signal, stress suite, and pilot decision. |
| Fix made after the cold run, or `No fix needed; cold run clean` | No fix needed; cold run clean. |
| Rerun result after the fix | Not applicable; the first cold run was clean. |

## Local preflight fix — does not replace the partner cold run

On 2026-11-17, a local app launch using the parent `FIN_43900/.venv` failed because Windows Application Control blocked Pandas/PyArrow's binary `_compute` component. The Project 2 app did not need Pandas, so `app.py` was changed to render its three result tables with Markdown rather than Pandas dataframes. The standalone app test then completed with zero app exceptions and zero displayed errors; all five portfolio-engine tests passed. The fix was committed and pushed as `8919427` (`Remove blocked Pandas dependency`).

This is a historical local preflight check only. The separate partner report is recorded above; the local check does not replace it.

## Changed input — historical cost exercise

The following table preserves the earlier cost exercise and its disclosures. It is not an instruction to repeat or rewrite that prediction. The primary submission record is the later [student-authored ACWI prediction](changed-input-prediction-acwi.md) at commit 054f0d3, with the [results and nine before/after/restored screenshots](changed-input-results-acwi.md). The student states the ACWI prediction was independently written with AI off; later formatting/Git assistance is disclosed separately.

| Lab 20 check | Location | Status |
|---|---|---|
| Prediction written before run | `docs/validation-history-2026-11-22.md` | Historical cost record; prior AI discussion and reported instructor exception retained. Not the primary ACWI exercise. |
| Immutable pre-run commit and GitHub push | Git history | `d49857a2c5e4b70b2493a2a5d837896d79b0a4c7`, pushed before the user-supplied run screenshots. |
| Before and after output saved | `docs/evidence/cost-45bp/` | Before and after screenshots preserved. |
| Actual decision effect and explanation | `docs/validation-history-2026-11-22.md` | Historical cost exercise: student confirmed retaining a pilot subject to committee review; weights changed by 10 points and volatility rose. Current ACWI decision effect is documented separately. |

## Code explanation — recorded partner report

The recorded exchange concerned `constrained_portfolio` and `mandate_verdict`: 5-point compositions become long-only weights, mandate checks screen each mix, and the lowest-volatility feasible result is retained. The student-reported question and answer follow; they are not a verbatim transcript.

| Required fact | Student entry |
|---|---|
| Partner question | Student reports that the partner asked while looking at the code: “Why did the portfolio's net-return estimate increase when you increased its implementation cost?” |
| Answer from the code | Student reports explaining in their own words that costs reduce net return at fixed weights, but the app searches again after costs change. ACWI increased from 30% to 40%, raising gross estimated return enough to cover the higher cost; the selected net estimate increased from 6.02% to 6.32% and volatility also increased. `net = gross - annual_cost` applies the cost, and `constrained_portfolio` searches the feasible allocations again. This is a summary of the student-reported response, not a verbatim transcript. Codex supplied a study explanation during this discussion; an entirely AI-closed exchange is not independently verified. |
| Role swap | Student confirms swapping roles and listening to the partner explain their code. |

## Reflection

| Prompt | Student response |
|---|---|
| What did the cold run reveal that you could not see? | Student-approved reflection, with Codex assistance in wording: “The cold run helped me learn that I can use Codex to run another person's app from their repository by following their README. My partner also ran my app successfully without encountering a failure.” |
| What will you keep unchanged before the deadline? | Student-approved reflection: “Before the deadline, I will keep my committed prediction and original before-and-after screenshots unchanged so the evidence accurately preserves the test.” |

## Decision line

**Conditional classroom process pilot only.** A mandate PASS is not committee authorization; the recorded ACWI -3pp result requires REVIEW. Pause for infeasibility, a selected/fixed-suite weight move greater than 20 points, or failed source verification. Selected exactly-20-point moves, cost above 25bp, and SGOV outside the original candidate review band require reassessment. The frozen DGS10 capture and open price-vintage/rights limitations restrict use as documented in the current memo.

## Before deadline

Do not alter the human-authored changed-input prediction after its pre-run commit. Do not replace submitted videos, transcripts, visible output, or the recommendation after the deadline. Use `docs/submission-checklist.md` for the remaining Project 2 submission actions.
