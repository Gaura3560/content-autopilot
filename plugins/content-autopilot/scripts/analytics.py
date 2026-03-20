#!/usr/bin/env python3
"""Content analytics dashboard — deterministic calculations from content-history.json.

Usage:
    python3 analytics.py               # Full dashboard (last 30 days)
    python3 analytics.py --days 7      # Custom period
    python3 analytics.py --json        # JSON output
"""

import sys
import json
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data_manager import load_history, load_profile, filter_entries_by_days, today_str


def calc_posting_frequency(entries: list, days: int) -> dict:
    """Calculate posting frequency metrics."""
    if not entries:
        return {
            "total": 0, "weekly_avg": 0, "longest_gap": 0,
            "streak": 0, "consistency_pct": 0,
        }

    dates = sorted(set(e.get("date", "") for e in entries))
    total = len(entries)
    weeks = max(days / 7, 1)
    weekly_avg = round(total / weeks, 1)

    # Longest gap
    longest_gap = 0
    for i in range(1, len(dates)):
        d1 = date.fromisoformat(dates[i - 1])
        d2 = date.fromisoformat(dates[i])
        gap = (d2 - d1).days
        longest_gap = max(longest_gap, gap)

    # Current streak (consecutive days ending today)
    streak = 0
    check_date = date.today()
    date_set = set(dates)
    while check_date.isoformat() in date_set:
        streak += 1
        check_date -= timedelta(days=1)

    # Consistency: days with posts / total days
    consistency = round(len(dates) / max(days, 1) * 100)

    return {
        "total": total,
        "weekly_avg": weekly_avg,
        "longest_gap": longest_gap,
        "streak": streak,
        "consistency_pct": min(consistency, 100),
    }


def calc_funnel_balance(entries: list) -> dict:
    """Calculate funnel stage distribution."""
    stages = Counter(e.get("funnel_stage") for e in entries if e.get("funnel_stage"))
    total = sum(stages.values())
    if total == 0:
        return {"TOFU": 0, "MOFU": 0, "BOFU": 0, "total": 0}

    return {
        "TOFU": {"count": stages.get("TOFU", 0), "pct": round(stages.get("TOFU", 0) / total * 100)},
        "MOFU": {"count": stages.get("MOFU", 0), "pct": round(stages.get("MOFU", 0) / total * 100)},
        "BOFU": {"count": stages.get("BOFU", 0), "pct": round(stages.get("BOFU", 0) / total * 100)},
        "total": total,
    }


def calc_title_logics(entries: list) -> dict:
    """Calculate title logic usage distribution."""
    logics = Counter()
    for e in entries:
        for logic in e.get("title_logics_used", []):
            logics[logic] += 1

    all_logics = [
        "Numbers", "Simplicity", "Paradox", "Enemy", "Question",
        "Ideal Self", "Secret", "Coined Term", "Unexpected",
    ]

    total = sum(logics.values())
    result = {}
    for logic in all_logics:
        count = logics.get(logic, 0)
        pct = round(count / total * 100) if total > 0 else 0
        result[logic] = {"count": count, "pct": pct}

    unused = [l for l in all_logics if logics.get(l, 0) == 0]
    return {"logics": result, "unused": unused, "total": total}


def calc_category_dist(entries: list) -> dict:
    """Calculate content category distribution."""
    cats = Counter(e.get("category", "unknown") for e in entries)
    total = sum(cats.values())
    result = {}
    for cat, count in cats.most_common():
        result[cat] = {"count": count, "pct": round(count / total * 100) if total > 0 else 0}
    return result


def calc_platform_dist(entries: list) -> dict:
    """Calculate platform distribution."""
    result = {
        "note": {"total": 0, "free": 0, "paid": 0},
        "x": {"total": 0, "single": 0, "thread": 0},
        "instagram": {"total": 0, "avg_hashtags": 0},
    }
    ig_hashtags = []

    for e in entries:
        platforms = e.get("platforms", {})
        if "note" in platforms:
            result["note"]["total"] += 1
            ntype = platforms["note"].get("type", "free")
            if ntype in result["note"]:
                result["note"][ntype] += 1
        if "x" in platforms:
            result["x"]["total"] += 1
            xfmt = platforms["x"].get("format", "single")
            if xfmt in result["x"]:
                result["x"][xfmt] += 1
        if "instagram" in platforms:
            result["instagram"]["total"] += 1
            ig_hashtags.append(platforms["instagram"].get("hashtag_count", 0))

    if ig_hashtags:
        result["instagram"]["avg_hashtags"] = round(sum(ig_hashtags) / len(ig_hashtags), 1)

    return result


def format_bar(pct: int, width: int = 20) -> str:
    """Create a text progress bar."""
    filled = int(pct / 100 * width)
    return "#" * filled + "-" * (width - filled)


def display_dashboard(freq: dict, funnel: dict, logics: dict,
                      categories: dict, platforms: dict,
                      days: int, funnel_enabled: bool) -> None:
    """Display the full analytics dashboard."""
    print("=" * 50)
    print("  Content Analytics Dashboard")
    print(f"  Period: last {days} days | Date: {today_str()}")
    print("=" * 50)
    print()

    # Posting frequency
    print(f"Posting: {freq['total']} posts | {freq['weekly_avg']}/week | {freq['streak']}-day streak")
    print(f"  Consistency: {freq['consistency_pct']}% | Longest gap: {freq['longest_gap']} days")
    print()

    # Funnel balance
    if funnel_enabled and funnel.get("total", 0) > 0:
        print("Funnel Balance:")
        targets = {"TOFU": 50, "MOFU": 30, "BOFU": 20}
        for stage in ["TOFU", "MOFU", "BOFU"]:
            data = funnel.get(stage, {})
            if isinstance(data, dict):
                pct = data.get("pct", 0)
                bar = format_bar(pct)
                print(f"  {stage} [{bar}] {pct}% (target: {targets[stage]}%)")
        print()

    # Title logics
    if logics["total"] > 0:
        print("Title Logic Usage:")
        for logic, data in sorted(logics["logics"].items(), key=lambda x: x[1]["count"], reverse=True):
            if data["count"] > 0:
                bar = format_bar(data["pct"])
                print(f"  {logic}: {data['count']} ({data['pct']}%) [{bar}]")
        if logics["unused"]:
            print(f"  Unused: {', '.join(logics['unused'])}")
        print()

    # Categories
    if categories:
        print("Content Categories:")
        for cat, data in categories.items():
            print(f"  {cat}: {data['count']} ({data['pct']}%)")
        print()

    # Platforms
    print("Platform Activity:")
    n = platforms["note"]
    print(f"  note:      {n['total']} posts ({n['free']} free / {n['paid']} paid)")
    x = platforms["x"]
    print(f"  X:         {x['total']} posts ({x['single']} single / {x['thread']} threads)")
    ig = platforms["instagram"]
    print(f"  Instagram: {ig['total']} posts (avg {ig['avg_hashtags']} hashtags)")
    print()

    print("=" * 50)


def main():
    args = sys.argv[1:]
    days = 30
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
    funnel_enabled = True
    if profile:
        funnel_enabled = profile.get("funnel", {}).get("enabled", True)

    entries = filter_entries_by_days(history, days)

    if not entries:
        if output_json:
            print(json.dumps({"status": "no_data", "message": "No entries found. Run /daily-autopilot first."}))
        else:
            print("No content history found. Run /daily-autopilot to start building data.")
        return

    freq = calc_posting_frequency(entries, days)
    funnel = calc_funnel_balance(entries)
    logics = calc_title_logics(entries)
    categories = calc_category_dist(entries)
    platforms = calc_platform_dist(entries)

    if output_json:
        print(json.dumps({
            "status": "ok",
            "days": days,
            "posting": freq,
            "funnel": funnel,
            "title_logics": logics,
            "categories": categories,
            "platforms": platforms,
        }, ensure_ascii=False, indent=2))
    else:
        display_dashboard(freq, funnel, logics, categories, platforms, days, funnel_enabled)


if __name__ == "__main__":
    main()
