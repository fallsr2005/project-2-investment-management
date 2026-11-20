"""Recompute an audit report without overwriting the original visible output.

Run: python reproduce.py --output outputs/reproduced-results.json
"""
import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from portfolio_engine import (
    baseline_portfolios, constrained_portfolio, decision_status,
    estimate_from_prices, result_for_scenario,
)

ROOT = Path(__file__).resolve().parent


def report():
    source = ROOT / "data" / "prices.csv"
    estimates = estimate_from_prices(source)
    base = constrained_portfolio(estimates, 0.0, 0.10)
    scenarios = {}
    for name, params in {
        "ACWI minus one point": {"acwi_return_adjustment": -0.01},
        "last 36 returns": {"last_36": True},
        "annual cost 25bp": {"annual_cost": 0.0025},
        "SGOV minimum 20%": {"minimum_sgov": 0.20},
        "recorded annual cost 45bp": {"annual_cost": 0.0045},
        "infeasibility probe SGOV minimum 100%": {"minimum_sgov": 1.0},
    }.items():
        _, result = result_for_scenario(source, **params)
        status, reasons = decision_status(result, base, params.get("annual_cost", 0.0))
        scenarios[name] = {"inputs": params, "result": result, "status": status, "reasons": reasons}
    return {
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "price_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "historical_estimates_not_forecasts": asdict(estimates),
        "base": base,
        "baselines": baseline_portfolios(estimates, 0.0, 0.10),
        "scenarios": scenarios,
        "numerical_recommendation": "conditional classroom pilot",
        "operational_hold": "Verify the DGS10 vintage before adoption; original source response is absent.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "reproduced-results.json")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report(), indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"Saved reproduced results: {args.output}")
