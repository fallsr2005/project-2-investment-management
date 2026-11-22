AI used: ChatGPT/Codex assisted with code structure, tests, and documentation; the analysis and decision require my review and are mine.

Education only — not investment advice.

# Project 2 — Investment Management Application

This is a reproducible classroom portfolio-analysis app for FIN 43900. It evaluates a long-only four-ETF mandate and recommends whether a committee should pilot the process. The included output is based on saved monthly adjusted prices, so its return, volatility, and correlation figures are historical estimates—not forecasts.

## Decision

**Pilot, not full adoption.** The base 5-point-grid search selects 70% SGOV and 30% ACWI, with a 6.02% estimated annual return and 4.56% estimated annual volatility. The result is sensitive to its historical window: the last-36-return run selects 90% SGOV and 10% ACWI. See [the decision memo](docs/decision-memo.md) and [current reproduced output](outputs/reproduced-results.json). The original [November 16 output](visible_output.json) is historical evidence; its DGS10 section has been superseded by the dated source correction.

The proposed horizon is a three-month classroom pilot with monthly reviews, subject to committee approval. The base feasible candidate range within the original review band is 65–70% SGOV / 30–35% ACWI, paired to total 100%; every mix must pass independently after costs. At 45 basis points of cost, 60/40 SGOV/ACWI requires committee reassessment. DGS10 is now verified against a preserved current source-page snapshot; it is not retrospective September-vintage evidence.

## Mandate

| Field | Classroom definition |
|---|---|
| Objective | Minimize estimated annual volatility while estimated net annual return is at least 6.0% |
| Universe | SGOV, SCHR, USIG, and ACWI only |
| Benchmark | 60% ACWI / 40% USIG |
| Risk measure | Annualized sample volatility calculated from monthly simple returns |
| Limits | Long-only, weights sum to 100%, SGOV reserve at least 10%; 5-percentage-point allocation grid |
| Point-in-time signal | DGS10 as known through its saved ALFRED vintage; monitoring only, not a return forecast |

The app displays both required baselines—equal weight and the 60/40 benchmark—alongside the constrained allocation. It shows every mandate check and the rule behind each failure.

## Run it

Open a terminal in the repository folder (the folder containing `app.py`). Python 3.12 or 3.13 is recommended. If you downloaded a ZIP, extract it first. Run the following once to install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Then this single command starts the app:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The app starts with `data/prices.csv`. It accepts an optional replacement CSV only when it has exactly these columns, in this order: `date,SGOV,SCHR,USIG,ACWI`; dates must be consecutive monthly observations, oldest first.

## Verify

```powershell
python -m unittest discover -s tests -v
```

The 17-test suite checks data validation, both windows, calculations against preserved output, cost-driven reoptimization, baseline verdicts, single-asset volatility, STOP/REVIEW boundaries, DGS10 source verification, and the captured Yahoo price lineage. Source tests reject altered raw responses, incorrect ticker identities, missing months, and null adjusted prices.

Reproduce an audit report without changing the original output:

```powershell
.\.venv\Scripts\python.exe reproduce.py --output outputs/reproduced-results.json
```

Verify the November 22 price-source capture entirely offline:

```powershell
python audit_price_sources.py --snapshot data/source-evidence/prices-20261122T233854Z
```

This checks raw-response hashes and reconstructs the later comparison dataset and report without changing the app's input. See [price lineage](docs/price-data-lineage.md) for results and boundaries.

## Project map

| Location | Purpose |
|---|---|
| `app.py` | Streamlit interface; constrained portfolio, two baselines, point-in-time signal, and stress suite |
| `portfolio_engine.py` | CSV validation, historical estimates, portfolio metrics, mandate verdicts, and grid search |
| `data/prices.csv` | 60 monthly adjusted-price observations, October 2021–September 2026 |
| `visible_output.json` | Saved base, baseline, and standard-stress results without running code |
| `docs/investment-mandate.md` | Formal classroom mandate, benchmark, risk measure, limits, and stop conditions |
| `docs/lab-20-project-2-readiness.md` | Lab 20 readiness evidence and the required partner/AI-closed entries |
| `docs/decision-memo.md` | Committee-ready decision and monitoring plan |
| `docs/validation-and-ai-use.md` | Sources, tests, limitations, AI disclosure, and Locked Changed-Input Record status |
| `docs/data-card-dgs10.md` | Point-in-time signal definition, timing, revision treatment, and use rule |
| `docs/video-*-script.md` | Recording guides; revise the matching transcript after recording if spoken wording differs |
| `manifest.csv` | Brightspace submission index; replace only the URL placeholders after publishing |

## Sources and limitations

Lab 14/15 records report a Yahoo Finance chart-endpoint download on 2026-10-22; the original raw response is unavailable. The original downloader and relevant lab excerpts are bundled. A separate November 22 capture now preserves all four current raw responses, retrieval times, hashes, and a reproducible comparison. Price levels differ, while the base mix remains 70% SGOV / 30% ACWI and displays the same 6.02% return and 4.56% volatility. This corroborates the later source comparison, not the original download timestamp or historical information availability. The data uses adjusted closes, which can be revised. DGS10 is from the Federal Reserve Bank of St. Louis; see its data card for the captured current-review evidence. Third-party redistribution rights remain unverified; see the price-lineage record.

The project does not model taxes, bid-ask spreads, turnover, drawdown, investor liquidity needs, or realized performance. The 5-point grid is not a continuous optimizer. A passing arithmetic check does not validate a forward-looking return assumption. Adjusted closes already incorporate vendor distribution/split adjustments and fund-level effects; the explicit cost stress is additional implementation cost, not a second deduction of fund expenses.

DGS10's current source-page capture is preserved with a timestamp and hash in `data/source-evidence/`; the app reads 2026-11-18 at 5.07%, available at capture on 2026-11-20 at 06:08 UTC. It does not substantiate the older September claim. See the [price lineage](docs/price-data-lineage.md), [rubric evidence map](docs/rubric-evidence-map.md), and [requirement audit](docs/project-2-requirement-audit.md). Historical evidence and the original changed-input prediction remain preserved in Git history.
