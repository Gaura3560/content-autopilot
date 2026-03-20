---
name: meta-learning
description: System self-improvement engine — track which skills the user actually uses, which recommendations they follow, and which outputs they value. Automatically optimize skill suggestions, workflow defaults, and advisor priorities based on real user behavior. The system that makes 119 skills feel like 10.
---

# Meta-Learning

119 skills that learn which ones YOU actually need. The system adapts to you.

## When to Activate

- User says `/meta-learning` or `/meta`
- Auto-running in background — tracks all skill usage
- User says "simplify my experience"

## Data: meta-learning.json

```json
{
  "version": "1.0",
  "skill_usage": {
    "daily-autopilot": { "uses": 45, "last_used": "2026-03-21", "satisfaction": "high" },
    "content-grader": { "uses": 38, "last_used": "2026-03-21", "satisfaction": "high" },
    "trend-predictor": { "uses": 2, "last_used": "2026-02-15", "satisfaction": "unknown" },
    "audience-psychograph": { "uses": 0, "last_used": null, "satisfaction": "unknown" }
  },
  "recommendation_follow_rate": {
    "advisor": 0.72,
    "engagement-predictor": 0.45
  },
  "user_patterns": {
    "preferred_workflow": "morning",
    "active_hours": "09:00-12:00",
    "skill_chain_preference": ["trend-scout", "content-writer", "grade", "pre-publish"]
  }
}
```

## Commands

### `/meta` — Show learning insights
### `/meta simplify` — Hide unused skills, surface favorites
### `/meta reset` — Reset learning (fresh start)

## Workflow

### Learning Dashboard

```
============================================
  Meta-Learning — System Intelligence
  Based on {N} sessions, {N} skill uses
============================================

--- Your Core Skills (used 10+ times) ---
  1. /daily-autopilot — {N} uses (your main workflow)
  2. /content-writer — {N} uses
  3. /grade — {N} uses
  4. /pre-publish — {N} uses
  5. /perf-log — {N} uses

--- Underutilized (available but unused) ---
  /audience-psychograph — never used (could improve targeting)
  /trend-predictor — used once (try again with more data)
  /content-arbitrage — never used (high potential for your profile)

--- Recommendations Accuracy ---
  /advisor recommendations: {percentage}% followed
  /engagement-predictor: {percentage}% accurate vs actual
  /best-time suggestions: {percentage}% followed

--- Learned Patterns ---
  You typically work: {time_range}
  Your preferred flow: {skill_chain}
  You skip: {skills_consistently_skipped}
  You always use after writing: {skills}

--- Adaptive Changes Made ---
  1. /advisor now prioritizes {skill} (you follow it most)
  2. /workflow morning adjusted to match your actual pattern
  3. Hidden {N} skills you've never used from quick suggestions

============================================

Simplify further? /meta simplify
```

### Simplify Mode

```
/meta simplify

Based on your usage, showing simplified interface:

DAILY (your essentials):
  /autopilot → /grade → /publish-check

WEEKLY:
  /report → /batch 7

MONTHLY:
  /algorithm → /competitor-scout → /dna

AVAILABLE (hidden from defaults, accessible anytime):
  {87 other skills — type the command to use}

This reduces daily cognitive load from 119 skills to ~5 commands.
Revert with /meta reset
```

### Continuous Learning

After every session:
```
Meta-learning updated:
  Skills used this session: {list}
  Recommendations followed: {count}/{total}
  New pattern detected: {pattern}
```

## Integration

- **skill-advisor**: Priorities shaped by meta-learning data
- **workflow-chain**: Default workflows adapted to usage patterns
- **ALL skills**: Usage frequency tracked automatically
- **weekly-report**: Meta-learning insights in report

## Quality Gate

- [ ] Learning is based on actual behavior (not assumed)
- [ ] Simplification doesn't hide critical skills
- [ ] User can always access any skill (nothing locked)
- [ ] Patterns reflect real usage, not just recent
- [ ] Reset option available (no permanent changes)
