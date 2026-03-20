---
name: hashtag-optimizer
description: Deep hashtag research and optimization for Instagram — analyze volume, competition, relevance to generate the optimal 30-tag set per post. Avoids same-tag repetition (algorithm penalty), tracks used hashtags, and rotates sets automatically.
---

# Hashtag Optimizer

Get found on Instagram with the right hashtags — researched, rotated, and algorithm-safe.

## When to Activate

- User says `/hashtag {topic}` or `/hashtag`
- User asks "what hashtags should I use?"
- User asks "optimize my hashtags"
- Auto-called by content-writer and carousel-generator for Instagram

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Data: hashtag-sets.json

Location: `~/.content-autopilot/hashtag-sets.json`

```json
{
  "version": "1.0",
  "sets": [
    {
      "id": "set-001",
      "topic": "AI automation",
      "created_at": "2026-03-21",
      "tags": {
        "big": ["#AI", "#automation", "#productivity"],
        "medium": ["#AItools", "#workautomation", "#techlife"],
        "niche": ["#AIforsmallbiz", "#automationtips", "#nocodetool"]
      },
      "used_dates": ["2026-03-21"],
      "performance_notes": null
    }
  ],
  "banned_tags": [],
  "rotation_rule": "no_repeat_within_3_days"
}
```

## Commands

### `/hashtag {topic}` — Generate optimized hashtag set for a topic
### `/hashtag rotate` — Get today's set (auto-rotated from saved sets)
### `/hashtag banned add {tag}` — Add a tag to banned list
### `/hashtag audit` — Check recent hashtag performance patterns
### `/hashtag sets` — View all saved hashtag sets

## Workflow

### Step 1: Research Hashtags

Use WebSearch to gather hashtag data:

```
Search: "best Instagram hashtags {topic} {year}"
Search: "Instagram hashtag research {niche}"
Search: "#{keyword}" — check related tags
Search: "Instagram banned hashtags {year}" — avoid penalties
```

### Step 2: Categorize by Tier

```
Hashtag Research: "{topic}"
============================================

--- Tier 1: Big (100K-1M+ posts) — 10 tags ---
Discovery potential: High | Ranking difficulty: Hard
  1. #{tag} — {estimated_posts}
  2. #{tag} — {estimated_posts}
  ...10 tags

--- Tier 2: Medium (10K-100K posts) — 10 tags ---
Discovery potential: Medium | Ranking difficulty: Medium
  1. #{tag} — {estimated_posts}
  2. #{tag} — {estimated_posts}
  ...10 tags

--- Tier 3: Niche (<10K posts) — 10 tags ---
Discovery potential: Focused | Ranking difficulty: Easy
  1. #{tag} — {estimated_posts}
  2. #{tag} — {estimated_posts}
  ...10 tags

Total: 30 tags (Instagram optimal)

============================================

Copy-paste ready:
{all 30 tags in one block, space-separated}
```

### Step 3: Rotation Management

**Why rotate:** Instagram penalizes accounts that use the same hashtags repeatedly.

```
Rotation Rules:
  - Never use the exact same 30-tag set within 3 days
  - Swap at least 10 tags between consecutive posts
  - Keep 10-15 "core" tags + rotate 15-20 "variable" tags
  - Track usage in hashtag-sets.json

Today's recommendation:
  Core tags (keep): {15 tags}
  Variable tags (rotated): {15 tags from unused pool}
  Last used: {date of last similar set}
```

### Step 4: Banned Tag Check

Cross-check against known banned/shadowbanned hashtags:
```
Banned tag check:
  [ ] No banned hashtags found — safe to use
  or
  [!] Warning: #{tag} is currently banned/restricted
      Remove and replace with: #{alternative}
```

### Step 5: Save and Track

Save the generated set to hashtag-sets.json.
Mark the set as used when the post is published.

## Hashtag Placement Strategy

```
Current algorithm preference:
  Placement: {in caption / first comment} — research latest preference
  Timing: Add {immediately / within 1 min of posting}

  Note: Algorithm preferences change — /algorithm tracks this
```

## Integration with Other Skills

- **content-writer**: Auto-generates hashtags using this skill for Instagram
- **carousel-generator**: Includes optimized hashtags in carousel captions
- **algorithm-guide**: Hashtag strategy updates based on algorithm changes
- **content-analytics**: Can correlate hashtag sets with engagement patterns

## Quality Gate

- [ ] 30 tags total (Instagram optimal)
- [ ] 3-tier distribution (big/medium/niche = 10/10/10)
- [ ] No banned or restricted tags included
- [ ] Not repeating the same set within 3 days
- [ ] Tags are relevant to the specific post topic
- [ ] Tags include both English and Japanese where appropriate
