#!/usr/bin/env python3
"""Full system integrity audit — check all data files for consistency.

Usage:
    python3 deep_audit.py           # Full audit
    python3 deep_audit.py --json    # JSON output
"""

import sys
import json
from pathlib import Path
from datetime import date, timedelta

sys.path.insert(0, str(Path(__file__).parent))

from data_manager import (
    DATA_DIR, OUTPUT_DIR, PROFILE_PATH, HISTORY_PATH, SERIES_PATH,
    load_json, load_profile, load_history, load_series, today_str,
)


def check_file_exists(path: Path, name: str) -> dict:
    """Check if a data file exists and is valid JSON."""
    if not path.exists():
        return {"name": name, "status": "MISSING", "valid": False, "detail": str(path)}

    try:
        data = load_json(path)
        if data is None:
            return {"name": name, "status": "EMPTY", "valid": False, "detail": "File is empty"}
        return {"name": name, "status": "OK", "valid": True, "detail": f"{len(json.dumps(data))} bytes"}
    except json.JSONDecodeError as e:
        return {"name": name, "status": "INVALID_JSON", "valid": False, "detail": str(e)}


def audit_profile(profile: dict) -> list:
    """Audit profile completeness."""
    issues = []
    if profile is None:
        issues.append({"severity": "CRITICAL", "item": "profile.json missing — run /setup-profile"})
        return issues

    required_fields = [
        ("theme.main", profile.get("theme", {}).get("main")),
        ("platforms", profile.get("platforms")),
        ("style.preset", profile.get("style", {}).get("preset")),
    ]
    for field, value in required_fields:
        if not value:
            issues.append({"severity": "HIGH", "item": f"Profile field '{field}' is empty"})

    # Check for default/placeholder values
    if profile.get("theme", {}).get("main") == "":
        issues.append({"severity": "HIGH", "item": "Profile theme is blank — configure with /setup-profile"})

    return issues


def audit_history(history: dict) -> list:
    """Audit content history consistency."""
    issues = []
    entries = history.get("entries", [])

    if not entries:
        issues.append({"severity": "INFO", "item": "No content history — run /daily-autopilot"})
        return issues

    # Check for duplicate IDs
    ids = [e.get("id") for e in entries]
    dupes = set(i for i in ids if ids.count(i) > 1)
    if dupes:
        issues.append({"severity": "HIGH", "item": f"Duplicate entry IDs: {dupes}"})

    # Check for required fields
    for i, entry in enumerate(entries):
        if not entry.get("topic"):
            issues.append({"severity": "MEDIUM", "item": f"Entry {entry.get('id', i)}: missing topic"})
        if not entry.get("date"):
            issues.append({"severity": "MEDIUM", "item": f"Entry {entry.get('id', i)}: missing date"})
        if not entry.get("platforms"):
            issues.append({"severity": "LOW", "item": f"Entry {entry.get('id', i)}: no platforms recorded"})

    # Check for orphan file references
    for entry in entries:
        for platform, pdata in entry.get("platforms", {}).items():
            filepath = pdata.get("file")
            if filepath:
                full_path = OUTPUT_DIR / filepath
                if not full_path.exists():
                    issues.append({
                        "severity": "LOW",
                        "item": f"Entry {entry.get('id')}: file not found: {filepath}",
                    })

    # Check for staleness
    if entries:
        last_date_str = max(e.get("date", "") for e in entries)
        try:
            last_date = date.fromisoformat(last_date_str)
            gap = (date.today() - last_date).days
            if gap > 7:
                issues.append({
                    "severity": "MEDIUM",
                    "item": f"Last entry was {gap} days ago ({last_date_str})",
                })
        except ValueError:
            pass

    return issues


def audit_series(series_data: dict, history: dict) -> list:
    """Audit series consistency."""
    issues = []
    if series_data is None:
        return issues

    for series in series_data.get("series", []):
        sid = series.get("id", "unknown")
        if series.get("status") == "active":
            pending = [p for p in series.get("parts", []) if p.get("status") == "pending"]
            published = [p for p in series.get("parts", []) if p.get("status") == "published"]
            total = len(series.get("parts", []))

            # Cross-check with history
            history_entries = [
                e for e in history.get("entries", [])
                if e.get("series_id") == sid
            ]
            if len(published) != len(history_entries):
                issues.append({
                    "severity": "MEDIUM",
                    "item": f"Series '{sid}': {len(published)} published parts but {len(history_entries)} history entries",
                })

    return issues


def audit_output_dir() -> list:
    """Audit output directory."""
    issues = []
    if not OUTPUT_DIR.exists():
        issues.append({"severity": "LOW", "item": f"Output directory missing: {OUTPUT_DIR}"})
        return issues

    files = list(OUTPUT_DIR.glob("*"))
    if not files:
        issues.append({"severity": "INFO", "item": "Output directory is empty"})

    return issues


def main():
    output_json = "--json" in sys.argv

    # File checks
    file_checks = [
        check_file_exists(PROFILE_PATH, "profile.json"),
        check_file_exists(HISTORY_PATH, "content-history.json"),
        check_file_exists(SERIES_PATH, "active-series.json"),
    ]

    # Data audits
    profile = load_profile()
    history = load_history()
    series = load_series()

    all_issues = []
    all_issues.extend(audit_profile(profile))
    all_issues.extend(audit_history(history))
    all_issues.extend(audit_series(series, history))
    all_issues.extend(audit_output_dir())

    # Counts
    critical = sum(1 for i in all_issues if i["severity"] == "CRITICAL")
    high = sum(1 for i in all_issues if i["severity"] == "HIGH")
    medium = sum(1 for i in all_issues if i["severity"] == "MEDIUM")
    low = sum(1 for i in all_issues if i["severity"] == "LOW")
    info = sum(1 for i in all_issues if i["severity"] == "INFO")
    healthy = sum(1 for f in file_checks if f["valid"])

    result = {
        "status": "audited",
        "date": today_str(),
        "files": file_checks,
        "issues": all_issues,
        "summary": {
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "info": info,
            "healthy_files": healthy,
            "total_files": len(file_checks),
        },
    }

    if output_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("=" * 50)
        print("  System Deep Audit")
        print(f"  Date: {today_str()}")
        print("=" * 50)
        print()
        print("DATA FILES:")
        for f in file_checks:
            mark = "[x]" if f["valid"] else "[ ]"
            print(f"  {mark} {f['name']} — {f['status']} ({f['detail']})")
        print()

        if all_issues:
            print("ISSUES:")
            for issue in all_issues:
                sev = issue["severity"]
                print(f"  [{sev}] {issue['item']}")
            print()

        total_issues = critical + high + medium + low
        print(f"CRITICAL: {critical} | HIGH: {high} | MEDIUM: {medium} | LOW: {low} | INFO: {info}")
        print(f"HEALTHY FILES: {healthy}/{len(file_checks)}")
        print()

        if critical > 0:
            print("ACTION REQUIRED: Fix CRITICAL issues before using the system.")
        elif high > 0:
            print("RECOMMENDATION: Fix HIGH issues for best results.")
        elif total_issues == 0:
            print("All systems healthy.")

        print("=" * 50)


if __name__ == "__main__":
    main()
