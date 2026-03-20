---
name: batch-generator
description: Weekly batch content generation — generate 7 or 14 days of content in one session. Automatically selects topics based on content-history, active series, funnel balance, competitor gaps, and seasonal events. Eliminates the need for daily /autopilot runs.
---

# Batch Generator

Generate a full week (or more) of content in one sitting. No more daily runs.

## When to Activate

- User says `/batch`, `/batch 7`, or `/batch 14`
- User asks "generate a week's content"
- User asks "batch create content"
- User says "create content for the whole week"

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- `~/.content-autopilot/content-history.json` (for dedup and balance)
- Optional: `active-series.json`, `competitor-analysis.json`, `seasonal-calendar.json`

## Commands

### `/batch` or `/batch 7` — Generate 7 days of content
### `/batch 14` — Generate 14 days of content
### `/batch status` — Show progress of current batch
### `/batch preview` — Preview the planned topics without generating content

## Workflow

### Step 1: Load All Context

Read all available data files:
1. `profile.json` — theme, style, platforms, funnel settings
2. `content-history.json` — past topics (dedup), funnel balance
3. `active-series.json` — active series parts to include
4. `competitor-analysis.json` — gap opportunities
5. `seasonal-calendar.json` — upcoming events (if available)

### Step 2: Plan the Week

Auto-select topics for each day considering:

**Priority order for topic selection:**
1. Active series parts (must be included on their scheduled day)
2. Seasonal/event-driven topics (time-sensitive)
3. Competitor gap opportunities (strategic value)
4. Funnel balance correction (if off-target by >15%)
5. Trending topics (via WebSearch)
6. Evergreen topics (fill remaining days)

**Funnel balance targets per week (7 days):**
| Stage | Target Days | Platforms |
|-------|------------|-----------|
| TOFU | 3-4 days | X, Instagram |
| MOFU | 2 days | note (free) |
| BOFU | 1-2 days | note (paid) |

**Dedup rules:**
- No topic repeated from the last 30 days
- No two similar topics within the same batch
- Vary content pillars across the week

### Step 3: Present the Plan

```
============================================
  Weekly Content Plan (7 days)
  {start_date} — {end_date}
============================================

Day 1 ({weekday}) | {TOFU} | X thread
  Topic: "{topic}"
  Category: {trending/overseas/evergreen/competitor_gap/seasonal}
  Title logics: {suggested logics}

Day 2 ({weekday}) | {TOFU} | Instagram
  Topic: "{topic}"
  Category: {category}
  Title logics: {suggested logics}

Day 3 ({weekday}) | {MOFU} | note (free)
  Topic: "{topic}"
  Category: {category}
  Title logics: {suggested logics}

...

Day 7 ({weekday}) | {BOFU} | note (paid)
  Topic: "{topic}"
  Category: {category}
  Title logics: {suggested logics}

--- Balance ---
TOFU: 4 days (57%) | MOFU: 2 days (29%) | BOFU: 1 day (14%)
Pillars: {pillar1} x3, {pillar2} x2, {pillar3} x2

Approve this plan? (yes / edit day N / regenerate)
```

### Step 4: User Approval

Wait for user to approve or modify:
- `yes` — proceed to generation
- `edit day 3` — change topic/stage for a specific day
- `regenerate` — create a new plan from scratch
- `swap day 2 day 5` — swap two days' content

### Step 5: Batch Generate

For each approved day, invoke content-writer logic:
1. Research the topic (WebSearch)
2. Generate 3 title candidates, auto-select #1 (or use batch-specific titles)
3. Generate platform-native content
4. Save files with correct date naming

**File naming for batch:**
```
~/Desktop/content-autopilot-output/
  note_{date}.md
  x_{date}.md
  instagram_{date}.md
```

**Generation order:**
- Generate all content sequentially (Day 1 → Day 7)
- Display progress: `Generating Day {N}/{total}: "{topic}"...`
- Each day's content is complete before moving to the next

### Step 6: Record All Entries

For each generated day, append to `content-history.json`:
- Same schema as daily-autopilot Step 6.5
- `source: "batch"` to distinguish from daily generation
- A/B titles recorded for each

### Step 7: Summary

```
============================================
  Batch Generation Complete
  {count} days of content generated
============================================

Generated Files:
  Day 1: note_{date}.md, x_{date}.md, instagram_{date}.md
  Day 2: note_{date}.md, x_{date}.md, instagram_{date}.md
  ...
  Day 7: note_{date}.md, x_{date}.md, instagram_{date}.md

Total files: {count}
Total characters: {sum across all files}

Funnel balance: TOFU {N} | MOFU {N} | BOFU {N}
Pillars covered: {list}

--- Posting Schedule ---
Day 1 ({date}, {weekday}): Post X thread at {best_time}
Day 2 ({date}, {weekday}): Post Instagram at {best_time}
...

All content saved to ~/Desktop/content-autopilot-output/
============================================
```

## Visual Creator Integration

After text content batch is complete:
- Ask: "Generate images for all {N} days? (yes / no / select days)"
- If yes, invoke visual-creator for each day
- If select, let user pick which days need images

## Quick Batch Mode

`/batch 7 quick` — Skip all confirmations:
- Auto-select topics
- Auto-select titles (#1 candidate)
- Auto-generate all content
- Display final summary only

## Error Recovery

| Error | Recovery |
|-------|----------|
| WebSearch fails for a topic | Use domain knowledge, note limitation |
| Generation fails mid-batch | Save progress, resume from last completed day |
| Duplicate topic detected | Auto-replace with next best candidate |
| Funnel balance can't be achieved | Note deviation, explain why |

## Backward Compatibility

When `funnel.enabled = false`:
- Skip funnel balance optimization
- Assign platforms based on topic depth naturally
- All other batch features work normally

## Quality Gate

Before delivering:
- [ ] All {N} days have content for all active platforms
- [ ] No duplicate topics within the batch or last 30 days
- [ ] Funnel balance is within acceptable range (if enabled)
- [ ] Content pillars are varied across the week
- [ ] Files are correctly named with sequential dates
- [ ] All entries recorded in content-history.json
- [ ] Each day's content follows platform-native rules
