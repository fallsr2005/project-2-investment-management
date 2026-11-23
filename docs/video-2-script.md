AI used: ChatGPT/Codex assisted with code, tests, source checks, documentation, and this presentation draft. I am responsible for reviewing the analysis and owning the decision.

Education only — not investment advice.

# Video 2 — GitHub, PowerShell, and live app guide

Use **GitHub to show the submitted code**, **PowerShell to execute one existing test locally**, and **your app to demonstrate the result**. VS Code is not needed for this workflow.

Maximum **5:00**; target **4:20–4:45**. This is a rehearsal script, not your actual transcript. Timings are targets; measure your final exported recording. Explain the code naturally while pointing to it. Adjust personal statements to what you understand and actually show.

The [official Video 2 directions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/PROJECT-SUBMISSION-ARCHITECTURE.md#L120-L126) require architecture/data flow, key code and finance logic, reproduction, a meaningful validation or changed-input test, and one failure mode or limitation. The guide below covers those elements using existing project files.

## A. Before recording: open these browser tabs

Open these links in order. Keep this script on paper, your phone, or another unrecorded screen. Make the code large enough to read. GitHub line links position/highlight the relevant code; scroll within the file when instructed.

| Tab | Open this link | Purpose |
|---|---|---|
| 1 | [Repository home](https://github.com/fallsr2005/project-2-investment-management) | Show the submitted repository and files |
| 2 | [app.py: data-to-result calls](https://github.com/fallsr2005/project-2-investment-management/blob/main/app.py#L105-L113) | Show where the interface calls the engine |
| 3 | [data/prices.csv](https://github.com/fallsr2005/project-2-investment-management/blob/main/data/prices.csv) | Show column headings and first rows |
| 4 | [Engine: price validation](https://github.com/fallsr2005/project-2-investment-management/blob/main/portfolio_engine.py#L68-L101) | Start here; scroll down to estimates and covariance |
| 5 | [Engine: mandate and search](https://github.com/fallsr2005/project-2-investment-management/blob/main/portfolio_engine.py#L178-L224) | Show mandate, grid search and baselines |
| 6 | [Engine: decision rules](https://github.com/fallsr2005/project-2-investment-management/blob/main/portfolio_engine.py#L245-L259) | Show STOP/REVIEW/PILOT |
| 7 | [Existing cost test](https://github.com/fallsr2005/project-2-investment-management/blob/main/tests/test_portfolio_engine.py#L40-L48) | Explain what the test asserts |
| 8 | Your running app, usually [localhost:8501](http://localhost:8501) | Live cost demonstration |
| 9 | [Engine: signal verification](https://github.com/fallsr2005/project-2-investment-management/blob/main/portfolio_engine.py#L42-L55) | Source check and limitation |
| 10 | [README run instructions](https://github.com/fallsr2005/project-2-investment-management#run-it) | Explain how another user reproduces output |

You may use browser zoom and scroll to keep the named code visible. You do not need to read every line or open unrelated files. The line numbers refer to the current code; the function names identify the sections if line numbers later change.

### Prepare PowerShell and the app

1. In File Explorer, open your **project-2-investment-management** folder—the folder containing `app.py` and `portfolio_engine.py`.
2. Click File Explorer's address bar, type **powershell**, and press Enter. This opens PowerShell in that folder.
3. If the app is already running, use its existing tab/URL. Otherwise run the existing launch command below and open its printed Local URL:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Leave a server terminal running. For the test, open a **second PowerShell window in the same folder** by repeating steps 1–2. Keep that second window ready behind the browser. Use **Alt+Tab** to switch between it and the browser during recording. GitHub shows the code; this local window executes it.

Set the live app to these base values before recording:

- **All 59 monthly returns**.
- **Minimum SGOV reserve: 10%**.
- **Annual implementation-cost stress: 0.00**.
- **ACWI annual-return adjustment: 0.00**.
- No replacement CSV.

Confirm **70% SGOV / 30% ACWI**, **6.02% net estimate**, and **4.56% volatility**. The code shown on GitHub is the same project code in the local folder; use that folder for the command. The test/demonstration below is separate from your preserved protected ACWI experiment.

## B. Record: exact script and actions

Say the quoted text, not the action labels. Practice the tab changes once before recording.

### 0:00–0:20 — disclosures

**Show:** Tab 1, repository home. Keep your microphone and small webcam view active unless accommodated.

> I used ChatGPT and Codex to help with code, tests, source checks, and this presentation draft. I am responsible for the analysis and decision. This is education only, not investment advice.

### 0:20–0:50 — architecture and inputs

**Do:** Show Tab 2. Point to `estimate_from_prices`, `constrained_portfolio`, and `baseline_portfolios`. Then show Tab 3's column headings and first rows.

> The interface is in app dot py, while portfolio engine dot py contains the financial calculations. The app reads the saved monthly-price CSV, builds estimates, searches for a constrained portfolio, and evaluates both baselines. The CSV contains dates and adjusted prices for SGOV, SCHR, USIG, and ACWI. No live download is required to run this saved-data demonstration.

### 0:50–1:30 — validation, returns, and risk

**Do:** In Tab 4, point to the CSV column check and the positive/finite price and consecutive-month checks. Scroll down to `estimate_from_prices` at line 103. Point to the ratio-minus-one calculation, `returns[-36:]`, then `* 12` and `sqrt(12)` in the returned estimates. Briefly scroll to `covariance_matrix` and `volatility` around lines 140–166.

> The loader rejects incorrect columns, invalid prices, and nonconsecutive months. Sixty prices produce fifty-nine simple monthly returns. The shorter window uses the last thirty-six returns. Annual return is the monthly arithmetic mean times twelve; annual volatility uses sample standard deviation times the square root of twelve. Correlations use the same aligned returns. Portfolio risk combines weights with the covariance matrix, so it is not simply an average of individual volatilities.

### 1:30–2:10 — mandate, search, and baselines

**Do:** Show Tab 5. Point to `net = gross - annual_cost` and the four checks. Scroll slightly to `constrained_portfolio`; point to the `for units` loop and the line retaining a passing result with lower volatility. Show that `baseline_portfolios` calls `mandate_verdict` too.

> The mandate subtracts annual implementation cost from gross estimated return. It checks full investment, long-only weights, the SGOV minimum, and the six-percent net-return hurdle. The search divides the portfolio into five-percentage-point units, tests every allocation, and keeps the lowest-volatility feasible result. If none qualifies, it returns no portfolio. Equal weight and the sixty-forty ACWI-USIG benchmark use the same mandate checks. This is a discrete grid search, not a continuous optimum.

### 2:10–2:35 — decision rules

**Do:** Show Tab 6. Point to `STOP`, the greater-than-20-point condition, and the REVIEW reasons. `0.0025` means 25 basis points of annual cost.

> Feasibility and governance are separate. The decision function stops for infeasibility or a weight move greater than twenty percentage points. Exactly twenty points requires review. Costs above twenty-five basis points or SGOV outside the original candidate band also trigger review. A numerical pass is therefore not automatic committee approval.

### 2:35–3:20 — show and execute the meaningful test

**Do:** Show Tab 7. Point to the `.0045` cost, `.40` ACWI assertion, REVIEW assertion, and the final assertion that unchanged base weights fail. These are checks of the financial behavior most at risk when costs alter the feasible boundary.

> I test cost reoptimization because meeting the return hurdle depends on both costs and selected weights. This test adds forty-five basis points, checks that ACWI becomes forty percent, and verifies that net return equals gross return minus cost. It also checks the REVIEW decision. Keeping the original weights instead fails the return hurdle. I am running that existing test here.

**Now Alt+Tab to the second PowerShell window. Paste this exact command and press Enter:**

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_portfolio_engine.py -k cost45 -v
```

Wait for completion and show the output clearly. A successful run should show the test name, **Ran 1 test**, and **OK**. This selects one existing test, not the full 17-test suite. This guide has not performed a new run.

**Only if the actual result is successful, say:**

> The test reports OK. That checks specific financial behavior, rather than only checking whether the app opens.

If it reports an error, failure, or zero tests, do not say it passed. Stop and resolve the actual issue before finalizing the recording. Do not change the test simply to obtain a passing recording.

### 3:20–4:00 — demonstrate the same behavior in the app

**Do:** Alt+Tab back to the browser; select Tab 8.

1. Show the base allocation.
2. Change **only Annual implementation-cost stress** from **0.00 to 0.45**. This is **0.45% annually = 45 basis points**; do not enter 45.
3. Show the **top portfolio table**: SGOV **60%**, ACWI **40%**, net estimate **6.32%**, volatility **6.03%**.
4. Scroll down to **Decision rule** and point to **REVIEW**. The fixed standard stress suite does not follow the sidebar; the top table represents your selected scenario.
5. Restore cost to **0.00**, then return to the top table and show **70/30**, **6.02%**, **4.56%**.

> The live app shows the same behavior. With forty-five basis points of cost, it selects sixty percent SGOV and forty percent ACWI, estimates six-point-three-two percent net return and six-point-zero-three percent volatility, and requires REVIEW. Costs reduce return at fixed weights; the higher optimized return comes from taking more equity risk. I am restoring zero cost and the base allocation.

### 4:00–4:25 — source check and limitation

**Do:** Show Tab 9. Point to `read_bytes`, the hash comparison, and the observation date/value match.

> The signal check verifies the saved DGS10 file's hash and displayed date and value. Missing or inconsistent evidence stops operational use. However, this verifies a frozen snapshot, not live freshness or a historical backtest. Likewise, passing calculation tests does not prove that estimated returns will occur.

### 4:25–4:45 — how another user reproduces the result

**Do:** Show Tab 10's **Run it** instructions: create virtual environment, install requirements, and launch Streamlit. Point to the launch command. You have already shown the resulting live app; do not reinstall packages during the recording.

> A clean user follows these README setup steps and starts the app with the Streamlit command. The bundled prices reproduce the base table, and the tests check the recorded calculations and failure conditions. The model omits taxes, turnover, and drawdown, so reproducibility does not establish suitability for an actual investor.

Stop recording. Leave the app at its base settings.

## C. Understand these phrases before recording

These short explanations are rehearsal help, not additional deliverables:

- **Function:** a named block of code that performs a task. `load_prices` reads/checks prices; `constrained_portfolio` chooses the allocation.
- **Net return:** gross estimated return minus the assumed annual implementation cost.
- **Feasible:** the candidate passes all modeled mandate checks.
- **Grid search:** try all allowed allocations in 5-percentage-point steps; retain the passing one with lowest estimated volatility.
- **Covariance:** combines asset volatilities and how returns move together to calculate portfolio risk.
- **Assertion:** a test statement checking a specific expected result. A failed assertion makes the test fail.
- **Reoptimization:** search again after an input changes; the new weights can raise gross return enough to offset a higher cost.
- **0.0045 in code:** 0.45% per year, or 45bp. The app slider shows 0.45 before dividing by 100.
- **PASS versus REVIEW:** PASS means mandate arithmetic succeeds; REVIEW means a governance trigger still requires reassessment.

Point to code you understand and explain those relationships. You do not need to memorize every line or pronounce every symbol.

## D. Record, upload, and send back

Use the same Clipchamp screen/microphone/small-webcam setup as Video 1. Capture the whole screen so browser/PowerShell switching is recorded; position the webcam away from code, numbers and terminal results. Keep raw webcam recordings outside the course repository.

Before exporting, confirm:

- Both opening disclosures are audible.
- GitHub code, financial logic, and data flow are visible and explained.
- The existing cost test is actually executed and its real result shown.
- The selected app cost scenario shows REVIEW and returns to base.
- The source/failure limitation and README reproduction instructions are included.
- The **final exported recording is 5:00 or less**, with clear sound/readable text. The script is about 509 words; allow time for navigation and the command.

Upload the final MP4 as **Unlisted**, titled **Project 2 — Video 2: Code Walkthrough and Validation**. Correct the captions against the final video, test the link logged out, and send the YouTube link, displayed runtime, and downloaded final `.srt`. We will save the actual transcript and actual timestamp index. Keep `docs/transcript-video-2.txt` as a placeholder until the recording supplies its real words; this rehearsal script is not the transcript.
