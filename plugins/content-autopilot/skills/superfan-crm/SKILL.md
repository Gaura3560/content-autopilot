---
name: superfan-crm
description: Identify and nurture your most engaged readers — track repeat commenters, frequent sharers, and loyal supporters. Build a lightweight CRM for your top fans. 10 superfans are worth more than 10,000 passive followers.
---

# Superfan CRM

Your most engaged 1% drives 80% of your growth. Know them by name.

## When to Activate

- User says `/superfan` or `/crm`
- User asks "who are my most engaged readers?"
- User wants to build deeper audience relationships

## Data: superfans.json

```json
{
  "fans": [
    {
      "name": "Fan A",
      "handles": { "x": "@fan_a", "note": "fan_a", "instagram": "@fan_a" },
      "interactions": [
        { "date": "2026-03-20", "type": "comment", "platform": "note", "content": "Great article!" },
        { "date": "2026-03-18", "type": "reply", "platform": "x", "content": "This changed my workflow" }
      ],
      "total_interactions": 12,
      "first_interaction": "2026-01-15",
      "tier": "superfan",
      "notes": "Works in marketing, interested in AI automation",
      "last_contacted": "2026-03-15"
    }
  ]
}
```

## Commands

### `/crm` — Superfan dashboard
### `/crm add {handle}` — Add a fan manually
### `/crm contact-plan` — Generate outreach plan for top fans
### `/crm ambassador` — Design ambassador program

## Workflow

### Dashboard

```
============================================
  Superfan Dashboard — {count} tracked fans
============================================

Tier 1 — Superfans (10+ interactions):
  1. {name} (@{handle}) — {N} interactions, last: {date}
     Note: {personal note}
     Action: {suggest outreach if not contacted recently}

  2. {name} — {N} interactions
     ...

Tier 2 — Engaged (5-9 interactions):
  3. {name} — {N} interactions

Tier 3 — Promising (3-4 interactions):
  4. {name} — {N} interactions

--- Actions Due ---
  {name}: Not contacted in 30+ days → send thank you DM
  {name}: Commented 3 times this week → potential superfan upgrade

============================================
```

### Ambassador Program

```
Ambassador Program Design:

Benefits for ambassadors:
  - Early access to new content
  - Exclusive behind-the-scenes
  - Name mention in articles
  - Free access to paid content
  - Direct DM access to you

Ambassador responsibilities:
  - Share content regularly
  - Provide feedback on drafts
  - Participate in polls/challenges
  - Recruit new readers

Outreach template for inviting superfans to ambassador program.
```

## Quality Gate

- [ ] Fan data based on actual interactions (not fabricated)
- [ ] Tiers reflect genuine engagement levels
- [ ] Contact suggestions are timely and appropriate
- [ ] Ambassador program provides real value to fans
- [ ] Privacy respected (public interactions only)
