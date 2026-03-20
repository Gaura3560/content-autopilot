---
name: series-designer
description: Multi-day content series planner — designs 7-day or 30-day content series with narrative arc (TOFU->MOFU->BOFU progression), hooks, callbacks, and cliffhangers. Manages active series in active-series.json and integrates with daily-autopilot for daily part suggestions.
---

# Content Series Designer

Plan multi-day content series with a narrative arc that guides readers through your funnel.

## When to Activate

- User says `/series`, `/series 7`, or `/series 30`
- User says `/series status` to check active series progress
- User asks "plan a content series"
- User asks "I want to write a multi-part series"
- User wants to build audience momentum over multiple days

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- `~/.content-autopilot/content-history.json` (for context on past content)

## Data: active-series.json

Location: `~/.content-autopilot/active-series.json`

```json
{
  "version": "1.0",
  "series": [
    {
      "id": "series-2026-03-20-001",
      "title": "AI Automation in 7 Days",
      "topic": "Step-by-step AI automation for small businesses",
      "duration": 7,
      "created_at": "2026-03-20",
      "status": "active",
      "content_pillar": "AI Tools",
      "parts": [
        {
          "part": 1,
          "day": "2026-03-20",
          "stage": "TOFU",
          "platform": "x",
          "title": "Why 90% of businesses waste 3 hours/day on tasks AI can do",
          "hook": "Bold statistic to stop the scroll",
          "callback": null,
          "cliffhanger": "Tomorrow: the one tool that changes everything",
          "status": "published",
          "content_file": "x_2026-03-20.md"
        },
        {
          "part": 2,
          "day": "2026-03-21",
          "stage": "TOFU",
          "platform": "instagram",
          "title": "The AI tool stack I use to save 3 hours every day",
          "hook": "Visual tool comparison",
          "callback": "Yesterday's thread showed the problem — here's the solution",
          "cliffhanger": "Which tool to start with? Full guide dropping on note tomorrow",
          "status": "pending",
          "content_file": null
        }
      ]
    }
  ]
}
```

## Commands

### `/series` or `/series 7` — Create a 7-day series

Design a 7-day content series (default).

### `/series 30` — Create a 30-day series

Design a 30-day content series.

### `/series status` — Check active series progress

Display progress of all active series.

### `/series complete {id}` — Mark a series as completed

Mark a series as completed.

### `/series cancel {id}` — Cancel an active series

Mark a series as cancelled.

## Workflow: Create Series

### Step 1: Choose Topic

Ask the user for the series topic, or suggest based on:
1. Content history (topics that performed well)
2. Competitor gaps (from competitor-analysis.json if available)
3. Unfilled content pillars (from analytics)

```
What topic should the series cover?

Suggestions based on your history:
1. "{Topic A}" — your most engaging topic, expand into a series
2. "{Topic B}" — competitor gap, opportunity to own this space
3. Custom topic — describe what you want to cover

Select (1/2/3 or type topic):
```

### Step 2: Design Series Arc

#### 7-Day Series Arc

| Part | Day | Stage | Depth | Platform | Purpose |
|------|-----|-------|-------|----------|---------|
| 1 | Mon | TOFU | 20% | X | Hook — bold claim or surprising fact |
| 2 | Tue | TOFU | 30% | Instagram | Visual hook — emotional/relatable angle |
| 3 | Wed | MOFU | 50% | note (free) | Foundation — introduce the method/framework |
| 4 | Thu | MOFU | 60% | X thread | Deep dive — specific technique with example |
| 5 | Fri | MOFU | 70% | note (free) | Case study — real-world application |
| 6 | Sat | BOFU | 90% | note (paid) | Templates + step-by-step implementation |
| 7 | Sun | BOFU | 100% | note (paid) | Complete system + bonus materials |

#### 30-Day Series Arc

| Week | Focus | Stages | Platforms |
|------|-------|--------|-----------|
| Week 1 (Day 1-7) | Introduction & Hook | TOFU heavy | X, Instagram |
| Week 2 (Day 8-14) | Method & Framework | MOFU heavy | note (free), X |
| Week 3 (Day 15-21) | Deep Dives & Cases | MOFU/BOFU mix | note (free/paid), X |
| Week 4 (Day 22-30) | Premium & Synthesis | BOFU heavy | note (paid) |

### Step 3: Design Each Part

For each part in the series, define:

**1. Title** — using bestseller title logic, creating progression
**2. Hook** — the opening that grabs attention
**3. Callback** — reference to the previous part ("Yesterday we covered...")
**4. Cliffhanger** — teaser for the next part ("Tomorrow: the surprising...")
**5. Platform** — which platform this part lives on
**6. Funnel stage** — where in the funnel this part sits

```
## Series: "{Series Title}" — 7-Day Plan

### Part 1 (Day 1) — TOFU | X
Title: "{title}"
Hook: {opening line/concept}
Callback: (none — first part)
Cliffhanger: "{teaser for Part 2}"
Key point: {main takeaway}

### Part 2 (Day 2) — TOFU | Instagram
Title: "{title}"
Hook: {opening line/concept}
Callback: "Yesterday on X: {reference}"
Cliffhanger: "{teaser for Part 3}"
Key point: {main takeaway}

### Part 3 (Day 3) — MOFU | note (free)
Title: "{title}"
Hook: {opening line/concept}
Callback: "This week on X/Instagram: {reference}"
Cliffhanger: "{teaser for Part 4}"
Key point: {main takeaway}

...

### Part 7 (Day 7) — BOFU | note (paid)
Title: "{title}"
Hook: {opening line/concept}
Callback: "Over the last 6 days: {series summary}"
Cliffhanger: (none — series finale, CTA to next series or product)
Key point: {main takeaway}
Bonus: {template/tool/resource included}
```

### Step 4: Narrative Elements

**Callbacks** — create continuity:
- "Part 1 showed the problem. Now let's solve it."
- "Remember the 3-hour stat from Monday? Here's what happens when..."
- "You asked great questions on yesterday's post. Today's deep dive answers them."

**Cliffhangers** — drive anticipation:
- "Tomorrow: the one mistake that costs most businesses $10K+/year"
- "The full template drops Saturday on note. Follow to get notified."
- "Next: I'll show you exactly how Company X did this in 3 weeks"

**Progression** — build momentum:
- Each part reveals slightly more, never repeating
- Early parts pose questions, later parts answer them
- Free content creates hunger for paid content
- Final part delivers the complete picture

### Step 5: Save Series Plan

Save to `~/.content-autopilot/active-series.json` with the schema above.

### Step 6: Display Plan

```
============================================
  Content Series Plan
============================================

Series: "{title}"
Duration: {N} days ({start_date} — {end_date})
Topic: {description}
Pillar: {content_pillar}

--- Series Arc ---

Day 1 (Mon) | TOFU | X
  "{Part 1 title}"
  Hook: {hook concept}
  Cliffhanger: {teaser}

Day 2 (Tue) | TOFU | Instagram
  "{Part 2 title}"
  Hook: {hook concept}
  Callback: {reference to Day 1}
  Cliffhanger: {teaser}

...

Day 7 (Sun) | BOFU | note (paid)
  "{Part 7 title}"
  Hook: {hook concept}
  Callback: {series summary reference}
  Bonus: {premium content description}

--- Funnel Flow ---
TOFU (Days 1-2): Reach & hook on X/Instagram
MOFU (Days 3-5): Build trust on note (free)
BOFU (Days 6-7): Convert on note (paid)

Series saved to active-series.json
Run /daily-autopilot to generate today's series content.

============================================
```

## Workflow: Check Status (`/series status`)

```
============================================
  Active Series Status
============================================

Series: "{title}" ({N}-day series)
Progress: {completed}/{total} parts ({percentage}%)

[x] Day 1 — "{Part 1 title}" — published
[x] Day 2 — "{Part 2 title}" — published
[ ] Day 3 — "{Part 3 title}" — TODAY
[ ] Day 4 — "{Part 4 title}" — scheduled
...

Next up: Part {N} — "{title}"
Platform: {platform} | Stage: {stage}
Hook: {hook}
Callback: {callback from last published part}

Run /daily-autopilot to generate Part {N}.

============================================
```

If no active series:
```
No active series found.
Run /series to create a new content series.
```

## Integration with Other Skills

- **daily-autopilot**: Step 2.0 checks active-series.json and suggests the next part
- **content-writer**: Series mode adds hook/callback/cliffhanger to content
- **content-analytics**: Tracks series entries (grouped by series_id)
- **trend-scout**: May suggest series topics based on trending themes

## Backward Compatibility

When `funnel.enabled = false`:
- Series arc still works, but without funnel stage labels
- Platform assignments remain the same
- Depth progression still applies (good content strategy regardless)
- Skip funnel-specific CTAs in callbacks/cliffhangers

## Quality Gate

Before delivering:
- [ ] Series has clear narrative arc with progression
- [ ] Each part has a hook, callback (except Part 1), and cliffhanger (except last part)
- [ ] Platform assignments make sense for the content depth
- [ ] Funnel stages progress naturally (TOFU -> MOFU -> BOFU)
- [ ] Titles use varied bestseller logics (not the same pattern every day)
- [ ] active-series.json is saved correctly
- [ ] Series doesn't overlap with another active series
