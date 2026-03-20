---
name: revenue-forecast
description: Predict next month's content revenue from current trends — extrapolate from performance-log and monetize-data to forecast paid article sales, membership growth, and total revenue. Turn reactive reporting into proactive planning.
---

# Revenue Forecast

Don't wait for month-end to know your numbers. Predict and plan ahead.

## When to Activate

- User says `/forecast` or `/revenue-forecast`
- User asks "how much will I make next month?"
- User wants to plan revenue-driven content strategy

## Commands

### `/forecast` — Next month revenue prediction
### `/forecast {months}` — Multi-month forecast
### `/forecast scenario` — Best/worst/likely scenarios

## Workflow

### Step 1: Analyze Trends

From monetize-data.json + performance-log:
```
Revenue Trend Analysis:
  Month -3: ¥{amount}
  Month -2: ¥{amount}
  Month -1: ¥{amount}
  This month (so far): ¥{amount}
  Growth rate: {percentage}%/month
```

### Step 2: Generate Forecast

```
============================================
  Revenue Forecast — {next_month}
============================================

Predicted revenue: ¥{amount}
Confidence interval: ¥{low} — ¥{high}

Breakdown:
  Paid articles: ¥{amount} ({count} sales × ¥{avg_price})
  Membership: ¥{mrr} ({subscribers} × ¥{price})
  Other: ¥{amount}

--- Scenario Analysis ---

Best case (everything goes right): ¥{best}
  Assumes: {conditions}

Likely case: ¥{likely}
  Assumes: current trends continue

Worst case (things slow down): ¥{worst}
  Assumes: {conditions}

--- To Hit Your Goal (¥{goal}) ---

Gap: ¥{difference}
Actions needed:
  Option A: {N} more paid article sales
  Option B: {N} new membership subscribers
  Option C: Launch {product} at ¥{price}

Content plan to close the gap:
  Week 1: {BOFU content suggestion}
  Week 2: {launch/promotion suggestion}
  Week 3-4: {nurture + convert suggestion}

============================================
```

## Quality Gate

- [ ] Forecast based on actual historical data (not fabricated)
- [ ] Confidence intervals provided (not just a single number)
- [ ] Scenarios are realistic
- [ ] Actions to hit goal are specific and actionable
- [ ] Revenue breakdown by source
