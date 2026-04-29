import json
import re
from datetime import datetime, timezone, timedelta

def main():
    history_path = "data/history.json"
    with open(history_path, "r", encoding="utf-8") as f:
        history = json.load(f)

    experiments = history.get("experiments", [])
    
    # Sort them by current timestamp ascending so we process oldest first
    experiments.sort(key=lambda x: x.get("timestamp", ""))

    date_counters = {}
    
    for exp in experiments:
        exp_id = exp["id"]
        
        # Match YYYY-MM-DD or YYYY-MM
        match = re.match(r"^(20\d{2})-(\d{2})(?:-(\d{2}))?", exp_id)
        if match:
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3)) if match.group(3) else 1
            
            try:
                base_date = datetime(year, month, day, tzinfo=timezone.utc)
            except ValueError:
                # invalid date, default fallback
                base_date = datetime(2015, 1, 1, tzinfo=timezone.utc)
        else:
            # Fallback for old experiments
            base_date = datetime(2015, 1, 1, tzinfo=timezone.utc)

        # To prevent overlap and maintain relative order
        date_str = base_date.strftime("%Y-%m-%d")
        if date_str not in date_counters:
            date_counters[date_str] = 0
        
        # Add hours/minutes based on counter to preserve original order
        # Assuming < 1000 items per date
        new_timestamp = base_date + timedelta(seconds=date_counters[date_str] * 60)
        date_counters[date_str] += 1
        
        exp["timestamp"] = new_timestamp.isoformat()

    # Sort descending
    experiments.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
    history["experiments"] = experiments

    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)
        
    curr_exps = {}
    for e in experiments:
        if e["status"] != "deleted":
            curr_exps[e["id"]] = e
    with open("data/experiments.json", "w", encoding="utf-8") as f:
        json.dump(curr_exps, f, ensure_ascii=False, indent=4)
        
    print(f"Fixed timestamps for {len(experiments)} experiments.")

if __name__ == "__main__":
    main()
