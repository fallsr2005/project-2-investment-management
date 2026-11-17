AI used: ChatGPT/Codex helped draft this recording guide; I reviewed it and own the analysis and decision.

Education only — not investment advice.

# Video 2 recording guide — code walkthrough

Target duration: 4:15–4:45. Record this in your own words and replace the matching `.txt` transcript with the corrected words actually spoken.

1. **0:00–0:30 — Architecture.** Open the repository tree: `app.py` is the user interface, `portfolio_engine.py` performs calculations, `data/prices.csv` holds the saved inputs, `visible_output.json` holds executed results, and `tests/` validates them.
2. **0:30–1:20 — Data and estimates.** Show `load_prices` and `estimate_from_prices`. Explain the fixed tickers, consecutive monthly dates, simple returns, arithmetic annual return estimate, sample volatility, and correlation calculation.
3. **1:20–2:20 — Finance logic.** Show `mandate_verdict` and `constrained_portfolio`. Explain the 6.0% net-return hurdle, 10% SGOV reserve, long-only and 100% checks, and 5-point grid. Show how equal weight and 60/40 ACWI/USIG are evaluated with the same rules.
4. **2:20–3:10 — Live stress.** Run the app. Change ACWI's expected-return adjustment or cost; show the constrained output and the required pass/fail baseline verdicts.
5. **3:10–4:00 — Validation.** Run the unit tests. Show the DGS10 data card and distinguish its point-in-time monitoring use from a forecast.
6. **4:00–4:40 — Failure mode.** Explain that no feasible allocation stops the process, and a greater-than-20-point weight change stops it. Name historical estimation risk and the uncompleted Locked Changed-Input Record as the remaining integrity item.
