import csv
import urllib.request
import json
import os
from datetime import datetime, timezone, timedelta

url = "https://gist.githubusercontent.com/XYZenix/95de40ff80091c0ff7b0cfd610bd10d7/raw/aea71374db7e0d9d8446e89d37722431e6683bef/experiments.csv"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read().decode('utf-8').splitlines()

reader = csv.DictReader(content)
experiments = list(reader)

history_path = "data/history.json"
if os.path.exists(history_path):
    with open(history_path, "r", encoding="utf-8") as f:
        history = json.load(f)
else:
    history = {"experiments": [], "api_endpoints": [], "strings": []}

# To maintain historical order, we simulate older timestamps for earlier rows
now = datetime.now(timezone.utc)
base_time = now - timedelta(days=len(experiments))

# Clear existing experiments from history to avoid duplicates
existing_ids = set()
new_exps_history = []

for idx, row in enumerate(experiments):
    exp_id = row["name"].lower()  # use lowercase for id to match our datamining format
    kind = row["type"] if row["type"] else "unknown"
    # we don't have treatments in csv, just empty
    timestamp = (base_time + timedelta(days=idx)).isoformat()
    
    existing_ids.add(exp_id)
    new_exps_history.append({
        "id": exp_id,
        "kind": kind,
        "treatments": [],
        "status": "added",
        "timestamp": timestamp
    })

# prepend the backfilled experiments to history
history["experiments"] = new_exps_history + [e for e in history["experiments"] if e["id"] not in existing_ids]

with open(history_path, "w", encoding="utf-8") as f:
    json.dump(history, f, ensure_ascii=False, indent=4)

print(f"Backfilled {len(new_exps_history)} experiments into history.json")
