---
name: persona-switcher
description: Multi-persona content generation — write the same topic from different audience perspectives (beginner, advanced, executive, etc.). Multiply content output by 2-3x from a single research session. Manage multiple personas in profile.json.
---

# Persona Switcher

Write for different audiences simultaneously — multiply your content from one idea.

## When to Activate

- User says `/persona` or `/persona {name}`
- User says `/persona create {name}`
- User asks "write this for beginners too"
- User asks "create an executive version"
- User wants to target multiple audience segments

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/persona` — List all personas and switch
### `/persona create {name}` — Create a new persona
### `/persona {name}` — Switch active persona
### `/persona write {topic}` — Generate content for all personas at once
### `/persona compare` — Show how content differs across personas

## Profile Extension: personas

Added to `~/.content-autopilot/profile.json`:

```json
{
  "personas": [
    {
      "name": "beginner",
      "label": "AI beginner",
      "audience": {
        "knowledge_level": "beginner",
        "occupation": "office workers new to AI",
        "pain_points": ["overwhelmed by AI tools", "don't know where to start"],
        "vocabulary": "no jargon, explain everything"
      },
      "style_overrides": {
        "tone": "encouraging and patient",
        "sentence_length": "short",
        "emoji_usage": "moderate"
      },
      "content_depth": "30%",
      "primary_platform": "instagram",
      "active": true
    },
    {
      "name": "advanced",
      "label": "AI power user",
      "audience": {
        "knowledge_level": "advanced",
        "occupation": "tech leads, AI practitioners",
        "pain_points": ["need cutting-edge techniques", "efficiency optimization"],
        "vocabulary": "technical terms OK, skip basics"
      },
      "style_overrides": {
        "tone": "direct and data-driven",
        "sentence_length": "medium",
        "emoji_usage": "none"
      },
      "content_depth": "90%",
      "primary_platform": "note",
      "active": true
    },
    {
      "name": "executive",
      "label": "Business decision maker",
      "audience": {
        "knowledge_level": "intermediate",
        "occupation": "CEOs, managers, business owners",
        "pain_points": ["ROI of AI adoption", "team management with AI"],
        "vocabulary": "business terms, avoid deep tech"
      },
      "style_overrides": {
        "tone": "authoritative and strategic",
        "sentence_length": "medium",
        "emoji_usage": "none"
      },
      "content_depth": "60%",
      "primary_platform": "note",
      "active": true
    }
  ]
}
```

## Workflow: Create Persona (`/persona create`)

```
Creating a new persona:

1. Persona name (short, no spaces): ___
2. Label (who they are): ___
3. Knowledge level: beginner / intermediate / advanced
4. Occupation/role: ___
5. Pain points (2-3): ___
6. Vocabulary level: simple / accessible / technical / expert
7. Preferred tone: encouraging / casual / professional / authoritative / direct
8. Primary platform: note / x / instagram

Persona "{name}" created!
Switch to it with: /persona {name}
```

## Workflow: Multi-Persona Write (`/persona write {topic}`)

Generate the same topic for ALL active personas:

### Step 1: Research Once

Research the topic once (shared across all personas).

### Step 2: Generate Per Persona

For each active persona, generate content with:
- Adjusted depth level
- Persona-specific vocabulary
- Appropriate examples and analogies
- Platform-optimized format

### Step 3: Show Comparison

```
============================================
  Multi-Persona Content: "{topic}"
  Personas: {count} active
============================================

--- Beginner Version ---
Platform: Instagram
Title: "{beginner-friendly title}"
Depth: 30% — foundational concepts only
Key difference: Explains {concept} from scratch, uses analogy
Preview: "{first 200 chars}..."

--- Advanced Version ---
Platform: note (paid)
Title: "{technical title}"
Depth: 90% — cutting-edge techniques
Key difference: Skips basics, focuses on {advanced_technique}
Preview: "{first 200 chars}..."

--- Executive Version ---
Platform: note (free)
Title: "{business-oriented title}"
Depth: 60% — strategic implications
Key difference: Focuses on ROI, team impact, decision framework
Preview: "{first 200 chars}..."

============================================
Files saved:
  ~/Desktop/content-autopilot-output/persona_beginner_{date}.md
  ~/Desktop/content-autopilot-output/persona_advanced_{date}.md
  ~/Desktop/content-autopilot-output/persona_executive_{date}.md

Content multiplied: 1 topic → {count} pieces
============================================
```

## How Content Differs by Persona

| Element | Beginner | Advanced | Executive |
|---------|----------|----------|-----------|
| Opening | Relatable problem | Data/trend | Business impact |
| Vocabulary | Plain language | Technical terms | Business jargon |
| Examples | Everyday analogies | Code/implementation | Case studies + ROI |
| Depth | What + Why | How (detailed) | So What + Now What |
| CTA | "Try this one thing" | "Implement this system" | "Bring this to your team" |
| Tone | Encouraging | Direct | Strategic |
| Length | Short (1,500-2,000) | Long (3,000-5,000) | Medium (2,000-3,000) |

## Switching Active Persona

`/persona beginner` — Switch the default content-writer persona:

```
Active persona switched to: beginner (AI beginner)

All future content generation will use this persona's settings:
  Knowledge: beginner
  Tone: encouraging and patient
  Platform: Instagram (primary)
  Depth: 30%

Switch back with: /persona advanced
Write for all at once with: /persona write {topic}
```

## Integration with Other Skills

- **content-writer**: Uses active persona for all content generation
- **batch-generator**: Can alternate personas across the week
- **repurpose**: Repurpose = same content, different platform; persona = same topic, different audience
- **series-designer**: Series can target different personas on different days
- **trend-scout**: Topic ideas filtered by active persona's knowledge level

## Quality Gate

- [ ] Each persona version is genuinely different (not just vocabulary swaps)
- [ ] Depth matches the persona's knowledge level
- [ ] Examples are appropriate for each audience
- [ ] Vocabulary doesn't leak between personas (no jargon in beginner)
- [ ] Each version stands alone as valuable content
- [ ] Platform format matches each persona's primary platform
