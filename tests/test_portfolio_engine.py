import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from portfolio_engine import (  # noqa: E402
    DEFAULT_MINIMUM_SGOV,
    baseline_portfolios,
    constrained_portfolio,
    estimate_from_prices,
    load_prices,
    maximum_weight_change,
    mandate_verdict,
    decision_status,
    volatility,
    adjusted_estimates,
)


DATA = Path(__file__).resolve().parents[1] / "data" / "prices.csv"


class PortfolioEngineTests(unittest.TestCase):
    def test_base_matches_preserved_screenshot(self):
        estimates = estimate_from_prices(DATA)
        result = constrained_portfolio(estimates, 0, .10)
        self.assertAlmostEqual(result["weights"]["SGOV"], .70)
        self.assertAlmostEqual(result["net_return"], .06019889, places=7)
        self.assertAlmostEqual(result["volatility"], .04555754, places=7)

    def test_cost45_reoptimizes_and_requires_review(self):
        estimates = estimate_from_prices(DATA)
        base = constrained_portfolio(estimates, 0, .10)
        result = constrained_portfolio(estimates, .0045, .10)
        self.assertAlmostEqual(result["weights"]["ACWI"], .40)
        self.assertAlmostEqual(result["net_return"], result["gross_return"] - .0045)
        self.assertEqual(decision_status(result, base, .0045)[0], "REVIEW")
        fixed = mandate_verdict(base["weights"], estimates, .0045, .10)
        self.assertFalse(fixed["passes"])

    def test_infeasible_full_reserve_stops(self):
        estimates = estimate_from_prices(DATA)
        base = constrained_portfolio(estimates, 0, .10)
        result = constrained_portfolio(estimates, 0, 1.0)
        self.assertIsNone(result)
        self.assertEqual(decision_status(result, base, 0)[0], "STOP")

    def test_twenty_point_boundary_is_review_not_stop(self):
        estimates = estimate_from_prices(DATA)
        base = constrained_portfolio(estimates, 0, .10)
        short = constrained_portfolio(estimate_from_prices(DATA, True), 0, .10)
        self.assertEqual(decision_status(short, base, 0)[0], "REVIEW")
        far = dict(short, weights={"SGOV": .95, "SCHR": 0, "USIG": 0, "ACWI": .05})
        self.assertEqual(decision_status(far, base, 0)[0], "STOP")

    def test_single_asset_volatility_matches_input(self):
        estimates = estimate_from_prices(DATA)
        weights = dict.fromkeys(estimates.names, 0.0)
        weights["ACWI"] = 1.0
        self.assertAlmostEqual(volatility(weights, estimates), estimates.volatilities["ACWI"])

    def test_bad_prices_and_dates_rejected(self):
        raw = DATA.read_text()
        for bad in (raw.replace("83.389954", "nan"), raw.replace("2021-11-01", "2021-10-01")):
            with self.assertRaises(ValueError):
                load_prices(bad)

    def test_original_saved_output_matches_engine(self):
        import json
        saved = json.loads((DATA.parents[1] / "visible_output.json").read_text())
        estimates = estimate_from_prices(DATA)
        actual = constrained_portfolio(estimates, 0, .10)
        for field in ("net_return", "volatility"):
            self.assertAlmostEqual(actual[field], saved["portfolios"]["constrained_minimum_volatility"][field], places=7)
        for name, actual_baseline in baseline_portfolios(estimates, 0, .10).items():
            key = "equal_weight" if name == "Equal weight" else "benchmark_60_40_acwi_usig"
            self.assertAlmostEqual(actual_baseline["net_return"], saved["portfolios"][key]["net_return"], places=7)

    def test_prices_load_with_fixed_universe(self):
        dates, prices = load_prices(DATA)
        self.assertEqual(len(dates), 60)
        self.assertEqual(tuple(prices), ("SGOV", "SCHR", "USIG", "ACWI"))

    def test_estimates_have_expected_windows(self):
        self.assertEqual(estimate_from_prices(DATA).monthly_return_count, 59)
        self.assertEqual(estimate_from_prices(DATA, last_36=True).monthly_return_count, 36)

    def test_constrained_base_portfolio_is_feasible(self):
        result = constrained_portfolio(estimate_from_prices(DATA), 0.0, DEFAULT_MINIMUM_SGOV)
        self.assertIsNotNone(result)
        self.assertTrue(result["passes"])
        self.assertAlmostEqual(sum(result["weights"].values()), 1.0)
        self.assertGreaterEqual(result["weights"]["SGOV"], DEFAULT_MINIMUM_SGOV)

    def test_required_baselines_report_verdicts(self):
        results = baseline_portfolios(estimate_from_prices(DATA), 0.0, DEFAULT_MINIMUM_SGOV)
        self.assertEqual(set(results), {"Equal weight", "60/40 ACWI/USIG benchmark"})
        for result in results.values():
            self.assertIn("passes", result)
            self.assertIn("checks", result)

    def test_weight_change_is_in_percentage_units_as_a_decimal(self):
        change = maximum_weight_change(
            {"SGOV": 0.70, "SCHR": 0.0, "USIG": 0.0, "ACWI": 0.30},
            {"SGOV": 0.90, "SCHR": 0.0, "USIG": 0.0, "ACWI": 0.10},
        )
        self.assertAlmostEqual(change, 0.20)


if __name__ == "__main__":
    unittest.main()
