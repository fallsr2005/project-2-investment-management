AI used: ChatGPT/Codex helped develop code, tests, documentation, and this recording draft. I am responsible for reviewing the analysis and owning the final decision.

Education only — not investment advice.

# Video 2 — code walkthrough

Recording draft, not an actual transcript. Target 4:00–4:40; hard limit 5:00. Show a small webcam view unless accommodated. Speak the opening disclosures. Show actual code and actual test output; do not only read this document.

**Open the submitted repository in VS Code.**

The app imports one portfolio engine. `app.py` controls the interface, `portfolio_engine.py` performs the finance calculations, and `data/prices.csv` holds the saved four-fund inputs. The original visible output and screenshots preserve earlier results; `reproduce.py` creates a current report without overwriting them.

**Open `load_prices` and `estimate_from_prices`.**

The parser requires exactly SGOV, SCHR, USIG, and ACWI, positive finite prices, and consecutive monthly labels. The 60 prices produce 59 adjacent simple monthly returns. First-of-month labels identify a completed monthly price; they are not its availability timestamp. Annual return is monthly arithmetic mean times twelve; sample volatility is monthly sample standard deviation times the square root of twelve. The last-36 option changes the sample, not the target. Correlations use the same aligned return observations.

**Open `mandate_verdict` and `constrained_portfolio`.**

Gross return is the weighted return estimate. Net return subtracts an explicit annual implementation-cost assumption. The checks require full investment, nonnegative weights, the minimum SGOV reserve, and at least six percent net estimated return. Equal weight and the 60/40 benchmark use these same checks.

The search enumerates allocations in five-point steps. It keeps only qualifying portfolios and retains the one with lowest covariance-based volatility. It returns no result if none qualifies. This is an exhaustive grid search, not a continuous optimum.

**Run the test suite in the terminal.**

The tests check original saved numbers, reject malformed prices, compare single-asset volatility to its input, and exercise the 45-basis-point cost case. At fixed base weights, that cost misses the target; after reoptimization, the selected weights are 60/40 SGOV/ACWI. The tests also distinguish a 20-point REVIEW from a greater-than-20-point STOP, and test infeasibility at a 100-percent SGOV floor.

**Show `verify_signal_evidence` and `decision_status`.**

The source check compares the captured ALFRED page's hash and parses the actual observation date and value. Missing or changed evidence stops operational use. This snapshot only supports decisions at or after capture; it does not supply historical vintages. The numerical decision applies review and stop rules to selected allocations, rather than always saying pilot.

**Show the README and app.**

After installing requirements in a virtual environment, one Streamlit command starts the app. The base output is 70/30 SGOV/ACWI. Raising cost to 0.45 produces REVIEW; selecting a 100-percent SGOV floor produces STOP. Restore defaults after demonstrating those controls. Historical estimation risk and vendor revisions remain limitations, regardless of passing tests.
