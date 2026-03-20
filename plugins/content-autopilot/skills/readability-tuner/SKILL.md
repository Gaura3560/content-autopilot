---
name: readability-tuner
description: Japanese readability analysis and adjustment — measure sentence length, kanji density, jargon usage, and paragraph structure against the target audience's knowledge level. Auto-adjust content to match beginner/intermediate/advanced readers precisely.
---

# Readability Tuner

Match your writing precisely to your audience's reading level — not too simple, not too complex.

## When to Activate

- User says `/readability {file_path}` or `/readability`
- User asks "is this too complex for my audience?"
- User asks "simplify this" or "make this more advanced"
- Auto-suggested when content-grader detects readability issues

## Prerequisites

- `~/.content-autopilot/profile.json` (for audience.knowledge_level)
- Content file to analyze

## Commands

### `/readability {file_path}` — Analyze and score readability
### `/readability {file_path} beginner` — Adjust to beginner level
### `/readability {file_path} advanced` — Adjust to advanced level
### `/readability compare {file1} {file2}` — Compare readability

## Japanese Readability Metrics

| Metric | Beginner | Intermediate | Advanced |
|--------|----------|-------------|----------|
| Avg sentence length | < 30 chars | 30-50 chars | 50+ chars |
| Kanji ratio | < 20% | 20-35% | 35%+ |
| Jargon per 1000 chars | 0-2 | 3-5 | 6+ |
| Paragraph length | 1-2 sentences | 2-3 sentences | 3-5 sentences |
| Parenthetical explanations | Frequent | Occasional | Rare |
| Analogies/examples | Every concept | Key concepts | Minimal |

## Workflow

### Step 1: Analyze Content

```
Readability Analysis: "{title}"
============================================

Target audience: {knowledge_level from profile}

--- Metrics ---

Sentence length:
  Average: {chars} chars
  Target for {level}: {range} chars
  Status: {OK / too long / too short}
  Longest sentence: "{excerpt}" ({chars} chars, line {N})

Kanji density:
  Ratio: {percentage}%
  Target for {level}: {range}%
  Status: {OK / too dense / too simple}

Technical jargon:
  Found: {count} terms per 1000 chars
  Target for {level}: {range}
  Flagged terms: {term1}, {term2}, {term3}
  Status: {OK / too technical / oversimplified}

Paragraph structure:
  Average: {N} sentences per paragraph
  Target for {level}: {range}
  Status: {OK / too dense / too choppy}

Explanation density:
  Concepts without explanation: {count}
  For {level} audience, these need explanation:
    1. "{term}" — no explanation provided (line {N})
    2. "{term}" — explanation too brief (line {N})

--- Overall ---

Readability score: {score}/100
Level match: {actual_level} vs target {target_level}
Verdict: {MATCHED / TOO COMPLEX / TOO SIMPLE}

============================================
```

### Step 2: Auto-Adjust (if requested)

**Simplifying (making easier):**
- Split long sentences into shorter ones
- Replace kanji-heavy words with hiragana alternatives
- Add parenthetical explanations for technical terms: "AI（人工知能）"
- Add analogies: "これは○○のようなものです"
- Shorten paragraphs

**Complexifying (making more advanced):**
- Merge simple sentences into compound ones
- Use proper technical terminology without excessive explanation
- Remove overly basic explanations
- Add nuance and caveats
- Reference source material directly

```
Readability Adjustments Applied:

1. Line {N}: Split sentence (72 chars → 35 + 37 chars)
   Before: "{long_sentence}"
   After: "{sentence_1}" + "{sentence_2}"

2. Line {N}: Added explanation for "{jargon}"
   Before: "LLMを活用して..."
   After: "LLM（大規模言語モデル）を活用して..."

3. Line {N}: Added analogy
   Before: "ファインチューニングとは..."
   After: "ファインチューニングとは...たとえば、料理のレシピを自分好みにアレンジするようなものです"

Adjustments: {count}
New readability score: {before} → {after}/100
Level match: {MATCHED}
```

### Step 3: Audience Mismatch Alert

```
WARNING: Audience mismatch detected

Your content is written at {actual_level} level.
Your target audience is {target_level} (from profile.json).

Impact: {target_level} readers may find this {too complex / too basic}.
  - Too complex → readers bounce, engagement drops
  - Too basic → experts feel patronized, lower credibility

Recommendation: Adjust to {target_level} with /readability {file} {target}
```

## Integration with Other Skills

- **content-grader**: Readability score feeds into overall grade
- **content-writer**: Target readability during generation
- **persona-switcher**: Each persona has its own readability target
- **content-brief**: Include readability requirements in briefs
- **engagement-predictor**: Readability affects predicted engagement
- **brand-voice**: Readability is part of consistent voice

## Quality Gate

- [ ] Metrics are calculated accurately for Japanese text
- [ ] Adjustments preserve meaning (simplifying ≠ dumbing down)
- [ ] Technical terms are handled appropriately for the target level
- [ ] Analogies are relevant and clarifying (not confusing)
- [ ] Readability score reflects actual reading difficulty
