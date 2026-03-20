---
name: milestone-tracker
description: Auto-detect and celebrate content milestones — first sale, 10th article, 100-day streak, revenue goals. The only skill that makes you feel good about your progress.
---

# Milestone Tracker

You're doing more than you think. Let the system remind you.

## Commands

### `/milestone` — Check current milestones and progress
### `/milestone history` — All milestones achieved

## Auto-Detected Milestones

| Milestone | Trigger |
|-----------|---------|
| First article | 1st entry in content-history |
| 10 / 50 / 100 / 500 articles | Entry count thresholds |
| First paid sale | monetize-data first entry |
| Revenue ¥10K / ¥50K / ¥100K | Cumulative revenue |
| 7 / 30 / 100 day streak | Consecutive posting days |
| First series completed | Series status → complete |
| First A/B test winner | ab-tests first resolved |
| Content DNA established | content-dna.json created |

## Output

```
============================================
  Milestones
============================================

Achieved:
  [2026-01-15] First article published
  [2026-02-01] 10 articles milestone
  [2026-03-01] 30-day streak
  [2026-03-10] First paid sale (¥500)
  [2026-03-20] 50 articles milestone

Next milestone:
  100 articles — {N} more to go
  Revenue ¥50,000 — ¥{remaining} to go
  100-day streak — {N} days to go

Keep going.
============================================
```

Integrates with: weekly-report (milestones highlighted), content-history (auto-detection), monetize-data (revenue milestones).
