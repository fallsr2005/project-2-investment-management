AI used: ChatGPT/Codex assisted with code, tests, source checks, and documentation. I am responsible for reviewing the analysis and owning the decision.

Education only — not investment advice.

# Video 2 — code walkthrough

Preparation cues, not an actual transcript. Maximum **5:00**; aim for 4:00–4:40. Show the submitted code, terminal output, and a small webcam view unless accommodated. Say both disclosures at the opening. Explain the code rather than reading a script.

| Approximate time | Show and explain |
|---|---|
| 0:00–0:35 | Disclosures and architecture: `app.py` → `portfolio_engine.py` → frozen `data/prices.csv`; separate source audit and saved reports. |
| 0:35–1:20 | `load_prices` / `estimate_from_prices`: fixed four-ticker columns; positive finite prices; consecutive months; 60 prices → 59 simple returns; last-36 uses 37 prices. Annual arithmetic mean ×12, sample standard deviation ×√12; aligned covariance/correlation. Month labels are not availability dates. |
| 1:20–2:10 | `mandate_verdict` / `constrained_portfolio`: long-only, weights sum to one, SGOV floor, net-return hurdle. Gross minus annual implementation cost gives net. Enumerate every 5-point composition, reject infeasible candidates, retain lowest covariance-based volatility. Both baselines use the same mandate checks. |
| 2:10–3:00 | Run the existing test suite in your recording, if ready to demonstrate it. Explain a meaningful test: cost drag at fixed weights versus reoptimization, or exactly-20 REVIEW versus greater-than-20 STOP. The prior saved result is 17 passing tests; describe the actual terminal result if it differs. |
| 3:00–3:50 | `decision_status` and source checks: selected-scenario STOP/REVIEW/PILOT; fixed-suite stop propagation; DGS10 hash/date/value check. Explain that a hash does not prove historical authenticity, freshness, or permissions. Show `audit_price_sources.py` and the preserved later-source comparison; no network capture is needed. |
| 3:50–4:40 | App: base 70/30 SGOV/ACWI; cost 0.45% produces REVIEW; 100% SGOV floor produces STOP. The previously recorded ACWI -3pp result is 50/50, PASS feasibility and REVIEW governance. Restore defaults after demonstrations. End with run instructions and one material limitation. |

Use the README's virtual environment. A later demonstration is separate from the protected student exercise; do not rewrite its prediction or replace its screenshots. The app does not automatically test signal freshness/revision history or data rights. After recording, supply a corrected actual transcript and timestamps.
