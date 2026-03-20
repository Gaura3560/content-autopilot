---
name: anomaly-alert
description: Detect unusual patterns in your content performance — sudden engagement spikes, traffic drops, follower surges, or viral moments. Alert you to both opportunities (ride the wave) and threats (diagnose the problem) before you discover them manually.
---

# Anomaly Alert

Something unusual just happened with your content. You need to know NOW.

## When to Activate

- User says `/anomaly` or `/anomaly check`
- Auto-triggered when performance-log data shows outliers
- User asks "anything unusual happening?"

## Commands

### `/anomaly check` — Scan for anomalies in recent data
### `/anomaly {date}` — Check specific date
### `/anomaly history` — Review past anomalies and outcomes

## Anomaly Types

| Type | Signal | Response |
|------|--------|----------|
| Viral spike | 5x+ normal engagement | Ride the wave — post more |
| Traffic surge | 3x+ normal PV | Find the source, amplify |
| Engagement drop | 50%+ decline | Diagnose — algorithm? content? timing? |
| Follower spike | Unusual follow rate | Identify trigger, replicate |
| Follower loss | Unusual unfollow rate | Assess — controversial post? |
| External mention | Someone big shared you | Thank, engage, amplify |

## Workflow

```
/anomaly check

============================================
  Anomaly Scan — Last 7 Days
============================================

ANOMALY DETECTED:

1. [OPPORTUNITY] Engagement spike on "{title}" ({date})
   Normal: {avg} likes | Actual: {actual} likes ({X}x normal)
   Probable cause: {analysis}
     - Shared by @{large_account} at {time}
     - Trending hashtag #{tag} included

   Recommended actions:
     a) Post follow-up thread within 2 hours: "{suggested_content}"
     b) Pin this post to your profile
     c) Reply to all comments (algorithm boost while hot)
     d) Create note article expanding on this topic

2. [CONCERN] PV drop on note articles (last 3 days)
   Normal: {avg} PV/article | Current: {actual} PV/article ({X}% drop)
   Probable causes:
     a) Algorithm change? (run /algorithm to check)
     b) Posting time shifted? (check against best-times)
     c) Topic fatigue? (same topic 4 times this week)

   Recommended diagnostic:
     1. /algorithm — check for platform changes
     2. /content-dna — check if recent content matches your DNA
     3. /post-mortem — analyze the underperforming pieces

NO ANOMALIES:
  X engagement: {stable} (within normal range)
  Instagram saves: {stable}
  Follower growth: {stable}

============================================
```

### Anomaly History

```
Past anomalies and outcomes:
  {date}: Viral spike on "{title}" → gained {N} followers
    Lesson: {what caused it, stored in content-dna}
  {date}: Engagement drop → diagnosed as algorithm change
    Lesson: {adaptation made}
```

## Integration

- **performance-log**: Anomalies detected from logged data
- **algorithm-guide**: Check if anomaly matches algorithm change
- **instant-react**: Ride viral anomalies with rapid follow-up
- **post-mortem**: Deep analysis of anomaly causes
- **weekly-report**: Anomalies highlighted in report
- **content-dna**: Anomaly lessons feed into DNA

## Quality Gate

- [ ] Anomaly thresholds based on YOUR normal range (not generic)
- [ ] Both opportunities AND threats detected
- [ ] Probable causes are investigated, not assumed
- [ ] Recommended actions are time-sensitive (act fast for spikes)
- [ ] Historical anomalies tracked for pattern recognition
