---
name: viral-reverse
description: Reverse-engineer viral content — paste a URL or text of content that went viral, and get a structural breakdown of WHY it worked (hook, narrative arc, emotional triggers, CTA, timing). Then generate a version adapted to your topic and style.
---

# Viral Reverse Engineering

Deconstruct why content went viral — then build your own version.

## When to Activate

- User says `/viral-reverse {url}` or `/viral {url}`
- User says `/viral {text}`
- User asks "why did this go viral?"
- User asks "how can I make something like this?"
- User pastes a viral post and asks for analysis

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- URL or text of viral content to analyze

## Commands

### `/viral {url}` — Analyze a viral post by URL
### `/viral {text}` — Analyze pasted viral content
### `/viral adapt {url} {your_topic}` — Analyze AND generate your version

## Workflow

### Step 1: Fetch Content

**If URL provided:**
- Use WebFetch/WebSearch to retrieve the content
- Extract: full text, engagement metrics (if visible), author, platform, date

**If text provided:**
- Use the pasted text directly
- Ask which platform it's from if not obvious

### Step 2: Structural Breakdown

Analyze every element of the viral content:

```
============================================
  Viral Reverse Engineering
  Source: {platform} | Author: {author}
  Engagement: {metrics if available}
============================================

--- 1. HOOK ANALYSIS ---
Opening: "{first line/sentence}"
Hook type: {surprise/data/question/story/empathy/authority/urgency}
Hook strength: {score}/10
Why it works: {specific explanation}
  - {element 1}: {why this grabs attention}
  - {element 2}: {cognitive trigger it activates}

--- 2. NARRATIVE STRUCTURE ---
Format: {thread/article/carousel/single post}
Arc: {pattern name}
  Opening: {what it does in the first 10%}
  Rising: {how tension/curiosity builds}
  Climax: {the peak insight/reveal}
  Resolution: {how it wraps up}
  CTA: {what action it asks for}

Flow map:
  [Hook] → [Problem] → [Tension] → [Reveal] → [Proof] → [CTA]
  or
  [Hook] → [Promise] → [Step 1] → [Step 2] → ... → [Payoff] → [CTA]

--- 3. EMOTIONAL TRIGGERS ---
Primary emotion: {curiosity/fear/aspiration/outrage/humor/belonging}
Secondary emotion: {emotion}
Trigger mechanism:
  - "{specific phrase}" → triggers {emotion} because {reason}
  - "{specific phrase}" → triggers {emotion} because {reason}

Emotional arc: {neutral → curious → surprised → motivated}

--- 4. VALUE MECHANICS ---
Value type: {practical/entertainment/social currency/identity/information}
Shareability driver: "People share this because {reason}"
Save driver: "People save this because {reason}"
Comment driver: "People comment because {reason}"

--- 5. TITLE/HEADLINE ANALYSIS ---
Title: "{title}"
Title logics used: {logic 1} + {logic 2}
Why it works: {specific analysis}
Character count: {count} | Optimal for: {platform}

--- 6. TIMING & CONTEXT ---
Posted: {date/time if known}
Context: {what was happening in the world/niche that made this timely}
Evergreen potential: {high/medium/low}

--- 7. PLATFORM OPTIMIZATION ---
Platform-specific elements:
  - {element 1}: {how it leverages platform features}
  - {element 2}: {algorithm-friendly aspects}
  - {element 3}: {engagement triggers}

============================================

VIRAL FORMULA SUMMARY:
{hook_type} hook + {emotion} emotion + {value_type} value
+ {structure} structure + {timing} timing
= Viral potential

Replicability score: {score}/10
(How easily this pattern can be applied to other topics)

============================================
```

### Step 3: Generate Your Version

If user requests adaptation (`/viral adapt {url} {topic}`):

```
--- Your Adapted Version ---

Original pattern: {summary of viral structure}
Your topic: {user_topic}
Your style: {from profile.json}

Adapted content:

{Full content piece following the same structure but with user's topic,
voice, and platform preferences. Maintains the viral mechanics while
being original content.}

--- Adaptation Notes ---
Kept from original:
  - {structural element preserved}
  - {emotional trigger replicated}
  - {hook pattern adapted}

Changed for your brand:
  - {topic-specific adjustment}
  - {style adaptation}
  - {platform optimization}
```

### Step 4: Save to Swipe File

If swipe-file skill is available:
```
Save this analysis to your swipe file? (yes / no)
```

If yes, save the structural breakdown and adaptation to swipe-file.

## Pattern Library

Common viral patterns identified across platforms:

| Pattern | Structure | Best For |
|---------|-----------|----------|
| Curiosity Loop | Hook → tease → reveal → tease → reveal → CTA | X threads |
| Contrarian Bomb | Bold claim → evidence → "but here's what no one says" | Hot takes |
| Data Storytelling | Surprising stat → context → implication → action | note articles |
| Transformation Arc | Before → struggle → discovery → after → how | Story content |
| List Escalation | Good → better → best → mind-blowing | Listicles |
| Mystery Reveal | Question → wrong answers → right answer → why | Educational |

## Quality Gate

- [ ] Analysis is based on the actual content (not assumptions)
- [ ] Emotional triggers are specifically identified (not generic)
- [ ] Adapted version is genuinely original (not a copy with swapped words)
- [ ] Replicability score honestly reflects difficulty
- [ ] Platform-specific optimization points are accurate
- [ ] Viral mechanics are explained in transferable terms
