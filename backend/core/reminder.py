import json
import os
from datetime import datetime

reminder_file = "shared/data/reminders.json"

def set_reminder(name, time_str):
    reminder = {
        "name": name,
        "time": time_str,
        "created_at": datetime.now().isoformat()
    }

    if os.path.exists(reminder_file):
        with open(reminder_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(reminder)

    with open(reminder_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def get_reminders():
    if os.path.exists(reminder_file):
        with open(reminder_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []