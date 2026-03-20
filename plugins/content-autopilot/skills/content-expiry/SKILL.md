---
name: content-expiry
description: Content shelf-life management — set expiry dates on time-sensitive content, auto-remind when data needs updating, and flag stale content before it damages credibility. Proactive content maintenance instead of reactive discovery.
---

# Content Expiry Manager

Don't let outdated content damage your credibility — manage shelf life proactively.

## When to Activate

- User says `/expiry` or `/content-expiry`
- User says `/expiry set {file} {days}`
- User asks "which content is getting stale?"
- Auto-suggested when content contains dated information

## Prerequisites

- `~/.content-autopilot/content-history.json`

## Data Extension: content-history.json

Each entry gets an `expiry` field:

```json
{
  "expiry": {
    "review_date": "2026-06-20",
    "expiry_type": "data_dependent",
    "stale_indicators": ["contains 2026 Q1 data", "tool pricing mentioned"],
    "auto_detected": true,
    "status": "active"
  }
}
```

## Expiry Types

| Type | Default Review | Trigger | Example |
|------|---------------|---------|---------|
| data_dependent | 90 days | Contains statistics/numbers | "Market size is $210B" |
| tool_review | 60 days | Mentions specific tools/pricing | "Tool X costs $29/month" |
| trend_piece | 30 days | About current trends | "The latest AI trend is..." |
| evergreen | 180 days | Timeless advice | "5 principles of good writing" |
| event_based | Event date + 7 days | Tied to specific event | "Before the conference..." |
| regulatory | 30 days | Legal/compliance content | "Current ステマ規制 requires..." |

## Commands

### `/expiry` — Show all content approaching or past expiry
### `/expiry set {file} {days}` — Set custom expiry for a file
### `/expiry scan` — Auto-detect expiry dates for all content
### `/expiry dashboard` — Full expiry management dashboard

## Workflow

### Step 1: Auto-Detection (`/expiry scan`)

Scan content-history for expiry indicators:

```
Expiry Auto-Detection Results:
============================================

Scanned: {N} articles

Auto-detected expiry dates:

1. "{title}" ({date})
   Type: data_dependent
   Contains: "AI market size: $210B (2026 Q1)"
   Review by: {date + 90 days}
   Status: {days} days until review

2. "{title}" ({date})
   Type: tool_review
   Contains: "ChatGPT costs $20/month"
   Review by: {date + 60 days}
   Status: {days} days until review — PRICE MAY HAVE CHANGED

3. "{title}" ({date})
   Type: trend_piece
   Contains: "The latest trend in..."
   Review by: {date + 30 days}
   Status: EXPIRED — {days} days overdue!

Auto-detected: {count} expiry dates set
Manual review needed: {count} articles couldn't be auto-classified

============================================
```

### Step 2: Expiry Dashboard (`/expiry dashboard`)

```
============================================
  Content Expiry Dashboard
============================================

EXPIRED (needs immediate attention):
  1. "{title}" ({date}) — expired {N} days ago
     Reason: {expiry_type}
     Action: /refresh or unpublish
  2. "{title}" ({date}) — expired {N} days ago

EXPIRING THIS WEEK:
  3. "{title}" — expires in {N} days
     Stale indicators: {list}
     Action: Schedule /refresh

EXPIRING THIS MONTH:
  4. "{title}" — expires in {N} days
  5. "{title}" — expires in {N} days

HEALTHY (not expiring soon):
  {count} articles with {avg} days until review

--- Summary ---
  Expired: {count} (ACTION NEEDED)
  Expiring soon: {count} (plan refresh)
  Healthy: {count}
  No expiry set: {count} (run /expiry scan)

============================================
```

### Step 3: Auto-Refresh Integration

When content expires:
```
Content expired: "{title}"

Recommended actions:
1. /refresh {file} — Update with current data
2. /unpublish — If content is no longer relevant
3. /expiry extend {file} 30 — Extend if still current after checking

The refresh skill will:
  - Search for updated data
  - Replace stale statistics
  - Verify tool pricing
  - Update trend references
  - Vault the old version automatically
```

## Integration with Other Skills

- **content-refresh**: Expiry triggers refresh workflow
- **content-vault**: Old versions backed up before refresh
- **fact-checker**: Re-verify expired data points
- **weekly-report**: Expiry warnings in weekly summary
- **content-calendar**: Schedule refresh tasks for expiring content
- **compliance-checker**: Regulatory content has short expiry

## Quality Gate

- [ ] Auto-detection catches most time-sensitive content
- [ ] Expiry dates are reasonable for each content type
- [ ] Dashboard clearly shows priority order
- [ ] Refresh workflow is integrated (not just a warning)
- [ ] Evergreen content has longer but still existing expiry
