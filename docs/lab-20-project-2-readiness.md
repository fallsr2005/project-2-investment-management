# Lab 20 — Project 2 Readiness

**Decision question:** Could a committee member who has never met me reach the Project 2 decision from this repository, and does that decision survive one changed input?

## Repository readiness

| Lab 20 requirement | Repository evidence | Status |
|---|---|---|
| Tool | `app.py` provides one interactive control set, mandate verdicts, two baselines, the constrained portfolio, and stress results | Locally verified |
| One-command run instructions | `README.md` contains the Streamlit command | Locally verified |
| Visible output | `visible_output.json` displays the mandate, inputs, base allocation, baselines, stress results, and DGS10 record without execution | Locally verified |
| Decision memo | `docs/decision-memo.md` agrees with the visible-output base result: 70% SGOV / 30% ACWI, 6.02% estimate, 4.56% volatility, and pilot recommendation | Locally checked |
| Validation and AI use | `docs/validation-and-ai-use.md` records sources, tests, standard stress evidence, limitations, AI use, and the required Locked Changed-Input structure | Locked record pending |
| Videos and transcripts | Recording guides and transcript placeholders exist in `docs/` | Pending recording, caption review, and upload |

## Cold run — partner entry required

This must be completed by a partner from the published GitHub repository. Do not replace it with an assisted run or claim this is complete before the partner does it.

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

This is a local preflight check only. The partner must still perform and document an independent cold run from the GitHub repository.

## Changed input — AI-closed student entry required

The Project 2 validation file contains the required Locked Changed-Input Record. For Lab 20, first close AI tools and choose a new load-bearing input that has not been run with AI assistance. Before the run, write the old and new value with units, expected direction of the decision numbers, and anticipated decision effect. Commit and push that prediction. Run once, preserve before/after output, then finish the reconciliation.

| Lab 20 check | Location | Status |
|---|---|---|
| Prediction written before run | `docs/validation-and-ai-use.md` | Recorded; prior AI discussion and reported instructor exception disclosed; AI-off compliance remains for instructor determination. |
| Immutable pre-run commit and GitHub push | Git history | `d49857a2c5e4b70b2493a2a5d837896d79b0a4c7`, pushed before the user-supplied run screenshots. |
| Before and after output saved | `docs/evidence/cost-45bp/` | Before and after screenshots preserved. |
| Actual decision effect and explanation | `docs/validation-and-ai-use.md` | Student confirms keeping the pilot subject to committee review, with reassessment before implementing the changed allocation. App remains feasible; weights change by 10 points and volatility rises. The memo's cost and pilot-range triggers require reassessment. |

## Code explanation — partner entry required

Open `constrained_portfolio` and `mandate_verdict` in `portfolio_engine.py`. Explain how the 5-point compositions become long-only weights, how the four mandate checks screen each mix, and why the lowest-volatility feasible result is retained. The partner asks one question; record it and the answer after the conversation.

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

**Pilot the process, not full adoption, while all mandated constraints remain feasible and no stress moves a base weight by more than 20 percentage points; reverse to pause/reject if feasibility fails, the DGS10 vintage is unusable, or the stability condition breaks.**

## Before deadline

Do not alter the human-authored changed-input prediction after its pre-run commit. Do not replace submitted videos, transcripts, visible output, or the recommendation after the deadline. Use `docs/submission-checklist.md` for the remaining Project 2 submission actions.
