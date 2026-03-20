---
name: content-roi
description: Per-content ROI calculation — track time invested vs revenue generated for every content piece. Answer "is this type of content worth my time?" with actual numbers. Identify your highest and lowest ROI content types to focus effort.
---

# Content ROI Calculator

Not all content is worth the same effort. Know which content earns its keep.

## When to Activate

- User says `/content-roi` or `/roi`
- User says `/roi log {file} {minutes}`
- User asks "is this content type worth my time?"
- User wants to optimize time allocation

## Prerequisites

- `~/.content-autopilot/content-history.json` with performance data
- `~/.content-autopilot/monetize-data.json` (for revenue)
- Time investment data (logged by user)

## Data Extension: content-history.json

```json
{
  "time_invested": {
    "research_minutes": 15,
    "writing_minutes": 45,
    "editing_minutes": 10,
    "visual_minutes": 5,
    "total_minutes": 75
  }
}
```

## Commands

### `/roi` — ROI dashboard for all content types
### `/roi log {file} {minutes}` — Log time spent on content
### `/roi {content_type}` — ROI for specific type (note/x/ig/carousel/etc)
### `/roi optimize` — Recommendations for time reallocation

## Workflow

### Step 1: Log Time Investment

```
/roi log note_2026-03-21.md 75

Time logged for "{title}":
  Total: 75 minutes

Breakdown (estimate):
  Research: ~15 min (20%)
  Writing: ~45 min (60%)
  Editing: ~10 min (13%)
  Visuals: ~5 min (7%)

Adjust breakdown? (yes / accept)
```

### Step 2: Calculate ROI

```
============================================
  Content ROI Dashboard
  Period: Last 30 days
  Hourly rate: ¥{rate}/hour (set with /roi rate {amount})
============================================

--- Per-Content ROI ---

Highest ROI:
  1. "{title}" (X thread)
     Time: 30 min (¥{cost}) → Revenue: ¥{revenue}
     ROI: +{percentage}% | Revenue/hour: ¥{per_hour}

  2. "{title}" (note paid)
     Time: 90 min (¥{cost}) → Revenue: ¥{revenue}
     ROI: +{percentage}%

  3. "{title}" (IG carousel)
     Time: 45 min (¥{cost}) → Revenue: ¥{revenue} (attributed)
     ROI: +{percentage}%

Lowest ROI:
  1. "{title}" (note free)
     Time: 120 min (¥{cost}) → Revenue: ¥{revenue} (attributed)
     ROI: {negative/low}%
     Note: Free content builds trust — ROI is long-term

--- ROI by Content Type ---

| Type | Avg Time | Avg Revenue | Avg ROI | Revenue/Hour |
|------|----------|------------|---------|-------------|
| X thread | {min} min | ¥{rev} | {roi}% | ¥{per_hr} |
| X single | {min} min | ¥{rev} | {roi}% | ¥{per_hr} |
| note free | {min} min | ¥{rev} | {roi}% | ¥{per_hr} |
| note paid | {min} min | ¥{rev} | {roi}% | ¥{per_hr} |
| IG carousel | {min} min | ¥{rev} | {roi}% | ¥{per_hr} |
| IG reel | {min} min | ¥{rev} | {roi}% | ¥{per_hr} |
| Newsletter | {min} min | ¥{rev} | {roi}% | ¥{per_hr} |

Best revenue/hour: {type} (¥{amount}/hour)
Worst revenue/hour: {type} (¥{amount}/hour)

--- Time Allocation ---

Current allocation:
  note articles: {percentage}% of time
  X content: {percentage}%
  IG content: {percentage}%
  Other: {percentage}%

Optimal allocation (based on ROI):
  note paid: {percentage}% (+{change})
  X threads: {percentage}% (+{change})
  IG carousels: {percentage}% ({change})
  note free: {percentage}% ({change}) — reduce but don't eliminate

============================================
```

### Step 3: Optimization Recommendations

```
ROI Optimization Recommendations:

1. Increase: X threads (+{minutes}/week)
   Reason: Highest ROI at ¥{per_hour}/hour
   Impact: +¥{estimated_monthly}/month

2. Maintain: note paid articles
   Reason: High absolute revenue, worth the time investment

3. Reduce: {low_roi_type} (-{minutes}/week)
   Reason: ¥{per_hour}/hour — below your threshold
   Redirect this time to: X threads

4. Experiment: IG Reels (data insufficient)
   Reason: Only {N} data points — need more to judge ROI
   Action: Create {N} more Reels and measure

Estimated impact of reallocation:
  Current monthly revenue: ¥{current}
  Projected after optimization: ¥{projected} (+{percentage}%)
```

## Integration with Other Skills

- **attribution-model**: Revenue attributed to calculate ROI
- **performance-log**: Performance data needed for indirect ROI
- **monetize-report**: Revenue data for direct ROI
- **batch-generator**: Allocate batch days by ROI priority
- **weekly-report**: ROI summary included in report
- **advisor**: Recommends time allocation based on ROI

## Quality Gate

- [ ] Time data is based on user input (not fabricated)
- [ ] Revenue includes both direct and attributed revenue
- [ ] Free content ROI acknowledges long-term trust building
- [ ] Recommendations don't eliminate essential content types
- [ ] ROI calculation formula is transparent
