---
name: deep-audit
description: Full system integrity audit — check all data files for consistency, find broken references, stale data, and cross-skill contradictions. Ensure 129 skills are working as one coherent system, not 129 isolated tools.
---

# Deep Audit

129 skills. 15+ data files. Are they all in sync?

## Commands

### `/deep-audit` — Full system audit
### `/deep-audit fix` — Auto-fix detected issues

## Checks

```
============================================
  System Deep Audit
============================================

DATA FILES:
  [x] profile.json — valid, complete
  [x] content-history.json — {N} entries, no orphans
  [ ] content-dna.json — STALE ({N} days old, {N} new entries since)
  [x] algorithm-guide.json — updated {N} days ago
  [ ] best-times.json — MISSING (run /best-time)
  [x] monetize-data.json — {N} entries

CROSS-REFERENCES:
  [x] content-history ↔ vault — all referenced files exist
  [ ] content-history ↔ performance — {N} entries missing perf data
  [x] active-series ↔ content-history — series entries aligned
  [ ] hook-library ↔ content-dna — {N} hooks not scored

FEEDBACK LOOPS:
  [x] perf-log → content-dna: connected
  [ ] ab-test → content-dna: {N} results not applied
  [x] post-mortem → hook-library: connected
  [ ] confidence calibration: {N} days since last calibrate

ISSUES: {count} | WARNINGS: {count} | HEALTHY: {count}

Auto-fix available for {N} issues. Run /deep-audit fix
============================================
```

Integrates with: ALL data files, confidence-score (triggers recalibration), feedback-loop-status.
