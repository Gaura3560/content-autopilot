---
name: cross-platform-sync
description: Cross-platform consistency checker — verify the same topic published across multiple platforms doesn't contain contradictions, conflicting numbers, or mismatched claims. Catches "note says 3 steps but X thread says 5 steps" before your audience notices.
---

# Cross-Platform Sync

Same topic, different platforms — make sure the message is consistent everywhere.

## When to Activate

- User says `/sync-check {date}` or `/cross-sync`
- User asks "are my platforms saying the same thing?"
- Auto-suggested by pre-publish when content exists for same topic on multiple platforms

## Prerequisites

- Multiple content files for the same topic on different platforms

## Commands

### `/sync-check {date}` — Check all platforms for a date's content
### `/sync-check {file1} {file2}` — Check two specific files
### `/sync-check all` — Audit recent cross-platform content

## What Gets Checked

| Check | Example Problem | Severity |
|-------|----------------|----------|
| Number mismatch | note: "3 steps" / X: "5 steps" | High |
| Claim conflict | note: "Tool A is best" / IG: "Tool B wins" | High |
| Depth inversion | X has more detail than note (should be opposite) | Medium |
| CTA conflict | note says "DM me" / X says "check note" (circular) | Medium |
| Date mismatch | Different dates/timelines cited | Medium |
| Tone clash | note: professional / IG: too casual on same topic | Low |

## Workflow

### Step 1: Identify Cross-Platform Content

```
Cross-platform content for {date}:

Topic: "{topic}"
Platforms:
  note: "note_{date}.md" — 3,200 chars, MOFU
  X: "x_{date}.md" — 5-tweet thread, TOFU
  IG: "instagram_{date}.md" — carousel, TOFU

Checking consistency across all 3...
```

### Step 2: Compare and Report

```
============================================
  Cross-Platform Sync Check
  Topic: "{topic}" ({date})
============================================

NUMBER CONSISTENCY:
  note: "7つのAIツール" (7 tools)
  X: "5つのAIツール" (5 tools)
  IG: "7つのAIツール" (7 tools)
  [MISMATCH] X says 5, others say 7
  Fix: Update X thread to match (7 tools)

CLAIM CONSISTENCY:
  note: "ChatGPTが最も汎用的"
  X: "ChatGPTが最も汎用的"
  IG: "ChatGPTがおすすめ"
  [OK] Consistent (IG is simplified but not contradictory)

DEPTH CONSISTENCY:
  note: 80% depth (expected for MOFU) — OK
  X: 30% depth (expected for TOFU) — OK
  IG: 50% depth (expected for TOFU) — OK
  [OK] Depth appropriate per platform

CTA CONSISTENCY:
  note: "有料記事でさらに詳しく"
  X: "詳しくはnoteで → {url}"
  IG: "プロフィールのリンクから"
  [OK] All CTAs point toward monetization (consistent funnel)

TERMINOLOGY:
  note: "AI自動化ツール"
  X: "AIツール"
  IG: "AI自動化"
  [MINOR] Terminology varies — consider standardizing to "AI自動化ツール"

--- Summary ---
  Mismatches: {count}
  Warnings: {count}
  Consistent: {count}

  Sync score: {percentage}%

============================================

Fix mismatches? (yes / select / no)
```

## Integration with Other Skills

- **consistency-auditor**: Time-series consistency (past vs present)
- **cross-platform-sync**: Same-time consistency (across platforms)
- **content-writer**: Generates consistent cross-platform content
- **pre-publish**: Sync check before publishing multi-platform content
- **repurpose**: Check sync after repurposing content

## Quality Gate

- [ ] All platforms for the same topic checked
- [ ] Number/fact mismatches detected accurately
- [ ] Acceptable depth differences not flagged (30% vs 80% is intentional)
- [ ] CTA flow makes sense across platforms
- [ ] Terminology variations tracked
