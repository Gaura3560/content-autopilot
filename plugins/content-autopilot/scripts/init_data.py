#!/usr/bin/env python3
"""Initialize all data files for content-autopilot. Idempotent — safe to run multiple times.

Usage:
    python3 init_data.py
    python3 init_data.py --force   # Reset all data files (destructive)
"""

import sys
from pathlib import Path

# Allow importing data_manager from same directory
sys.path.insert(0, str(Path(__file__).parent))

from data_manager import (
    DATA_DIR, OUTPUT_DIR, PROFILE_PATH, HISTORY_PATH, SERIES_PATH,
    ensure_data_dir, ensure_output_dir, load_json, save_json, now_iso,
)

EMPTY_HISTORY = {"version": "1.0", "entries": []}

EMPTY_SERIES = {"version": "1.0", "series": []}

SAMPLE_PROFILE = {
    "version": "1.0",
    "created_at": None,
    "updated_at": None,
    "theme": {
        "main": "AI x ビジネス",
        "keywords": ["AI", "自動化", "生産性", "ビジネス", "効率化"],
    },
    "audience": {
        "age_range": "25-45",
        "occupation": "ビジネスパーソン・個人事業主",
        "pain_points": ["時間が足りない", "AIの活用方法がわからない", "業務効率を上げたい"],
        "knowledge_level": "intermediate",
    },
    "platforms": ["note", "x", "instagram"],
    "style": {
        "method": "preset",
        "preset": "professional",
        "tone": "authoritative yet approachable",
        "sentence_length": "medium",
        "vocabulary": "accessible technical terms",
        "paragraph_style": "short paragraphs with line breaks",
        "emoji_usage": "minimal",
        "first_person": True,
        "sample_urls": [],
    },
    "brand": {
        "primary_color": "#FF6B35",
        "secondary_color": "#1A1A2E",
        "logo_path": None,
        "font_preference": None,
    },
    "funnel": {
        "enabled": False,
        "note_url": "",
        "x_handle": "",
        "instagram_handle": "",
        "monetization": {
            "type": "paid_articles",
            "lead_magnet": "",
            "membership_url": None,
            "lead_magnet_url": None,
        },
    },
    "competitors": [],
}


def init_file(path: Path, default_data: dict, force: bool = False) -> str:
    """Initialize a data file if it doesn't exist. Returns status message."""
    if path.exists() and not force:
        return f"  EXISTS  {path.name}"
    save_json(path, default_data)
    action = "RESET" if force else "CREATED"
    return f"  {action}  {path.name}"


def main():
    force = "--force" in sys.argv

    print("=" * 50)
    print("  Content Autopilot — Data Initialization")
    print("=" * 50)
    print()

    # Create directories
    ensure_data_dir()
    ensure_output_dir()
    print(f"  Data dir:   {DATA_DIR}")
    print(f"  Output dir: {OUTPUT_DIR}")
    print()

    # Initialize data files
    print("Data files:")

    if not PROFILE_PATH.exists():
        ts = now_iso()
        sample = {**SAMPLE_PROFILE, "created_at": ts, "updated_at": ts}
        print(init_file(PROFILE_PATH, sample, force))
        print("    NOTE: Run /setup-profile to configure your profile")
    elif force:
        ts = now_iso()
        sample = {**SAMPLE_PROFILE, "created_at": ts, "updated_at": ts}
        print(init_file(PROFILE_PATH, sample, force))
    else:
        print(f"  EXISTS  {PROFILE_PATH.name}")

    print(init_file(HISTORY_PATH, EMPTY_HISTORY, force))
    print(init_file(SERIES_PATH, EMPTY_SERIES, force))

    print()
    print("Initialization complete.")
    if force:
        print("WARNING: --force was used. All data files have been reset.")
    print()
    print("Next steps:")
    print("  Run /daily-autopilot to generate content")
    if not PROFILE_PATH.exists() or force:
        print("  (Optional: Run /setup-profile to customize your profile)")
    print("=" * 50)


if __name__ == "__main__":
    main()
