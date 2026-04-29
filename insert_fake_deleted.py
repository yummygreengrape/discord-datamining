import json
from datetime import datetime, timezone

with open("data/history.json", "r", encoding="utf-8") as f:
    history = json.load(f)

# Insert a fake deleted experiment
fake_exp = {
    "id": "2026-99_fake_test_experiment",
    "kind": "user",
    "treatments": ["Control", "Treatment 1"],
    "status": "deleted",
    "timestamp": datetime.now(timezone.utc).isoformat()
}
history["experiments"].insert(0, fake_exp)

with open("data/history.json", "w", encoding="utf-8") as f:
    json.dump(history, f, indent=4, ensure_ascii=False)

# Update latest_changes to trigger the bot
with open("data/latest_changes.json", "r", encoding="utf-8") as f:
    changes = json.load(f)

changes["deleted_experiments"].append(fake_exp)
changes["timestamp"] = fake_exp["timestamp"]
# Ensure build hash is different so the bot triggers
changes["build_hash"] = "fake-build-hash-for-testing"

with open("data/latest_changes.json", "w", encoding="utf-8") as f:
    json.dump(changes, f, indent=4, ensure_ascii=False)

print("Injected fake deleted experiment.")
