---
name: annual-review
description: Comprehensive annual content review — total output, revenue, growth, top performers, lessons learned, and next-year strategy. The year-end report that shows how far you've come.
---

# Annual Review

365 days of content creation — distilled into one report.

## Commands

### `/annual-review` — Generate this year's review
### `/annual-review {year}` — Specific year
### `/annual-review compare` — This year vs last year

## Output

```
============================================
  Annual Content Review — {year}
============================================

OUTPUT:
  Total content: {N} pieces across {N} platforms
  Total characters: {N} (~{pages} book pages equivalent)
  Consistency: {N}/{365} days ({percentage}%)
  Best month: {month} ({N} pieces)

GROWTH:
  Followers: {start} → {end} (+{growth})
  note subscribers: {start} → {end}
  Email list: {start} → {end}

REVENUE:
  Total: ¥{amount}
  Paid articles: ¥{amount} ({N} sales)
  Membership: ¥{amount}
  Best month: {month} (¥{amount})

TOP CONTENT:
  1. "{title}" — {engagement metrics}
  2. "{title}" — {metrics}
  3. "{title}" — {metrics}

LESSONS:
  1. {biggest lesson from post-mortem data}
  2. {second lesson}
  3. {third lesson}

NEXT YEAR STRATEGY:
  Focus: {recommendation based on DNA + trends}
  Goal: {specific targets}
  Priority skills: {top 5 skills to use more}

============================================
```

Integrates with: all data files, content-dna, monetize-data, performance-log.
