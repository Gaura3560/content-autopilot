---
name: engagement-predictor
description: Predict engagement before publishing — score expected performance based on content-dna patterns, algorithm alignment, posting time, hook strength, title logic history, and audience match. Know if a post will land BEFORE it goes live.
---

# Engagement Predictor

Know how your content will perform before you publish — data-driven prediction, not guesswork.

## When to Activate

- User says `/engagement-predict {file_path}` or `/predict-engagement {file}`
- User asks "how will this post perform?"
- User asks "should I publish this or improve it first?"
- Auto-suggested by daily-autopilot after content generation

## Prerequisites

- `~/.content-autopilot/content-history.json` (10+ entries for baseline)
- `~/.content-autopilot/content-dna.json` (for pattern matching)
- `~/.content-autopilot/algorithm-guide.json` (for platform alignment)
- Content file to evaluate

## Commands

### `/predict-engagement {file_path}` — Predict engagement for a file
### `/predict-engagement compare {file1} {file2}` — Compare two pieces
### `/predict-engagement optimize {file_path}` — Predict + suggest improvements

## Prediction Factors

| Factor | Weight | Source |
|--------|--------|--------|
| Hook strength | 25% | Hook type vs your DNA's strongest hooks |
| Title logic match | 20% | A/B history win rates for this logic combo |
| Algorithm alignment | 15% | Current platform boost/suppress signals |
| Posting time | 10% | best-times.json optimal window |
| Topic DNA match | 15% | Is this your sweet spot topic? |
| Format match | 10% | Your best-performing format on this platform |
| Content length | 5% | Optimal range for this platform |

## Workflow

### Step 1: Analyze Content

Read the file and extract:
- Platform (from filename)
- Hook type and strength
- Title logics used
- Topic category
- Content format and length
- Posting time (if specified)

### Step 2: Compare Against Baselines

Cross-reference with all historical data:

```
Analyzing "{title}" against your performance history...

Hook: "{first_line}"
  Type: {data_hook}
  Your data hook win rate: {X}% (from {N} uses)
  Baseline: your average hook is {type} at {Y}%
  Prediction factor: {above/at/below} baseline

Title: "{title}"
  Logics: {Numbers + Paradox}
  Your win rate for this combo: {X}% (from {N} A/B tests)
  Prediction factor: {above/at/below}

Algorithm: {platform}
  Current boosts: {content_type} — your content {matches/doesn't match}
  Current suppresses: {behavior} — {clear/flagged}
  Prediction factor: {favorable/neutral/unfavorable}

Topic: "{topic_category}"
  Your sweet spot match: {X}% overlap
  Prediction factor: {strong/moderate/weak}

Format: {thread/article/carousel}
  Your best format on {platform}: {format}
  This content: {matches/differs}
  Prediction factor: {optimal/suboptimal}
```

### Step 3: Generate Prediction

```
============================================
  Engagement Prediction
  Content: "{title}"
  Platform: {platform}
============================================

Predicted engagement: {score}/100

  Compared to your average: {+X% / -X% / on par}

  Breakdown:
    Hook strength:       {score}/25 — {reason}
    Title logic:         {score}/20 — {reason}
    Algorithm alignment: {score}/15 — {reason}
    Topic DNA match:     {score}/15 — {reason}
    Posting time:        {score}/10 — {reason}
    Format match:        {score}/10 — {reason}
    Content length:      {score}/5  — {reason}

  Prediction confidence: {low/medium/high}
  (based on {N} historical data points)

--- Verdict ---
{score >= 75}: STRONG — publish as-is, this should perform well
{score 50-74}: DECENT — publishable, but improvements below could boost it
{score < 50}: WEAK — consider the improvements below before publishing

--- Improvement Opportunities ---
(changes that would increase the predicted score)

1. [+{points}] Change hook to {type}: "{suggested_hook}"
   Reason: Your {type} hooks average {X}% higher engagement

2. [+{points}] Post at {time} instead of {current_time}
   Reason: {time} is your peak engagement window

3. [+{points}] Add {element} to match current algorithm preference
   Reason: {platform} currently boosts {element}

If all improvements applied: predicted score {new_score}/100 (+{gain})

============================================
```

### Step 4: Compare Mode

`/predict-engagement compare file1.md file2.md`:

```
Head-to-head prediction:

"{title_1}": {score_1}/100
"{title_2}": {score_2}/100

Winner: "{title}" by +{difference} points

Key differences:
  Hook: {file_1} {score} vs {file_2} {score}
  Title: {file_1} {score} vs {file_2} {score}
  ...

Recommendation: Publish "{winner_title}" — {reason}
```

## Integration with Other Skills

- **content-grader**: Grader = quality, predictor = expected results
- **daily-autopilot**: Show prediction after content generation
- **batch-generator**: Rank batch content by predicted performance
- **content-dna**: Core data source for prediction model
- **algorithm-guide**: Platform optimization alignment
- **weekly-report**: Compare predictions vs actual results

## Calibration

Track prediction accuracy over time:
```
Prediction accuracy (last 30 days):
  Predictions made: {count}
  Within ±20% of actual: {percentage}%
  Overestimated: {count} times
  Underestimated: {count} times

  Calibration: {good/needs adjustment}
```

## Quality Gate

- [ ] Prediction based on actual historical data (not fabricated)
- [ ] Confidence level honestly reflects data availability
- [ ] Improvement suggestions are specific and actionable
- [ ] Low-data situations clearly flagged as low confidence
- [ ] Not presented as guaranteed outcome — always a prediction
