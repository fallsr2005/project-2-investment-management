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
| AI-off prediction written before run | `docs/validation-and-ai-use.md` | **PENDING** |
| Immutable pre-run commit and GitHub push | Git history | **PENDING** |
| Before and after output saved | `visible_output.json` or a dated output artifact | **PENDING** |
| Actual decision effect and explanation | `docs/validation-and-ai-use.md` | **PENDING** |

## Code explanation — partner entry required

Open `constrained_portfolio` and `mandate_verdict` in `portfolio_engine.py`. Explain how the 5-point compositions become long-only weights, how the four mandate checks screen each mix, and why the lowest-volatility feasible result is retained. The partner asks one question; record it and the answer after the conversation.

| Required fact | Student entry |
|---|---|
| Partner question | **PENDING** |
| Answer from the code | **PENDING** |

## Decision line

**Pilot the process, not full adoption, while all mandated constraints remain feasible and no stress moves a base weight by more than 20 percentage points; reverse to pause/reject if feasibility fails, the DGS10 vintage is unusable, or the stability condition breaks.**

## Before deadline

Do not alter the human-authored changed-input prediction after its pre-run commit. Do not replace submitted videos, transcripts, visible output, or the recommendation after the deadline. Use `docs/submission-checklist.md` for the remaining Project 2 submission actions.
