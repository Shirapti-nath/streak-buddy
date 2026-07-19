import tempfile
from pathlib import Path
import json
from datetime import date, timedelta

import pytest

import streak_buddy.streak as streak


def test_mark_and_get_streak(tmp_path, monkeypatch):
    # Use a temp file for STREAK_FILE
    temp_file = tmp_path / "s.json"
    monkeypatch.setattr(streak, "STREAK_FILE", temp_file)
    # first mark
    s1 = streak.mark_today()
    assert s1 == 1
    # marking again same day doesn't change
    s2 = streak.mark_today()
    assert s2 == 1
    # simulate next day
    yesterday = date.today() - timedelta(days=1)
    data = {"last": yesterday.isoformat(), "streak": 5}
    temp_file.write_text(json.dumps(data))
    s3 = streak.mark_today()
    assert s3 == 6
