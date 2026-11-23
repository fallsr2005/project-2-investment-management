# Project 2 investment mandate

**Purpose:** evaluate a long-only classroom portfolio process. The objective, reserve floor, horizon, and governance thresholds are explicit classroom choices, not inferred client needs or a personal investment recommendation.

| Field | Definition |
|---|---|
| Intended user/action | Classroom investment committee deciding whether to authorize a conditional process pilot; no trades requested |
| Horizon/cadence | Three-month classroom evaluation, reviewed monthly; student confirmed November 20; actual committee approval required |
| Objective | Lowest estimated annual volatility with estimated **net** annual return at least 6.0% |
| Universe | SGOV: Treasury-bill reserve; SCHR: intermediate Treasury bonds; USIG: investment-grade corporate bonds; ACWI: global equities |
| Benchmark | 60% ACWI / 40% USIG; transparent comparison, not an allocation requirement |
| Risk measure | Annualized sample volatility of monthly simple returns from adjusted prices |
| Hard limits | Long-only; weights sum to 100%; SGOV is the only reserve-eligible fund and must be at least 10%; no borrowing or short positions |
| Search | Exhaustive 5-percentage-point grid; optimal only among feasible grid candidates |
| Cost | Base zero implementation cost; annual sensitivity cost is deducted from estimated gross return before checking feasibility |
| Signal | DGS10 monitors Treasury-rate conditions relevant to SCHR; not a return forecast or optimizer input. The bundled value is a frozen November 20 capture. See the [data card](data-card-dgs10.md). |

## Allocation interpretation

The base is 70% SGOV / 30% ACWI, with SCHR/USIG at zero. The **original candidate review band** is 65–75% SGOV; its **base-feasible grid subset** is 65–70% SGOV paired with 30–35% ACWI, totaling 100%. The 75% SGOV / 25% ACWI endpoint fails the 6% base hurdle. Neither band is a substitute for checking feasibility after changed assumptions and costs.

The 6% hurdle is a testable classroom objective, not a demonstrated expected outcome. The 10% SGOV floor is a minimum reserve assumption, not a calculated cash requirement or volatility cap. Annualized risk/return estimates are not three-month promises. The three-month pilot evaluates operation and decision consistency, not annual performance reliability.

## Governance

- **PASS/FAIL:** mandate arithmetic only; PASS does not authorize use.
- **Selected-scenario STOP:** no feasible selected/reference allocation, a selected weight move greater than 20 percentage points from base, or any fixed-suite case that is infeasible or moves a weight by more than 20 points.
- **Selected-scenario REVIEW:** exactly 20 points, cost above 25 basis points annually, or SGOV outside the original 65–75% candidate review band.
- **Selected-scenario PILOT:** none of those numerical triggers; still conditional on evidence review and committee approval. The fixed-suite 20-point window sensitivity remains a human-review limitation, even while the base selected case displays PILOT.
- **Evidence/governance pause:** missing or inconsistent DGS10 source verification stops operational use. A later decision needs refreshed, preserved signal evidence and review of publication/revision timing. Changes to the mandate require committee reassessment; the app does not automatically adjudicate source freshness or revisions.

## Boundaries

See the [price lineage](price-data-lineage.md) and [source-limitation review](source-limitations-review.md). The October download date is lab-reported, the later price capture does not prove an original vintage, and Yahoo access/redistribution rights remain unverified. These gaps are not cured by passing arithmetic tests or educational purpose.

Taxes, turnover, bid-ask spreads, drawdown, personal spending needs, and realized performance are outside the model. SGOV can fluctuate; it is not cash or a guaranteed loss limit.
