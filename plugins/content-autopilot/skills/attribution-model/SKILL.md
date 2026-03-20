---
name: attribution-model
description: Multi-touch content attribution — trace which TOFU content ultimately led to which paid conversions. Connect the dots between free content, follower growth, and revenue. Answer the question "which of my free content is actually making money?"
---

# Attribution Model

Which free content is actually making you money? Connect the dots across your funnel.

## When to Activate

- User says `/attribution` or `/attribution analyze`
- User asks "which content drives the most revenue?"
- User asks "what's my best converting content?"
- User wants to understand content → revenue pathways

## Prerequisites

- `~/.content-autopilot/content-history.json` with performance data
- `~/.content-autopilot/monetize-data.json` with revenue data

## Commands

### `/attribution` — Full attribution analysis
### `/attribution {content_id}` — Attribution for specific content
### `/attribution paths` — Show most common conversion paths
### `/attribution roi-rank` — Rank all content by attributed revenue

## Attribution Models

| Model | Logic | Best For |
|-------|-------|----------|
| Last-touch | Credit to the last content before purchase | Simple, conservative |
| First-touch | Credit to the content that brought them in | Understanding acquisition |
| Linear | Equal credit across all touchpoints | Fair distribution |
| Time-decay | More credit to recent touchpoints | Recency-aware |
| Position-based | 40% first, 20% middle, 40% last | Balanced understanding |

## Workflow

### Step 1: Build Conversion Paths

From performance-log and monetize-data, reconstruct likely paths:

```
Conversion path analysis:
  Purchase: "{paid_article}" on {date} (¥{amount})

  Likely path (reconstructed from timing + topics):
  Day 1: X thread "{title}" → {N} link clicks to note
  Day 3: note free article "{title}" → reader followed
  Day 7: note free article "{title}" → read + liked
  Day 10: Purchased paid article → ¥{amount}

  Attribution (position-based model):
    X thread: 40% credit (¥{amount}) — first touch
    Free article 1: 10% credit (¥{amount}) — middle
    Free article 2: 10% credit (¥{amount}) — middle
    Paid article page: 40% credit (¥{amount}) — last touch
```

### Step 2: Attribution Dashboard

```
============================================
  Content Attribution Report
  Period: {date_range}
  Model: Position-based (recommended)
============================================

--- Top Revenue-Generating Content ---
(ranked by attributed revenue across all conversions)

1. "{title}" (X thread, {date}) — ¥{attributed_revenue}
   Role: First touch in {N} conversion paths
   Why: This thread drives the most note traffic

2. "{title}" (note free, {date}) — ¥{attributed_revenue}
   Role: Trust builder in {N} paths
   Why: Readers who read this are {X}x more likely to purchase

3. "{title}" (note free, {date}) — ¥{attributed_revenue}
   Role: Last free touch before purchase in {N} paths

--- Most Common Conversion Paths ---

Path 1 ({N} conversions):
  X thread → note free → note free → note paid
  Avg days: {N} days from first touch to purchase

Path 2 ({N} conversions):
  IG carousel → note free → note paid
  Avg days: {N} days

Path 3 ({N} conversions):
  X single → note free (lead magnet) → note paid
  Avg days: {N} days

--- Revenue by Content Type ---

X threads: ¥{total} attributed ({percentage}%)
X singles: ¥{total} ({percentage}%)
IG carousels: ¥{total} ({percentage}%)
IG reels: ¥{total} ({percentage}%)
note free: ¥{total} ({percentage}%)
Newsletters: ¥{total} ({percentage}%)

--- Funnel Efficiency ---

TOFU → MOFU conversion: {rate}%
MOFU → BOFU conversion: {rate}%
Overall funnel efficiency: {rate}%

Best TOFU for conversion: "{title}" ({rate}% click-through)
Best MOFU for conversion: "{title}" ({rate}% purchase rate)

============================================

Recommendation:
  Create MORE content like "{top_performing_title}" — it has
  the highest revenue attribution.

  Your best conversion path takes {N} days. Plan your funnel
  accordingly with /series {N} or /drip to match this timeline.

============================================
```

## Integration with Other Skills

- **performance-log**: Raw data for attribution
- **monetize-report**: Revenue data to attribute
- **audience-journey**: Journey map + attribution = complete picture
- **content-roi**: Attribution feeds into per-content ROI
- **batch-generator**: Prioritize content types with best attribution
- **weekly-report**: Attribution insights in weekly summary

## Quality Gate

- [ ] Attribution is clearly labeled as "estimated" (not tracked)
- [ ] Multiple models available (users can compare)
- [ ] Conversion paths reconstructed from actual data
- [ ] Revenue attribution sums correctly
- [ ] Recommendations based on attribution patterns
- [ ] Limitations clearly stated (estimation, not tracking)
