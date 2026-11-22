# Step 1 & Step 2: Pre-Run Prediction (Commit & Push to GitHub Before Running)

## Input Change and Units

- Control: ACWI annual-return adjustment slider in the sidebar.
- Old value: 0.00 percentage points (0.00%), which leaves ACWI at its historical 11.25% annualized arithmetic-mean return over all 59 monthly returns.
- New value: -3.00 percentage points (-3.00%), which lowers ACWI's annual return assumption toward 8.25%.

## Predicted Direction and Magnitude

- ACWI weight: Goes up by roughly +15 to +25 percentage points from 30.00% to around 45%–55% on the 5% allocation grid.
- SGOV weight: Goes down by roughly -15 to -25 percentage points from 70.00% to around 45%–55%, staying above the 10% minimum.
- SCHR and USIG weights: Stay around 0.00% because their historical returns (-0.15% and 0.04%) are weak compared to their volatilities (5.44% and 7.93%).
- Volatility: Goes up noticeably from 4.56%, roughly +2.5 to +4.5 percentage points higher (around 7.0%–9.0%).
- Net return: Lands right around or slightly above the 6.00% hurdle (roughly 6.00%–6.40%), unless no 5%-grid mix can hit 6.00% after the cut.

## Financial Reasoning

- Cutting ACWI's return by 3.00 percentage points trims about 0.90 percentage points off a 70% SGOV / 30% ACWI mix (0.30 × 3.00%), which would pull the base 6.02% return down near 5.1% if weights stayed put.
- Since the mandate requires at least a 6.0% net annual return at the lowest possible volatility, the optimizer has to shift out of low-volatility SGOV (0.48% volatility) and into higher-volatility ACWI (14.88% volatility) just to clear the return hurdle.

## Expected Decision Effect

- If a 5%-grid portfolio still reaches 6.00% net return, the numerical verdict may stay PASS / PILOT, but with bigger weight changes from base and higher risk which would be making a strong case against moving past a small pilot without another committee review.
- If no 5%-grid portfolio can hit 6.00% net return, the portfolio becomes infeasible under this stress test.
