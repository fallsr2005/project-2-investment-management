AI used: ChatGPT/Codex assisted with code, tests, source checks, documentation, and this presentation draft. I am responsible for reviewing the analysis and owning the decision.

Education only — not investment advice.

# Video 2 — code walkthrough, test, and reproduction

This is a rehearsal script with exact screen actions, **not an actual transcript**. Maximum **5:00**; aim for **4:20–4:45**. Timings are rehearsal targets, not a measured recording. Speak naturally while pointing to the actual code and output; adapt personal statements to what you understand and demonstrate.

Video 2 answers: **How does the code turn data into results, how can another user reproduce them, and which meaningful check passes or fails?** The [course architecture](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/PROJECT-SUBMISSION-ARCHITECTURE.md) calls for submitted code, financial logic, reproduction, a material test, and a failure mode or limitation. A screen-only tour of the app is insufficient. Use your voice and a small webcam view unless accommodated.

## 1. Prepare before pressing Record

### Open the actual project in VS Code

1. Open **VS Code → File → Open Folder**.
2. Select the folder `project-2-investment-management` inside your `FIN_43900` workspace. Its Explorer should show `app.py`, `portfolio_engine.py`, `data`, `tests`, and `README.md` at the top level.
3. Open these files using **Ctrl+P**, typing the filename/path, then Enter:
   - `README.md`
   - `app.py`
   - `data/prices.csv`
   - `portfolio_engine.py`
   - `tests/test_portfolio_engine.py`
4. Make code and terminal text large enough to read. Keep the script on paper, a phone, or a separate unrecorded screen. Do not display the script instead of the code.

Navigation used below: **Ctrl+P** switches files; **Ctrl+G**, line number, Enter jumps to a code line. The listed lines match the current submitted files. If they differ later, **Ctrl+F** for the named function is a fallback. Clear the search box afterward so it does not obscure the code.

### Prepare the app and terminal

In VS Code choose **Terminal → New Terminal**. Confirm the terminal is in the project folder. If necessary:

```powershell
cd C:\Users\rocco\OneDrive\Documents\FIN_43900\project-2-investment-management
```

If the app is not already running, use:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the Local URL printed by Streamlit. If the app is already running, use its existing tab/URL rather than starting a duplicate server. Leave the terminal running the server alone.

Prepare the app at its base controls:

- All 59 monthly returns.
- Minimum SGOV reserve **10%**.
- Annual implementation-cost stress **0.00**.
- ACWI annual-return adjustment **0.00**.
- No replacement CSV.

Confirm the base result is **70% SGOV / 30% ACWI**, net estimate **6.02%**, volatility **4.56%**. This is an ordinary recording demonstration, separate from the already preserved protected exercise.

Open **another terminal** with the terminal panel's **+** button. Use this second terminal for the recorded test. Keep this command ready to type/paste during the test segment:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_portfolio_engine.py -k cost45 -v
```

This selects **one existing cost test**, not all 17 tests. A successful run should show its name, **Ran 1 test**, and **OK**. This guide has not executed a new run. If the command fails or the actual output differs, stop and resolve it before saying it passed; do not edit the test merely to make the recording look successful.

## 2. Timed script and screen actions

Only the quoted paragraphs are spoken. Point to the named code while explaining it. Rehearse the navigation once before recording.

### 0:00–0:20 — opening disclosures

**Screen:** VS Code with the project Explorer visible and `app.py` open. Do not start with a blank desktop or this script.

> I used ChatGPT and Codex to help with code, tests, source checks, and this presentation draft. I am responsible for the analysis and decision. This is education only, not investment advice.

### 0:20–0:50 — architecture and inputs

**Screen actions:**

1. In `app.py`, use **Ctrl+G → 6** to show imports from the portfolio engine.
2. Use **Ctrl+G → 105** to show reading inputs, estimating returns, and calling `constrained_portfolio` and `baseline_portfolios`.
3. Briefly open `data/prices.csv` with **Ctrl+P** and show its header and first few rows.

> The interface is in app dot py, while portfolio engine dot py contains the financial calculations. The app reads the saved monthly-price CSV, builds estimates, searches for a constrained portfolio, and evaluates both baselines. The CSV contains dates and adjusted prices for SGOV, SCHR, USIG, and ACWI. No live download is required to run this saved-data demonstration.

### 0:50–1:30 — validation, return estimates, and risk

**Screen actions:**

1. Open `portfolio_engine.py`; jump to **line 68**, `load_prices`. Point to fixed columns, finite/positive prices, and consecutive-month checks.
2. Jump to **line 103**, `estimate_from_prices`. Point to `prices[name][index] / prices[name][index - 1] - 1`, then `returns[-36:]`.
3. Scroll to the return statement around **line 129**, showing `* 12` and `sqrt(12)`.
4. Jump to **line 140**, then briefly **156**, showing covariance construction and the weighted variance calculation.

> The loader rejects incorrect columns, invalid prices, and nonconsecutive months. Sixty prices produce fifty-nine simple monthly returns. The shorter window uses the last thirty-six returns. Annual return is the monthly arithmetic mean times twelve; annual volatility uses sample standard deviation times the square root of twelve. Correlations use the same aligned returns. Portfolio risk combines weights with the covariance matrix, so it is not simply an average of individual volatilities.

### 1:30–2:10 — mandate, grid search, and baselines

**Screen actions:**

1. Jump to **line 178**, `mandate_verdict`. Point to `gross`, `net = gross - annual_cost`, and the four `checks`.
2. Jump to **line 203**, `constrained_portfolio`. Point to the allocation loop and the `result["passes"]` / minimum-volatility comparison.
3. Scroll down to **line 216**, `baseline_portfolios`, and point out that both use `mandate_verdict`.

> The mandate subtracts annual implementation cost from gross estimated return. It checks full investment, long-only weights, the SGOV minimum, and the six-percent net-return hurdle. The search divides the portfolio into five-percentage-point units, tests every allocation, and keeps the lowest-volatility feasible result. If none qualifies, it returns no portfolio. Equal weight and the sixty-forty ACWI-USIG benchmark use the same mandate checks. This is a discrete grid search, not a continuous optimum.

### 2:10–2:35 — decision logic

**Screen:** jump to **line 245**, `decision_status`. Show the STOP branches and REVIEW reasons. Point to `0.0025` when saying twenty-five basis points.

> Feasibility and governance are separate. The decision function stops for infeasibility or a weight move greater than twenty percentage points. Exactly twenty points requires review. Costs above twenty-five basis points or SGOV outside the original candidate band also trigger review. A numerical pass is therefore not automatic committee approval.

### 2:35–3:20 — demonstrate a meaningful automated test

**Screen actions:**

1. Open `tests/test_portfolio_engine.py`; use **Ctrl+G → 40** to show `test_cost45_reoptimizes_and_requires_review`.
2. Point to the base and `.0045` cost search, the ACWI `.40` assertion, the REVIEW assertion, and `self.assertFalse(fixed["passes"])`.
3. Click the second terminal. Run the prepared single-test command. Show the actual result clearly.

> I test cost reoptimization because meeting the return hurdle depends on both costs and selected weights. This test adds forty-five basis points, checks that ACWI becomes forty percent, and verifies that net return equals gross return minus cost. It also checks the REVIEW decision. Keeping the original weights instead fails the return hurdle. I am running that existing test here.

**After the command completes successfully, say:**

> The test reports OK. That checks specific financial behavior, rather than only checking whether the app opens.

If it does not report OK, do not say that last paragraph. Record only after the cause is understood and the actual result can be explained.

### 3:20–4:00 — connect the test to the live interface

**Screen actions:**

1. Switch to the app tab and show the base 70/30 allocation.
2. Leave window/reserve/ACWI controls unchanged. Change **Annual implementation-cost stress** from **0.00 → 0.45**. This means **0.45% per year = 45 basis points**. Do not enter 45.
3. Show the top table's **60% SGOV / 40% ACWI**, **6.32% net estimate**, and **6.03% volatility**.
4. Scroll to **Decision rule** and point to **REVIEW**. The fixed standard stress table does not follow the sidebar; the top table is the selected case.
5. Restore cost to **0.00** and return to the top table; confirm base **70/30**, **6.02%**, and **4.56%**.

> The live app shows the same behavior. With forty-five basis points of cost, it selects sixty percent SGOV and forty percent ACWI, estimates six-point-three-two percent net return and six-point-zero-three percent volatility, and requires REVIEW. Costs reduce return at fixed weights; the higher optimized return comes from taking more equity risk. I am restoring zero cost and the base allocation.

### 4:00–4:25 — source verification and one limitation

**Screen:** return to `portfolio_engine.py`, **line 42**, `verify_signal_evidence`. Point to reading the saved file, comparing its SHA-256, and matching its date/value.

> The signal check verifies the saved DGS10 file's hash and displayed date and value. Missing or inconsistent evidence stops operational use. However, this verifies a frozen snapshot, not live freshness or a historical backtest. Likewise, passing calculation tests does not prove that estimated returns will occur.

### 4:25–4:45 — show how another user reproduces the result

**Screen:** open `README.md`. Use **Ctrl+F → Run it**. Show the virtual-environment creation, dependency installation, and Streamlit launch command. Do not reinstall dependencies while recording. Finish with the app launch command visible, then stop recording.

> A clean user follows these README setup steps and starts the app with the Streamlit command. The bundled prices reproduce the base table, and the tests check the recorded calculations and failure conditions. The model omits taxes, turnover, and drawdown, so reproducibility does not establish suitability for an actual investor.

## 3. Recording and completion

Use the same Clipchamp **screen, microphone, and small webcam** arrangement as Video 1. Capture the whole screen so switching between VS Code and the app is visible. Keep the webcam away from code, test output and portfolio numbers. Save raw webcam recordings outside the course repository.

Before final export, check:

- Both opening disclosures are audible.
- Actual source code is visible and explained, not just filenames or the app.
- The cost test's code and actual successful terminal output can be read.
- The cost demonstration shows the selected top table and REVIEW, then returns to base.
- The source/failure limitation and README reproduction instructions are included.
- Your exported recording is **5:00 or less**. Aim below the limit; the timing table is not a guarantee.

You can rehearse in sections and use ordinary edits, retaining a faithful demonstration. Keep camera/screen/audio aligned when cutting. Use the final edited recording for caption generation.

Upload the exported MP4 to YouTube as **Unlisted**, with title **Project 2 — Video 2: Code Walkthrough and Validation**. Correct the actual captions, check access logged out, and send the YouTube link, displayed duration, and downloaded corrected `.srt` file. We will create `docs/transcript-video-2.txt` from that final speech and update actual manifest timestamps. The current transcript placeholder must not be replaced with this rehearsal script.

## Quick understanding check before recording

Be comfortable explaining these in your own words:

- `0.0045` in code is 0.45% annually, or 45bp; the app slider displays `0.45` before dividing by 100.
- The objective is minimum estimated volatility **subject to** the return/reserve constraints, not maximum return.
- Reoptimization can select a higher-net-return portfolio after costs by accepting more equity risk; the same unchanged weights still lose return from costs.
- Passing the test means the tested assertions held; it does not prove the forecast or every possible input is correct.
- The ordinary cost demonstration does not rewrite or replace the already preserved student ACWI prediction/experiment.

These are explanations of existing project behavior, not additional deliverables or new features.
