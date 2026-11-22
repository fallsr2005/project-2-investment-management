"""Download five complete years of monthly Yahoo Finance adjusted closes."""
import csv
import datetime as dt
import json
import urllib.request

TICKERS = ("SGOV", "SCHR", "USIG", "ACWI")
# October 2021 through September 2026; end is exclusive.
START = 1633046400
END = 1790812800


def download(ticker):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?period1={START}&period2={END}&interval=1mo&events=history")
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)["chart"]["result"][0]
    values = result["indicators"]["adjclose"][0]["adjclose"]
    return {dt.datetime.fromtimestamp(timestamp, dt.timezone.utc).strftime("%Y-%m"):
            value for timestamp, value in zip(result["timestamp"], values) if value is not None}


def main():
    data = {ticker: download(ticker) for ticker in TICKERS}
    months = sorted(data[TICKERS[0]])
    if len(months) != 60 or any(set(data[ticker]) != set(months) for ticker in TICKERS):
        raise ValueError("Expected 60 complete, matching monthly observations per ticker.")
    with open("prices.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(("date", *TICKERS))
        for month in months:
            writer.writerow((month + "-01", *(f"{data[ticker][month]:.6f}" for ticker in TICKERS)))
    print(f"Wrote {len(months)} months: {months[0]} through {months[-1]}.")


if __name__ == "__main__":
    main()
