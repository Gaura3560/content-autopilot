---
name: audience-simulator
description: Simulate how different audience segments would react to your content before publishing — predict where beginners get confused, where experts get bored, where skeptics disengage, and where fans share. The virtual focus group for content creators.
---

# Audience Simulator

Test your content on virtual readers before real ones see it.

## When to Activate

- User says `/audience-sim {file_path}` or `/simulate {file}`
- User asks "how will my audience react to this?"
- User asks "will beginners understand this?"
- User wants pre-publish audience feedback without real testing

## Prerequisites

- `~/.content-autopilot/profile.json` (audience definition)
- Content file to simulate
- Optional: `content-dna.json` (for calibration from real performance data)

## Commands

### `/simulate {file_path}` — Full audience simulation
### `/simulate {file_path} {segment}` — Simulate specific segment
### `/simulate {file_path} heatmap` — Generate attention heatmap

## Audience Segments

| Segment | Behavior | Key Metric |
|---------|----------|-----------|
| First-time visitor | Scanning, deciding if worth reading | Will they keep reading past line 5? |
| Loyal follower | Reading carefully, comparing to past content | Will they share it? |
| Beginner | Needs explanation, gets lost easily | Where do they get confused? |
| Expert | Skims for new insights, critical of depth | Where do they get bored? |
| Skeptic | Questions everything, needs proof | Where do they disengage? |
| Potential customer | Evaluating if your paid content is worth buying | Will they click the CTA? |

## Workflow

### Step 1: Simulate Reading Experience

For each segment, simulate a read-through:

```
============================================
  Audience Simulation: "{title}"
  Segments: 6 virtual readers
============================================

--- FIRST-TIME VISITOR ---
Simulated behavior:
  Line 1-3: {reading/scanning}
  Decision point (line 5): {CONTINUE / BOUNCE}
  "{first_line}" — {compelling enough? / not enough?}

  Predicted: {X}% would continue reading
  Issue: {if bounce rate high, explain why}
  Fix: {specific suggestion to improve hook}

--- LOYAL FOLLOWER ---
Simulated behavior:
  Reading: Full read-through
  Engagement points:
    Line {N}: "{excerpt}" — would like/save this
    Line {N}: "{excerpt}" — would share this with quote
    Line {N}: "{excerpt}" — would comment on this

  Share probability: {percentage}%
  Comment probability: {percentage}%
  Save probability: {percentage}%

--- BEGINNER ---
Simulated behavior:
  Confusion points:
    Line {N}: "{jargon}" — lost here (no explanation)
    Line {N}: "{concept}" — needs analogy or example
    Line {N}: "{logical_leap}" — too fast, needs intermediate step

  Drop-off prediction: Line {N} ({percentage}% would stop here)
  Completion rate: {percentage}%
  Understanding score: {score}/10

--- EXPERT ---
Simulated behavior:
  Boredom points:
    Line {N}: "{basic_explanation}" — already know this, skip
    Line {N}: "{shallow_analysis}" — want more depth here

  Value points:
    Line {N}: "{insight}" — this is genuinely useful, even for experts

  "Worth my time" score: {score}/10
  Would they recommend to peers: {yes/no}

--- SKEPTIC ---
Simulated behavior:
  Doubt points:
    Line {N}: "{unsupported_claim}" — "Where's the evidence?"
    Line {N}: "{logical_fallacy}" — "That doesn't follow"
    Line {N}: "{anecdote_as_proof}" — "That's just one case"

  Trust points:
    Line {N}: "{cited_data}" — "OK, that's credible"
    Line {N}: "{acknowledged_limitation}" — "Honest, I respect that"

  Convinced score: {score}/10

--- POTENTIAL CUSTOMER ---
Simulated behavior:
  Interest curve:
    Lines 1-10: {building interest / neutral / declining}
    Lines 11-30: {engagement level}
    CTA encounter: Line {N}

  CTA reaction: "{would they click? why/why not}"
  Purchase intent: {score}/10
  Objections: {what's stopping them from buying}

============================================

--- ATTENTION HEATMAP ---

Line  | Visitor | Follower | Beginner | Expert | Skeptic | Customer
1-5   | ████    | ████     | ████     | ██     | ███     | ███
6-10  | ███     | ████     | ███      | ██     | ███     | ███
11-20 | ██      | ████     | ██       | ███    | ████    | ████
21-30 | █       | ████     | █        | ████   | ██      | ████
31-40 | █       | ███      | █        | ████   | ██      | ███
CTA   | █       | ███      | █        | ██     | █       | ████

Legend: ████ high attention  ██ medium  █ low/lost

Key insight: {biggest takeaway from the heatmap}

============================================

--- COMBINED RECOMMENDATIONS ---

Critical (affects all segments):
  1. {issue affecting 4+ segments}

Segment-specific:
  2. For beginners: {fix}
  3. For skeptics: {fix}
  4. For customers: {fix}

If all fixes applied:
  Predicted completion rate: {before}% → {after}%
  Predicted share rate: {before}% → {after}%
  Predicted CTA click rate: {before}% → {after}%

============================================
```

## Calibration with Real Data

When performance-log data is available:
```
Simulation calibration:
  Previous simulation predicted: {X}% engagement
  Actual result: {Y}% engagement
  Accuracy: {percentage}%

  Adjusting simulation weights based on real data...
  Future simulations will be {more/less} {conservative/optimistic}
```

## Integration with Other Skills

- **multi-review**: Multi-review = quality perspectives; audience-sim = reader experience
- **engagement-predictor**: Simulation data enhances prediction accuracy
- **readability-tuner**: Beginner simulation identifies readability issues
- **persona-switcher**: Each persona maps to a simulation segment
- **content-grader**: Simulation results inform grade calibration
- **performance-log**: Real data calibrates future simulations

## Quality Gate

- [ ] Each segment has genuinely distinct behavior pattern
- [ ] Confusion/boredom/doubt points are specific (line numbers)
- [ ] Attention heatmap reflects realistic reading behavior
- [ ] Recommendations are actionable and prioritized
- [ ] Simulation acknowledges it's predictive, not definitive
- [ ] Calibrated against real data when available
