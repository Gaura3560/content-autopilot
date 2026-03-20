---
name: smart-cta
description: Data-driven CTA optimization engine — generates the best call-to-action for each content piece based on A/B history, funnel position, platform conventions, and algorithm-guide data. Replaces guesswork with evidence-based CTA selection.
---

# Smart CTA Engine

Generate the highest-converting CTA for every piece of content — powered by your data.

## When to Activate

- User says `/smart-cta` or `/cta`
- User says `/cta {platform} {funnel_stage}`
- User asks "what CTA should I use?"
- Auto-called by content-writer when generating CTAs

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- `~/.content-autopilot/content-history.json` (for pattern learning)
- Optional: `algorithm-guide.json` (for platform-specific optimization)

## Commands

### `/cta` — Interactive CTA generator
### `/cta {platform} {funnel_stage}` — Generate CTA for specific context
### `/cta analyze` — Analyze CTA performance across your history
### `/cta library` — Browse CTA templates by category

## CTA Decision Matrix

| Platform | Funnel Stage | Primary CTA | Secondary CTA |
|----------|-------------|-------------|---------------|
| X | TOFU | RT + Follow | note link |
| X | MOFU | note link | Thread bookmark |
| X | BOFU | Paid article link | Membership link |
| Instagram | TOFU | Save + Share | Profile link |
| Instagram | MOFU | Link in bio | DM for resource |
| Instagram | BOFU | Profile link → paid | Swipe up (Stories) |
| note | MOFU (free) | Like + Follow | Related article |
| note | BOFU (paid) | Next article | Membership |
| Newsletter | Any | Click through | Forward to friend |

## Workflow

### Step 1: Determine Context

Gather:
- Platform (x/instagram/note/newsletter)
- Funnel stage (TOFU/MOFU/BOFU)
- Content type (thread/article/carousel/single)
- Content topic
- Algorithm current preferences (from algorithm-guide.json)

### Step 2: Analyze Historical CTA Performance

If content-history.json has sufficient data:
```
CTA Performance Analysis:

By action type:
  "Follow" CTAs: used {N} times — {effectiveness}
  "Save" CTAs: used {N} times — {effectiveness}
  "Link" CTAs: used {N} times — {effectiveness}
  "Reply" CTAs: used {N} times — {effectiveness}
  "RT/Share" CTAs: used {N} times — {effectiveness}

By platform:
  X: "{best_performing_cta}" works best
  Instagram: "{best_performing_cta}" works best
  note: "{best_performing_cta}" works best

By funnel stage:
  TOFU: {best_cta_type} — {reason}
  MOFU: {best_cta_type} — {reason}
  BOFU: {best_cta_type} — {reason}
```

### Step 3: Generate Optimized CTAs

Provide 3 CTA options ranked by predicted effectiveness:

```
Smart CTA Recommendations:
Platform: {platform} | Stage: {stage} | Topic: {topic}

1. [Recommended] "{cta_text}"
   Type: {action_type}
   Why: {reason based on data + algorithm + platform}
   Placement: {where in the content}

2. [Alternative] "{cta_text}"
   Type: {action_type}
   Why: {reason}
   Placement: {where}

3. [Experimental] "{cta_text}"
   Type: {action_type}
   Why: Untested pattern — worth trying for data
   Placement: {where}
```

### Step 4: CTA Templates by Category

**Engagement CTAs (boost algorithm signals):**
```
X: "Like if you agree. RT if someone needs to hear this."
X: "Which point surprised you? Reply with the number."
IG: "Save this for when you need it (bookmark icon)"
IG: "Tag someone who needs to see this"
note: "This helped you? Hit 'suki' to help others find it too"
```

**Traffic CTAs (drive funnel flow):**
```
X→note: "Full breakdown with templates → {note_url}"
X→note: "The 70% I didn't share here is on note → link in bio"
IG→note: "Complete guide on note — link in profile"
note free→paid: "Templates + step-by-step in the paid version ↓"
```

**Community CTAs (build relationships):**
```
X: "I'm curious — what's your experience with {topic}?"
IG: "DM me '{keyword}' and I'll send you the {resource}"
note: "What topic should I cover next? Comment below"
```

**Conversion CTAs (monetize):**
```
note: "This article gives you the 'what'. The paid version gives you the 'how'."
note: "Monthly members get this + {N} more exclusive articles → {membership_url}"
X: "I put everything I know about {topic} into one guide → {paid_url}"
```

### Step 5: Algorithm-Aligned Optimization

Check algorithm-guide.json for current platform preferences:
```
Algorithm alignment:
  X currently boosts: {engagement_type} → use CTA type: {recommended}
  Instagram currently boosts: {behavior} → use CTA type: {recommended}
  Avoid: {suppressed_behavior} — don't use {cta_type} right now
```

## Integration with Other Skills

- **content-writer**: Calls smart-cta for every piece of content's CTA
- **engagement-templates**: CTA logic informs template selection
- **content-grader**: CTA Clarity score uses smart-cta analysis
- **launch-sequence**: Each launch day gets optimized CTAs
- **content-dna**: CTA patterns feed into DNA analysis

## Quality Gate

- [ ] CTAs are platform-appropriate (length, format, tone)
- [ ] Funnel stage alignment is correct
- [ ] Algorithm preferences factored in (if data available)
- [ ] Historical performance considered (if data available)
- [ ] CTAs feel natural within the content (not forced)
- [ ] Experimental option included for continuous learning
