"""Capture a public ALFRED page and its retrieval metadata without credentials.

The response is a current retrieval snapshot, not a reconstructed old vintage.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
URL = "https://alfred.stlouisfed.org/series?seid=DGS10"

if __name__ == "__main__":
    result = subprocess.run(
        ["curl.exe", "--fail", "-L", "-sS", "--max-time", "25", URL],
        capture_output=True, check=True,
    )
    raw = result.stdout
    text = raw.decode("utf-8")
    if "DGS10" not in text or '"dateModified"' not in text:
        raise ValueError("Response is not the expected ALFRED DGS10 page.")
    folder = ROOT / "data" / "source-evidence"
    folder.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc)
    filename = "dgs10-" + stamp.strftime("%Y%m%dT%H%M%SZ") + ".html"
    (folder / filename).write_bytes(raw)
    metadata = {"source_url": URL, "retrieved_utc": stamp.isoformat(),
                "file": filename, "sha256": hashlib.sha256(raw).hexdigest(),
                "scope": "Current source-page snapshot only; not evidence of an earlier vintage."}
    (folder / (filename + ".json")).write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2))
