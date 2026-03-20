---
name: compliance-checker
description: Legal compliance checker for content — detect potential violations of 景品表示法 (misleading advertising), 薬機法 (health claims), ステマ規制 (stealth marketing), and copyright issues. Flags risky phrases and suggests compliant alternatives. Essential for monetized content.
---

# Compliance Checker

Protect yourself from legal trouble — catch compliance issues before publishing.

## When to Activate

- User says `/compliance {file_path}` or `/compliance`
- User asks "is this legally safe to publish?"
- User asks "check for 景品表示法/薬機法"
- Auto-suggested before publishing paid or affiliate content

## Prerequisites

- Content file to check

## Commands

### `/compliance {file_path}` — Check a specific file
### `/compliance all` — Check all today's content
### `/compliance rules` — Show current compliance rules summary

## Compliance Areas

### 1. 景品表示法 (Misleading Advertising)

**Flagged patterns:**
```
HIGH RISK:
  - "絶対に" / "必ず" / "確実に" + 成果表現
    → Replace with: "〜の可能性があります" / "多くの方が実感"
  - "No.1" / "業界最高" without data source
    → Add: "(○○調査, 2026年)" or remove claim
  - "誰でもできる" / "簡単に"
    → Add qualifier: "基礎知識があれば" / "個人差があります"

MEDIUM RISK:
  - Before/after claims without disclaimers
    → Add: "※個人の感想です。効果には個人差があります"
  - Income/earnings claims
    → Add: "※成果を保証するものではありません"
  - "無料" with hidden conditions
    → Clearly state all conditions upfront
```

### 2. 薬機法 (Pharmaceutical/Health Claims)

**Flagged patterns:**
```
HIGH RISK:
  - Health/medical effect claims: "〜が治る" / "〜に効く" / "〜を改善"
    → Replace with experience-based: "〜を使ってみた感想"
  - Supplement/food efficacy claims
    → Use: "栄養補給として" / "健康的な生活をサポート"
  - Beauty product effect claims: "シミが消える" / "若返る"
    → Replace with: "使用感レビュー" / "個人の使用体験"
```

### 3. ステマ規制 (Stealth Marketing)

**Flagged patterns:**
```
HIGH RISK (2023年10月施行):
  - Paid promotion without "PR" or "広告" label
    → Must add: 記事冒頭に「PR」「広告」「提供」表記
  - Affiliate links without disclosure
    → Add: "※本記事にはアフィリエイトリンクが含まれます"
  - Gifted product review without disclosure
    → Add: "※商品は提供いただきました"
  - Sponsored content disguised as organic
    → Label clearly as "タイアップ" or "PR"
```

### 4. 著作権 (Copyright)

**Flagged patterns:**
```
MEDIUM RISK:
  - Long quotes without attribution
    → Add source and keep quotes within "fair use" length
  - Images without license verification
    → Note: check image licensing
  - Reproducing full articles/threads from others
    → Summarize in your own words, link to original
```

## Workflow

### Step 1: Scan Content

Read the file and scan for flagged patterns:

```
Compliance Check: "{title}"
============================================

Scanned: {char_count} characters

--- Results ---

[HIGH] Line {N}: "確実に月10万円稼げる方法"
  Issue: 景品表示法 — 成果を保証する表現
  Fix: "月10万円を目指す方法（※成果を保証するものではありません）"

[HIGH] Line {N}: No PR disclosure found
  Issue: ステマ規制 — affiliate link detected but no disclosure
  Fix: Add at top: "※本記事にはアフィリエイトリンクが含まれます"

[MEDIUM] Line {N}: "このサプリで体調が良くなった"
  Issue: 薬機法 — 健康効果の示唆
  Fix: "このサプリを試してみた個人の感想です（※効果には個人差があります）"

[LOW] Line {N}: Long quote from external source
  Issue: 著作権 — 引用の範囲を超える可能性
  Fix: Shorten quote, add clear attribution

--- Summary ---
  HIGH risk: {count} issues
  MEDIUM risk: {count} issues
  LOW risk: {count} issues

  Overall: {SAFE / REVIEW NEEDED / FIX REQUIRED}

============================================

Auto-fix all issues? (yes / select / no)
```

### Step 2: Auto-Fix

For each issue, apply the suggested fix:
- Replace risky phrases with compliant alternatives
- Add required disclosures
- Insert disclaimers

### Step 3: Certification

After fixes:
```
Compliance re-check: PASSED

All {count} issues resolved.
Content is ready for publication.

Note: This check covers common compliance patterns but
does not constitute legal advice. For high-stakes content
(high-value products, health claims), consult a legal professional.
```

## Integration with Other Skills

- **content-writer**: Auto-run compliance check on BOFU/paid content
- **affiliate-writer**: Mandatory compliance check before saving
- **launch-sequence**: Check all launch content for compliance
- **pre-publish**: Include compliance status in pre-publish checklist
- **content-grader**: Compliance issues reduce overall grade

## Quality Gate

- [ ] All major compliance areas checked (景表法, 薬機法, ステマ, 著作権)
- [ ] Fixes preserve meaning while being compliant
- [ ] PR/affiliate disclosures are properly placed (top of content)
- [ ] Disclaimer text is appropriate for the claim type
- [ ] False positives minimized (not flagging normal language)
- [ ] Clear disclaimer that this is not legal advice
