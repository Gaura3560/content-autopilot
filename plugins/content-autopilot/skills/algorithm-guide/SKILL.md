---
name: algorithm-guide
description: Up-to-date platform algorithm intelligence — research the latest X, Instagram, and note algorithm changes and ranking factors. Provides actionable recommendations that content-writer and best-time automatically reference. Refreshes monthly.
---

# Algorithm Guide

Stay ahead of platform algorithm changes — know what gets boosted and what gets buried.

## When to Activate

- User says `/algorithm` or `/algo`
- User says `/algorithm {platform}` (e.g., `/algorithm instagram`)
- User asks "what's the latest algorithm change?"
- User asks "why is my reach dropping?"
- Auto-referenced by content-writer and best-time for optimization

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/algorithm` — Full report for all platforms
### `/algorithm {platform}` — Report for specific platform (x/instagram/note)
### `/algorithm changes` — Recent changes only (last 30 days)
### `/algorithm tips` — Quick actionable tips

## Workflow

### Step 1: Research Current Algorithm State

Use WebSearch to gather the latest information:

**X (Twitter):**
```
Search: "X algorithm update {year} {month}"
Search: "Twitter algorithm ranking factors {year}"
Search: "X algorithm changes latest"
Search: "how X algorithm works {year}"
```

**Instagram:**
```
Search: "Instagram algorithm update {year} {month}"
Search: "Instagram Reels algorithm {year}"
Search: "Instagram carousel algorithm boost {year}"
Search: "Instagram reach dropping {year} fix"
```

**note:**
```
Search: "note アルゴリズム {year}"
Search: "note おすすめ 表示 仕組み"
Search: "note PV 上げ方 {year}"
Search: "note 検索 上位 コツ"
```

### Step 2: Compile Algorithm Report

```
============================================
  Platform Algorithm Intelligence Report
  Updated: {date}
============================================

=== X (Twitter) ===

Current ranking signals (by weight):
  1. [HIGH] {signal} — {explanation}
  2. [HIGH] {signal} — {explanation}
  3. [MEDIUM] {signal} — {explanation}
  4. [MEDIUM] {signal} — {explanation}
  5. [LOW] {signal} — {explanation}

What gets BOOSTED:
  + {content type/behavior that algorithm favors}
  + {content type/behavior}
  + {content type/behavior}

What gets SUPPRESSED:
  - {content type/behavior that algorithm penalizes}
  - {content type/behavior}
  - {content type/behavior}

Recent changes:
  {date}: {change description and impact}
  {date}: {change description and impact}

Action items for your content:
  1. {specific actionable tip}
  2. {specific actionable tip}
  3. {specific actionable tip}

---

=== Instagram ===

Current ranking signals (by weight):
  Feed:
    1. [HIGH] {signal}
    2. [HIGH] {signal}
    3. [MEDIUM] {signal}

  Reels:
    1. [HIGH] {signal}
    2. [HIGH] {signal}
    3. [MEDIUM] {signal}

  Explore:
    1. [HIGH] {signal}
    2. [MEDIUM] {signal}

Format priority (current boost order):
  1st: {format} — {boost level and reason}
  2nd: {format} — {boost level}
  3rd: {format} — {boost level}
  4th: {format} — {least boosted}

What gets BOOSTED:
  + {specific behavior/content type}
  + {specific behavior/content type}

What gets SUPPRESSED:
  - {specific behavior/content type}
  - {specific behavior/content type}

Hashtag strategy (current):
  Optimal count: {N} hashtags
  Placement: {in caption / first comment}
  Mix: {strategy}

Action items:
  1. {specific tip}
  2. {specific tip}
  3. {specific tip}

---

=== note ===

Discovery mechanisms:
  1. {how note surfaces content}
  2. {ranking factor}
  3. {ranking factor}

What gets featured:
  + {content characteristic}
  + {content characteristic}

SEO factors (note internal search):
  1. {factor}
  2. {factor}
  3. {factor}

Action items:
  1. {specific tip}
  2. {specific tip}

============================================
```

### Step 3: Save Algorithm Data

Save to `~/.content-autopilot/algorithm-guide.json`:
```json
{
  "version": "1.0",
  "updated_at": "2026-03-21",
  "platforms": {
    "x": {
      "boost_signals": [],
      "suppress_signals": [],
      "recent_changes": [],
      "tips": []
    },
    "instagram": {
      "boost_signals": [],
      "suppress_signals": [],
      "format_priority": [],
      "hashtag_strategy": {},
      "tips": []
    },
    "note": {
      "discovery_factors": [],
      "seo_factors": [],
      "tips": []
    }
  }
}
```

### Step 4: Quick Tips (`/algorithm tips`)

Concise, actionable summary:
```
Algorithm Quick Tips (updated {date}):

X:
  DO: {tip} | DON'T: {anti-tip}
  DO: {tip} | DON'T: {anti-tip}

Instagram:
  DO: {tip} | DON'T: {anti-tip}
  Best format right now: {format}

note:
  DO: {tip} | DON'T: {anti-tip}
  Best posting time: {time}
```

## Integration with Other Skills

- **content-writer**: Checks algorithm-guide.json to optimize format, length, hashtags
- **best-time**: References algorithm data for timing recommendations
- **carousel-generator**: Adjusts slide count/format based on current IG algorithm
- **content-grader**: Includes algorithm alignment in Platform Fit score
- **batch-generator**: Selects optimal format per day based on algorithm data

## Auto-Refresh

Algorithm data becomes stale after ~30 days. When other skills reference algorithm-guide.json:
- If `updated_at` > 30 days ago, suggest: "Algorithm data is {N} days old. Run /algorithm to refresh."

## Quality Gate

- [ ] Information is sourced from recent, credible sources
- [ ] Specific dates cited for algorithm changes
- [ ] Tips are actionable (not vague "post good content")
- [ ] Platform-specific nuances captured (feed vs Reels vs Explore)
- [ ] Saved data is structured for other skills to consume
