"""Reject unusable or altered provider evidence, not just incorrect app outputs."""
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit_price_sources import audit, parse_response

SNAPSHOT = Path(__file__).resolve().parents[1] / 'data/source-evidence/prices-20261122T233854Z'


class PriceLineageTests(unittest.TestCase):
    def test_saved_capture_reproduces_and_base_decision_is_stable(self):
        actual, csv_text = audit(SNAPSHOT)
        expected = json.loads((SNAPSHOT / 'comparison-report.json').read_text(encoding='utf-8'))
        self.assertEqual(actual, expected)
        self.assertEqual(csv_text, (SNAPSHOT / 'comparison-prices.csv').read_text(encoding='utf-8'))
        self.assertEqual(actual['saved_base']['weights'], actual['later_capture_base']['weights'])

    def test_corrupted_raw_response_is_rejected(self):
        with patch('audit_price_sources.Path.read_bytes', return_value=b'changed raw evidence'):
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                audit(SNAPSHOT)

    def test_wrong_symbol_missing_month_or_null_price_is_rejected(self):
        raw = (SNAPSHOT / 'ACWI.json').read_bytes()
        payload = json.loads(raw)
        result = payload['chart']['result'][0]
        from datetime import datetime, timezone
        months = [datetime.fromtimestamp(t, timezone.utc).strftime('%Y-%m') for t in result['timestamp']]
        with self.assertRaisesRegex(ValueError, 'unexpected source symbol'):
            parse_response(raw, 'SGOV', months)
        with self.assertRaisesRegex(ValueError, 'months do not match'):
            parse_response(raw, 'ACWI', months[:-1])
        result['indicators']['adjclose'][0]['adjclose'][0] = None
        with self.assertRaisesRegex(ValueError, 'invalid adjusted price'):
            parse_response(json.dumps(payload).encode(), 'ACWI', months)


if __name__ == '__main__':
    unittest.main()
