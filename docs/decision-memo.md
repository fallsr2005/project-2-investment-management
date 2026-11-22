AI used: ChatGPT/Codex assisted with code structure, tests, and documentation; I reviewed the analysis and own the decision.

Education only — not investment advice.

# Decision memo — Project 2 investment-management application

## Recommendation and committee ask

**Recommendation: conditional three-month classroom pilot centered on 70% SGOV and 30% ACWI, with monthly committee review.** Under the base estimates, the feasible grid candidates in the original review band are **65–70% SGOV and 30–35% ACWI**, paired to total 100%; SCHR and USIG are 0%. The previously stated 65–75% SGOV band was a candidate review band, not a guarantee of feasibility: its 75% SGOV / 25% ACWI endpoint estimates only 5.65% before costs and fails the 6.0% hurdle. Each allocation must be checked again after costs and input changes. The horizon is a proposed classroom governance choice, not an inferred client requirement or three-month return promise.

The committee should approve the pilot only if it accepts the saved-data limitations, the point-in-time DGS10 monitoring rule, and the stop conditions below. The requested action is approval to operate the app and review its outputs—not authorization to place trades.

Student decision confirmed November 20, 2026: approve this recommendation for a three-month classroom evaluation with monthly reviews, the stated candidate allocation range, and the review/stop conditions. This confirms the student's judgment; actual committee authorization remains the requested action. Three months can evaluate operation and decision consistency, but cannot establish attainment of the 6% annual return estimate or reliability across market cycles.

## Mandate and as-of boundary

The application searches long-only allocations among SGOV, SCHR, USIG, and ACWI in 5-percentage-point steps. It minimizes annualized historical volatility subject to weights totaling 100%, SGOV at least 10%, and estimated net annual return at least 6.0%. The 60/40 ACWI/USIG allocation is the benchmark; annualized sample volatility is the risk measure.

The base price window is 60 monthly adjusted-close observations, October 2021–September 2026, reported downloaded from Yahoo Finance on 2026-10-22 in the prior lab notes. This creates 59 monthly simple returns. The date labels identify the first of the represented month, not the trade or availability date; September's close represents the completed September month. All estimates are historical. The current DGS10 observation is November 18 at 5.07%, from a raw ALFRED page captured November 20 at 06:08 UTC. Its hash and date/value are checked by the app; it is information available for this current review, not proof of an old vintage. The earlier September claim is retained only in historical records and remains unverified.

A separate November 22 capture of all four Yahoo series now corroborates the saved price history: later adjusted-price levels differ, but the base allocation and both baseline verdicts remain unchanged. Raw responses, timestamps, hashes, and an offline comparison are linked in the [price lineage](price-data-lineage.md). This does not establish the original October retrieval date or third-party redistribution rights; these remain conditions for use beyond this classroom review.

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
| Recorded 45-basis-point annual cost | 60% SGOV / 40% ACWI; 6.32% net; 6.03% volatility | 10-point shift; student retains pilot subject to committee review before implementing this allocation. It breaches the cost and candidate-band review triggers. |

The app's numerical status is STOP if no allocation is feasible or a selected/standard scenario moves a weight by more than 20 percentage points from base. It requests REVIEW for exactly 20 points, cost above 25 basis points, or SGOV outside the original candidate band. Missing or inconsistent DGS10 evidence separately stops operational use. The fixed standard stress suite does not change with sidebar controls; the top table shows the selected scenario.

## Monitoring and reversal triggers

- Re-run and pause the pilot if an approved scenario has no feasible allocation or changes any base weight by more than 20 percentage points.
- Escalate the current 20-point historical-window difference before any move beyond the 65–75% SGOV pilot range.
- Reassess if DGS10 cannot be evaluated from an ALFRED vintage available at the decision date, has material revisions, or is stale beyond its expected publication lag.
- Re-run if estimated implementation costs exceed 25 basis points annually, the 6.0% hurdle changes, or the SGOV floor changes.
- Do not infer safety from low historical SGOV volatility; the reserve fund can fluctuate and is not cash.

## Limitations

This simplified model omits taxes, turnover, drawdown, bid-ask spreads, personal liquidity needs, rebalancing mechanics, and a continuous optimizer. Yahoo adjusted-close data may be revised. DGS10 is a monitoring signal, not a forecast. The app's arithmetic and tests establish reproducibility, not the correctness of forward-looking estimates.

Complete AI-use details, tests, and the required Locked Changed-Input Record are in [validation-and-ai-use.md](validation-and-ai-use.md).
