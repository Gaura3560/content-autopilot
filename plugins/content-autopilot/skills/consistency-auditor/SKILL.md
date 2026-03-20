---
name: consistency-auditor
description: Cross-content consistency checker — detect contradictions, conflicting advice, outdated claims, and factual inconsistencies across your entire content history. Protects brand credibility by ensuring you never contradict yourself.
---

# Consistency Auditor

Never contradict yourself — catch conflicts between your new content and everything you've ever published.

## When to Activate

- User says `/consistency-audit {file_path}` or `/consistency`
- User asks "does this contradict anything I've written?"
- User asks "am I being consistent?"
- Auto-suggested for opinion pieces and advice content

## Prerequisites

- `~/.content-autopilot/content-history.json` (with content file references)
- Content file to check
- Access to previous content files in `~/Desktop/content-autopilot-output/`

## Commands

### `/consistency {file_path}` — Check against all history
### `/consistency audit` — Full consistency audit of recent content
### `/consistency {file1} {file2}` — Check two specific files against each other

## What Gets Checked

| Check Type | Example | Severity |
|-----------|---------|----------|
| Direct contradiction | "Always do X" vs "Never do X" | Critical |
| Number mismatch | "saves 3 hours" vs "saves 2 hours" (same claim) | High |
| Recommendation flip | "Tool A is best" → "Tool B is best" (no explanation) | High |
| Stance drift | Gradually shifting position without acknowledgment | Medium |
| Outdated reference | Citing the same stat with different numbers | Medium |
| Terminology inconsistency | "AI" vs "人工知能" vs "AI技術" (mixed usage) | Low |

## Workflow

### Step 1: Extract Claims from New Content

Read the new content and extract:
- Factual claims and statements
- Recommendations and advice
- Numbers and statistics
- Opinions and positions
- Terminology used

### Step 2: Search Content History

For each extracted claim, search previous content:
- Read content-history.json for topic matches
- Load matching previous content files
- Compare claims, recommendations, and positions

### Step 3: Present Findings

```
============================================
  Consistency Audit: "{new_title}"
  Checked against: {N} previous content pieces
============================================

CONTRADICTIONS FOUND:

1. [CRITICAL] Direct contradiction
   New (line {N}): "The best approach is to start with Tool A"
   Previous ("{old_title}", {date}): "Tool B is the clear winner for beginners"
   Impact: Readers who read both will lose trust
   Options:
     A) Acknowledge the change: "I previously recommended B, but after
        testing A for 3 months, I've changed my mind because..."
     B) Update the old article
     C) Remove the claim from the new article

2. [HIGH] Number mismatch
   New (line {N}): "AI saves an average of 3 hours per day"
   Previous ("{old_title}", {date}): "AI saves up to 2 hours per day"
   Impact: Inconsistent data undermines credibility
   Options:
     A) Use the verified number (run /fact-check)
     B) Cite different sources for different numbers
     C) Use a range: "2-3 hours per day"

3. [MEDIUM] Stance drift
   New: Positive stance on {topic}
   3 months ago: Skeptical stance on {topic}
   2 months ago: Neutral stance on {topic}
   This month: Positive stance on {topic}
   Impact: Not a contradiction per se, but readers may notice the shift
   Option: Acknowledge growth: "My thinking on {topic} has evolved..."

CONSISTENT (confirmed matches):
  4. "{claim}" — matches "{old_title}" ({date}) — CONSISTENT
  5. "{claim}" — matches "{old_title}" ({date}) — CONSISTENT

TERMINOLOGY CHECK:
  You use: "AI" ({N} times), "人工知能" ({N} times), "AI技術" ({N} times)
  Recommendation: Standardize to "{most_used}" for brand consistency

--- Summary ---
  Critical contradictions: {count}
  High-priority mismatches: {count}
  Medium issues: {count}
  Consistent claims: {count}/{total}

  Consistency score: {percentage}%

============================================
```

### Step 4: Auto-Fix Options

For each contradiction:
```
Fix options for contradiction #{N}:

1. [Add context] Insert acknowledgment of position change
   "{I previously recommended X. After {reason}, I now recommend Y.}"

2. [Update old] Flag old content for /refresh with corrected information

3. [Remove claim] Remove the contradicting claim from new content

4. [Reconcile] Rewrite both to be compatible:
   "{Both X and Y are valid depending on {context}...}"

Apply fix? (1/2/3/4 / skip)
```

## Integration with Other Skills

- **fact-checker**: Verify which version of conflicting claims is correct
- **content-refresh**: Update old content when contradictions are found
- **content-grader**: Consistency score included in grade
- **brand-voice**: Voice consistency is a subset of overall consistency
- **weekly-report**: Flag consistency issues in weekly summary

## Quality Gate

- [ ] All major claims in new content are checked against history
- [ ] Contradictions are accurately identified (not false positives)
- [ ] Fix options preserve brand credibility
- [ ] Acknowledged stance changes are acceptable (not flagged as errors)
- [ ] Terminology consistency is practical (not pedantic)
