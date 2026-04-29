import json

# Remove from history.json
with open("data/history.json", "r", encoding="utf-8") as f:
    history = json.load(f)

history["experiments"] = [exp for exp in history.get("experiments", []) if exp.get("id") != "2026-99_fake_test_experiment"]

with open("data/history.json", "w", encoding="utf-8") as f:
    json.dump(history, f, indent=4, ensure_ascii=False)

# Remove from latest_changes.json
with open("data/latest_changes.json", "r", encoding="utf-8") as f:
    changes = json.load(f)

changes["deleted_experiments"] = [exp for exp in changes.get("deleted_experiments", []) if exp.get("id") != "2026-99_fake_test_experiment"]
# Revert build hash if it's the fake one
if changes.get("build_hash") == "fake-build-hash-for-testing":
    changes["build_hash"] = history.get("build_hash", "c253ffbeac4eb787ee0f638f1042b7e152c035c8")

with open("data/latest_changes.json", "w", encoding="utf-8") as f:
    json.dump(changes, f, indent=4, ensure_ascii=False)

print("Removed fake deleted experiment.")
