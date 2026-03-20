---
name: performance-log
description: Record actual post-publish performance data — likes, retweets, PV, saves, comments, shares, and revenue per content piece. The missing feedback loop that makes every other analytics skill accurate instead of estimated. Without this, all predictions are guesses.
---

# Performance Log

Close the feedback loop — record real results so every future prediction is based on ACTUAL data.

## When to Activate

- User says `/perf-log` or `/perf-log {date}`
- User says `/perf add {platform} {metric} {value}`
- User asks "log today's performance"
- Auto-suggested 24-48 hours after publishing

## Prerequisites

- `~/.content-autopilot/content-history.json` (to match entries)

## Data Extension: content-history.json

Each entry gets a `performance` field:

```json
{
  "id": "2026-03-20-001",
  "performance": {
    "logged_at": "2026-03-22",
    "x": {
      "impressions": 5200,
      "likes": 87,
      "retweets": 23,
      "replies": 12,
      "bookmarks": 45,
      "link_clicks": 34,
      "profile_visits": 18
    },
    "note": {
      "pv": 320,
      "likes": 45,
      "comments": 8,
      "shares": 5,
      "paid_purchases": 3,
      "revenue": 1500
    },
    "instagram": {
      "reach": 2100,
      "likes": 156,
      "saves": 89,
      "shares": 12,
      "comments": 23,
      "profile_visits": 45
    },
    "engagement_rate": 4.2,
    "funnel_conversions": {
      "x_to_note": 34,
      "ig_to_note": 45,
      "free_to_paid": 3
    }
  }
}
```

## Commands

### `/perf-log` — Interactive performance logging for recent content
### `/perf-log {date}` — Log performance for a specific date's content
### `/perf add x likes 87` — Quick add a single metric
### `/perf-log batch` — Log performance for the whole week at once
### `/perf summary` — Show performance trends

## Workflow

### Step 1: Select Content to Log

```
Recent content without performance data:

1. "{title}" ({date}) — X thread + note + IG
   Published: {N} hours ago — ready to log

2. "{title}" ({date}) — X single + IG carousel
   Published: {N} days ago — ready to log

3. "{title}" ({date}) — note article
   Published: {N} days ago — ready to log

Log which? (1/2/3/all)
```

### Step 2: Input Performance Data

```
Logging performance for: "{title}" ({date})

--- X Performance ---
Impressions: ___
Likes: ___
Retweets: ___
Replies: ___
Bookmarks: ___
Link clicks (to note): ___
(Enter numbers, or "skip" for unavailable metrics)

--- note Performance ---
Page views: ___
Likes (suki): ___
Comments: ___
Paid purchases (if paid article): ___
Revenue: ¥___

--- Instagram Performance ---
Reach: ___
Likes: ___
Saves: ___
Shares: ___
Comments: ___
Profile visits: ___

(type "done" when finished)
```

### Step 3: Auto-Calculate Derived Metrics

```
Performance logged! Derived metrics:

Engagement rate: {calculated}%
  X: {rate}% (likes+RT+replies / impressions)
  IG: {rate}% (likes+saves+comments / reach)
  note: {rate}% (likes+comments / PV)

Funnel conversion:
  X → note: {link_clicks} clicks ({conversion}% of impressions)
  IG → note: {profile_visits} visits
  note free → paid: {purchases} ({conversion}% of PV)

Compared to your average:
  X engagement: {above/below} avg ({avg}%)
  note PV: {above/below} avg ({avg})
  IG saves: {above/below} avg ({avg})

Performance score: {score}/100 (relative to your own history)
```

### Step 4: Performance Summary (`/perf summary`)

```
============================================
  Performance Summary — Last 30 Days
============================================

Best performing content:
  1. "{title}" ({date}) — engagement: {rate}%
     Why it worked: {auto-analysis based on content-dna}
  2. "{title}" ({date}) — engagement: {rate}%
  3. "{title}" ({date}) — engagement: {rate}%

Worst performing:
  1. "{title}" ({date}) — engagement: {rate}%
     Possible reason: {analysis}

Trends:
  X avg engagement: {this_month}% vs {last_month}% ({change})
  note avg PV: {this_month} vs {last_month} ({change})
  IG avg saves: {this_month} vs {last_month} ({change})

Correlations found:
  - {hook_type} hooks: {X}% higher engagement than average
  - {posting_time} posts: {X}% more impressions
  - {title_logic}: {X}% higher click-through
  - {topic}: consistently your best performing topic

============================================
```

## Integration with Other Skills (THIS IS THE KEY)

Performance data flows into EVERY analytics skill:
- **content-dna**: Patterns based on REAL results, not guesses
- **engagement-predictor**: Calibrates predictions against actual outcomes
- **content-grader**: Grade calibrated to YOUR actual performance
- **weekly-report**: Real numbers instead of estimates
- **monetize-report**: Actual revenue per content piece
- **algorithm-guide**: Verify which algorithm tips actually helped
- **ab-test-runner**: A/B tests based on actual performance data
- **post-mortem**: Detailed analysis requires real metrics
- **batch-generator**: Prioritize content types with proven performance

## Quality Gate

- [ ] Performance data saved to correct content-history entry
- [ ] Derived metrics calculated accurately
- [ ] Comparison against averages uses actual historical data
- [ ] Missing metrics handled gracefully (not zero, just null)
- [ ] Performance logging prompted at appropriate intervals (24-48h)
