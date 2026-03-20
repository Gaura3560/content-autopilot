---
name: multi-review
description: Multi-perspective content review — evaluate content simultaneously from 4 reader viewpoints (beginner, expert, skeptic, competitor). Catches blind spots that single-perspective review misses. The most thorough quality gate in the system.
---

# Multi-Perspective Review

One perspective has blind spots. Four perspectives have none.

## When to Activate

- User says `/multi-review {file_path}`
- User asks "review this from multiple angles"
- User asks "what would a skeptic think of this?"
- User wants the most thorough quality check possible

## Prerequisites

- Content file to review
- `~/.content-autopilot/profile.json`

## Commands

### `/multi-review {file_path}` — Full 4-perspective review
### `/multi-review {file_path} {perspective}` — Single perspective
### `/multi-review compare {file1} {file2}` — Multi-review comparison

## The 4 Perspectives

| Perspective | Asks | Catches |
|------------|------|---------|
| Beginner | "Do I understand this?" | Jargon, assumptions, unclear logic |
| Expert | "Is this accurate and deep enough?" | Oversimplifications, outdated info, shallow analysis |
| Skeptic | "Why should I believe this?" | Weak evidence, logical fallacies, missing sources |
| Competitor | "How would I attack this?" | Vulnerability in arguments, better alternatives unmentioned |

## Workflow

### Step 1: Run All 4 Reviews

```
============================================
  Multi-Perspective Review: "{title}"
  Platform: {platform} | {chars} chars
============================================

--- BEGINNER PERSPECTIVE ---
"I'm new to {topic}. Here's my experience reading this:"

Understanding score: {score}/10

Issues:
  1. Line {N}: "{jargon_term}" — I don't know what this means
     Fix: Add explanation or use simpler word

  2. Line {N}: Jumps from {concept_A} to {concept_B} — lost me
     Fix: Add transition sentence explaining the connection

  3. Section {N}: Too many new concepts at once
     Fix: Break into smaller sections or add examples

Strengths:
  - {what worked for a beginner}
  - {positive element}

Verdict: {Would a beginner finish reading? yes/no/maybe}

--- EXPERT PERSPECTIVE ---
"I know {topic} deeply. Here's my assessment:"

Depth score: {score}/10

Issues:
  1. Line {N}: "{claim}" — this is an oversimplification
     Reality: {nuanced version of the claim}
     Fix: Add caveat or qualify the statement

  2. Line {N}: Missing {important_aspect} that experts would expect
     Fix: Add section addressing {aspect}

  3. Data: "{stat}" is from {year} — newer data available
     Fix: Update to {newer_data} from {source}

Strengths:
  - {what an expert would respect}
  - {credibility-building element}

Verdict: {Would an expert share this? yes/no/maybe}

--- SKEPTIC PERSPECTIVE ---
"I don't believe anything without proof. Show me the evidence."

Credibility score: {score}/10

Issues:
  1. Line {N}: "{claim}" — where's the evidence?
     Status: No source cited
     Fix: Add citation or qualify as opinion

  2. Line {N}: "{logical_leap}" — this doesn't follow
     Fallacy: {type of logical fallacy if applicable}
     Fix: Add connecting evidence or reasoning

  3. Line {N}: Anecdotal evidence presented as general truth
     Fix: Add "in my experience" qualifier or cite broader data

Strengths:
  - {well-supported claims}
  - {credibility elements present}

Verdict: {Would a skeptic be convinced? yes/no/partially}

--- COMPETITOR PERSPECTIVE ---
"I write about the same topic. Here's how I'd attack this."

Defensibility score: {score}/10

Vulnerabilities:
  1. "{claim}" — a competitor could counter with {counter_argument}
     Defense: Preemptively address this objection

  2. Missing: {topic_angle} that competitors cover
     Fix: Add section or acknowledge limitation

  3. Stronger alternatives: {alternative_approach} not mentioned
     Fix: Compare approaches, explain why yours is better for {audience}

Unique value:
  - {what makes this piece defensible against competition}
  - {unique insight competitors lack}

Verdict: {Is this the best article on this topic? yes/not yet}

============================================

--- COMBINED VERDICT ---

Overall review score: {avg}/10

Priority fixes (cross-perspective):
  1. [Beginner + Skeptic] Line {N}: needs explanation AND evidence
  2. [Expert + Competitor] Section {N}: too shallow, competitors go deeper
  3. [All 4] CTA: {issue all perspectives agree on}

Strengths confirmed by multiple perspectives:
  1. {strength identified by 3+ perspectives}
  2. {strength}

If you fix the top 3 issues, this content is bulletproof.

============================================
```

## Integration with Other Skills

- **content-grader**: Grader = rule-based; multi-review = perspective-based
- **engagement-predictor**: Multi-review score correlates with engagement
- **readability-tuner**: Beginner perspective overlaps with readability
- **fact-checker**: Skeptic perspective overlaps with fact-checking
- **benchmark**: Expert perspective overlaps with benchmarking
- **workflow-chain**: Add to "publish" workflow for maximum quality gate

## Quality Gate

- [ ] All 4 perspectives genuinely distinct (not overlapping feedback)
- [ ] Issues are specific with line numbers and fixes
- [ ] Each perspective has both issues AND strengths
- [ ] Combined verdict identifies truly universal issues
- [ ] Priority fixes are actionable in order of impact
