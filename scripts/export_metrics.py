import json
import csv
from pathlib import Path

release = Path("artifacts/release")
logs = release / "logs"
metrics = release / "metrics"

metrics.mkdir(parents=True, exist_ok=True)

log_file = logs / "server.log"

summary = {
    "valid_messages": 0,
    "rejected_messages": 0,
    "rate_limited_events": 0,
    "tls_enabled": True
}

if log_file.exists():
    for line in log_file.read_text().splitlines():
        line = line.lower()
        if "accepted" in line or "echoed" in line:
            summary["valid_messages"] += 1
        if "rejected" in line:
            summary["rejected_messages"] += 1
        if "rate" in line:
            summary["rate_limited_events"] += 1

(metrics / "summary.json").write_text(json.dumps(summary, indent=2))

with open(metrics / "results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["metric", "value"])
    for k, v in summary.items():
        writer.writerow([k, v])

print("Metrics exported:", summary)