#!/usr/bin/env python3
"""Content Autopilot — context analyzer and execution manifest generator.

Usage:
    python3 autopilot.py                 # context mode (default)
    python3 autopilot.py --mode context  # same as above
    python3 autopilot.py --mode execute  # execution manifest with concrete steps
    python3 autopilot.py --mode summary  # cumulative intelligence from history
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

DATA_DIR = Path.home() / ".content-autopilot"
PROFILE_PATH = DATA_DIR / "profile.json"
HISTORY_PATH = DATA_DIR / "content-history.json"
SERIES_PATH = DATA_DIR / "active-series.json"

# ---------------------------------------------------------------------------
# Fallback Topic Library
# category x stage combinations for when WebSearch fails
# ---------------------------------------------------------------------------
FALLBACK_TOPICS = {
    ("trending", "TOFU"): "{keyword}の最新トレンド{year}年版 — 知らないと損する{count}つのポイント",
    ("trending", "MOFU"): "{keyword}を始めるならまずこの3ステップ — 初心者が最短で成果を出す方法",
    ("trending", "BOFU"): "{keyword}で収益化する具体的な方法 — 実践者が語るリアルな数字",
    ("overseas", "TOFU"): "海外で話題の{keyword}事例{count}選 — 日本ではまだ知られていない最新動向",
    ("overseas", "MOFU"): "海外の{keyword}成功事例から学ぶ — 日本で再現するための具体的手順",
    ("overseas", "BOFU"): "海外で実証済みの{keyword}メソッド — そのまま使えるテンプレート付き",
    ("evergreen", "TOFU"): "{keyword}入門ガイド{year}年決定版 — 今日から始める{count}つの基本",
    ("evergreen", "MOFU"): "{keyword}中級者が陥る{count}つの罠 — プロが教える回避テクニック",
    ("evergreen", "BOFU"): "{keyword}完全ガイド — プロが教える実践テクニックと収益化の全手順",
}


def load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def compute_funnel_balance(history: dict | None) -> dict:
    """Compute TOFU/MOFU/BOFU balance from last 7 days."""
    if not history or not history.get("entries"):
        return {"TOFU": 0, "MOFU": 0, "BOFU": 0, "total": 0, "recommended_stage": "TOFU"}

    cutoff = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    recent = [e for e in history["entries"] if e.get("date", "") >= cutoff]

    counts = {"TOFU": 0, "MOFU": 0, "BOFU": 0}
    for entry in recent:
        stage = entry.get("funnel_stage", "TOFU")
        if stage in counts:
            counts[stage] += 1

    total = sum(counts.values()) or 1
    targets = {"TOFU": 0.50, "MOFU": 0.30, "BOFU": 0.20}

    # Find the stage with the largest deficit from target
    deficits = {
        stage: targets[stage] - (counts[stage] / total)
        for stage in targets
    }
    recommended = max(deficits, key=deficits.get)

    return {
        **counts,
        "total": sum(counts.values()),
        "percentages": {s: round(counts[s] / total * 100) for s in counts},
        "recommended_stage": recommended,
    }


def check_already_generated_today(history: dict | None) -> tuple[bool, str]:
    """Check if content was already generated today. Returns (bool, suffix)."""
    today = datetime.now().strftime("%Y-%m-%d")
    if not history or not history.get("entries"):
        return False, ""

    today_entries = [e for e in history["entries"] if e.get("date") == today]
    if not today_entries:
        return False, ""

    # Auto-suffix: -002, -003, etc.
    suffix = f"-{len(today_entries) + 1:03d}"
    return True, suffix


def get_active_series(series_data: dict | None) -> dict | None:
    """Get the first active series with a pending part."""
    if not series_data or not series_data.get("series"):
        return None

    for series in series_data["series"]:
        if series.get("status") != "active":
            continue
        pending = [p for p in series.get("parts", []) if p.get("status") == "pending"]
        if pending:
            return {
                "series_id": series["id"],
                "series_title": series["title"],
                "next_part": pending[0],
                "total_parts": len(series.get("parts", [])),
                "completed_parts": len(series.get("parts", [])) - len(pending),
            }
    return None


def generate_fallback_topic(profile: dict, stage: str, category: str) -> str:
    """Generate a fallback topic from the library."""
    keywords = profile.get("theme", {}).get("keywords", ["AI"])
    keyword = keywords[0] if keywords else "AI"
    year = datetime.now().year

    key = (category, stage)
    template = FALLBACK_TOPICS.get(key, FALLBACK_TOPICS[("evergreen", "TOFU")])

    return template.format(keyword=keyword, year=year, count=5)


def build_search_query(profile: dict, stage: str, category: str) -> str:
    """Build a search query from profile keywords and stage."""
    keywords = profile.get("theme", {}).get("keywords", ["AI"])
    main_theme = profile.get("theme", {}).get("main", "AI")
    year_month = datetime.now().strftime("%Y-%m")

    category_modifiers = {
        "trending": "latest trends",
        "overseas": "overseas international",
        "evergreen": "complete guide best practices",
    }
    modifier = category_modifiers.get(category, "trends")

    return f"{main_theme} {' '.join(keywords[:2])} {modifier} {year_month}"


def determine_note_type(stage: str) -> str:
    """Determine note type (free/paid) based on funnel stage."""
    return "paid" if stage == "BOFU" else "free"


def mode_context(profile: dict, history: dict | None, series_data: dict | None) -> dict:
    """Return context JSON for Claude to interpret."""
    balance = compute_funnel_balance(history)
    already, suffix = check_already_generated_today(history)
    active_series = get_active_series(series_data)

    return {
        "status": "ready",
        "profile": {
            "theme": profile.get("theme", {}),
            "platforms": profile.get("platforms", []),
            "style": profile.get("style", {}),
            "funnel_enabled": profile.get("funnel", {}).get("enabled", False),
        },
        "funnel_balance": balance,
        "active_series": active_series,
        "already_generated_today": already,
        "file_suffix": suffix if already else "",
        "keywords": profile.get("theme", {}).get("keywords", []),
    }


def mode_execute(profile: dict, history: dict | None, series_data: dict | None) -> dict:
    """Return a concrete execution manifest with steps and fallback topics."""
    balance = compute_funnel_balance(history)
    already, suffix = check_already_generated_today(history)
    active_series = get_active_series(series_data)

    recommended_stage = balance["recommended_stage"]
    platforms = profile.get("platforms", ["note", "x", "instagram"])

    # Determine category based on balance and recent history
    recent_categories = []
    if history and history.get("entries"):
        cutoff = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        recent_categories = [
            e.get("category", "")
            for e in history["entries"]
            if e.get("date", "") >= cutoff
        ]

    category_priority = ["trending", "overseas", "evergreen"]
    chosen_category = next(
        (cat for cat in category_priority if recent_categories.count(cat) < 2),
        "trending",
    )

    # If active series exists, use series info
    if active_series:
        series_part = active_series["next_part"]
        recommended_stage = series_part.get("stage", recommended_stage)
        platforms = [series_part.get("platform", platforms[0])]

    search_query = build_search_query(profile, recommended_stage, chosen_category)
    fallback = generate_fallback_topic(profile, recommended_stage, chosen_category)
    note_type = determine_note_type(recommended_stage)
    today = datetime.now().strftime("%Y-%m-%d")
    file_suffix = suffix if already else ""

    # Build execution plan steps
    plugin_root = "${CLAUDE_PLUGIN_ROOT}"
    steps = [
        {
            "step": 1,
            "action": "websearch",
            "query": search_query,
            "fallback_topic": fallback,
        },
        {
            "step": 2,
            "action": "generate",
            "platforms": platforms,
            "stage": recommended_stage,
            "note_type": note_type,
        },
        {
            "step": 3,
            "action": "grade",
            "cmd": f"python3 {plugin_root}/scripts/grader.py {{note_file}} --json",
        },
        {
            "step": 4,
            "action": "check",
            "cmd": f"python3 {plugin_root}/scripts/pre_publish.py {{note_file}} --json",
        },
        {
            "step": 5,
            "action": "record",
            "cmd": (
                f"python3 {plugin_root}/scripts/record_history.py"
                f' --topic "{{topic}}" --stage {recommended_stage}'
                f" --category {chosen_category} --date {today}"
                + (f" --suffix={file_suffix}" if file_suffix else "")
                + (f" --series-id {active_series['series_id']}" if active_series else "")
            ),
        },
    ]

    content_spec = {
        "topic_constraints": (
            f"テーマ: {profile.get('theme', {}).get('main', 'AI x business')}, "
            f"カテゴリ: {chosen_category}, ステージ: {recommended_stage}"
        ),
        "note": {
            "length": "2000-5000文字",
            "type": note_type,
            "sections": "3-7",
            "cta": "noteフォロー + リードマグネット" if recommended_stage != "BOFU" else "有料記事購入",
        },
        "x": {
            "format": "thread",
            "tweets": "5-7",
            "each_max": 140,
            "cta": "note誘導",
        },
        "instagram": {
            "hook_max": 125,
            "hashtags": "25-30",
            "cta": "プロフリンク",
        },
    }

    return {
        "status": "ready",
        "execution_plan": steps,
        "content_spec": content_spec,
        "recommended_stage": recommended_stage,
        "chosen_category": chosen_category,
        "fallback_topic": fallback,
        "already_generated_today": already,
        "file_suffix": file_suffix,
        "active_series": active_series,
        "funnel_balance": balance,
    }


def mode_summary(history: dict | None) -> dict:
    """Return cumulative intelligence data computed from content-history.json."""
    empty_result = {
        "status": "ready",
        "total_runs": 0,
        "streak_days": 0,
        "funnel_health": {"TOFU": 0, "MOFU": 0, "BOFU": 0, "balanced": False},
        "title_logic_distribution": {},
        "best_title_logic": {"name": "N/A", "percentage": 0},
        "categories_used": {},
        "total_platforms": {},
        "quality_trend": "no_data",
        "first_run_date": None,
        "last_run_date": None,
    }

    if not history or not history.get("entries"):
        return empty_result

    entries = history["entries"]
    total_runs = len(entries)

    # --- dates ---
    dates = sorted(e.get("date", "") for e in entries if e.get("date"))
    first_run_date = dates[0] if dates else None
    last_run_date = dates[-1] if dates else None

    # --- streak_days (consecutive days with entries, counting back from today) ---
    today = datetime.now().date()
    unique_dates = sorted({d for d in dates if d}, reverse=True)
    streak_days = 0
    check_date = today
    for d in unique_dates:
        try:
            entry_date = datetime.strptime(d, "%Y-%m-%d").date()
        except ValueError:
            continue
        if entry_date == check_date:
            streak_days += 1
            check_date -= timedelta(days=1)
        elif entry_date < check_date:
            break
    # If today has no entry yet, check if streak starts from yesterday
    if streak_days == 0 and unique_dates:
        check_date = today - timedelta(days=1)
        for d in unique_dates:
            try:
                entry_date = datetime.strptime(d, "%Y-%m-%d").date()
            except ValueError:
                continue
            if entry_date == check_date:
                streak_days += 1
                check_date -= timedelta(days=1)
            elif entry_date < check_date:
                break

    # --- funnel_health ---
    stage_counts = {"TOFU": 0, "MOFU": 0, "BOFU": 0}
    for entry in entries:
        stage = entry.get("funnel_stage", "")
        if stage in stage_counts:
            stage_counts[stage] += 1
    funnel_total = sum(stage_counts.values()) or 1
    funnel_pcts = {s: round(stage_counts[s] / funnel_total * 100) for s in stage_counts}
    # balanced = each stage within 10% of target (TOFU 50, MOFU 30, BOFU 20)
    targets = {"TOFU": 50, "MOFU": 30, "BOFU": 20}
    balanced = all(abs(funnel_pcts[s] - targets[s]) <= 10 for s in targets)
    funnel_health = {**funnel_pcts, "balanced": balanced}

    # --- title_logic_distribution ---
    title_logic_counts: dict[str, int] = {}
    for entry in entries:
        for logic in entry.get("title_logics_used", []):
            title_logic_counts[logic] = title_logic_counts.get(logic, 0) + 1
    logic_total = sum(title_logic_counts.values()) or 1
    title_logic_distribution = {
        k: round(v / logic_total * 100)
        for k, v in sorted(title_logic_counts.items(), key=lambda x: -x[1])
    }
    if title_logic_counts:
        best_name = max(title_logic_counts, key=title_logic_counts.get)
        best_title_logic = {
            "name": best_name,
            "percentage": round(title_logic_counts[best_name] / logic_total * 100),
        }
    else:
        best_title_logic = {"name": "N/A", "percentage": 0}

    # --- categories_used ---
    category_counts: dict[str, int] = {}
    for entry in entries:
        cat = entry.get("category", "")
        if cat:
            category_counts[cat] = category_counts.get(cat, 0) + 1

    # --- total_platforms ---
    platform_counts: dict[str, int] = {}
    for entry in entries:
        for plat in entry.get("platforms", []):
            platform_counts[plat] = platform_counts.get(plat, 0) + 1

    # --- quality_trend (based on activity density over recent weeks) ---
    if total_runs < 2:
        quality_trend = "no_data"
    else:
        cutoff_recent = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        cutoff_prior = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")
        recent_count = sum(
            1 for e in entries
            if e.get("date", "") >= cutoff_recent
        )
        prior_count = sum(
            1 for e in entries
            if cutoff_prior <= e.get("date", "") < cutoff_recent
        )
        if recent_count > prior_count:
            quality_trend = "improving"
        elif recent_count == prior_count:
            quality_trend = "stable"
        else:
            quality_trend = "declining"

    return {
        "status": "ready",
        "total_runs": total_runs,
        "streak_days": streak_days,
        "funnel_health": funnel_health,
        "title_logic_distribution": title_logic_distribution,
        "best_title_logic": best_title_logic,
        "categories_used": category_counts,
        "total_platforms": platform_counts,
        "quality_trend": quality_trend,
        "first_run_date": first_run_date,
        "last_run_date": last_run_date,
    }


def main():
    parser = argparse.ArgumentParser(description="Content Autopilot context/manifest")
    parser.add_argument(
        "--mode",
        choices=["context", "execute", "summary"],
        default="context",
        help="context: return raw context. execute: return execution manifest. summary: cumulative intelligence.",
    )
    args = parser.parse_args()

    # Load data
    profile = load_json(PROFILE_PATH)

    # summary mode does not require profile
    if args.mode == "summary":
        history = load_json(HISTORY_PATH)
        result = mode_summary(history)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if not profile:
        result = {
            "status": "error",
            "error": "profile_missing",
            "message": "profile.json が見つかりません。先に /setup-profile を実行してください。",
            "fix_cmd": "setup-profile スキルを実行",
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(1)

    history = load_json(HISTORY_PATH)
    series_data = load_json(SERIES_PATH)

    if args.mode == "context":
        result = mode_context(profile, history, series_data)
    else:
        result = mode_execute(profile, history, series_data)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
