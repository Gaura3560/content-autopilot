---
name: energy-adapter
description: Adapt recommendations to your current energy level — low energy gets easy tasks (recycle, micro, curate), high energy gets ambitious tasks (research, series, course). Same system, different intensity.
---

# Energy Adapter

Low energy? Do less but don't stop. High energy? Go big.

## Commands

### `/energy low` — Easy tasks only (10-15 min)
### `/energy medium` — Standard tasks (30-60 min)
### `/energy high` — Ambitious tasks (60+ min)

## Task Mapping

| Energy | Tasks | Time |
|--------|-------|------|
| Low | `/recycle`, `/micro`, `/curate`, `/bank withdraw`, `/cap` | 10-15 min |
| Medium | `/daily-autopilot`, `/grade`, `/perf-log`, `/hooks` | 30-60 min |
| High | `/batch 7`, `/research`, `/series`, `/course`, `/launch` | 60+ min |

## Workflow

```
/energy low

Today's low-energy plan (15 min total):
  1. /recycle — reshare "{title}" with new hook (5 min)
  2. /micro — extract 3 posts from recent article (5 min)
  3. /perf-log — log yesterday's numbers (5 min)

Done. Streak maintained. Rest now.
```

Integrates with: advisor (filters by energy), workflow-chain (energy-specific workflows), burnout-detector (auto-suggests low when risk detected).
