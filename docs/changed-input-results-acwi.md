# ACWI changed-input record: results and restoration

## Record and provenance

The pre-run prediction is preserved unchanged in [changed-input-prediction-acwi.md](changed-input-prediction-acwi.md), committed and pushed at [`054f0d3a82d62a772c13f495ccc084646d1df2af`](https://github.com/fallsr2005/project-2-investment-management/commit/054f0d3a82d62a772c13f495ccc084646d1df2af) before the student supplied the changed-run screenshots. The commit provides the pre-run timestamp; screenshot capture times are not independently authenticated here.

The student states the prediction, comparison, explanation, and actual decision effect are their own wording. Codex formatted and committed the student-supplied prediction, acknowledged screenshots and section structure during the exchange, and later assembled this report and copied the original screenshot files. This report preserves the student's supplied after-run wording, including the requested change from “Matched exactly—dropping” to “Matched exactly because dropping.” Codex did not operate the changed-input run. Because AI chat remained part of the exchange, this record does not certify AI-off compliance; instructor interpretation remains unresolved. The earlier cost-test record remains preserved separately.

## Evidence index

| Stage | Controls and portfolio | Inputs and signal | Stress suite and decision |
|---|---|---|---|
| Before: ACWI adjustment 0.00 | [Screenshot](evidence/acwi-minus-3pp/before-portfolio.png) | [Screenshot](evidence/acwi-minus-3pp/before-inputs.png) | [Screenshot](evidence/acwi-minus-3pp/before-decision.png) |
| After: ACWI adjustment -3.00 percentage points | [Screenshot](evidence/acwi-minus-3pp/after-portfolio.png) | [Screenshot](evidence/acwi-minus-3pp/after-inputs.png) | [Screenshot](evidence/acwi-minus-3pp/after-decision.png) |
| Restored: ACWI adjustment 0.00 | [Screenshot](evidence/acwi-minus-3pp/restored-portfolio.png) | [Screenshot](evidence/acwi-minus-3pp/restored-inputs.png) | [Screenshot](evidence/acwi-minus-3pp/restored-decision.png) |

The screenshots show the other controls unchanged: all 59 monthly returns, 10% minimum SGOV reserve, 0.00 annual implementation cost, and no replacement CSV selected. The restored screenshots show 70% SGOV / 30% ACWI, 6.02% estimated net return, 4.56% volatility, and PILOT numerical status. The fixed standard stress suite is separate from the selected scenario and does not follow sidebar changes.

## Comparison of Prediction vs. Actual Output

- ACWI return input: Matched exactly because dropping the adjustment slider to -3.00 percentage points lowered ACWI's annual arithmetic-mean return estimate from 11.25% to 8.25%.
- Portfolio weights: Landed right in the middle of the predicted range. ACWI rose +20.00 percentage points (from 30.00% to 50.00%, vs. the predicted +15 to +25 percentage points), SGOV dropped -20.00 percentage points (from 70.00% to 50.00%, vs. the predicted -15 to -25 percentage points), and SCHR and USIG both stayed at 0.00% as expected.
- Estimated net return: Matched the predicted range (6.00%–6.40%), coming in at 6.01% (down slightly from 6.02% in the base case) and just barely clearing the 6.0% mandate hurdle.
- Portfolio volatility: Increased from 4.56% to 7.50% (+2.94 percentage points), sitting comfortably inside the predicted +2.5 to +4.5 percentage-point jump (7.0%–9.0%).
- Largest weight change from base: Jumped from 0.00 percentage points to 20.00 percentage points.

## Explanation of Differences

- Why 50% SGOV / 50% ACWI was the exact stopping point: With SGOV earning 3.78% and ACWI adjusted down to 8.25%, a 55% SGOV / 45% ACWI split only produces 0.55(3.78%) + 0.45(8.25%) = 5.79%, which misses the 6.0% net return minimum. Stepping up one 5-percentage-point grid increment to 50% SGOV / 50% ACWI yields 0.50(3.78%) + 0.50(8.25%) = 6.015% (6.01%), making it the lowest-volatility feasible allocation on the grid.
- Why the decision rule changed more sharply than anticipated: While the portfolio still passed the 6.0% return constraint (PASS), the prediction only anticipated keeping PILOT with extra caution, whereas the app's built-in governance logic actively downgraded the numerical decision from PILOT to REVIEW because 50% SGOV falls outside the original 65%–75% SGOV candidate band and triggers a 20.00-percentage-point shift threshold.
- Impact on benchmarks: Notice that the 60/40 ACWI/USIG benchmark also flipped from failing only the SGOV reserve rule to failing both the SGOV reserve rule and the 6.0% net return hurdle (4.97% net estimate).

## Actual Decision Effect

- Numerical decision shifts from PILOT to REVIEW: Even though the 50% SGOV / 50% ACWI portfolio still passes the 6.0% return target (6.01%), it cannot be approved directly for a pilot under this scenario.
- Committee escalation required: Because SGOV drops to 50.00% (outside the 65%–75% review band) and volatility jumps by nearly three percentage points to 7.50%, the 20.00-percentage-point reallocation requires formal committee escalation and reassessment before adopting the strategy.
