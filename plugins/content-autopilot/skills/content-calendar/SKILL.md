---
name: content-calendar
description: Unified content calendar — visualize all content across all platforms in one view. Combines content-history, active-series, seasonal events, batch plans, launch sequences, and challenge schedules. The single source of truth for "what's planned, what's published, what's next."
---

# Content Calendar

See everything in one place — past, present, and planned content across all platforms.

## When to Activate

- User says `/calendar` or `/calendar {month}`
- User asks "what's my content schedule?"
- User asks "show me this week/month"
- User wants to see the big picture

## Prerequisites

- `~/.content-autopilot/content-history.json` (published content)
- Optional: active-series.json, seasonal-calendar.json, launch plans, challenge plans

## Commands

### `/calendar` — Show this week's calendar
### `/calendar week` — This week (Mon-Sun)
### `/calendar month` — This month overview
### `/calendar {month}` — Specific month (e.g., `/calendar april`)
### `/calendar next` — Next 7 days with recommendations
### `/calendar gaps` — Find unplanned days

## Workflow

### Step 1: Aggregate All Data Sources

Read and merge:
1. `content-history.json` — published content (past)
2. `active-series.json` — series parts (planned)
3. `seasonal-calendar.json` — events (opportunities)
4. Batch plans — generated content waiting to post
5. Launch sequences — campaign days
6. Challenge schedules — challenge daily content

### Step 2: Generate Calendar View

**Weekly View (`/calendar week`):**
```
============================================
  Content Calendar — Week of {date}
============================================

Mon {date}:
  [PUBLISHED] note: "{title}" (MOFU, free)
  [PUBLISHED] X: "{title}" (TOFU, thread)
  [PUBLISHED] IG: "{title}" (TOFU, carousel)

Tue {date}:
  [PUBLISHED] X: "{title}" (TOFU, single)
  [PLANNED]   IG Story: series part 3

Wed {date}:
  [PLANNED]   note: "{batch_title}" (MOFU, free)
  [PLANNED]   X: "{batch_title}" (TOFU, thread)
  [EVENT]     {seasonal event} — content opportunity

Thu {date}:
  [EMPTY] — no content planned
  [SUGGEST]   Topic: "{suggestion based on funnel balance}"
              Platform: {recommended}

Fri {date}:
  [PLANNED]   note (paid): series part 5 (BOFU)
  [LAUNCH]    Day -3: "{product}" teaser post

Sat {date}:
  [EMPTY] — no content planned
  [SUGGEST]   Recycle: "{old_title}" with fresh angle

Sun {date}:
  [CHALLENGE] Day 4: "{challenge name}" prompt
  [PLANNED]   IG: carousel from batch

--- Week Summary ---
Published: {count} | Planned: {count} | Empty: {count} days
Platforms: note {N} | X {N} | IG {N} | LinkedIn {N}
Funnel: TOFU {N} | MOFU {N} | BOFU {N}
Series: "{name}" Part {current}/{total}

============================================
```

**Monthly Overview (`/calendar month`):**
```
============================================
  Content Calendar — {Month} {Year}
============================================

Week 1 ({date range}):
  Mon: note + X | Tue: X | Wed: note + X + IG
  Thu: — | Fri: note (paid) | Sat: — | Sun: IG
  Published: 8 | Planned: 0 | Gaps: 2

Week 2 ({date range}):
  Mon: launch -7 | Tue: X | Wed: note + X
  Thu: IG carousel | Fri: note | Sat: launch -1 | Sun: —
  Published: 2 | Planned: 5 | Gaps: 1

Week 3 ({date range}):
  Mon: LAUNCH DAY | Tue: launch +1 | Wed: note
  Thu: X + IG | Fri: note | Sat: — | Sun: recap
  Planned: 7 | Gaps: 1

Week 4 ({date range}):
  (empty — plan with /batch 7)
  Planned: 0 | Gaps: 7

--- Monthly Summary ---
Total content: {count} published + {count} planned
Platform distribution: note {N} | X {N} | IG {N}
Funnel balance: TOFU {N}% | MOFU {N}% | BOFU {N}%
Events this month: {count}
Active series: {name} ({status})
Active launch: {name} ({phase})

Recommendations:
  Week 4 is completely empty — run /batch 7 to fill it
  {event} on {date} — plan content 3 days before

============================================
```

### Step 3: Gap Analysis (`/calendar gaps`)

```
Content Gaps Found:
  {date}: No content planned — suggest {topic + platform}
  {date}: No content planned — suggest {topic}
  {date}: Only X, no note — add note article
  {date}: No BOFU content this week — add paid article

Fill all gaps? (yes / select / /batch to auto-fill)
```

### Step 4: Next 7 Days (`/calendar next`)

```
Next 7 Days — Recommended Schedule:
============================================

{date} ({weekday}):
  Planned: {content if any}
  Recommended: {topic} on {platform} ({stage})
  Best time: {time from best-times.json}
  Reason: {why this topic/platform/stage today}

{date} ({weekday}):
  ...

============================================
Run /daily-autopilot to execute today's recommendation.
Run /batch 7 to generate the full week.
```

## Integration with Other Skills

- **daily-autopilot**: Calendar shows what's already planned for today
- **batch-generator**: Batch fills calendar gaps
- **series-designer**: Series parts appear on their scheduled days
- **seasonal-calendar**: Events appear as opportunities
- **launch-sequence**: Launch days appear on calendar
- **challenge-designer**: Challenge days appear on calendar
- **weekly-report**: Calendar summary included in report

## Quality Gate

- [ ] All data sources correctly merged (no duplicates)
- [ ] Published vs planned vs empty clearly distinguished
- [ ] Funnel balance visible at a glance
- [ ] Gaps are identified with actionable suggestions
- [ ] Platform coverage is visible
- [ ] Events and special activities (launches, challenges) highlighted
