# Project 2 investment mandate

**Purpose:** evaluate a diversified, long-only classroom portfolio process. This mandate is an educational assumption, not a personal investment recommendation.

| Field | Definition |
|---|---|
| Intended user | Classroom investment committee reviewing whether to pilot the process |
| Proposed horizon and cadence | Three-month classroom evaluation pilot, reviewed monthly; committee approval required. Annualized return/volatility are model conventions, not three-month promises. No actual trading is requested. |
| Objective | Select the lowest estimated annual-volatility allocation with estimated **net** annual return at least 6.0% |
| Permitted universe | SGOV (Treasury-bill reserve), SCHR (intermediate Treasury bonds), USIG (investment-grade corporate bonds), and ACWI (global equities) |
| Benchmark | 60% ACWI / 40% USIG, used as a transparent comparison—not an allocation requirement |
| Risk measure | Annualized sample volatility of monthly simple returns from adjusted prices |
| Hard limits | Long-only; weights must sum to 100%; SGOV is the only reserve-eligible fund and must be at least 10%; no borrowing or short positions |
| Search method | Exhaustive 5-percentage-point grid, so the result is the lowest-risk feasible grid allocation, not a continuous optimum |
| Cost treatment | Base case assumes zero annual implementation cost; cost sensitivities subtract an explicit annual assumption from the estimated return before checking the objective |
| Point-in-time rule | DGS10 may be used only from the ALFRED vintage available at the decision date; it monitors SCHR conditions and is not an optimizer forecast input |

## Governance and stop conditions

The committee should pause the process if the app finds no feasible allocation, a standard stress moves any weight by more than 20 percentage points from the base result, the DGS10 vintage is unavailable or materially revised, or the objective/reserve rule changes. An exactly 20-point shift is escalated for review.

## Out of scope

### Audit clarification — 2026-11-19

The earlier September DGS10 claim remains unsupported. As of the 2026-11-20 correction, the app instead uses a preserved ALFRED source-page snapshot captured at 06:08 UTC, reporting November 18 at 5.07%. It is admissible only for reviews at or after that capture time; it is not historical-vintage evidence. See `data-card-dgs10.md`. The original candidate review band is not an automatic mandate pass: the base-feasible candidates within it are 65–70% SGOV / 30–35% ACWI, paired to total 100%.

This simplified mandate does not claim to model taxes, turnover, bid-ask spreads, maximum drawdown, personal spending needs, or realized performance. It does not treat SGOV as cash or a guaranteed loss limit.
