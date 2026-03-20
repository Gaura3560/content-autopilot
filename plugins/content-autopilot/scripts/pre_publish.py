#!/usr/bin/env python3
"""Pre-Publish Checker — final validation before publishing (Japanese-aware).

Usage:
    python3 pre_publish.py <file_path>                    # human-readable
    python3 pre_publish.py <file_path> --json             # structured JSON
    python3 pre_publish.py <file_path> --json --platform note  # explicit platform
"""

import argparse
import json
import re
import sys
from pathlib import Path


def count_chars_ja(text: str) -> int:
    """Count characters for Japanese content."""
    return len(text)


def detect_platform(file_path: str) -> str:
    """Detect platform from filename."""
    name = Path(file_path).stem.lower()
    if name.startswith("note"):
        return "note"
    if name.startswith("x_") or name.startswith("x-"):
        return "x"
    if name.startswith("instagram") or name.startswith("ig"):
        return "instagram"
    return "note"


# ---------------------------------------------------------------------------
# Check functions — each returns {"name": str, "pass": bool, "detail": str}
# ---------------------------------------------------------------------------

def check_not_empty(content: str) -> dict:
    """Content must not be empty."""
    stripped = content.strip()
    return {
        "name": "content_exists",
        "pass": len(stripped) > 50,
        "detail": f"文字数: {len(stripped)}" if stripped else "コンテンツが空です",
    }


def check_no_placeholder(content: str) -> dict:
    """No placeholder text remaining."""
    placeholders = [
        r"\{[^}]+\}",       # {placeholder}
        r"\[TODO\]",         # [TODO]
        r"\[TBD\]",          # [TBD]
        r"FIXME",
        r"XXX",
        r"ここに.*を入れる",
        r"＊＊.*＊＊",       # **placeholder**
        r"\*\*[A-Z_]+\*\*",
    ]
    found = []
    for pat in placeholders:
        matches = re.findall(pat, content)
        found.extend(matches)

    return {
        "name": "no_placeholders",
        "pass": len(found) == 0,
        "detail": f"プレースホルダー発見: {found[:3]}" if found else "OK",
    }


def check_cta_present(content: str, platform: str) -> dict:
    """CTA must be present (Japanese patterns)."""
    cta_patterns_ja = [
        r"フォロー",
        r"いいね",
        r"シェア",
        r"コメント",
        r"リプ",
        r"保存",
        r"ブックマーク",
        r"プロフ(?:ィール)?",
        r"詳しくは",
        r"続きは",
        r"チェック",
        r"登録",
        r"購読",
        r"読んでみて",
        r"見てみて",
        r"試してみて",
        r"ダウンロード",
        r"無料",
        r"限定",
        r"今すぐ",
        r"こちら",
        r"noteで",
        r"記事で",
        r"リンク",
    ]

    found = [pat for pat in cta_patterns_ja if re.search(pat, content)]

    # Platform-specific CTA requirements
    if platform == "x":
        x_cta = any(re.search(pat, content) for pat in [r"noteで", r"記事で", r"リンク", r"プロフ", r"詳しくは", r"続きは"])
        if not x_cta:
            return {
                "name": "cta_present",
                "pass": False,
                "detail": "X投稿にnote誘導CTAがありません。「続きはnoteで」等を追加してください",
            }
    elif platform == "instagram":
        ig_cta = any(re.search(pat, content) for pat in [r"プロフ", r"リンク", r"ハイライト"])
        if not ig_cta:
            return {
                "name": "cta_present",
                "pass": False,
                "detail": "Instagram投稿にプロフリンク誘導CTAがありません",
            }

    return {
        "name": "cta_present",
        "pass": len(found) > 0,
        "detail": f"CTA検出: {len(found)}個" if found else "CTAが見つかりません",
    }


def check_length(content: str, platform: str) -> dict:
    """Content length must fit platform requirements (Japanese char count)."""
    char_count = count_chars_ja(content)

    limits = {
        "note": {"min": 1500, "max": 8000, "label": "note記事"},
        "x": {"min": 50, "max": 1400, "label": "Xスレッド"},  # thread total
        "instagram": {"min": 100, "max": 2200, "label": "Instagramキャプション"},
    }

    limit = limits.get(platform, limits["note"])

    if char_count < limit["min"]:
        return {
            "name": "length_check",
            "pass": False,
            "detail": f"{limit['label']}: {char_count}文字（最低{limit['min']}文字必要）",
        }
    if char_count > limit["max"]:
        return {
            "name": "length_check",
            "pass": False,
            "detail": f"{limit['label']}: {char_count}文字（上限{limit['max']}文字超過）",
        }

    return {
        "name": "length_check",
        "pass": True,
        "detail": f"{limit['label']}: {char_count}文字（範囲内）",
    }


def check_hashtags(content: str, platform: str) -> dict:
    """Instagram: hashtag count check."""
    if platform != "instagram":
        return {"name": "hashtags", "pass": True, "detail": "スキップ（Instagram以外）"}

    hashtags = re.findall(r"#\S+", content)
    count = len(hashtags)

    if count < 15:
        return {
            "name": "hashtags",
            "pass": False,
            "detail": f"ハッシュタグ: {count}個（最低15個推奨、理想25-30個）",
        }
    if count > 30:
        return {
            "name": "hashtags",
            "pass": False,
            "detail": f"ハッシュタグ: {count}個（上限30個を超過）",
        }

    return {
        "name": "hashtags",
        "pass": True,
        "detail": f"ハッシュタグ: {count}個",
    }


def check_tweet_length(content: str, platform: str) -> dict:
    """X: individual tweet length check (140 chars for Japanese)."""
    if platform != "x":
        return {"name": "tweet_length", "pass": True, "detail": "スキップ（X以外）"}

    # Split tweets by common delimiters
    tweets = re.split(r"\n---\n|\n\d+[./]\s", content)
    violations = []

    for i, tweet in enumerate(tweets):
        text = tweet.strip()
        if not text:
            continue
        length = count_chars_ja(text)
        if length > 140:
            violations.append(f"ツイート{i+1}: {length}文字")

    if violations:
        return {
            "name": "tweet_length",
            "pass": False,
            "detail": f"140文字超過: {', '.join(violations)}",
        }

    return {
        "name": "tweet_length",
        "pass": True,
        "detail": f"全ツイートが140文字以内",
    }


def check_no_sensitive(content: str) -> dict:
    """No sensitive/problematic content."""
    sensitive_patterns = [
        (r"(?:個人情報|住所|電話番号|メールアドレス)", "個人情報"),
        (r"(?:パスワード|API[_\s]?[Kk]ey|シークレット)", "認証情報"),
        (r"(?:死|殺|暴力)", "不適切表現"),
    ]

    found = []
    for pattern, label in sensitive_patterns:
        if re.search(pattern, content):
            found.append(label)

    return {
        "name": "no_sensitive",
        "pass": len(found) == 0,
        "detail": f"警告: {', '.join(found)}を含む可能性" if found else "OK",
    }


def check_formatting(content: str, platform: str) -> dict:
    """Basic formatting checks."""
    issues = []

    # Double spaces
    if "  " in content:
        issues.append("連続スペース")

    # Trailing whitespace
    lines_with_trailing = [
        i + 1 for i, line in enumerate(content.split("\n"))
        if line != line.rstrip() and line.strip()
    ]
    if len(lines_with_trailing) > 3:
        issues.append(f"末尾空白（{len(lines_with_trailing)}行）")

    # Empty headers
    empty_headers = re.findall(r"^#{1,3}\s*$", content, re.MULTILINE)
    if empty_headers:
        issues.append("空の見出し")

    return {
        "name": "formatting",
        "pass": len(issues) == 0,
        "detail": f"フォーマット問題: {', '.join(issues)}" if issues else "OK",
    }


def run_all_checks(content: str, platform: str) -> dict:
    """Run all pre-publish checks."""
    checks = [
        check_not_empty(content),
        check_no_placeholder(content),
        check_cta_present(content, platform),
        check_length(content, platform),
        check_hashtags(content, platform),
        check_tweet_length(content, platform),
        check_no_sensitive(content),
        check_formatting(content, platform),
    ]

    passed = [c for c in checks if c["pass"]]
    failed = [c for c in checks if not c["pass"]]

    return {
        "platform": platform,
        "all_pass": len(failed) == 0,
        "total_checks": len(checks),
        "passed": len(passed),
        "failed": len(failed),
        "checks": checks,
    }


def format_human_readable(result: dict) -> str:
    """Format result for human reading."""
    lines = [
        "=" * 44,
        "  Pre-Publish Check — 公開前チェック",
        "=" * 44,
        "",
        f"プラットフォーム: {result['platform']}",
        f"結果: {'ALL PASS' if result['all_pass'] else 'FAIL'}",
        f"チェック: {result['passed']}/{result['total_checks']} 合格",
        "",
    ]

    for check in result["checks"]:
        icon = "[OK]" if check["pass"] else "[NG]"
        lines.append(f"  {icon} {check['name']}: {check['detail']}")

    lines.append("")
    if not result["all_pass"]:
        lines.append("上記のNGを修正してから公開してください。")
    else:
        lines.append("公開準備完了です。")
    lines.append("=" * 44)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Pre-Publish Checker")
    parser.add_argument("file", help="Content file to check")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--platform", help="Override platform detection")
    args = parser.parse_args()

    file_path = Path(args.file).expanduser()
    if not file_path.exists():
        error = {"error": f"ファイルが見つかりません: {file_path}"}
        if args.json:
            print(json.dumps(error, ensure_ascii=False))
        else:
            print(f"Error: {error['error']}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    platform = args.platform or detect_platform(str(file_path))
    result = run_all_checks(content, platform)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_human_readable(result))

    sys.exit(0 if result["all_pass"] else 1)


if __name__ == "__main__":
    main()
