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
)


DATA = Path(__file__).resolve().parents[1] / "data" / "prices.csv"


class PortfolioEngineTests(unittest.TestCase):
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
