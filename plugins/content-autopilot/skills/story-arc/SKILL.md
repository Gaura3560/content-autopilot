---
name: story-arc
description: Narrative framework library — apply Hero's Journey, 3-act structure, Kishōtenketsu, or Freytag's Pyramid to your content. Transform flat information into compelling narratives that readers can't stop reading. The structure behind every great story.
---

# Story Arc

Facts inform. Stories transform. Give your content narrative power.

## When to Activate

- User says `/story-arc {type}` or `/story-arc {file}`
- User asks "make this into a story"
- User asks "structure this as a narrative"
- User wants to transform informational content into narrative content

## Prerequisites

- Content file or topic + source material

## Available Story Arcs

| Arc | Structure | Best For |
|-----|-----------|----------|
| Hero's Journey | Call → Trials → Transformation → Return | Personal transformation stories |
| 3-Act | Setup → Confrontation → Resolution | Article/thread structure |
| Kishōtenketsu | Introduction → Development → Twist → Conclusion | Japanese audience, surprise reveals |
| Freytag's Pyramid | Exposition → Rising → Climax → Falling → Resolution | Dramatic narratives |
| Sparkline | What Is → What Could Be (alternating) | Persuasive presentations |
| In Medias Res | Start in the middle → Flashback → Resolution | Attention-grabbing openings |

## Commands

### `/story-arc {type} {file}` — Apply arc to existing content
### `/story-arc {type} {topic}` — Write new content with arc
### `/story-arc detect {file}` — Detect narrative structure in content
### `/story-arc all` — Show all arcs with examples

## Workflow

### Step 1: Apply Story Arc

**Kishōtenketsu (Japanese-optimized):**
```
Applying Kishōtenketsu to: "{topic}"

起 (Ki — Introduction):
  "{Set the scene — introduce the topic naturally}"
  Establish the world the reader knows.

承 (Shō — Development):
  "{Develop the idea — build understanding}"
  Go deeper, add examples, build the foundation.

転 (Ten — Twist):
  "{The unexpected turn — this is where magic happens}"
  Challenge everything established. The "but actually..."
  This is the moment readers screenshot and share.

結 (Ketsu — Conclusion):
  "{Bring it together — new understanding}"
  Reconcile the twist with the setup. Reader sees topic differently.

Why Kishōtenketsu works for Japanese audiences:
  - No antagonist needed (unlike Hero's Journey)
  - Surprise/revelation drives engagement
  - Natural flow for educational content
  - The "転" is what gets shared on X
```

**Hero's Journey (for personal stories):**
```
1. Ordinary World: "{your life before the change}"
2. Call to Adventure: "{what triggered the journey}"
3. Refusal: "{initial resistance or doubt}"
4. Mentor/Guide: "{who or what helped you}"
5. Crossing the Threshold: "{committing to the change}"
6. Trials: "{specific challenges faced}"
7. The Ordeal: "{the hardest moment}"
8. Reward: "{what you gained}"
9. Return: "{sharing the knowledge with others — this article}"
```

### Step 2: Transform Content

```
Story Arc Transformation: "{title}"
============================================

BEFORE (flat structure):
  Heading 1: What is {topic}
  Heading 2: Why it matters
  Heading 3: How to do it
  Heading 4: Conclusion
  Feel: Textbook

AFTER (Kishōtenketsu):
  起: "When I first heard about {topic}, I thought..."
  承: "The standard approach is {method}. It works because..."
  転: "But here's what nobody tells you: {twist}"
  結: "Once you see {topic} through this lens..."
  Feel: Discovery journey

Changes: Structure rewritten, examples reframed as narrative,
data points woven into story rather than listed.
============================================
```

## Integration with Other Skills

- **content-writer**: Story arc applied during content generation
- **story-bank**: Personal stories slotted into arc positions
- **series-designer**: Multi-day series use overarching story arc
- **persuasion-framework**: Story arc + persuasion = maximum impact
- **voice-script**: Spoken content especially benefits from narrative structure

## Quality Gate

- [ ] Arc structure is followed faithfully
- [ ] Content retains informational value (story doesn't replace substance)
- [ ] The "twist" or turning point is genuinely surprising
- [ ] Narrative flows naturally (not forced into the framework)
- [ ] Appropriate arc selected for the content type
