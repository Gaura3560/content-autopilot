---
name: workflow-chain
description: Custom skill chain builder — combine multiple skills into a single command that runs them in sequence. Define "morning routine", "publish flow", "weekly review" as one-click workflows. Compress 89 skills into YOUR personal shortcuts.
---

# Workflow Chain

89 skills → your personal shortcuts. One command, multiple skills, zero thinking.

## When to Activate

- User says `/workflow` or `/workflow {name}`
- User says `/workflow create {name}`
- User asks "chain these skills together"
- User wants to automate a multi-step process

## Prerequisites

- `~/.content-autopilot/profile.json`

## Data: workflows.json

Location: `~/.content-autopilot/workflows.json`

```json
{
  "version": "1.0",
  "workflows": [
    {
      "name": "morning",
      "description": "Daily content creation routine",
      "steps": [
        { "skill": "advisor", "args": "quick", "stop_if_fail": false },
        { "skill": "daily-autopilot", "args": "", "stop_if_fail": true },
        { "skill": "content-grader", "args": "{output_file}", "stop_if_fail": false },
        { "skill": "pre-publish", "args": "{output_file}", "stop_if_fail": false }
      ],
      "created_at": "2026-03-21",
      "run_count": 12
    }
  ]
}
```

## Pre-Built Workflows

### `/workflow morning` — Daily Content Routine
```
Steps:
  1. /advisor quick — what's the priority today?
  2. /daily-autopilot — create today's content
  3. /grade {output} — quality check
  4. /pre-publish {output} — final checklist
  5. /perf-log — log yesterday's performance (if not done)

Duration: ~20 minutes
```

### `/workflow publish` — Pre-Publish Pipeline
```
Steps:
  1. /grade {file} — quality score
  2. /fact-check {file} — verify claims
  3. /readability {file} — audience match
  4. /compliance {file} — legal check
  5. /brand-voice {file} — voice consistency
  6. /sentiment {file} — emotion check
  7. /pre-publish {file} — platform checklist
  8. /sync-check {file} — cross-platform consistency
  9. /engagement-predict {file} — performance prediction

Duration: ~10 minutes
All 9 checks in sequence, issues highlighted.
```

### `/workflow weekly` — Weekly Review
```
Steps:
  1. /perf-log batch — log all unlogged performance
  2. /report — weekly performance summary
  3. /post-mortem week — analyze what worked/didn't
  4. /expiry — check for stale content
  5. /advisor — plan next week
  6. /batch 7 — generate next week's content

Duration: ~30 minutes
```

### `/workflow optimize` — Content Optimization Deep Dive
```
Steps:
  1. /content-dna update — refresh your DNA profile
  2. /ab-test results — check experiment outcomes
  3. /benchmark calibrate — update benchmarks
  4. /algorithm — refresh platform intelligence
  5. /journey bottlenecks — find funnel leaks
  6. /cannibal-check — SEO health

Duration: ~15 minutes, run monthly
```

## Commands

### `/workflow` — List all workflows
### `/workflow {name}` — Run a workflow
### `/workflow create {name}` — Create custom workflow
### `/workflow edit {name}` — Modify a workflow
### `/workflow delete {name}` — Remove a workflow

## Workflow: Create Custom

```
/workflow create launch-prep

Define your workflow steps:
(Enter skill commands in order, one per line. Type "done" when finished.)

1. /competitor-scout
2. /trend-predict
3. /content-writer {topic}
4. /grade {output}
5. /fact-check {output}
6. /visual-creator
7. /pre-publish {output}
done

Workflow "launch-prep" created with 7 steps.
Run with: /workflow launch-prep
```

## Execution

```
Running workflow: "morning"
============================================

[1/5] /advisor quick...
  → Top action: Log performance for 3 posts
  → Continuing...

[2/5] /daily-autopilot...
  → Topic selected: "{topic}"
  → Content generated for note + X + IG
  → Files saved to output directory

[3/5] /grade note_2026-03-21.md...
  → Score: 82/100 (Good)
  → 2 minor issues flagged

[4/5] /pre-publish note_2026-03-21.md...
  → 11/12 checks passed
  → 1 issue: missing internal link → auto-fixed

[5/5] /perf-log...
  → 3 posts logged

============================================
  Workflow "morning" complete
  Duration: {time}
  Issues found: {count}
  Content ready: {files}
============================================
```

## Variable Passing

Workflows can pass outputs between steps:
```
Step 2 output file → Step 3 input → Step 4 input
{output_file} variable auto-populated from previous step
```

## Integration with Other Skills

- **ALL skills** — any skill can be chained into a workflow
- **skill-advisor** — recommends which workflow to run
- **weekly-report** — shows workflow usage statistics

## Quality Gate

- [ ] Steps execute in correct order
- [ ] Variables pass between steps correctly
- [ ] Failures handled gracefully (continue or stop based on config)
- [ ] Total duration estimated before execution
- [ ] Custom workflows saved and reusable
