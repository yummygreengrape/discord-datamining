import json

with open("data/history.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for key in ["experiments", "api_endpoints", "strings"]:
    if key in data and isinstance(data[key], list):
        data[key].sort(key=lambda x: x.get("timestamp", ""), reverse=True)

with open("data/history.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Sorted history.json by timestamp descending.")
