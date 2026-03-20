---
name: content-bank
description: Maintain a reserve of 5-7 days of ready-to-publish content for emergencies — illness, vacation, burnout, or life events. Auto-select time-independent pieces from batch generation and store them as insurance. Never break your streak.
---

# Content Bank

Your content insurance policy. When life happens, your streak doesn't break.

## When to Activate

- User says `/content-bank` or `/bank`
- User says `/bank deposit` to add content
- User says `/bank withdraw` to use banked content
- Auto-suggested by burnout-detector when risk is elevated

## Data: content-bank.json

```json
{
  "version": "1.0",
  "target_reserve": 7,
  "entries": [
    {
      "id": "bank-001",
      "title": "5 Timeless AI Productivity Principles",
      "platforms": { "x": "bank_x_001.md", "note": "bank_note_001.md", "ig": "bank_ig_001.md" },
      "category": "evergreen",
      "deposited_at": "2026-03-21",
      "expiry": "2026-06-21",
      "status": "banked"
    }
  ]
}
```

## Commands

### `/bank` — Show current reserve status
### `/bank deposit {file}` — Add content to the bank
### `/bank withdraw` — Use banked content (publish today)
### `/bank auto-fill` — Auto-generate content to fill the bank

## Workflow

### Status Dashboard

```
============================================
  Content Bank — Emergency Reserve
============================================

Reserve: {current}/{target} days
Status: {FULL / LOW / EMPTY}

Banked content:
  1. "{title}" — deposited {date}, expires {date}
     Platforms: X + note + IG
  2. "{title}" — deposited {date}
  3. "{title}" — deposited {date}

{If LOW}:
  WARNING: Reserve below target.
  Run /bank auto-fill to generate {N} more pieces.

{If FULL}:
  Reserve is full. You're protected for {N} days.

============================================
```

### Auto-Fill

```
/bank auto-fill

Generating {N} evergreen pieces for the bank...
(Only time-independent content — no trending topics)

Requirements:
  - Must be publishable anytime (no date references)
  - Evergreen topics only
  - Pre-graded and pre-checked

Generated:
  1. "{title}" — grade: {score}/100 ✓
  2. "{title}" — grade: {score}/100 ✓
  ...

Bank reserve: {before} → {after}/{target} days
```

### Withdraw (Emergency Use)

```
/bank withdraw

Releasing banked content for today:
  "{title}" — all platforms ready

  X: bank_x_001.md — copy-paste ready
  note: bank_note_001.md — copy-paste ready
  IG: bank_ig_001.md — copy-paste ready

Bank reserve: {N-1}/{target} days
Reminder: Refill bank when you're back with /bank auto-fill
```

## Quality Gate

- [ ] Banked content is genuinely time-independent
- [ ] Content expires after 90 days (refresh or replace)
- [ ] Reserve target is maintained (auto-fill suggestions)
- [ ] Withdrawal is instant (no generation needed)
- [ ] Quality checked before banking (grade 70+)
