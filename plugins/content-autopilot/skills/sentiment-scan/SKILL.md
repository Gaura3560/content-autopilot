---
name: sentiment-scan
description: Content sentiment and emotional tone analysis — quantify the emotional profile of your content (positive/negative/neutral, excitement/calm, confidence/uncertainty). Detect mismatches between intended and actual tone. Ensure every piece evokes the emotion you want.
---

# Sentiment Scan

Your content has an emotional fingerprint — make sure it's the one you intended.

## When to Activate

- User says `/sentiment {file_path}` or `/sentiment`
- User asks "what emotion does this evoke?"
- User asks "is the tone right?"
- Auto-called by brand-voice for tone component

## Prerequisites

- Content file to analyze

## Commands

### `/sentiment {file_path}` — Analyze emotional tone
### `/sentiment compare {file1} {file2}` — Compare emotional profiles
### `/sentiment adjust {file_path} {target_emotion}` — Adjust tone

## Emotional Dimensions

| Dimension | Scale | Detects |
|-----------|-------|---------|
| Valence | Positive ←→ Negative | Overall optimism/pessimism |
| Arousal | Exciting ←→ Calm | Energy level |
| Confidence | Assertive ←→ Uncertain | Authority level |
| Warmth | Personal ←→ Distant | Connection level |
| Urgency | Urgent ←→ Relaxed | Time pressure |

## Workflow

### Step 1: Analyze Content

Scan every sentence for emotional markers:

```
Sentiment Analysis: "{title}"
============================================

--- Overall Emotional Profile ---

Valence:    [██████████░░░░] 72% Positive
Arousal:    [████████░░░░░░] 58% Exciting
Confidence: [███████████░░░] 82% Assertive
Warmth:     [███████░░░░░░░] 52% Personal
Urgency:    [████░░░░░░░░░░] 30% Relaxed

Primary emotion: Inspiring (confident + positive + moderate energy)
Secondary emotion: Educational (assertive + calm)

--- Section-by-Section ---

Introduction (lines 1-8):
  Emotion: Curiosity (question + tension)
  Strength: Strong — good hook energy

Section 1 (lines 9-22):
  Emotion: Informative (neutral + confident)
  Strength: Steady — maintains trust

Section 2 (lines 23-38):
  Emotion: Exciting (positive + high energy)
  Strength: Peak — this is where the content shines

Conclusion (lines 39-48):
  Emotion: Motivating (positive + urgent + warm)
  Strength: Good close — drives action

--- Emotional Arc ---

[Curious] → [Informed] → [Excited] → [Motivated]
       ↑ hook    ↑ build     ↑ peak      ↑ close

This follows the {pattern_name} emotional arc.
Effectiveness: {high/medium/low} for {platform}

============================================
```

### Step 2: Detect Tone Mismatches

```
--- Tone Alignment Check ---

Your intended tone (from profile.json): {authoritative yet approachable}

Mismatch detected:
  Line {N}: "{sentence}" — reads as {aggressive}, not {authoritative}
  Suggestion: Soften with "{revised_sentence}"

  Line {N}: "{sentence}" — reads as {distant}, not {approachable}
  Suggestion: Add personal touch: "{revised_sentence}"

Alignment score: {percentage}% match with intended tone
```

### Step 3: Adjust Tone (`/sentiment adjust {file} inspiring`)

```
Adjusting tone to: "inspiring"

Changes:
  1. Line {N}: Increased positive valence
     Before: "{neutral_sentence}"
     After: "{positive_sentence}"

  2. Line {N}: Increased energy/arousal
     Before: "{calm_sentence}"
     After: "{energetic_sentence}"

  3. Line {N}: Added warmth/personal touch
     Before: "{distant_sentence}"
     After: "{warm_sentence}"

Adjustments: {count}
New emotional profile: {updated_scores}
```

## Integration with Other Skills

- **brand-voice**: Sentiment is the emotional layer of voice consistency
- **content-grader**: Tone alignment score included in grade
- **engagement-predictor**: Emotional profile affects predicted engagement
- **persona-switcher**: Each persona has target emotional profile
- **content-writer**: Target emotion specified during generation

## Quality Gate

- [ ] Sentiment analysis covers all emotional dimensions
- [ ] Section-by-section breakdown provided (not just overall)
- [ ] Mismatches are specific (line numbers, examples)
- [ ] Adjustments preserve meaning while changing tone
- [ ] Emotional arc is analyzed (not just flat average)
