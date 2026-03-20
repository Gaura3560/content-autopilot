#!/usr/bin/env python3
"""Shared JSON data manager for content-autopilot scripts.

All other scripts import this module for consistent file I/O.
Data directory: ~/.content-autopilot/
"""

import json
import os
from datetime import datetime, date
from pathlib import Path
from typing import Any, Optional

DATA_DIR = Path.home() / ".content-autopilot"
OUTPUT_DIR = Path.home() / "Desktop" / "content-autopilot-output"

PROFILE_PATH = DATA_DIR / "profile.json"
HISTORY_PATH = DATA_DIR / "content-history.json"
SERIES_PATH = DATA_DIR / "active-series.json"


def ensure_data_dir() -> Path:
    """Create data directory if it doesn't exist. Returns the path."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def ensure_output_dir() -> Path:
    """Create output directory if it doesn't exist. Returns the path."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR


def load_json(path: Path) -> Optional[dict]:
    """Load a JSON file. Returns None if file doesn't exist."""
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    """Save data to a JSON file with pretty printing."""
    ensure_data_dir()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_profile() -> Optional[dict]:
    """Load profile.json. Returns None if not found."""
    return load_json(PROFILE_PATH)


def load_history() -> dict:
    """Load content-history.json. Creates empty if not found."""
    data = load_json(HISTORY_PATH)
    if data is None:
        data = {"version": "1.0", "entries": []}
        save_json(HISTORY_PATH, data)
    return data


def load_series() -> Optional[dict]:
    """Load active-series.json. Returns None if not found."""
    return load_json(SERIES_PATH)


def today_str() -> str:
    """Return today's date as YYYY-MM-DD string."""
    return date.today().isoformat()


def now_iso() -> str:
    """Return current datetime as ISO string."""
    return datetime.now().isoformat()


def next_entry_id(history: dict, target_date: str) -> str:
    """Generate the next sequential entry ID for a given date.

    Format: YYYY-MM-DD-001, YYYY-MM-DD-002, etc.
    """
    existing = [
        e["id"] for e in history.get("entries", [])
        if e.get("id", "").startswith(target_date)
    ]
    seq = len(existing) + 1
    return f"{target_date}-{seq:03d}"


def filter_entries_by_days(history: dict, days: int) -> list:
    """Filter history entries to the last N days."""
    cutoff = date.today().isoformat()
    from datetime import timedelta
    cutoff_date = (date.today() - timedelta(days=days)).isoformat()
    return [
        e for e in history.get("entries", [])
        if e.get("date", "") >= cutoff_date
    ]


if __name__ == "__main__":
    # Quick self-test
    ensure_data_dir()
    print(f"Data dir: {DATA_DIR}")
    print(f"Profile exists: {PROFILE_PATH.exists()}")
    print(f"History exists: {HISTORY_PATH.exists()}")
    print(f"Today: {today_str()}")
    print("data_manager OK")
