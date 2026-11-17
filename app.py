"""Streamlit interface for the Project 2 constrained-portfolio decision."""

from pathlib import Path
import streamlit as st

from portfolio_engine import (
    DEFAULT_MINIMUM_SGOV,
    OBJECTIVE_RETURN,
    POINT_IN_TIME_SIGNAL,
    TICKERS,
    adjusted_estimates,
    baseline_portfolios,
    constrained_portfolio,
    estimate_from_prices,
    maximum_weight_change,
)


ROOT = Path(__file__).resolve().parent
DEFAULT_PRICES = ROOT / "data" / "prices.csv"


def as_source(upload):
    return upload.getvalue() if upload is not None else DEFAULT_PRICES


def percent(value):
    return f"{value:.2%}"


def allocation_table(results):
    rows = []
    for name, result in results.items():
        if result is None:
            rows.append({"Portfolio": name, "Verdict": "FAIL — no feasible allocation"})
            continue
        row = {"Portfolio": name}
        row.update({ticker: percent(result["weights"][ticker]) for ticker in TICKERS})
        row.update(
            {
                "Gross estimate": percent(result["gross_return"]),
                "Cost assumption": percent(result["annual_cost"]),
                "Net estimate": percent(result["net_return"]),
                "Volatility": percent(result["volatility"]),
                "SGOV reserve": percent(result["sgov_weight"]),
                "Verdict": "PASS" if result["passes"] else "FAIL — " + "; ".join(
                    name for name, passed in result["checks"].items() if not passed
                ),
            }
        )
        rows.append(row)
    return rows


def render_table(rows):
    """Render a simple Markdown table without importing Pandas or PyArrow.

    This keeps the application usable in managed Windows environments where optional
    binary data packages are blocked by application-control policy.
    """
    if not rows:
        st.info("No rows to display.")
        return
    columns = list(dict.fromkeys(key for row in rows for key in row))
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        values = [str(row.get(column, "")).replace("|", "/") for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    st.markdown("\n".join(lines))


def scenario_row(label, result, base):
    if result is None:
        return {"Scenario": label, "Result": "STOP — no feasible allocation", "Largest weight change": "n/a"}
    change = maximum_weight_change(base["weights"], result["weights"])
    return {
        "Scenario": label,
        "Result": "PASS" if result["passes"] else "FAIL",
        "SGOV": percent(result["weights"]["SGOV"]),
        "SCHR": percent(result["weights"]["SCHR"]),
        "USIG": percent(result["weights"]["USIG"]),
        "ACWI": percent(result["weights"]["ACWI"]),
        "Net estimate": percent(result["net_return"]),
        "Volatility": percent(result["volatility"]),
        "Largest weight change": percent(change),
    }


st.set_page_config(page_title="Project 2 — Investment Management", layout="wide")
st.title("Project 2 — Investment Management Application")
st.caption("AI used: ChatGPT/Codex assisted with code structure, tests, and documentation; I reviewed the analysis and own the decision. Education only — not investment advice.")
st.write("Historical adjusted-price estimates are not forecasts. The search is long-only and evaluates every 5-percentage-point allocation.")

with st.sidebar:
    st.header("Mandate and scenario")
    window = st.radio("Historical window", ("All 59 monthly returns", "Last 36 monthly returns"))
    minimum_sgov = st.slider("Minimum SGOV reserve", 0, 50, int(DEFAULT_MINIMUM_SGOV * 100), 5) / 100
    annual_cost = st.slider("Annual implementation-cost stress", 0.0, 1.0, 0.0, 0.05) / 100
    acwi_adjustment = st.slider("ACWI annual-return adjustment", -5.0, 5.0, 0.0, 0.25) / 100
    upload = st.file_uploader("Optional replacement monthly-price CSV", type="csv")

try:
    source = as_source(upload)
    last_36 = window.startswith("Last")
    raw_estimates = estimate_from_prices(source, last_36=last_36)
    estimates = adjusted_estimates(raw_estimates, acwi_adjustment)
    selected = constrained_portfolio(estimates, annual_cost, minimum_sgov)
    baselines = baseline_portfolios(estimates, annual_cost, minimum_sgov)
except ValueError as error:
    st.error(str(error))
    st.stop()

st.subheader("Mandate")
st.write(
    f"Objective: lowest estimated volatility with estimated **net** annual return of at least {OBJECTIVE_RETURN:.1%}; "
    f"universe: {', '.join(TICKERS)}; benchmark: 60% ACWI / 40% USIG; risk measure: annualized historical volatility; "
    f"limits: long-only, weights total 100%, and SGOV at least {minimum_sgov:.0%}."
)
st.caption(
    f"Loaded period: {raw_estimates.first_price_date} through {raw_estimates.last_price_date}; "
    f"{raw_estimates.monthly_return_count} monthly returns. Cost is a scenario assumption, not observed performance."
)

st.subheader("Constrained portfolio and required baselines")
all_results = {"Constrained minimum-volatility portfolio": selected, **baselines}
render_table(allocation_table(all_results))
if selected is None:
    st.error("The process stops: no 5-point allocation meets every mandate rule under this scenario.")
else:
    st.success("The constrained portfolio is feasible for the selected scenario. See the standard stress suite before adopting it.")

st.subheader("Historical inputs")
input_rows = [
    {
        "Ticker": ticker,
        "Annual arithmetic-mean return estimate": percent(estimates.returns[ticker]),
        "Annual sample volatility": percent(estimates.volatilities[ticker]),
    }
    for ticker in TICKERS
]
render_table(input_rows)

st.subheader("Point-in-time signal — DGS10")
st.write(
    f"As known on **{POINT_IN_TIME_SIGNAL['as_known_on']}**, DGS10's latest available observation was "
    f"**{POINT_IN_TIME_SIGNAL['last_observation_date']} = {POINT_IN_TIME_SIGNAL['value_percent']:.2f}%**. "
    f"It had a {POINT_IN_TIME_SIGNAL['publication_lag']}."
)
st.caption(
    "Use: monitor the SCHR Treasury sleeve and verify that each decision uses an ALFRED vintage available at the decision date. "
    "This signal is not used as a return forecast. Source: " + POINT_IN_TIME_SIGNAL["source_url"]
)

st.subheader("Standard stress suite")
base_estimates = estimate_from_prices(source, last_36=False)
base = constrained_portfolio(base_estimates, 0.0, DEFAULT_MINIMUM_SGOV)
if base is None:
    st.error("Bundled base case is unexpectedly infeasible; check the saved data.")
else:
    stress_specs = [
        ("Base: all returns, 0 cost, 10% SGOV", False, 0.0, 0.0, 0.10),
        ("Estimate: ACWI return minus 1 percentage point", False, -0.01, 0.0, 0.10),
        ("Window: last 36 returns", True, 0.0, 0.0, 0.10),
        ("Cost: 25 basis points annually", False, 0.0, 0.0025, 0.10),
        ("Constraint: SGOV minimum 20%", False, 0.0, 0.0, 0.20),
    ]
    rows = []
    stop = False
    for label, use_last_36, return_adjustment, cost, reserve in stress_specs:
        stress_estimates = adjusted_estimates(estimate_from_prices(source, last_36=use_last_36), return_adjustment)
        outcome = constrained_portfolio(stress_estimates, cost, reserve)
        rows.append(scenario_row(label, outcome, base))
        if outcome is None or (outcome and maximum_weight_change(base["weights"], outcome["weights"]) > 0.20 + 1e-12):
            stop = True
    render_table(rows)
    if stop:
        st.error("Stop condition met: a scenario has no feasible allocation or moves a weight by more than 20 percentage points from base. Do not adopt; reassess the mandate and estimates.")
    else:
        st.info("Stop condition not met in this fixed suite. The 36-month-window difference remains a material limitation and supports a pilot, not full adoption.")

st.subheader("Decision rule")
st.write("Recommendation: **pilot, not full adoption**. Start from the base allocation only after the committee accepts the historical-estimate limitation and point-in-time DGS10 rule. Reassess if no scenario is feasible, any stress moves a weight by more than 20 points, the DGS10 vintage is unavailable, or the committee changes the 6.0% target or SGOV reserve requirement.")
