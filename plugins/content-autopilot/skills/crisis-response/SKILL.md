---
name: crisis-response
description: Crisis management playbook for content creators — handle backlash, misinformation, trolls, and controversies with pre-built response frameworks. Decide when to apologize, correct, ignore, or fight back. The fire extinguisher you prepare before the fire.
---

# Crisis Response

Prepare for the worst so you never panic. Every creator faces a crisis eventually.

## When to Activate

- User says `/crisis` or `/crisis {type}`
- User says "I'm being attacked" or "my post went wrong"
- User faces negative publicity or backlash

## Commands

### `/crisis` — Show all crisis types and playbooks
### `/crisis {type}` — Specific crisis playbook
### `/crisis assess {situation}` — Assess severity and recommend response

## Crisis Types

| Type | Severity | Example |
|------|----------|---------|
| Factual error | Medium | You published wrong data |
| Misunderstood post | Medium | Your words taken out of context |
| Troll attack | Low | Individual harassment |
| Coordinated backlash | High | Multiple people piling on |
| Plagiarism accusation | High | Accused of copying |
| Offensive content | Critical | Unintentionally offensive |
| Legal threat | Critical | Copyright/defamation claim |

## Workflow

### Step 1: Assess Severity

```
/crisis assess "I posted wrong statistics and people are calling me out"

Crisis Assessment:
============================================

Type: Factual error
Severity: MEDIUM
Urgency: HIGH (correct quickly before it spreads)
Scale: {N} people have responded

Response framework: CORRECT AND OWN

Recommended action (in order):
  1. [IMMEDIATE — within 1 hour]
     Post correction on same platform
     Template: "Correction: I cited {wrong_data} in my earlier post.
     The accurate figure is {correct_data} ({source}).
     Thank you to {person} for flagging this. Accuracy matters."

  2. [WITHIN 24 HOURS]
     Update the original content with correction
     Add: "Update {date}: This article has been corrected. {details}"

  3. [WITHIN 48 HOURS]
     Note article: "What I Got Wrong and What I Learned"
     (Turns crisis into credibility-building content)

  DO NOT:
  - Delete the original post (looks like cover-up)
  - Argue with critics (escalates)
  - Ignore it (looks arrogant)

============================================
```

### Response Frameworks

```
CORRECT AND OWN — for factual errors
  Acknowledge → Correct → Thank the reporter → Show what you learned

CLARIFY — for misunderstandings
  "I see how this could be read that way. What I meant was..."
  Restate clearly → Don't blame the reader

IGNORE AND BLOCK — for trolls
  Individual troll with no following → block silently
  Never engage publicly with trolls

APOLOGIZE — for genuinely offensive content
  "I was wrong. I'm sorry." (no "I'm sorry IF...")
  Remove the content → Explain what you'll do differently

LEGAL — for serious threats
  Don't respond publicly → Consult a professional
  Screenshot everything → Don't delete evidence
```

## Quality Gate

- [ ] Assessment matches actual severity
- [ ] Response framework is appropriate for the crisis type
- [ ] Templates are ready to customize immediately
- [ ] "DO NOT" list prevents common mistakes
- [ ] Turns crisis into credibility when possible
