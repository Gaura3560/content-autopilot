---
name: content-analytics
description: Content performance analytics dashboard — tracks posting frequency, funnel balance trends, title logic usage rates, content pillar coverage, and provides actionable recommendations. Manages content-history.json as the central data store for all content autopilot features.
---

# Content Analytics

Analyze your content history and get actionable insights to improve your content strategy.

## When to Activate

- User says `/analytics` or `/content-analytics`
- User asks "how is my content performing?"
- User asks "what should I improve?"
- User wants to see posting patterns, funnel balance, or title analysis

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- `~/.content-autopilot/content-history.json` should exist (created automatically by daily-autopilot)
- If content-history.json is missing, create an empty one and inform the user

## Data Schema: content-history.json

Location: `~/.content-autopilot/content-history.json`

```json
{
  "version": "1.0",
  "entries": [
    {
      "id": "2026-03-20-001",
      "date": "2026-03-20",
      "topic": "AI automation for small businesses",
      "category": "trending",
      "funnel_stage": "TOFU",
      "platforms": {
        "note": {
          "title": "7 Days to Transform Your AI Workflow",
          "file": "note_2026-03-20.md",
          "type": "free",
          "char_count": 3200
        },
        "x": {
          "title": "AI Thread: 7 habits",
          "file": "x_2026-03-20.md",
          "format": "thread",
          "tweet_count": 5
        },
        "instagram": {
          "title": "AI Workflow Tips",
          "file": "instagram_2026-03-20.md",
          "hashtag_count": 30
        }
      },
      "title_logics_used": ["Numbers", "Simplicity"],
      "content_pillar": "AI Tools",
      "source_url": "https://example.com/article",
      "source": "original",
      "series_id": null,
      "ab_titles": {
        "chosen": "7 Days to Transform Your AI Workflow",
        "alternative": "Still doing it manually? The AI future of work",
        "winner": null
      }
    }
  ]
}
```

## Workflow

### Step 1: Load Data

Read both files:
1. `~/.content-autopilot/profile.json` — for theme, platforms, funnel settings
2. `~/.content-autopilot/content-history.json` — for content entries

If content-history.json doesn't exist:
```
Content history not found. Creating empty history file.
Run /daily-autopilot to start building your content history.
```
Create the file with `{"version": "1.0", "entries": []}` and exit.

If content-history.json has fewer than 3 entries:
```
Content history has only {N} entries. Analytics work best with 7+ entries.
Current data will be analyzed, but recommendations may be limited.
```

### Step 2: Calculate Metrics

Compute the following from content-history.json entries:

**2a. Posting Frequency**
```
Posting Frequency (last 30 days):
  Total posts: {count}
  Weekly average: {avg}/week
  Longest gap: {N} days ({date range})
  Current streak: {N} days
  Consistency score: {percentage}% (target: daily)
```

**2b. Funnel Balance Trend (if funnel enabled)**
```
Funnel Balance (last 30 days):
  TOFU: {count} ({percentage}%) — target: 50%
  MOFU: {count} ({percentage}%) — target: 30%
  BOFU: {count} ({percentage}%) — target: 20%

  Trend (last 7 vs previous 7):
    TOFU: {prev}% → {current}% ({arrow up/down})
    MOFU: {prev}% → {current}% ({arrow up/down})
    BOFU: {prev}% → {current}% ({arrow up/down})

  Balance health: {Good / Needs adjustment / Significantly off}
```

**2c. Title Logic Usage**
```
Title Logic Usage (all time):
  1. Numbers:     {count} ({percentage}%) ████████
  2. Simplicity:  {count} ({percentage}%) ██████
  3. Paradox:     {count} ({percentage}%) █████
  4. Enemy:       {count} ({percentage}%) ███
  5. Question:    {count} ({percentage}%) ██
  6. Ideal Self:  {count} ({percentage}%) █
  7. Secret:      {count} ({percentage}%) █
  8. Coined Term: {count} ({percentage}%)
  9. Unexpected:  {count} ({percentage}%)

  Most used combination: {logic1} + {logic2} ({count} times)
  Never used: {list of unused logics}
  Recommendation: Try {unused logic} — it works well for {genre match}
```

**2d. Content Pillar Coverage**
```
Content Pillar Coverage (last 30 days):
  {Pillar 1}: {count} posts ({percentage}%)
  {Pillar 2}: {count} posts ({percentage}%)
  {Pillar 3}: {count} posts ({percentage}%)
  Uncategorized: {count} posts

  Gap: {Pillar name} has no content in the last 14 days
```

**2e. Category Distribution**
```
Content Categories:
  Trending:  {count} ({percentage}%)
  Overseas:  {count} ({percentage}%)
  Evergreen: {count} ({percentage}%)
  Repurposed: {count} ({percentage}%)
```

**2f. Platform Distribution**
```
Platform Activity:
  note:      {count} posts ({free count} free / {paid count} paid)
  X:         {count} posts ({single count} single / {thread count} threads)
  Instagram: {count} posts (avg {N} hashtags)
```

### Step 3: A/B Title Analysis (if data exists)

If entries have `ab_titles.winner` data:
```
A/B Title Results:
  Total A/B tests: {count}
  Resolved: {count} (A: {a_wins} / B: {b_wins})
  Pending: {count}

  Winning logic patterns:
    {Logic combo 1}: {win_rate}% win rate ({sample_size} tests)
    {Logic combo 2}: {win_rate}% win rate ({sample_size} tests)

  Untested combinations: {list}
```

### Step 4: Generate Recommendations

Based on all metrics, provide 3-5 actionable recommendations:

```
Recommended Actions:

1. [Funnel] BOFU content is at {X}% (target: 20%). Create a paid note
   article this week on {suggested pillar}.

2. [Title] You've never used "Coined Term" logic. Try it for your next
   {theme} article — it works especially well for AI/Tech content.

3. [Consistency] You had a {N}-day gap last week. Consider using
   /series to plan a 7-day content series for momentum.

4. [Pillar] "{Pillar name}" hasn't been covered in 14 days. Today's
   topic recommendation: {specific idea in that pillar}.

5. [Platform] Instagram posts are {below/above} average. Consider
   {repurposing note content with /repurpose note→instagram}.
```

### Step 5: Display Dashboard

Present all metrics in a single dashboard view:

```
============================================
  Content Analytics Dashboard
  Period: {start_date} — {end_date}
============================================

Posting: {total} posts | {avg}/week | {streak}-day streak

Funnel Balance:
  TOFU ████████████░░░░░░░░ 55% (target: 50%)
  MOFU ██████░░░░░░░░░░░░░░ 28% (target: 30%)
  BOFU ███░░░░░░░░░░░░░░░░░ 17% (target: 20%)

Top Title Logics: Numbers (40%), Simplicity (30%), Paradox (20%)
Unused Logics: Coined Term, Unexpected Combination

Pillar Coverage: {Pillar1} 45% | {Pillar2} 35% | {Pillar3} 20%

A/B Tests: {resolved}/{total} resolved | Best combo: {logic1}+{logic2}

--- Recommendations ---
1. {top recommendation}
2. {second recommendation}
3. {third recommendation}

============================================
```

## Helper: Record Content Entry

Other skills (daily-autopilot, repurpose, series-designer) call this function to add entries:

**Entry creation template:**
```json
{
  "id": "{date}-{sequence_number}",
  "date": "{YYYY-MM-DD}",
  "topic": "{topic description}",
  "category": "{trending|overseas|evergreen|competitor_gap}",
  "funnel_stage": "{TOFU|MOFU|BOFU|null}",
  "platforms": {},
  "title_logics_used": [],
  "content_pillar": "{pillar name or null}",
  "source_url": "{url or null}",
  "source": "{original|repurpose}",
  "series_id": "{series_id or null}",
  "ab_titles": {
    "chosen": "{selected title}",
    "alternative": "{runner-up title}",
    "winner": null
  }
}
```

**Sequence number logic:**
- Read existing entries for the same date
- Increment: `{date}-001`, `{date}-002`, etc.

## Commands

### `/analytics` — Full dashboard (default)
Display the complete analytics dashboard as described above.

### `/title-winner {date} {A|B}` — Record A/B test winner
```
# Mark which title performed better
/title-winner 2026-03-20 A    → chosen title wins
/title-winner 2026-03-20 B    → alternative title wins
```

Update the entry's `ab_titles.winner` field to `"chosen"` or `"alternative"`.

### `/title-report` — A/B title analysis
Display:
- Logic-by-logic win rates
- Strongest logic combinations
- Untested combinations
- Recommendations for next A/B test

## Backward Compatibility

When `funnel.enabled = false`:
- Skip funnel balance metrics
- Skip funnel-related recommendations
- All other metrics (posting frequency, title logic, pillar coverage) work normally

## Output

- Analytics dashboard displayed in terminal
- No files saved (read-only analysis)
- Recommendations based on data patterns

## Quality Gate

Before displaying:
- [ ] All metrics calculated from actual data (no fabricated numbers)
- [ ] Percentages sum to ~100% where applicable
- [ ] Recommendations are specific and actionable
- [ ] Funnel metrics only shown when funnel.enabled = true
- [ ] Empty/insufficient data handled gracefully
- [ ] Date ranges are correct and clearly stated
