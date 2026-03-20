---
name: confidence-score
description: Add confidence levels to ALL system recommendations — distinguish "based on 50 data points (high confidence)" from "educated guess (low confidence)". Every prediction, suggestion, and analysis gets a transparent confidence tag so users know what to trust.
---

# Confidence Score

Not all recommendations are equal. Know which ones to trust and which ones to question.

## When to Activate

- User says `/confidence` or `/confidence status`
- Auto-applied: every skill output should include confidence tagging
- User asks "how sure are you about this?"

## Commands

### `/confidence` — System-wide confidence report
### `/confidence {skill}` — Confidence level for a specific skill
### `/confidence calibrate` — Recalibrate based on prediction vs actual

## Confidence Levels

| Level | Symbol | Basis | Trust Level |
|-------|--------|-------|-------------|
| Very High | ★★★★★ | 30+ data points + validated by A/B test | Act on this |
| High | ★★★★ | 15-29 data points from performance-log | Strongly consider |
| Medium | ★★★ | 5-14 data points or cross-referenced estimates | Use with judgment |
| Low | ★★ | < 5 data points or single-source estimate | Treat as hypothesis |
| Guess | ★ | No data, pure heuristic/general knowledge | Test before trusting |

## Workflow

### System-Wide Report

```
============================================
  System Confidence Report
============================================

Data foundation:
  content-history entries: {N}
  Entries with performance data: {N}/{total} ({percentage}%)
  A/B tests completed: {N}
  DNA last updated: {date}

Skill confidence levels:

HIGH CONFIDENCE (★★★★+):
  content-dna: ★★★★ — based on {N} entries with performance
  best-time: ★★★★ — confirmed by {N} posts across time slots
  smart-cta: ★★★★ — {N} CTA variants tested

MEDIUM CONFIDENCE (★★★):
  engagement-predictor: ★★★ — {N} predictions vs actuals
  content-grader: ★★★ — calibrated against {N} benchmarks
  trend-scout: ★★★ — WebSearch-based, variable quality

LOW CONFIDENCE (★★):
  audience-psychograph: ★★ — inferred, not surveyed
  revenue-forecast: ★★ — only {N} months of data
  content-genome: ★★ — limited niche sample

TO IMPROVE CONFIDENCE:
  1. Log performance for {N} unlogged posts → raises ALL confidence
  2. Complete {N} more A/B tests → confirms DNA hypotheses
  3. Run /original-research survey → validates psychograph

============================================
```

### Per-Skill Confidence

Every skill output includes:
```
[Confidence: ★★★★ HIGH — based on 23 performance-logged entries]
```
or
```
[Confidence: ★★ LOW — estimate based on limited data. Log more performance with /perf-log to improve.]
```

### Calibration

```
/confidence calibrate

Comparing predictions vs actuals (last 30 days):

  engagement-predictor:
    Predictions: {N}
    Accuracy (within ±20%): {percentage}%
    Bias: {over/under-estimates by {X}%}
    Adjusted: confidence ★★★ → ★★★★ (improving)

  revenue-forecast:
    Predictions: {N}
    Accuracy: {percentage}%
    Adjusted: confidence ★★ → ★★ (needs more data)

Calibration applied. Future predictions adjusted for known biases.
```

## Integration

- **ALL skills**: Every skill's output tagged with confidence level
- **advisor**: Recommendations sorted by confidence (high-confidence first)
- **performance-log**: More data → higher confidence everywhere
- **ab-test-runner**: Completed tests upgrade confidence from ★★ to ★★★★

## Quality Gate

- [ ] Every recommendation has a visible confidence tag
- [ ] Confidence levels based on actual data availability
- [ ] Calibration compares predictions vs actuals
- [ ] "How to improve confidence" actions are specific
- [ ] Low confidence is flagged, not hidden
