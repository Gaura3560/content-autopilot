---
name: content-grader
description: Pre-publish content quality scoring — evaluates readability, hook strength, CTA clarity, SEO readiness, platform fit, and engagement potential. Returns a 0-100 score with specific improvement suggestions. Use before publishing to catch issues.
---

# Content Grader

Score your content before publishing — catch weak spots and maximize impact.

## When to Activate

- User says `/grade` or `/grade {file_path}`
- User asks "is this ready to publish?"
- User asks "how good is this content?"
- User wants feedback on a draft

## Prerequisites

- Content file or text to grade
- `~/.content-autopilot/profile.json` (for platform and audience context)

## Commands

### `/grade {file_path}` — Grade a specific file
### `/grade` — Interactive: select from recent content
### `/grade all` — Grade all today's content at once

## Scoring Dimensions (100 points total)

| Dimension | Max Points | What It Measures |
|-----------|-----------|-----------------|
| Hook Strength | 20 | Does the opening stop the scroll? |
| Readability | 20 | Is it easy to read for the target audience? |
| Value Density | 20 | Is every paragraph earning its place? |
| CTA Clarity | 15 | Is the next action obvious and compelling? |
| Platform Fit | 15 | Does it follow platform conventions? |
| SEO Readiness | 10 | (note only) Keywords, headings, structure |

## Workflow

### Step 1: Load Content

Read the content file and detect platform from filename:
- `note_*.md` → note grading criteria
- `x_*.md` → X grading criteria
- `instagram_*.md` → Instagram grading criteria
- `voice_*.md` → Voice script grading criteria

### Step 2: Analyze Each Dimension

**Hook Strength (0-20):**
```
Check:
- First sentence/line creates curiosity or surprise? (+5)
- Uses a proven hook pattern (data/question/story/paradox)? (+5)
- Would YOU stop scrolling for this? (+5)
- Platform-appropriate length? (+5)

Deductions:
- Generic opening ("Today I want to talk about...") (-10)
- No hook at all (starts with background) (-15)
- Clickbait that content doesn't deliver on (-10)
```

**Readability (0-20):**
```
Check:
- Average sentence length < 40 chars (Japanese)? (+5)
- Paragraphs ≤ 3 sentences? (+5)
- No jargon without explanation? (+5)
- Visual breaks (headings, lists, spacing)? (+5)

Deductions:
- Wall of text (paragraph > 5 sentences) (-5 per instance)
- Passive voice overuse (-3)
- Inconsistent tone (-5)
```

**Value Density (0-20):**
```
Check:
- Every section has a concrete takeaway? (+5)
- Specific examples/data (not generic advice)? (+5)
- No filler paragraphs? (+5)
- Reader learns something new? (+5)

Deductions:
- Filler phrases ("As we all know...") (-2 per instance)
- Repeating the same point (-5)
- Generic advice without specifics (-5)
```

**CTA Clarity (0-15):**
```
Check:
- Clear next action for the reader? (+5)
- CTA matches funnel stage? (+5)
- CTA feels natural (not forced)? (+5)

Deductions:
- No CTA at all (-10)
- Multiple competing CTAs (-5)
- CTA disconnected from content (-5)
```

**Platform Fit (0-15):**
```
note:
  - 2,000-5,000 chars? (+5)
  - H2 section headings? (+5)
  - Proper conclusion section? (+5)

X:
  - Each tweet ≤ 280 chars? (+5)
  - Thread has hook + body + CTA structure? (+5)
  - Standalone value per tweet? (+5)

Instagram:
  - Hook visible before "more" fold? (+5)
  - 25-30 hashtags in 3 tiers? (+5)
  - Line breaks for readability? (+5)
```

**SEO Readiness (0-10, note only):**
```
Check:
- Target keyword in title? (+3)
- Target keyword in first paragraph? (+2)
- H2 headings contain related keywords? (+3)
- Internal link opportunity identified? (+2)
```

### Step 3: Display Report Card

```
============================================
  Content Grade Report
  File: {filename}
  Platform: {platform}
============================================

Overall Score: {score}/100 — {grade_label}

  Hook Strength:   {score}/20 {bar} {emoji}
  Readability:     {score}/20 {bar} {emoji}
  Value Density:   {score}/20 {bar} {emoji}
  CTA Clarity:     {score}/15 {bar} {emoji}
  Platform Fit:    {score}/15 {bar} {emoji}
  SEO Readiness:   {score}/10 {bar} {emoji}

--- Grade Scale ---
90-100: Publish now — this is strong
80-89:  Good — minor tweaks recommended
70-79:  Decent — address the issues below
60-69:  Needs work — significant improvements needed
<60:    Rewrite recommended

--- Issues Found ---
1. [Hook] {specific issue and how to fix it}
2. [Readability] {specific issue and fix}
3. [CTA] {specific issue and fix}

--- Quick Fixes ---
1. {actionable one-line fix}
2. {actionable one-line fix}
3. {actionable one-line fix}

--- Strengths ---
1. {what's working well}
2. {what's working well}

============================================
Estimated engagement: {low/medium/high} based on similar content patterns
============================================
```

### Grade Labels

| Score | Label | Action |
|-------|-------|--------|
| 90-100 | A+ Excellent | Publish immediately |
| 80-89 | A Good | Publish with minor tweaks |
| 70-79 | B Decent | Fix highlighted issues |
| 60-69 | C Needs Work | Address all issues before publishing |
| <60 | D Rewrite | Consider a fresh approach |

### Step 4: Auto-Fix Offer

If score is 60-79:
```
Would you like me to auto-fix the highlighted issues? (yes / no / fix specific #)
```

If yes, apply fixes and re-grade to show improvement.

## Integration with Other Skills

- **daily-autopilot**: Optional Step 5.5 — auto-grade before saving
- **batch-generator**: Grade each day's content, flag any below 70
- **content-writer**: Display score after generation as quality check

## Quality Gate

- [ ] Scoring is consistent and reproducible
- [ ] Issues are specific (not generic "improve readability")
- [ ] Quick fixes are actually actionable in 1-2 minutes
- [ ] Platform-specific criteria correctly applied
- [ ] Auto-fix doesn't change the author's voice
