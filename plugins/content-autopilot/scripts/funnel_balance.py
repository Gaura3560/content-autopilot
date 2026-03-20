#!/usr/bin/env python3
"""Calculate funnel balance (TOFU/MOFU/BOFU) from content history.

Usage:
    python3 funnel_balance.py              # Last 7 days
    python3 funnel_balance.py --days 30    # Last 30 days
    python3 funnel_balance.py --json       # JSON output for piping

Output: Funnel distribution + recommended next stage.
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data_manager import load_history, load_profile, filter_entries_by_days

# Ideal funnel balance targets
TARGETS = {"TOFU": 50, "MOFU": 30, "BOFU": 20}
STAGES = ["TOFU", "MOFU", "BOFU"]


def count_stages(entries: list) -> dict:
    """Count entries per funnel stage."""
    counts = {"TOFU": 0, "MOFU": 0, "BOFU": 0}
    for e in entries:
        stage = e.get("funnel_stage")
        if stage in counts:
            counts[stage] += 1
    return counts


def calculate_balance(counts: dict) -> dict:
    """Calculate percentages and deviations from target."""
    total = sum(counts.values())
    if total == 0:
        return {
            stage: {"count": 0, "pct": 0, "target": TARGETS[stage], "deviation": 0}
            for stage in STAGES
        }
    result = {}
    for stage in STAGES:
        pct = round(counts[stage] / total * 100)
        result[stage] = {
            "count": counts[stage],
            "pct": pct,
            "target": TARGETS[stage],
            "deviation": pct - TARGETS[stage],
        }
    return result


def recommend_stage(balance: dict) -> str:
    """Recommend the next funnel stage based on current balance.

    Returns the stage that is most underrepresented relative to its target.
    """
    if all(b["count"] == 0 for b in balance.values()):
        return "TOFU"  # Default for first run

    # Find the stage with the largest negative deviation (most underrepresented)
    worst_stage = min(STAGES, key=lambda s: balance[s]["deviation"])
    return worst_stage


def recommend_category(stage: str) -> str:
    """Map funnel stage to content category recommendation."""
    mapping = {
        "TOFU": "trending",
        "MOFU": "overseas",
        "BOFU": "evergreen",
    }
    return mapping.get(stage, "trending")


def format_bar(pct: int, width: int = 20) -> str:
    """Create a text progress bar."""
    filled = int(pct / 100 * width)
    return "#" * filled + "-" * (width - filled)


def main():
    args = sys.argv[1:]
    days = 7
    output_json = False

    i = 0
    while i < len(args):
        if args[i] == "--days" and i + 1 < len(args):
            days = int(args[i + 1])
            i += 2
        elif args[i] == "--json":
            output_json = True
            i += 1
        else:
            i += 1

    history = load_history()
    profile = load_profile()

    # Check if funnel is enabled
    funnel_enabled = True
    if profile and not profile.get("funnel", {}).get("enabled", True):
        funnel_enabled = False

    entries = filter_entries_by_days(history, days)
    counts = count_stages(entries)
    balance = calculate_balance(counts)
    recommended = recommend_stage(balance)
    recommended_category = recommend_category(recommended)

    result = {
        "days": days,
        "total_entries": len(entries),
        "funnel_enabled": funnel_enabled,
        "balance": balance,
        "recommended_stage": recommended,
        "recommended_category": recommended_category,
    }

    if output_json:
        print(json.dumps(result, ensure_ascii=False))
        return

    # Human-readable output
    total = len(entries)
    print(f"Funnel Balance (last {days} days, {total} entries):")
    print()
    for stage in STAGES:
        b = balance[stage]
        bar = format_bar(b["pct"])
        dev = b["deviation"]
        dev_str = f"+{dev}" if dev > 0 else str(dev)
        print(f"  {stage}: {b['count']} ({b['pct']}%) [{bar}] target: {b['target']}% ({dev_str})")
    print()

    if total == 0:
        print("No history data yet (first run).")
        print(f"Recommendation: Start with TOFU content for maximum reach.")
    else:
        stage_desc = {"TOFU": "reach/awareness", "MOFU": "trust-building", "BOFU": "monetization"}
        print(f"Recommended next stage: {recommended} ({stage_desc[recommended]})")
        print(f"Suggested category: {recommended_category}")

        # Highlight significant imbalances
        for stage in STAGES:
            dev = balance[stage]["deviation"]
            if abs(dev) > 15:
                direction = "over" if dev > 0 else "under"
                print(f"  WARNING: {stage} is {direction}-represented by {abs(dev)}%")


if __name__ == "__main__":
    main()
