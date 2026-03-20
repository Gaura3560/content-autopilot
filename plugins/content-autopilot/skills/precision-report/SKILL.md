---
name: precision-report
description: Quantitative precision report for all predictive skills — compare predictions vs actuals, calculate accuracy rates, identify systematic biases, and show improvement trends. The accountability layer that keeps the system honest.
---

# Precision Report

How accurate is this system? Here are the numbers. No hiding.

## Commands

### `/precision` — Full precision report
### `/precision {skill}` — Precision for specific skill
### `/precision trend` — Accuracy trend over time

## Output

```
============================================
  System Precision Report
  Based on {N} predictions vs {N} actuals
============================================

SKILL ACCURACY RANKING:

1. best-time: {accuracy}% — {N} data points
   Bias: {none / tends to over/underestimate}

2. content-grader: {accuracy}% — {N} graded vs actual performance
   Correlation: grade score vs engagement r={correlation}

3. engagement-predictor: {accuracy}% — {N} predictions
   Avg error: ±{percentage}%
   Bias: overestimates by {N}% on average

4. revenue-forecast: {accuracy}% — {N} months predicted
   Avg error: ±¥{amount}

5. readability-tuner: {accuracy}% — target level match
   Verified by: audience-simulator alignment

IMPROVEMENT TREND:
  Month 1: {overall_accuracy}% (few data points)
  Month 2: {accuracy}% (improving)
  Month 3: {accuracy}% (stabilizing)

SYSTEMATIC BIASES:
  - engagement-predictor overestimates X thread performance by {N}%
  - revenue-forecast underestimates membership revenue
  - content-grader hook score doesn't correlate with actual CTR

ACTIONS TO IMPROVE PRECISION:
  1. Log {N} more performance entries (/perf-log)
  2. Complete {N} more A/B tests (/ab-test)
  3. Recalibrate predictor (/confidence calibrate)

============================================
```

Integrates with: ALL predictive skills, performance-log (actuals), confidence-score (calibration), meta-learning (which predictions users trust).
