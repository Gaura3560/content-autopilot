---
name: best-time
description: Optimal posting time analysis — research platform-specific engagement patterns for the user's niche and audience, recommend best times to post on note, X, and Instagram. Integrates with daily-autopilot to display posting time suggestions.
---

# Best Time to Post

Find the optimal posting times for your niche and audience on each platform.

## When to Activate

- User says `/best-time`
- User asks "when should I post?"
- User asks "what's the best time to post on X/note/Instagram?"
- Automatically referenced in daily-autopilot output

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Workflow

### Step 1: Load Profile Context

Read `profile.json` and extract:
- `audience.age_range` — affects active hours
- `audience.occupation` — affects weekday patterns (office workers vs freelancers)
- `theme.main` — niche-specific patterns
- `platforms` — which platforms to analyze

### Step 2: Research Optimal Times

Use WebSearch to gather current data:

**Search queries per platform:**

**X (Twitter):**
```
"best time to post on X {year}" {niche}
"X engagement by hour" {audience_type}
"Twitter analytics best posting time Japan"
```

**note:**
```
"note 投稿 最適時間"
"note PV 時間帯"
"note アクセス ピーク"
```

**Instagram:**
```
"best time to post Instagram {year}" {niche}
"Instagram engagement by hour" {audience_type}
"Instagram 投稿時間 最適 日本"
```

### Step 3: Analyze and Personalize

Combine research data with audience profile:

**Audience-specific adjustments:**
| Audience Type | Peak Hours | Reasoning |
|--------------|-----------|-----------|
| Office workers | 7-8 AM, 12-1 PM, 7-9 PM | Commute, lunch, after work |
| Students | 8-9 AM, 3-5 PM, 9-11 PM | Before class, after school, night |
| Freelancers | 9-11 AM, 2-4 PM, 8-10 PM | Flexible schedule, work breaks |
| Business owners | 6-7 AM, 12 PM, 9-10 PM | Early morning, lunch, late evening |
| Parents | 9-10 AM, 1-2 PM, 9-11 PM | After drop-off, nap time, after bedtime |

**Day-of-week patterns:**
| Day | Engagement Level | Best For |
|-----|-----------------|----------|
| Monday | Medium | Professional content, MOFU |
| Tuesday | High | Best overall engagement |
| Wednesday | High | Mid-week boost |
| Thursday | High | Build-up to weekend |
| Friday | Medium-Low | Lighter content, TOFU |
| Saturday | Variable | Personal/lifestyle content |
| Sunday | Medium | Planning content, BOFU |

### Step 4: Display Recommendations

```
============================================
  Best Posting Times for Your Niche
  Theme: {theme.main} | Audience: {audience_type}
============================================

--- X (Twitter) ---
Best times:
  1st: {time} ({weekdays}) — {reason}
  2nd: {time} ({weekdays}) — {reason}
  3rd: {time} ({weekdays}) — {reason}
Avoid: {time range} — lowest engagement
Best day: {day} | Worst day: {day}
Thread timing: Post tweet 1 at {time}, space 5-10 min between tweets

--- note ---
Best times:
  1st: {time} ({weekdays}) — {reason}
  2nd: {time} ({weekdays}) — {reason}
Avoid: {time range} — low traffic
Best day: {day} (highest PV)
Note: Morning posts tend to get picked up by note's recommendation algorithm

--- Instagram ---
Best times:
  1st: {time} ({weekdays}) — {reason}
  2nd: {time} ({weekdays}) — {reason}
  3rd: {time} ({weekdays}) — {reason}
Avoid: {time range}
Best day: {day} | Worst day: {day}
Reels: Post 1-2 hours before peak for algorithm pickup
Stories: {time range} for maximum views

============================================

Tip: These are starting recommendations based on your niche and
audience profile. Track your own metrics over 2-4 weeks and adjust.

============================================
```

### Step 5: Save Recommendations

Save to `~/.content-autopilot/best-times.json`:
```json
{
  "version": "1.0",
  "analyzed_at": "2026-03-20",
  "audience_type": "office_workers",
  "platforms": {
    "x": {
      "best_times": [
        {"time": "07:30", "days": ["mon", "tue", "wed", "thu", "fri"], "score": 95},
        {"time": "12:00", "days": ["mon", "tue", "wed", "thu", "fri"], "score": 90},
        {"time": "20:00", "days": ["mon", "tue", "wed", "thu"], "score": 85}
      ],
      "best_day": "tuesday",
      "worst_day": "sunday"
    },
    "note": {
      "best_times": [
        {"time": "07:00", "days": ["mon", "tue", "wed", "thu", "fri"], "score": 90},
        {"time": "12:00", "days": ["sat", "sun"], "score": 85}
      ],
      "best_day": "tuesday",
      "worst_day": "saturday"
    },
    "instagram": {
      "best_times": [
        {"time": "19:00", "days": ["mon", "tue", "wed", "thu", "fri"], "score": 95},
        {"time": "12:00", "days": ["mon", "tue", "wed", "thu", "fri"], "score": 80}
      ],
      "best_day": "wednesday",
      "worst_day": "monday"
    }
  }
}
```

## Integration with Other Skills

- **daily-autopilot**: Step 6 output summary includes "Best time to post: {time}" for each platform
- **batch-generator**: Posting schedule uses best-times.json for scheduling recommendations
- **content-analytics**: Can correlate posting time with engagement (future enhancement)

## Backward Compatibility

No funnel dependency — works identically regardless of `funnel.enabled` setting.

## Quality Gate

Before delivering:
- [ ] Recommendations are based on actual research data (not generic advice)
- [ ] Personalized to user's audience type and niche
- [ ] All active platforms are covered
- [ ] Times are in the user's local timezone
- [ ] Sources are cited for key claims
- [ ] best-times.json is saved for other skills to reference
