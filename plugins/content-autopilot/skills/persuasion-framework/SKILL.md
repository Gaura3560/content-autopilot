---
name: persuasion-framework
description: Apply proven persuasion frameworks to your content — AIDA, PAS, BAB, PASONA, Cialdini's 6 principles, and more. Transform informational content into content that MOVES people to action. The science of making your writing compelling.
---

# Persuasion Framework

Good content informs. Great content persuades. Apply the science of influence.

## When to Activate

- User says `/persuasion {framework}` or `/persuasion {file}`
- User asks "make this more compelling"
- User asks "apply AIDA/PAS/PASONA to this"
- User wants to increase conversion from content

## Prerequisites

- Content file to enhance (or topic to write with framework)

## Available Frameworks

| Framework | Structure | Best For |
|-----------|-----------|----------|
| AIDA | Attention → Interest → Desire → Action | Sales pages, CTAs |
| PAS | Problem → Agitate → Solution | Pain-point content |
| BAB | Before → After → Bridge | Transformation stories |
| PASONA | Problem → Affinity → Solution → Offer → Narrow → Action | Japanese market DRM |
| 4Ps | Promise → Picture → Proof → Push | Landing pages |
| Cialdini 6 | Reciprocity, Commitment, Social Proof, Authority, Liking, Scarcity | Any persuasive content |
| Story Selling | Hook → Struggle → Discovery → Transformation → Offer | Narrative sales |

## Commands

### `/persuasion {framework} {file}` — Apply framework to existing content
### `/persuasion {framework} {topic}` — Write new content using framework
### `/persuasion analyze {file}` — Detect which frameworks are already present
### `/persuasion all` — Show all frameworks with examples

## Workflow

### Step 1: Apply Framework

**PAS (Problem → Agitate → Solution):**
```
Applying PAS to: "{title}"

--- PROBLEM ---
Current opening: "{current_opening}"
PAS opening: "{rewritten to clearly state the reader's problem}"
  "If you're {doing X}, you're losing {Y} every single day."

--- AGITATE ---
Current body: {how it currently addresses the problem}
PAS agitation: "{amplify the pain — make them FEEL it}"
  "And it gets worse. While you {struggle}, your competitors {benefit}.
  Every day you wait costs you {specific_loss}."

--- SOLUTION ---
Current solution section: {how solution is presented}
PAS solution: "{present your content/product as THE answer}"
  "Here's the good news: {solution} takes just {time} to implement,
  and the results speak for themselves: {proof}."

Changes made: {count}
Persuasion score: {before}/10 → {after}/10
```

**Cialdini's 6 Principles (enhancement layer):**
```
Cialdini analysis of "{title}":

[x] Reciprocity — giving value before asking (present in intro)
[ ] Commitment — small yes before big ask (MISSING)
    Add: "Try step 1 today" before the paid CTA
[x] Social proof — others' results (present in Section 3)
[ ] Authority — credentials/expertise (MISSING)
    Add: "After {N} years of {experience}..."
[x] Liking — personal connection (present in story section)
[ ] Scarcity — limited availability/time (MISSING)
    Add: "This approach works now, but {reason it may change}"

Principles present: 3/6
Recommendation: Add commitment + authority + scarcity for maximum persuasion
```

**PASONA (Japanese market optimized):**
```
Applying PASONA:

P (Problem): {pain point — resonate with the reader}
A (Affinity): {show you understand — "I've been there too"}
S (Solution): {your method/content as the answer}
O (Offer): {what they get — specific deliverables}
N (Narrowing): {who this is for / urgency / scarcity}
A (Action): {clear single CTA}
```

### Step 2: Before/After Comparison

```
Persuasion Enhancement: "{title}"
============================================

BEFORE (informational):
  Opening: "In this article, we'll discuss AI automation..."
  Structure: Inform → Explain → Conclude
  CTA: "Follow for more"
  Persuasion score: 3/10

AFTER (persuasive, PAS framework):
  Opening: "You're spending 3 hours a day on tasks AI could do in 10 minutes."
  Structure: Problem → Agitate → Solution → Proof → Action
  CTA: "Get the complete automation template → {link}"
  Persuasion score: 8/10

Key changes:
  1. Opening: Generic intro → Pain-point hook
  2. Body: Information → Emotional journey
  3. CTA: Passive → Active with specific value
  4. Added: Social proof, authority, scarcity elements

============================================
```

## Integration with Other Skills

- **content-writer**: Apply framework during initial generation
- **smart-cta**: CTAs enhanced by persuasion principles
- **launch-sequence**: Launch content uses heavy persuasion
- **affiliate-writer**: Product content with ethical persuasion
- **engagement-predictor**: Persuasion-enhanced content scores higher

## Quality Gate

- [ ] Framework applied authentically (not manipulatively)
- [ ] Content still provides genuine value (not just selling)
- [ ] Emotional triggers are ethical (real problems, real solutions)
- [ ] Specific framework elements clearly identified
- [ ] Before/after comparison shows clear improvement
