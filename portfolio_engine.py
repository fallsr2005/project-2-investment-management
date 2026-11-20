"""Reproducible portfolio calculations for FIN 43900 Project 2.

All returns are historical estimates from the supplied monthly adjusted-close file.
They are not forecasts or investment advice.
"""

from __future__ import annotations

import csv
import io
import hashlib
import re
from dataclasses import dataclass
from datetime import date
from math import isfinite, sqrt
from pathlib import Path
from statistics import mean, stdev
from typing import Iterable


TICKERS = ("SGOV", "SCHR", "USIG", "ACWI")
OBJECTIVE_RETURN = 0.06
DEFAULT_MINIMUM_SGOV = 0.10
GRID_STEP = 0.05

# This is a point-in-time monitoring signal, not a return forecast or optimizer input.
POINT_IN_TIME_SIGNAL = {
    "series_id": "DGS10",
    "name": "10-year Treasury constant-maturity rate",
    "source_url": "https://fred.stlouisfed.org/series/DGS10",
    "as_known_on": "2026-11-20T06:08:22.334570+00:00",
    "last_observation_date": "2026-11-18",
    "value_percent": 5.07,
    "publication_lag": "source updated 2026-11-19 at 15:16 CST; captured 2026-11-20 at 06:08 UTC",
    "evidence_status": "captured current source page; not a reconstructed historical vintage",
    "evidence_file": "data/source-evidence/dgs10-20261120T060822Z.html",
    "evidence_sha256": "9a2017ca4195f97c8246fa92112cdff6c3fac4a94d06c72177b5d73f31da80e1",
    "use": "monitoring condition for the SCHR Treasury sleeve; not an optimizer return input",
}


def verify_signal_evidence():
    """Fail closed if the saved source differs or lacks the displayed observation."""
    source = Path(__file__).resolve().parent / POINT_IN_TIME_SIGNAL["evidence_file"]
    try:
        raw = source.read_bytes()
    except OSError:
        return False
    if hashlib.sha256(raw).hexdigest() != POINT_IN_TIME_SIGNAL["evidence_sha256"]:
        return False
    text = raw.decode("utf-8")
    match = re.search(r'(\d{4}-\d{2}-\d{2}):\s*<span class="series-meta-observation-value">([\d.]+)</span>', text)
    return bool(match and match[1] == POINT_IN_TIME_SIGNAL["last_observation_date"]
                and float(match[2]) == POINT_IN_TIME_SIGNAL["value_percent"])


@dataclass(frozen=True)
class Estimates:
    names: tuple[str, ...]
    returns: dict[str, float]
    volatilities: dict[str, float]
    correlations: list[list[float]]
    monthly_return_count: int
    first_price_date: str
    last_price_date: str


def load_prices(source: str | bytes | Path) -> tuple[list[date], dict[str, list[float]]]:
    """Read consecutive, oldest-first monthly adjusted prices for the fixed mandate universe."""
    if isinstance(source, Path):
        text = source.read_text(encoding="utf-8-sig")
    elif isinstance(source, bytes):
        text = source.decode("utf-8-sig")
    else:
        text = source
    rows = list(csv.reader(io.StringIO(text)))
    if not rows or tuple(cell.strip() for cell in rows[0]) != ("date", *TICKERS):
        raise ValueError("CSV columns must be exactly: date, SGOV, SCHR, USIG, ACWI.")
    dates: list[date] = []
    values = {name: [] for name in TICKERS}
    for row in rows[1:]:
        if not row or all(not cell.strip() for cell in row):
            continue
        if len(row) != len(TICKERS) + 1:
            raise ValueError("Each row needs a date and one positive price for every mandate ticker.")
        try:
            observed = date.fromisoformat(row[0].strip())
            prices = [float(cell) for cell in row[1:]]
        except ValueError as exc:
            raise ValueError("Dates must be YYYY-MM-DD and prices must be numeric.") from exc
        if any(not isfinite(price) or price <= 0 for price in prices):
            raise ValueError("Adjusted prices must be positive and finite.")
        if dates and observed.year * 12 + observed.month != dates[-1].year * 12 + dates[-1].month + 1:
            raise ValueError("Prices must be consecutive monthly observations, oldest first.")
        dates.append(observed)
        for name, price in zip(TICKERS, prices):
            values[name].append(price)
    if len(dates) < 37:
        raise ValueError("At least 37 monthly prices are required for the 36-return sensitivity window.")
    return dates, values


def estimate_from_prices(source: str | bytes | Path, last_36: bool = False) -> Estimates:
    """Estimate arithmetic annual returns, sample annual volatility, and correlations."""
    dates, prices = load_prices(source)
    series = {
        name: [prices[name][index] / prices[name][index - 1] - 1 for index in range(1, len(dates))]
        for name in TICKERS
    }
    if last_36:
        series = {name: returns[-36:] for name, returns in series.items()}
    averages = {name: mean(returns) for name, returns in series.items()}
    deviations = {name: stdev(returns) for name, returns in series.items()}
    if any(value <= 0 for value in deviations.values()):
        raise ValueError("Each ticker needs nonzero historical volatility.")
    correlations: list[list[float]] = []
    for left in TICKERS:
        row = []
        for right in TICKERS:
            if left == right:
                row.append(1.0)
                continue
            covariance = sum(
                (a - averages[left]) * (b - averages[right])
                for a, b in zip(series[left], series[right])
            ) / (len(series[left]) - 1)
            row.append(max(-1.0, min(1.0, covariance / (deviations[left] * deviations[right]))))
        correlations.append(row)
    return Estimates(
        names=TICKERS,
        returns={name: averages[name] * 12 for name in TICKERS},
        volatilities={name: deviations[name] * sqrt(12) for name in TICKERS},
        correlations=correlations,
        monthly_return_count=len(series[TICKERS[0]]),
        first_price_date=dates[-37].isoformat() if last_36 else dates[0].isoformat(),
        last_price_date=dates[-1].isoformat(),
    )


def covariance_matrix(estimates: Estimates) -> list[list[float]]:
    return [
        [
            estimates.correlations[i][j]
            * estimates.volatilities[left]
            * estimates.volatilities[right]
            for j, right in enumerate(estimates.names)
        ]
        for i, left in enumerate(estimates.names)
    ]


def gross_return(weights: dict[str, float], estimates: Estimates) -> float:
    return sum(weights[name] * estimates.returns[name] for name in estimates.names)


def volatility(weights: dict[str, float], estimates: Estimates) -> float:
    matrix = covariance_matrix(estimates)
    values = [weights[name] for name in estimates.names]
    variance = sum(
        values[i] * values[j] * matrix[i][j]
        for i in range(len(values))
        for j in range(len(values))
    )
    if variance < -1e-12:
        raise ValueError("Portfolio variance was negative; check the covariance inputs.")
    return sqrt(max(0.0, variance))


def compositions(total: int, count: int) -> Iterable[tuple[int, ...]]:
    if count == 1:
        yield (total,)
        return
    for part in range(total + 1):
        for remaining in compositions(total - part, count - 1):
            yield (part, *remaining)


def mandate_verdict(
    weights: dict[str, float], estimates: Estimates, annual_cost: float, minimum_sgov: float
) -> dict[str, object]:
    """Evaluate every checkable Project 2 rule; costs are an explicit sensitivity assumption."""
    total = sum(weights.values())
    gross = gross_return(weights, estimates)
    net = gross - annual_cost
    checks = {
        "Weights sum to 100%": abs(total - 1.0) < 1e-9,
        "Long-only": all(weight >= -1e-12 for weight in weights.values()),
        f"SGOV reserve >= {minimum_sgov:.0%}": weights.get("SGOV", 0.0) + 1e-12 >= minimum_sgov,
        f"Estimated net return >= {OBJECTIVE_RETURN:.1%}": net + 1e-12 >= OBJECTIVE_RETURN,
    }
    return {
        "weights": weights,
        "gross_return": gross,
        "annual_cost": annual_cost,
        "net_return": net,
        "volatility": volatility(weights, estimates),
        "sgov_weight": weights.get("SGOV", 0.0),
        "checks": checks,
        "passes": all(checks.values()),
    }


def constrained_portfolio(estimates: Estimates, annual_cost: float, minimum_sgov: float) -> dict[str, object] | None:
    """Find the lowest-volatility feasible long-only allocation on a 5-percentage-point grid."""
    if not 0 <= annual_cost < 1 or not 0 <= minimum_sgov <= 1:
        raise ValueError("Cost and reserve inputs must be between 0% and 100%.")
    best = None
    for units in compositions(round(1 / GRID_STEP), len(estimates.names)):
        weights = {name: unit * GRID_STEP for name, unit in zip(estimates.names, units)}
        result = mandate_verdict(weights, estimates, annual_cost, minimum_sgov)
        if result["passes"] and (best is None or result["volatility"] < best["volatility"] - 1e-12):
            best = result
    return best


def baseline_portfolios(estimates: Estimates, annual_cost: float, minimum_sgov: float) -> dict[str, dict[str, object]]:
    """Return the mandate benchmark and required equal-weight comparator."""
    equal_weight = {name: 1 / len(estimates.names) for name in estimates.names}
    benchmark = {"SGOV": 0.0, "SCHR": 0.0, "USIG": 0.40, "ACWI": 0.60}
    return {
        "Equal weight": mandate_verdict(equal_weight, estimates, annual_cost, minimum_sgov),
        "60/40 ACWI/USIG benchmark": mandate_verdict(benchmark, estimates, annual_cost, minimum_sgov),
    }


def adjusted_estimates(estimates: Estimates, acwi_return_adjustment: float) -> Estimates:
    """Apply an explicit sensitivity only to ACWI's annual expected-return estimate."""
    returns = dict(estimates.returns)
    returns["ACWI"] += acwi_return_adjustment
    return Estimates(
        names=estimates.names,
        returns=returns,
        volatilities=estimates.volatilities,
        correlations=estimates.correlations,
        monthly_return_count=estimates.monthly_return_count,
        first_price_date=estimates.first_price_date,
        last_price_date=estimates.last_price_date,
    )


def maximum_weight_change(left: dict[str, float], right: dict[str, float]) -> float:
    return max(abs(left[name] - right[name]) for name in TICKERS)


def decision_status(selected, base, annual_cost, suite_stopped=False):
    """Apply the documented stop and committee-review triggers to current results."""
    if selected is None or base is None:
        return "STOP", ["No feasible allocation under the selected or reference inputs."]
    change = maximum_weight_change(selected["weights"], base["weights"])
    if suite_stopped or change > 0.20 + 1e-12:
        return "STOP", ["A selected or standard stress moves a weight by more than 20 percentage points, or is infeasible."]
    reasons = []
    if annual_cost > 0.0025 + 1e-12:
        reasons.append("Annual implementation cost exceeds the 25-basis-point review trigger.")
    if not 0.65 - 1e-12 <= selected["weights"]["SGOV"] <= 0.75 + 1e-12:
        reasons.append("SGOV is outside the original 65–75% candidate review band.")
    if change >= 0.20 - 1e-12:
        reasons.append("A 20-percentage-point move requires committee escalation.")
    return ("REVIEW", reasons) if reasons else ("PILOT", ["Numerical checks allow a classroom pilot, subject to evidence review and committee approval."])


def result_for_scenario(
    source: str | bytes | Path,
    *,
    last_36: bool = False,
    acwi_return_adjustment: float = 0.0,
    annual_cost: float = 0.0,
    minimum_sgov: float = DEFAULT_MINIMUM_SGOV,
) -> tuple[Estimates, dict[str, object] | None]:
    estimates = adjusted_estimates(estimate_from_prices(source, last_36), acwi_return_adjustment)
    return estimates, constrained_portfolio(estimates, annual_cost, minimum_sgov)
