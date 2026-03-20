---
name: feedback-loop-status
description: Verify that all feedback loops are connected and functioning — perf-log feeds DNA, DNA feeds writer, writer feeds perf-log. If any link is broken, the system stops learning. This skill ensures continuous improvement is actually happening.
---

# Feedback Loop Status

The system is only smart if the loops are closed. Are they?

## Commands

### `/loop-status` — Check all feedback loops
### `/loop-status fix` — Reconnect broken loops

## Feedback Loops

```
============================================
  Feedback Loop Health
============================================

LOOP 1: Performance → DNA → Writer
  perf-log → content-dna: {CONNECTED / BROKEN — {N} unprocessed}
  content-dna → content-writer: {CONNECTED / STALE}
  Status: {HEALTHY / NEEDS UPDATE}
  Fix: /content-dna update

LOOP 2: A/B Test → DNA → Predictor
  ab-test results → content-dna: {status}
  content-dna → engagement-predictor: {status}
  Status: {HEALTHY / BROKEN}
  Fix: /ab-test apply

LOOP 3: Post-Mortem → Hooks + CTA
  post-mortem lessons → hook-library: {status}
  post-mortem lessons → smart-cta: {status}
  Status: {status}

LOOP 4: Predictor → Actual → Calibrate
  engagement-predictor → perf-log comparison: {status}
  confidence calibration: {last run: {date}}
  Status: {status}

OVERALL: {N}/{4} loops healthy
  System learning rate: {active/degraded/stalled}

============================================
```

Integrates with: deep-audit (sub-check), confidence-score (calibration trigger), all feedback-producing skills.
