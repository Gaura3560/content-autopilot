---
name: audience-journey
description: Map how readers flow through your content ecosystem — from discovery (X/IG) through trust-building (note free) to conversion (note paid). Identify bottlenecks, drop-off points, and optimize the reader path. The strategic view of your entire content funnel.
---

# Audience Journey Mapper

See how readers move through your content — and where they get stuck.

## When to Activate

- User says `/audience-journey` or `/journey`
- User asks "how do readers move through my content?"
- User asks "where am I losing readers?"
- User wants to optimize the content funnel flow

## Prerequisites

- `~/.content-autopilot/content-history.json` with performance data
- `~/.content-autopilot/profile.json` with funnel settings

## Commands

### `/journey` — Map the current audience journey
### `/journey bottlenecks` — Identify where readers drop off
### `/journey optimize` — Generate optimization plan
### `/journey {platform}` — Journey map for a specific platform

## Workflow

### Step 1: Map Current Journey

Using performance data from content-history:

```
============================================
  Audience Journey Map
============================================

STAGE 1: DISCOVERY (TOFU)
  Platform: X + Instagram
  ┌─────────────────────────────────────┐
  │  X impressions: ~{avg}/post         │
  │  IG reach: ~{avg}/post              │
  │  IG Reels reach: ~{avg}/reel        │
  │                                     │
  │  Click-through to note:             │
  │    X → note: {rate}% ({avg} clicks) │
  │    IG → note: {rate}% ({avg} visits)│
  └────────────┬────────────────────────┘
               │ {funnel_rate}% proceed
               ▼
STAGE 2: ENGAGEMENT (MOFU)
  Platform: note (free articles)
  ┌─────────────────────────────────────┐
  │  Avg PV per article: {avg}          │
  │  Avg read-through rate: ~{est}%     │
  │  Avg likes: {avg} ({rate}% of PV)   │
  │  Follow rate: ~{est}% of PV         │
  │                                     │
  │  Lead magnet downloads: {avg}/month │
  │  Email signups: {avg}/month         │
  └────────────┬────────────────────────┘
               │ {funnel_rate}% proceed
               ▼
STAGE 3: CONVERSION (BOFU)
  Platform: note (paid articles / membership)
  ┌─────────────────────────────────────┐
  │  Paid article purchases: {avg}/month│
  │  Membership subscribers: {total}    │
  │  Avg revenue per reader: ¥{avg}     │
  │  Free → paid conversion: {rate}%    │
  └─────────────────────────────────────┘

OVERALL FUNNEL:
  Impression → Click: {rate}%
  Click → Read: {rate}%
  Read → Follow: {rate}%
  Follow → Purchase: {rate}%
  Total: {impression} → {purchase} ({overall_rate}%)

============================================
```

### Step 2: Identify Bottlenecks (`/journey bottlenecks`)

```
Bottleneck Analysis:
============================================

BIGGEST DROP-OFF: {stage} → {next_stage}
  Current rate: {rate}%
  Industry benchmark: ~{benchmark}%
  Gap: {difference}% below benchmark

  Root causes:
  1. {cause} — {evidence from content data}
  2. {cause} — {evidence}
  3. {cause} — {evidence}

  Impact: Fixing this could add ~{estimate} conversions/month

SECONDARY BOTTLENECK: {stage}
  Current rate: {rate}%
  Issue: {description}

PERFORMING WELL: {stage}
  Current rate: {rate}%
  Above benchmark by {difference}%
  Strength: {what you're doing right}

============================================
```

### Step 3: Optimization Plan (`/journey optimize`)

```
Journey Optimization Plan:
============================================

Priority 1: Fix {stage} → {next_stage} drop-off
  Action: {specific action}
  Skills to use: {smart-cta / auto-linker / engagement-templates}
  Expected impact: +{estimate}% conversion at this stage
  Timeline: {N} weeks

Priority 2: Strengthen {stage}
  Action: {action}
  Skills to use: {skills}
  Expected impact: +{estimate}%

Priority 3: Expand {stage}
  Action: {action}
  Expected impact: +{estimate}%

Combined impact:
  Before: {current_conversions}/month
  After (estimated): {projected}/month
  Revenue impact: +¥{estimated_revenue}/month

============================================
```

## Integration with Other Skills

- **performance-log**: Journey data requires actual metrics
- **funnel-designer**: Journey shows if funnel design is working
- **smart-cta**: CTAs optimized for specific journey stage transitions
- **auto-linker**: Links guide readers through the journey
- **monetize-report**: Revenue data mapped to journey stages
- **content-calendar**: Content mix optimized for journey bottlenecks

## Quality Gate

- [ ] Journey map based on actual performance data where available
- [ ] Estimates clearly labeled as estimates (not presented as facts)
- [ ] Bottlenecks identified with specific evidence
- [ ] Optimization plan is actionable with specific skill references
- [ ] Revenue impact is conservatively estimated
