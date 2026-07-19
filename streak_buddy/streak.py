import json
from datetime import date, timedelta
from pathlib import Path

STREAK_FILE = Path.home() / ".streak_buddy.json"


def _load():
    if not STREAK_FILE.exists():
        return {}
    return json.loads(STREAK_FILE.read_text())


def _save(data):
    STREAK_FILE.write_text(json.dumps(data))


def mark_today():
    data = _load()
    last = data.get("last")
    today = date.today().isoformat()
    if last == today:
        return data.get("streak", 0)
    if last:
        last_date = date.fromisoformat(last)
        if last_date + timedelta(days=1) == date.fromisoformat(today):
            streak = data.get("streak", 0) + 1
        else:
            streak = 1
    else:
        streak = 1
    data["last"] = today
    data["streak"] = streak
    _save(data)
    return streak


def get_streak():
    data = _load()
    return data.get("streak", 0)


def reset():
    if STREAK_FILE.exists():
        STREAK_FILE.unlink()
