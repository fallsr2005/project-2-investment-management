"""Capture dated Yahoo responses, then reproduce an offline price-lineage audit.

Never overwrites data/prices.csv. A later capture cannot prove an earlier vintage.
Capture: python audit_price_sources.py --capture
Offline: python audit_price_sources.py --snapshot data/source-evidence/prices-TIMESTAMP
"""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from math import isfinite
from pathlib import Path
import subprocess

from portfolio_engine import (
    TICKERS, baseline_portfolios, constrained_portfolio, estimate_from_prices,
)

ROOT = Path(__file__).resolve().parent
START, END = 1633046400, 1790812800


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def parse_response(raw, ticker, expected_months):
    payload = json.loads(raw)
    chart = payload['chart']
    if chart.get('error') or not chart.get('result'):
        raise ValueError(f'{ticker}: source returned no usable result')
    result = chart['result'][0]
    if result['meta']['symbol'] != ticker:
        raise ValueError(f'{ticker}: unexpected source symbol')
    stamps = result['timestamp']
    values = result['indicators']['adjclose'][0]['adjclose']
    if len(stamps) != len(values):
        raise ValueError(f'{ticker}: timestamp/adjusted-price length mismatch')
    months = [datetime.fromtimestamp(t, timezone.utc).strftime('%Y-%m') for t in stamps]
    if months != expected_months:
        raise ValueError(f'{ticker}: source months do not match saved sample exactly')
    if any(v is None or not isfinite(v) or v <= 0 for v in values):
        raise ValueError(f'{ticker}: invalid adjusted price; no silent exclusions allowed')
    return values


def capture():
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    folder = ROOT / 'data' / 'source-evidence' / ('prices-' + stamp)
    folder.mkdir(parents=True, exist_ok=False)
    metadata = {
        'scope': 'Later current retrieval; not proof of the reported October 22 vintage.',
        'responses': {},
    }
    for ticker in TICKERS:
        url = (f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}'
               f'?period1={START}&period2={END}&interval=1mo&events=history')
        # Only the public response body is preserved; no cookies or credentials.
        result = subprocess.run(
            ['curl.exe', '--fail', '-L', '-sS', '--max-time', '30', '-A',
             'Mozilla/5.0', url], capture_output=True, check=True,
        )
        raw = result.stdout
        filename = ticker + '.json'
        (folder / filename).write_bytes(raw)
        metadata['responses'][ticker] = {
            'source_url': url, 'file': filename, 'sha256': sha256(raw),
            'retrieved_utc': datetime.now(timezone.utc).isoformat(),
        }
        (folder / 'metadata.json').write_text(
            json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
    return folder


def audit(folder):
    folder = Path(folder)
    metadata = json.loads((folder / 'metadata.json').read_text(encoding='utf-8'))
    saved_path = ROOT / 'data' / 'prices.csv'
    saved_raw = saved_path.read_bytes()
    rows = list(csv.DictReader(io.StringIO(saved_raw.decode('utf-8-sig'))))
    months = [row['date'][:7] for row in rows]
    refreshed, comparisons = {}, {}
    for ticker in TICKERS:
        entry = metadata['responses'][ticker]
        if entry['file'] != ticker + '.json':
            raise ValueError(f'{ticker}: unexpected response filename')
        raw = (folder / entry['file']).read_bytes()
        if sha256(raw) != entry['sha256']:
            raise ValueError(f'{ticker}: raw response hash mismatch')
        fresh = parse_response(raw, ticker, months)
        refreshed[ticker] = fresh
        old = [float(row[ticker]) for row in rows]
        differences = [abs(a - b) for a, b in zip(old, fresh)]
        comparisons[ticker] = {
            'observations': len(fresh),
            'matching_at_saved_six_decimals': sum(
                f'{a:.6f}' == f'{b:.6f}' for a, b in zip(old, fresh)),
            'maximum_absolute_price_difference_usd': max(differences),
            'maximum_relative_price_difference_percent': max(
                d / a * 100 for d, a in zip(differences, old)),
            'source_url': entry['source_url'],
            'raw_sha256': entry['sha256'],
            'retrieved_utc': entry['retrieved_utc'],
        }
    buffer = io.StringIO(newline='')
    writer = csv.writer(buffer, lineterminator='\n')
    writer.writerow(['date', *TICKERS])
    for i, row in enumerate(rows):
        writer.writerow([row['date'], *(f'{refreshed[t][i]:.6f}' for t in TICKERS)])
    # Apply the original six-decimal transformation before comparing estimates.
    comparison_csv = buffer.getvalue()
    saved = estimate_from_prices(saved_path)
    current = estimate_from_prices(comparison_csv)
    for ticker in TICKERS:
        comparisons[ticker]['annual_return_change_percentage_points'] = (
            current.returns[ticker] - saved.returns[ticker]) * 100
        comparisons[ticker]['annual_volatility_change_percentage_points'] = (
            current.volatilities[ticker] - saved.volatilities[ticker]) * 100
    return {
        'saved_price_sha256': sha256(saved_raw),
        'scope': metadata['scope'],
        'all_raw_hashes_verified': True,
        'all_months_matched': True,
        'per_ticker': comparisons,
        'saved_base': constrained_portfolio(saved, 0, .10),
        'later_capture_base': constrained_portfolio(current, 0, .10),
        'saved_baselines': baseline_portfolios(saved, 0, .10),
        'later_capture_baselines': baseline_portfolios(current, 0, .10),
        'interpretation': 'Differences are observed, not attributed to a specific vendor revision. '
                          'This comparison corroborates current-source proximity only; it does '
                          'not authenticate the original retrieval date or grant redistribution rights.',
    }, comparison_csv


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--capture', action='store_true')
    mode.add_argument('--snapshot', type=Path)
    args = parser.parse_args()
    folder = capture() if args.capture else args.snapshot
    report, comparison_csv = audit(folder)
    # Immutable capture bundle: offline verification recomputes but does not rewrite it.
    if args.capture:
        (folder / 'comparison-prices.csv').write_text(comparison_csv, encoding='utf-8')
        (folder / 'comparison-report.json').write_text(
            json.dumps(report, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    else:
        preserved = json.loads((folder / 'comparison-report.json').read_text(encoding='utf-8'))
        if report != preserved:
            raise ValueError('Recomputed audit differs from preserved report')
        if (folder / 'comparison-prices.csv').read_text(encoding='utf-8') != comparison_csv:
            raise ValueError('Reconstructed comparison CSV differs from preserved file')
    print('Verified price audit:', folder)
    for ticker, values in report['per_ticker'].items():
        print(ticker, 'max absolute price difference:',
              values['maximum_absolute_price_difference_usd'])
    print('Saved / later base weights:', report['saved_base']['weights'],
          report['later_capture_base']['weights'])


if __name__ == '__main__':
    main()
