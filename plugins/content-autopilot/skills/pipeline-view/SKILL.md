---
name: pipeline-view
description: Content pipeline visualization — see all content at every stage from idea to published. Track ideas, drafts, in-review, scheduled, and published states. Calendar shows WHEN; pipeline shows WHERE things are in the process. The content operations dashboard.
---

# Pipeline View

Calendar shows when. Pipeline shows where. See every piece of content's status at a glance.

## When to Activate

- User says `/pipeline` or `/pipeline-view`
- User asks "what's in progress?"
- User asks "show me my content pipeline"
- User wants to see the production status of all content

## Prerequisites

- `~/.content-autopilot/content-history.json`
- Optional: active-series.json, batch plans, launch plans

## Data: pipeline-state.json

Location: `~/.content-autopilot/pipeline-state.json`

```json
{
  "version": "1.0",
  "items": [
    {
      "id": "pipe-001",
      "title": "AI Automation Deep Dive",
      "stage": "idea",
      "source": "comment-miner",
      "created_at": "2026-03-21",
      "platform": "note",
      "priority": "high",
      "notes": "Multiple readers asked about this"
    },
    {
      "id": "pipe-002",
      "title": "7 Productivity Hacks",
      "stage": "draft",
      "source": "batch-generator",
      "created_at": "2026-03-20",
      "platform": "x",
      "file": "~/Desktop/content-autopilot-output/x_2026-03-25.md",
      "priority": "medium"
    }
  ]
}
```

## Pipeline Stages

```
[IDEA] → [RESEARCH] → [DRAFT] → [REVIEW] → [SCHEDULED] → [PUBLISHED] → [ANALYZED]
```

| Stage | Description | Actions Available |
|-------|------------|-------------------|
| Idea | Topic identified, not started | /content-writer, /brief |
| Research | Topic being researched | /trend-scout, WebSearch |
| Draft | Content written, not reviewed | /grade, /compliance, /brand-voice |
| Review | Under quality review | /fact-check, /readability, /pre-publish |
| Scheduled | Ready, waiting for posting time | /calendar, /best-time |
| Published | Live on platform | /perf-log, /post-mortem |
| Analyzed | Performance logged and lessons extracted | /post-mortem, complete |

## Commands

### `/pipeline` — Show current pipeline overview
### `/pipeline add {title}` — Add an idea to the pipeline
### `/pipeline move {id} {stage}` — Move item to next stage
### `/pipeline {stage}` — Filter by stage

## Workflow

### Step 1: Display Pipeline (`/pipeline`)

```
============================================
  Content Pipeline
  Total items: {count}
============================================

IDEAS ({count}):
  1. "{title}" — {platform} | {priority} | Source: {source}
  2. "{title}" — {platform} | {priority} | Source: {source}
  3. "{title}" — {platform} | {priority} | Source: {source}

RESEARCH ({count}):
  4. "{title}" — researching since {date}

DRAFT ({count}):
  5. "{title}" — drafted {date}, needs review
     File: {file_path}
  6. "{title}" — drafted {date}

REVIEW ({count}):
  7. "{title}" — grade: {score}/100, {issues} issues to fix
     Checklist: [x]grade [x]compliance [ ]fact-check [ ]pre-publish

SCHEDULED ({count}):
  8. "{title}" — publish {date} at {time} on {platform}
  9. "{title}" — publish {date} at {time}

PUBLISHED (last 7 days, {count}):
  10. "{title}" — {date} on {platform} | perf logged: {yes/no}
  11. "{title}" — {date} | perf logged: {yes/no}

ANALYZED ({count} this month):
  12. "{title}" — engagement: {rate}% | lessons: {count}

--- Pipeline Health ---
  Bottleneck: {stage} ({count} items stuck here)
  Avg time idea→published: {days} days
  Items without next action: {count}
  Overdue items: {count}

--- Suggested Actions ---
  1. Move "{title}" from draft to review — run /grade
  2. Log performance for "{title}" — run /perf-log
  3. Start research on "{title}" — run /trend-scout

============================================
```

### Step 2: Auto-Populate Pipeline

Items auto-added from:
- `/comment-mine` → Ideas
- `/trend-predict` → Ideas
- `/niche-monitor` → Ideas
- `/batch-generator` → Drafts
- `/daily-autopilot` → Published
- `/perf-log` → Analyzed

### Step 3: Move Items (`/pipeline move pipe-005 review`)

```
Moved: "{title}"
  From: draft → To: review

Review checklist:
  [ ] /grade — quality score
  [ ] /compliance — legal check
  [ ] /fact-check — verify claims
  [ ] /readability — audience match
  [ ] /pre-publish — platform checklist
  [ ] /benchmark — compare to your best

Run all review checks? (yes / select / skip)
```

## Integration with Other Skills

- **content-calendar**: Calendar = time view, pipeline = status view
- **daily-autopilot**: Moves items through pipeline automatically
- **batch-generator**: Creates items in draft stage
- **content-grader**: Review stage uses grader
- **performance-log**: Published → Analyzed transition
- **post-mortem**: Final analysis stage
- **weekly-report**: Pipeline status in weekly summary

## Quality Gate

- [ ] All pipeline stages clearly defined
- [ ] Items auto-populated from other skills
- [ ] Bottlenecks identified and highlighted
- [ ] Next actions suggested for stuck items
- [ ] Pipeline health metrics are meaningful
- [ ] Review stage has clear checklist of quality gates
