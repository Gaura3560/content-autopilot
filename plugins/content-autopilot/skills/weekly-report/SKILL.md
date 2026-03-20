---
name: weekly-report
description: Automated weekly performance summary — compiles content output, funnel balance, revenue progress, algorithm changes, upcoming events, and next-week recommendations into a single report. Save to Obsidian or display in terminal.
---

# Weekly Report

One report to rule them all — your complete content performance summary, every week.

## When to Activate

- User says `/weekly-report` or `/report`
- User asks "how did this week go?"
- User asks "give me a weekly summary"
- Can be scheduled as a recurring task

## Prerequisites

- `~/.content-autopilot/content-history.json` (content data)
- `~/.content-autopilot/profile.json` (context)
- Optional: monetize-data.json, best-times.json, algorithm-guide.json, active-series.json

## Commands

### `/report` — Generate this week's report
### `/report {date}` — Generate report for a specific week
### `/report save obsidian` — Save to Obsidian vault
### `/report compare` — Compare this week vs last week

## Workflow

### Step 1: Gather All Data

Read all available data files and compile metrics for the current week (Mon-Sun):

### Step 2: Generate Comprehensive Report

```
============================================
  Weekly Content Report
  Week of {start_date} — {end_date}
============================================

--- OUTPUT SUMMARY ---
Total content pieces: {count}
  note: {count} ({free}/{paid})
  X: {count} ({threads}/{singles})
  Instagram: {count} ({posts}/{carousels})
  Voice: {count}
  Newsletter: {count}
Total characters written: {sum}
Consistency: {days_posted}/{7} days ({percentage}%)

--- FUNNEL BALANCE ---
TOFU: {count} ({percentage}%) target: 50%  {on_track/adjust}
MOFU: {count} ({percentage}%) target: 30%  {on_track/adjust}
BOFU: {count} ({percentage}%) target: 20%  {on_track/adjust}
Balance health: {Good / Needs adjustment}
Trend: {improving / stable / declining} vs last week

--- CONTENT PILLARS ---
{Pillar 1}: {count} posts
{Pillar 2}: {count} posts
{Pillar 3}: {count} posts
Coverage: {all_covered / missing: pillar_name}

--- TITLE & HOOK PERFORMANCE ---
Title logics used: {list with counts}
A/B tests resolved: {count}/{total}
Best performing logic: {logic} ({win_rate}%)
Hook types used: {distribution}

--- SERIES PROGRESS ---
{If active series}:
  "{series_title}": Part {current}/{total} ({percentage}%)
  On schedule: {yes/no}
  Next part: {date} — "{part_title}"

--- MONETIZATION ---
{If monetize-data.json exists}:
  Revenue this week: ¥{amount}
  Monthly goal progress: ¥{current}/¥{goal} ({percentage}%)
  Paid article sales: {count}
  Membership: {subscribers} (+{new}/-{churn})
  Best converting content: "{title}"

--- ENGAGEMENT ---
Stories used from story-bank: {count}
Swipe file entries added: {count}
Hooks from hook-library used: {count}

--- ALGORITHM NOTES ---
{If algorithm-guide.json is recent}:
  Key algorithm tips applied: {list}
  Algorithm data freshness: {days} days old
  {If >30 days}: Run /algorithm to refresh

--- COMPETITOR LANDSCAPE ---
{If competitor-analysis.json exists}:
  Last competitor scan: {date}
  Open opportunities: {count}
  {If >14 days}: Run /competitor-scout to refresh

--- HIGHLIGHTS & WINS ---
1. {notable achievement this week}
2. {milestone reached}
3. {pattern discovered}

============================================

--- NEXT WEEK RECOMMENDATIONS ---

Priority 1: {most impactful action}
  Why: {data-driven reason}
  Action: {specific command to run}

Priority 2: {second action}
  Why: {reason}
  Action: {command}

Priority 3: {third action}
  Why: {reason}
  Action: {command}

Suggested topics for next week:
  Mon: {topic} ({stage}, {platform})
  Wed: {topic} ({stage}, {platform})
  Fri: {topic} ({stage}, {platform})

Run /batch 7 to generate next week's content now.

============================================
```

### Step 3: Week-over-Week Comparison (`/report compare`)

```
Week-over-Week Comparison:
  This week vs Last week

  Output: {this_week} vs {last_week} ({change}%)
  Consistency: {this}% vs {last}% ({change})
  TOFU balance: {this}% vs {last}%
  Revenue: ¥{this} vs ¥{last} ({change}%)
  New stories added: {this} vs {last}

  Trend: {improving / stable / declining}
  Momentum: {building / maintained / losing}
```

### Step 4: Save Report

**Terminal display:** Default — show in terminal.

**Obsidian save (`/report save obsidian`):**
```
Save location: {obsidian_vault_path}/Content Reports/weekly-report-{date}.md
```

**File save:**
```
~/Desktop/content-autopilot-output/reports/weekly-report-{date}.md
```

## Integration with Other Skills

- **content-analytics**: Weekly report is a superset of analytics data
- **monetize-report**: Revenue section pulls from monetize data
- **batch-generator**: Next-week recommendations feed into batch planning
- **seasonal-calendar**: Upcoming events mentioned in recommendations
- **content-dna**: DNA insights inform the recommendations

## Quality Gate

- [ ] All metrics calculated from actual data (not estimated)
- [ ] Week boundaries are correct (Mon-Sun)
- [ ] Recommendations are specific and actionable
- [ ] Week-over-week comparison uses matching periods
- [ ] Report is concise enough to read in 2-3 minutes
- [ ] Missing data sources handled gracefully (not errors)
