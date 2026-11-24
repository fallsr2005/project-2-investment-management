AI used: ChatGPT/Codex assisted with code, tests, source checks, documentation, and this presentation draft. I am responsible for reviewing the analysis and owning the decision.

Education only — not investment advice.

# Video 3 — short committee presentation

**Use only the live app. Target 3:30–4:15; absolute maximum 5:00.** This is a short rehearsal script, not an actual transcript. A word count cannot guarantee duration: do one timed rehearsal with the screen actions, then check the final exported video's runtime. The short script leaves a substantial buffer for scrolling and pauses.

**Speak only the quoted paragraphs below.** The action instructions are silent directions. Do not add the detailed line-by-line explanations from Video 2; this presentation defends the committee decision, not the code. Use your own natural delivery while keeping the facts and scope accurate.

The [official Video 3 requirement](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/PROJECT-SUBMISSION-ARCHITECTURE.md#L140-L165) is a committee presentation led by the decision, defending the recommendation/range/evidence/assumptions/risks/triggers and ending with a clear ask. [Project 2 specifically requires opening with the app running live](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md). Keep your small webcam view unless accommodated, microphone, and readable app visible.

## Prepare before recording

1. Open the running app in Chrome, usually [localhost:8501](http://localhost:8501). You do not need GitHub, PowerShell, tests, slides, or the memo on screen for this video.
2. Set **All 59 monthly returns**, **minimum SGOV 10%**, **cost 0.00**, **ACWI adjustment 0.00**, and no uploaded CSV.
3. Confirm the base table shows **70% SGOV / 30% ACWI**, **6.02%** net estimate, **4.56%** volatility.
4. Practice scrolling to these headings: **Constrained portfolio and required baselines → Standard stress suite → Decision rule → Point-in-time signal — DGS10**. Start the actual recording back at the title/mandate and base portfolio.
5. Keep the script on paper, your phone, or another unrecorded screen. Record the live app with your voice and small webcam, as in Videos 1–2. Position the webcam away from the figures.

## 1. Opening disclosures — about 20 seconds

**Silent action:** Start with the live app already visible, including its title and base result. Do not begin on this guide or a static screenshot.

> I used ChatGPT and Codex to help with code, tests, source checks, and this presentation draft. I am responsible for the analysis and decision. This is education only, not investment advice.

## 2. Recommendation, mandate, and base result — about 40 seconds

**Silent action:** Stay near the top. Point to the mandate and the constrained portfolio's base row. Leave all controls unchanged.

> I recommend a conditional three-month classroom pilot, reviewed monthly, rather than full adoption. The base allocation is seventy percent SGOV and thirty percent ACWI, with a six-point-zero-two percent net annual estimate and four-point-five-six percent volatility. The mandate minimizes estimated volatility, requires at least six percent net return and ten percent SGOV, and uses long-only weights totaling one hundred percent. The universe is SGOV, SCHR, USIG, and ACWI.

## 3. Comparisons and allocation range — about 30 seconds

**Silent action:** Point to the equal-weight and benchmark rows in the same top table. You do not need to show a separate document for the range statement.

> Equal weight fails the return hurdle at three-point-seven-three percent. The sixty-percent ACWI, forty-percent USIG benchmark has no SGOV and fails the reserve rule. Within the original candidate band, base-feasible grid candidates are sixty-five to seventy percent SGOV, paired with thirty to thirty-five percent ACWI. Each must pass again after costs.

## 4. Why the recommendation is conditional — about 45 seconds

**Silent action:**

1. Scroll to **Standard stress suite**. Point to the **last 36 returns** row showing **90% SGOV / 10% ACWI** and the **20-point** change. Do not switch the historical-window control.
2. Change **only ACWI annual-return adjustment** from **0.00 to -3.00**. Keep all 59 returns, cost 0.00 and reserve 10% unchanged.
3. Scroll back to the top portfolio table. Point to **50% SGOV / 50% ACWI**, **6.01%** net estimate and **7.50%** volatility.
4. Scroll to **Decision rule** and show **REVIEW**. The fixed stress table does not follow the slider; the top table shows this selected ACWI scenario.

> Window sensitivity argues against full adoption: the last thirty-six returns select ninety percent SGOV and ten percent ACWI, a twenty-point shift. Reducing ACWI's return assumption by three percentage points produces fifty-fifty weights, six-point-zero-one percent estimated net return and seven-point-five percent volatility. The portfolio still passes numerically, but the twenty-point change and candidate-band breach require REVIEW.

## 5. Restore the base — about 15 seconds

**Silent action:** Restore **ACWI annual-return adjustment to 0.00**. Scroll to the top table and show the base **70/30**, **6.02%**, **4.56%** result again. This is an ordinary live demonstration; the original protected experiment remains preserved separately.

> I would not implement that changed allocation without committee reassessment. I am restoring the original return adjustment, which returns the allocation to seventy-thirty.

## 6. Assumptions and source limits — about 35 seconds

**Silent action:** Scroll to **Point-in-time signal — DGS10** so the dated snapshot and verification banner are visible. Do not open code or read the full data card aloud.

> These estimates use fifty-nine monthly returns from adjusted prices through September twenty-twenty-six; they are not forecasts. The hurdle and reserve settings are classroom assumptions. DGS10 is a frozen November twentieth monitoring snapshot. Original download timing and data rights remain unverified. Taxes, turnover, spreads, drawdown and personal liquidity needs are not modeled.

## 7. Monitoring, reversals, and committee ask — about 40 seconds

**Silent action:** Scroll down to **Decision rule** and the committee ask. With the restored base settings, the selected status should be **PILOT**, subject to its stated conditions. Finish, then stop recording.

> Review a selected twenty-point move, costs above twenty-five basis points, or SGOV outside the original sixty-five to seventy-five percent candidate review band. Stop for infeasibility, a greater-than-twenty-point selected or standard-stress move, or failed signal verification. For a later decision, refresh the signal evidence. I ask the committee to authorize only the conditional process pilot, with monthly reviews and these restrictions. This requests process evaluation, not trades.

## Timing and accuracy check

The planned spoken sections total about **3:45**; screen movement and your speaking pace determine the actual duration. Before the final take, time one complete rehearsal **including all clicks and scrolling**. Aim to finish by **4:15**, leaving at least 45 seconds below the limit. If it takes longer, remove dead navigation/pauses or use the same prepared app positions; do not add more narration. The exported video itself must be ≤5:00.

Use these facts accurately:

- **65–70% SGOV / 30–35% ACWI** is the base-feasible grid subset. The original candidate review band is **65–75% SGOV**. These are different concepts.
- **Exactly 20 points → selected REVIEW; more than 20 → STOP.** The fixed window stress's exactly-20-point sensitivity supports human reassessment even while the restored selected base displays PILOT.
- The required **opening is live**. Use the live app for the slider demonstration too; you do not need another protected prediction or new analytical work.
- The model results are historical estimates, not guaranteed annual outcomes or three-month return promises. A mandate PASS is not permission to implement an allocation.
- Keep the source limitations consistent with the [decision memo](decision-memo.md); presenting a restricted classroom process pilot does not resolve those limitations.

## After recording

Use the same export/upload/caption process as Videos 1–2. Export the final edited MP4; verify runtime ≤5:00, clear voice/webcam, readable results and both opening disclosures. Upload as **Unlisted**, titled **Project 2 — Video 3: Investment Committee Presentation**. Correct the captions against that final video and test the link in Incognito.

Send the YouTube link, actual displayed runtime, final corrected `.srt`, and your confirmation that the live opening and visual evidence are clear. We will save the actual Video 3 transcript and update the manifest; this script is not the submitted transcript. Completing it will still leave the final package consistency/access/freeze and Brightspace submission steps.
