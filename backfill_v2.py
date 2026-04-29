import csv
import urllib.request
import json
import os
from datetime import datetime, timezone, timedelta

history_path = "data/history.json"
if os.path.exists(history_path):
    with open(history_path, "r", encoding="utf-8") as f:
        history = json.load(f)
else:
    history = {"experiments": [], "api_endpoints": [], "strings": []}

now = datetime.now(timezone.utc)

# 1. Backfill latest experiments.csv
url = "https://gist.githubusercontent.com/XYZenix/95de40ff80091c0ff7b0cfd610bd10d7/raw/experiments.csv"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read().decode('utf-8').splitlines()

reader = csv.DictReader(content)
experiments = list(reader)
base_time = now - timedelta(days=len(experiments))

existing_exp_ids = set()
new_exps_history = []

for idx, row in enumerate(experiments):
    exp_id = row["name"].lower() if row.get("name") else row.get("id", "").lower()
    if not exp_id:
        continue
    kind = row.get("type", "unknown")
    if not kind:
        kind = "unknown"
    timestamp = (base_time + timedelta(days=idx)).isoformat()
    
    existing_exp_ids.add(exp_id)
    new_exps_history.append({
        "id": exp_id,
        "kind": kind,
        "treatments": [],
        "status": "added",
        "timestamp": timestamp
    })

history["experiments"] = new_exps_history + [e for e in history.get("experiments", []) if e["id"] not in existing_exp_ids]
print(f"Backfilled {len(new_exps_history)} experiments.")

# 2. Backfill strings from message.txt
msg_path = "data/message.txt"
if os.path.exists(msg_path):
    with open(msg_path, "r", encoding="utf-8") as f:
        try:
            strings_dict = json.load(f)
            
            existing_str_keys = {s["key"] for s in history.get("strings", []) if s["lang"] == "ko"}
            new_str_history = []
            
            for k, v in strings_dict.items():
                if k not in existing_str_keys:
                    new_str_history.append({
                        "lang": "ko",
                        "key": k,
                        "value": v,
                        "status": "added",
                        "timestamp": now.isoformat()
                    })
            history["strings"] = history.get("strings", []) + new_str_history
            print(f"Backfilled {len(new_str_history)} Korean strings.")
        except json.JSONDecodeError as e:
            print("Failed to decode message.txt as JSON:", e)

with open(history_path, "w", encoding="utf-8") as f:
    json.dump(history, f, ensure_ascii=False, indent=4)

# Also update experiments.json
curr_exps = {}
for e in history["experiments"]:
    if e["status"] != "deleted":
        curr_exps[e["id"]] = e
with open("data/experiments.json", "w", encoding="utf-8") as f:
    json.dump(curr_exps, f, ensure_ascii=False, indent=4)

print("Migration complete!")
