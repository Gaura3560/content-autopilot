---
name: burnout-detector
description: Detect creator burnout early — analyze posting frequency trends, quality score decline, topic repetition, and engagement dropping patterns. Prescribe recovery actions before burnout hits. The sustainability guardian.
---

# Burnout Detector

The system that tells you to rest before you break.

## When to Activate

- User says `/burnout-check` or `/burnout`
- Auto-triggered when posting frequency drops 40%+ or quality scores decline 3 weeks in a row
- User says "I'm tired" or "I don't feel like writing"

## Commands

### `/burnout` — Full burnout risk assessment
### `/burnout recovery` — Generate recovery plan

## Warning Signals

| Signal | Detection | Severity |
|--------|-----------|----------|
| Posting frequency drop | 40%+ decline over 2 weeks | High |
| Quality score decline | 3+ consecutive weeks of lower grades | Medium |
| Topic repetition | Same topic cluster 5+ times in 2 weeks | Medium |
| Engagement decline | Despite consistent posting | Low-Medium |
| Longer creation time | ROI data shows increasing time per piece | Medium |

## Workflow

```
============================================
  Burnout Risk Assessment
============================================

Overall risk: {LOW / MODERATE / HIGH / CRITICAL}

Signals detected:
  Posting frequency: {current}/week vs {normal}/week ({change}%)
  Quality trend: {improving / stable / declining over N weeks}
  Topic variety: {score}/10 (low = repetitive)
  Creation pace: {current} min/article vs {normal} min

--- Risk Level ---
{If LOW}: You're doing great. Keep the current pace.
{If MODERATE}: Early signs detected. Consider:
  1. Use /batch 7 to pre-create next week (reduce daily pressure)
  2. Use /recycle to fill 2-3 days without new creation
  3. Schedule a content-free day this week
{If HIGH}: Clear burnout pattern. Recommended:
  1. Take 3 days off from content creation
  2. Pre-schedule existing content with /batch
  3. Use /micro to extract posts from old content (zero new writing)
  4. Run /unblock when you return (creative refresh)
{If CRITICAL}: Stop creating NOW. Recovery plan:
  1. 7-day content break (schedule recycled content)
  2. Run /advisor when you return
  3. Consider /workflow simplification

============================================
```

## Quality Gate

- [ ] Detection based on actual data patterns (not arbitrary thresholds)
- [ ] Recovery recommendations are practical
- [ ] Doesn't make user feel guilty for resting
- [ ] Pre-scheduled content keeps momentum during breaks
