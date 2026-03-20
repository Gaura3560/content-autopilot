---
name: skill-advisor
description: Intelligent skill recommendation engine — analyzes your current state across all data sources (history, pipeline, expiry, performance, calendar, DNA) and recommends exactly which skills to run next, in what order, and why. The "what should I do now?" answer for 89 skills.
---

# Skill Advisor

89 skills is powerful — but only if you know which one to use right now.

## When to Activate

- User says `/advisor` or `/what-next`
- User asks "what should I do?"
- User asks "where should I focus?"
- User feels overwhelmed by options
- Session start — proactive recommendation

## Prerequisites

- All available data files in `~/.content-autopilot/`

## Commands

### `/advisor` — Full recommendation based on current state
### `/advisor quick` — Top 3 actions only
### `/advisor {goal}` — Recommendations for a specific goal (growth/revenue/quality)

## Workflow

### Step 1: Assess Current State

Read ALL data sources and score the health of each area:

```
State Assessment:
  content-history.json: {exists/missing} — {N} entries, last: {date}
  content-dna.json: {exists/missing/stale} — analyzed: {date}
  performance data: {N}/{total} entries have performance logged
  active-series.json: {active series? Y/N}
  pipeline-state.json: {N} items in pipeline
  content-expiry: {N} expired, {N} expiring soon
  ab-tests.json: {N} active tests
  competitor-analysis.json: last scan: {date}
  algorithm-guide.json: last updated: {date}
  monetize-data.json: {exists/missing}
  best-times.json: {exists/missing}
  brand-voice.json: {exists/missing}
```

### Step 2: Identify Priorities

Score each area by urgency × impact:

```
Priority Matrix:
  [URGENT + HIGH IMPACT]:
    - {area}: {reason}
  [URGENT + MEDIUM IMPACT]:
    - {area}: {reason}
  [NOT URGENT + HIGH IMPACT]:
    - {area}: {reason}
```

### Step 3: Generate Recommendations

```
============================================
  Skill Advisor — Your Next Actions
  Based on: {data_sources_analyzed} data sources
============================================

--- RIGHT NOW (do today) ---

1. /perf-log — Log performance for {N} unlogged posts
   Why: You have {N} posts without performance data.
   Without this, predictions and DNA analysis are guesses.
   Time: ~5 minutes
   Impact: HIGH — unlocks accuracy for all analytics

2. /expiry — {N} articles have expired data
   Why: "{title}" has stale 2026 Q1 data (Q2 is available)
   Time: ~10 minutes (review) + /refresh if needed
   Impact: MEDIUM — protects credibility

3. /pipeline move {id} review — "{title}" stuck in draft
   Why: This has been in draft for {N} days
   Time: Run /grade + /pre-publish (~5 min)
   Impact: MEDIUM — content sitting unfinished

--- THIS WEEK ---

4. /ab-test new {element} — No active A/B tests
   Why: You have enough data to start testing {element}
   Time: Design takes 5 min, runs over 2 weeks
   Impact: HIGH — confirms what actually works

5. /algorithm — Algorithm data is {N} days old
   Why: Platform algorithms change monthly
   Time: ~3 minutes
   Impact: MEDIUM — keeps optimization current

6. /batch 7 — Next week has no planned content
   Why: Calendar shows {N} empty days next week
   Time: ~15 minutes
   Impact: HIGH — consistency drives growth

--- WHEN YOU HAVE TIME ---

7. /content-dna update — DNA based on {old_date} data
   Why: You have {N} new entries since last analysis
   Time: ~2 minutes
   Impact: MEDIUM — improves all future content

8. /competitor-scout — Last scan was {N} days ago
   Why: Competitors may have new content/strategies
   Time: ~5 minutes
   Impact: LOW-MEDIUM

--- YOUR CURRENT GOALS ---

For GROWTH: Focus on #6 (consistency) + /growth-hack
For REVENUE: Focus on #1 (data) + /monetize + /journey
For QUALITY: Focus on #4 (testing) + /benchmark

============================================
Next advisor check: Run /advisor again in 3-7 days
============================================
```

## Advisor Logic

Priority scoring algorithm:
```
Score = Urgency × Impact × Data_availability

Urgency:
  5: Expired content / broken data / empty calendar
  4: Stale data (30+ days) / stuck pipeline items
  3: Missing analysis / no active tests
  2: Optimization opportunities / growth tactics
  1: Nice-to-have improvements

Impact:
  5: Affects ALL future content (perf-log, DNA, algorithm)
  4: Affects revenue directly (monetize, journey, pricing)
  3: Affects growth (consistency, competitor, engagement)
  2: Affects quality (grade, benchmark, readability)
  1: Marginal improvement
```

## Integration with Other Skills

- References ALL 89 skills — knows when each is relevant
- Reads ALL data files — understands complete system state
- **This is the orchestration layer** — the brain that directs the skills

## Quality Gate

- [ ] Recommendations based on actual system state (not generic)
- [ ] Priority order reflects real urgency and impact
- [ ] Time estimates are realistic
- [ ] Each recommendation has a clear "why"
- [ ] Goal-specific recommendations match the stated goal
- [ ] Doesn't overwhelm (max 8-10 recommendations)
