---
name: monetize-report
description: Monetization tracking and funnel conversion analytics — record note paid article sales, membership subscribers, and revenue. Correlate TOFU content with paid conversions to identify which free content drives the most revenue. Manual input + analysis.
---

# Monetization Report

Track your content revenue and find out which free content drives the most paid conversions.

## When to Activate

- User says `/monetize-report` or `/monetize`
- User says `/monetize add` to record new data
- User asks "how much am I earning from content?"
- User asks "which content drives the most sales?"

## Prerequisites

- `~/.content-autopilot/profile.json` must exist with `funnel.enabled = true`
- `~/.content-autopilot/content-history.json` (for correlating content with conversions)
- `~/.content-autopilot/monetize-data.json` (created on first use)

## Commands

### `/monetize` — Show monetization dashboard
### `/monetize add` — Record new revenue data
### `/monetize add sale {date} {amount}` — Quick add a sale
### `/monetize add member {count}` — Update membership count
### `/monetize funnel` — Show funnel conversion analysis
### `/monetize goal {amount}` — Set monthly revenue goal

## Data: monetize-data.json

Location: `~/.content-autopilot/monetize-data.json`

```json
{
  "version": "1.0",
  "currency": "JPY",
  "monthly_goal": 50000,
  "entries": [
    {
      "date": "2026-03-20",
      "type": "paid_article",
      "article_title": "Complete AI Automation Guide",
      "amount": 500,
      "quantity": 3,
      "related_content_id": "2026-03-18-001",
      "notes": "Spike after X thread went viral"
    },
    {
      "date": "2026-03-20",
      "type": "membership",
      "subscribers": 15,
      "mrr": 7500,
      "churn": 1,
      "new": 3
    }
  ],
  "milestones": [
    {
      "date": "2026-03-15",
      "milestone": "First paid article sale",
      "amount": 500
    }
  ]
}
```

## Workflow

### Record Data (`/monetize add`)

Interactive data entry:
```
What would you like to record?

1. Paid article sale
2. Membership update
3. External product/service sale
4. Lead magnet download count

Select (1-4):
```

**For paid article sale:**
```
Article title: {input}
Sale price: {input} yen
Number of sales: {input}
Date: {input or today}
Related free content that drove the sale (optional): {select from recent history}
Notes (optional): {input}
```

**For membership update:**
```
Current subscriber count: {input}
Monthly recurring revenue: {input} yen
New subscribers this period: {input}
Churned subscribers this period: {input}
```

### Dashboard (`/monetize`)

```
============================================
  Monetization Dashboard
  Period: {month} {year}
============================================

--- Revenue Summary ---
Monthly goal: ¥{goal}
Current revenue: ¥{total} ({percentage}% of goal)
{progress_bar} ████████░░░░░░ {percentage}%

Breakdown:
  Paid articles: ¥{amount} ({count} sales)
  Membership:    ¥{mrr}/month ({subscribers} subscribers)
  Other:         ¥{amount}

--- Trends ---
Last 3 months:
  {month-2}: ¥{amount}
  {month-1}: ¥{amount}
  {month}:   ¥{amount} ({change}% {up/down})

MRR growth: {current_mrr} (net +{new} / -{churn} subscribers)

--- Top Performing Paid Content ---
1. "{article_title}" — ¥{revenue} ({count} sales)
2. "{article_title}" — ¥{revenue} ({count} sales)
3. "{article_title}" — ¥{revenue} ({count} sales)

--- Milestones ---
{emoji} {date}: {milestone description}

============================================
```

### Funnel Conversion Analysis (`/monetize funnel`)

Correlate TOFU content with eventual paid conversions:

```
============================================
  Funnel Conversion Analysis
============================================

--- TOFU → MOFU Conversion ---
X posts that drove note traffic:
  1. "{x_title}" ({date}) → {estimated_clicks} clicks to note
  2. "{x_title}" ({date}) → {estimated_clicks} clicks

Instagram posts that drove note traffic:
  1. "{ig_title}" ({date}) → {estimated_views} profile visits

--- MOFU → BOFU Conversion ---
Free articles that preceded paid sales:
  1. "{free_title}" ({date}) → {N} paid sales within 7 days
  2. "{free_title}" ({date}) → {N} paid sales within 7 days

--- Attribution Insights ---
Best performing funnel path:
  X thread → note free article → note paid article
  Conversion rate: ~{rate}% (estimated)

Content that drives the most revenue:
  Topic: "{topic}" — ¥{total_revenue} across {N} pieces
  Title logic: {logic combo} has highest conversion

--- Recommendations ---
1. Produce more TOFU content on "{high_converting_topic}"
   — this topic has the best TOFU→BOFU conversion
2. Your BOFU content on {day} performs best
   — schedule more paid articles on {day}
3. Lead magnet downloads: {count} this month
   — {conversion_to_paid}% converted to paid
============================================
```

**Note on attribution:**
Since direct tracking isn't possible (no analytics API), attribution is estimated based on:
- Timing: Sales that occur within 7 days of related free content
- Topic: Matching topics between free content and paid content
- User-provided `related_content_id` when recording sales

### Goal Tracking (`/monetize goal`)

```
/monetize goal 100000

Monthly revenue goal set: ¥100,000

To reach this goal, you need approximately:
  Option A: 200 paid article sales at ¥500 each
  Option B: 67 membership subscribers at ¥1,500/month
  Option C: Mix — 100 article sales (¥50K) + 34 members (¥51K)

Based on your current conversion rate:
  You need ~{N} TOFU posts/week to generate enough traffic
  Current pace: {current_rate}/week → projected: ¥{projected}/month

{above/below} target by ¥{difference}
```

## Integration with Other Skills

- **content-analytics**: Includes revenue metrics in dashboard
- **daily-autopilot**: Shows monthly revenue progress in summary
- **funnel-designer**: Uses conversion data to optimize funnel recommendations
- **batch-generator**: Prioritizes topics with higher conversion potential

## Backward Compatibility

When `funnel.enabled = false`:
- Basic revenue recording still works
- Funnel conversion analysis is unavailable (requires funnel tracking)
- Show message: "Enable funnel mode for conversion analysis"

## Quality Gate

Before delivering:
- [ ] Revenue calculations are accurate
- [ ] Percentages sum correctly
- [ ] Attribution logic is clearly estimated (not presented as exact)
- [ ] Recommendations are actionable and based on data
- [ ] monetize-data.json is saved correctly
- [ ] Currency is consistent throughout (JPY default)
