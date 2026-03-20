---
name: brand-voice
description: Brand voice consistency guardian — analyze content for tone drift, vocabulary consistency, personality alignment, and style coherence across all platforms. Scores "brand-ness" and flags deviations. Ensures every piece feels unmistakably YOU.
---

# Brand Voice Guardian

Ensure every piece of content sounds unmistakably like YOU — catch voice drift before publishing.

## When to Activate

- User says `/brand-voice` or `/brand-voice {file_path}`
- User asks "does this sound like me?"
- User asks "check the tone of this"
- Auto-referenced by content-grader for voice consistency scoring

## Prerequisites

- `~/.content-autopilot/profile.json` (style settings)
- `~/.content-autopilot/content-history.json` (baseline voice data)
- Minimum 5 content entries for voice baseline

## Commands

### `/brand-voice {file_path}` — Check a specific file for voice consistency
### `/brand-voice baseline` — Analyze your content history to establish voice baseline
### `/brand-voice compare {file1} {file2}` — Compare voice between two pieces
### `/brand-voice guide` — Generate a shareable brand voice guide document

## Workflow

### Step 1: Establish Voice Baseline (`/brand-voice baseline`)

Analyze content-history.json entries to extract your voice fingerprint:

```
Analyzing {N} content pieces for voice baseline...

Your Brand Voice Fingerprint:
============================================

Tone: {authoritative / casual / warm / provocative / educational}
  Confidence: {percentage}% consistent across content

Formality: {score}/10 (1=very casual, 10=very formal)
  Range: {min}-{max} across pieces

Vocabulary level: {simple / accessible / technical / expert}
  Signature words you use often: {word1}, {word2}, {word3}
  Words you never use: {word4}, {word5}

Sentence patterns:
  Average length: {chars} chars
  Preferred structures: {short-punchy / long-flowing / mixed}
  Opening patterns: {how you typically start paragraphs}

Personality markers:
  Humor frequency: {none / rare / occasional / frequent}
  Self-reference: {never / sometimes / often}
  Reader address: {formal / casual / direct}
  Emoji usage: {none / minimal / moderate / heavy}

Unique voice traits:
  1. {trait}: "{example from your content}"
  2. {trait}: "{example}"
  3. {trait}: "{example}"

Voice consistency score: {score}/100
  >80: Strong, recognizable voice
  60-80: Mostly consistent, some drift
  <60: Inconsistent — consider establishing clearer guidelines

============================================
```

Save to `~/.content-autopilot/brand-voice.json`.

### Step 2: Check Content (`/brand-voice {file}`)

Compare a piece against the baseline:

```
Brand Voice Check: "{title}"
============================================

Overall voice match: {score}/100

Dimension breakdown:
  Tone alignment:      {score}/20 {match_emoji}
  Vocabulary match:    {score}/20 {match_emoji}
  Sentence patterns:   {score}/20 {match_emoji}
  Personality markers: {score}/20 {match_emoji}
  Platform adaptation: {score}/20 {match_emoji}

--- Drift Detected ---
1. [Tone] Line {N}: "{excerpt}" — sounds more {formal/casual} than your baseline
   Suggestion: Rephrase to "{suggestion}"

2. [Vocabulary] Line {N}: "{word}" — you never use this word
   Your usual choice: "{your_typical_word}"

3. [Personality] Missing your signature {trait}
   Consider adding: "{suggestion}"

--- On-Brand Highlights ---
1. "{excerpt}" — perfectly matches your voice
2. "{excerpt}" — strong brand personality showing

============================================
```

### Step 3: Brand Voice Guide (`/brand-voice guide`)

Generate a shareable document for collaborators or outsourced writers:

```markdown
# {Name}'s Brand Voice Guide

## Voice Summary
{2-3 sentence description of the overall voice}

## Do's
- {specific guideline with example}
- {guideline}
- {guideline}

## Don'ts
- {anti-pattern with example}
- {anti-pattern}
- {anti-pattern}

## Vocabulary
**Use these words:** {list}
**Avoid these words:** {list}
**Signature phrases:** {list}

## Tone by Platform
- X: {platform-specific tone adjustment}
- Instagram: {adjustment}
- note: {adjustment}

## Example Sentences
Good: "{on-brand example}"
Bad: "{off-brand example}"
```

Save to `~/Desktop/content-autopilot-output/brand-voice-guide.md`.

## Integration with Other Skills

- **content-grader**: Includes voice score in overall grade
- **content-writer**: References brand-voice.json during generation
- **content-brief**: Includes voice guidelines in briefs for outsourcing
- **persona-switcher**: Each persona has its own voice variant
- **content-dna**: Voice traits feed into DNA analysis

## Quality Gate

- [ ] Baseline built from sufficient data (5+ entries minimum)
- [ ] Drift detection is specific (line numbers, exact excerpts)
- [ ] Suggestions preserve meaning while fixing voice
- [ ] Platform-appropriate voice variations are acceptable (not flagged)
- [ ] Voice guide is clear enough for a stranger to follow
