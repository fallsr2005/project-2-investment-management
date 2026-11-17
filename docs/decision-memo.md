AI used: ChatGPT/Codex assisted with code structure, tests, and documentation; I reviewed the analysis and own the decision.

Education only — not investment advice.

# Decision memo — Project 2 investment-management application

## Recommendation and committee ask

**Recommendation: pilot the process; do not fully adopt it.** Authorize a classroom pilot centered on **70% SGOV and 30% ACWI** under the stated 6.0% estimated-net-return objective and 10% SGOV minimum. For the pilot, an operating range of **65–75% SGOV and 25–35% ACWI** may be considered only after a documented monthly re-run; SCHR and USIG remain 0% in the base search. This is an analysis of historical estimates, not a recommendation to buy securities.

The committee should approve the pilot only if it accepts the saved-data limitations, the point-in-time DGS10 monitoring rule, and the stop conditions below. The requested action is approval to operate the app and review its outputs—not authorization to place trades.

## Mandate and as-of boundary

The application searches long-only allocations among SGOV, SCHR, USIG, and ACWI in 5-percentage-point steps. It minimizes annualized historical volatility subject to weights totaling 100%, SGOV at least 10%, and estimated net annual return at least 6.0%. The 60/40 ACWI/USIG allocation is the benchmark; annualized sample volatility is the risk measure.

The base price window is 60 monthly adjusted-close observations, October 2021–September 2026, downloaded from Yahoo Finance on 2026-10-22. This creates 59 monthly simple returns. All return, volatility, and correlation figures are historical estimates. The point-in-time DGS10 monitoring record uses the ALFRED vintage known on 2026-09-30, whose latest observation was 2026-09-29 at 5.26%.

## Base result and required comparisons

| Portfolio | SGOV / SCHR / USIG / ACWI | Estimated net return | Estimated volatility | Mandate verdict |
|---|---:|---:|---:|---|
| Constrained minimum-volatility portfolio | 70 / 0 / 0 / 30 | 6.02% | 4.56% | Pass |
| Equal weight | 25 / 25 / 25 / 25 | 3.73% | 6.54% | Fail: estimated net return below 6.0% |
| 60/40 ACWI/USIG benchmark | 0 / 0 / 40 / 60 | 6.77% | 11.59% | Fail: SGOV reserve below 10% |

The base allocation is the lowest-volatility feasible allocation among the discrete combinations tested. It does not prove that the allocation is continuously optimal or that the 6.0% return will occur.

## Stress evidence and decision interpretation

| Stress | Result | Interpretation |
|---|---|---|
| Reduce ACWI return estimate by 1 percentage point | 65% SGOV / 35% ACWI; 6.04% net; 5.29% volatility | A lower equity estimate needs more equity to clear the same hurdle; allocation shifts 5 points. |
| Use last 36 monthly returns | 90% SGOV / 10% ACWI; 6.05% net; 1.19% volatility | The largest 20-point shift is material. It supports a pilot rather than full adoption. |
| Apply 25-basis-point annual cost | 65% SGOV / 35% ACWI; 6.14% net; 5.29% volatility | Costs can move the feasible boundary; actual implementation costs require a fresh run. |
| Raise SGOV minimum to 20% | Base 70% SGOV / 30% ACWI remains feasible | The current result exceeds the stated reserve floor. |

The app stops the process if no feasible allocation remains, a standard stress moves any weight by more than 20 percentage points from base, or the required DGS10 point-in-time vintage is unavailable. An exactly 20-point movement is an escalation trigger for committee review even though it does not mechanically stop the test.

## Monitoring and reversal triggers

- Re-run and pause the pilot if an approved scenario has no feasible allocation or changes any base weight by more than 20 percentage points.
- Escalate the current 20-point historical-window difference before any move beyond the 65–75% SGOV pilot range.
- Reassess if DGS10 cannot be evaluated from an ALFRED vintage available at the decision date, has material revisions, or is stale beyond its expected publication lag.
- Re-run if estimated implementation costs exceed 25 basis points annually, the 6.0% hurdle changes, or the SGOV floor changes.
- Do not infer safety from low historical SGOV volatility; the reserve fund can fluctuate and is not cash.

## Limitations

This simplified model omits taxes, turnover, drawdown, bid-ask spreads, personal liquidity needs, rebalancing mechanics, and a continuous optimizer. Yahoo adjusted-close data may be revised. DGS10 is a monitoring signal, not a forecast. The app's arithmetic and tests establish reproducibility, not the correctness of forward-looking estimates.

Complete AI-use details, tests, and the required Locked Changed-Input Record are in [validation-and-ai-use.md](validation-and-ai-use.md).
