---
name: hook-library
description: Curated library of high-performing hook sentences and opening lines — categorized by type (surprise, empathy, question, data, story). Auto-populated from content-history and manually added entries. Referenced by content-writer for inspiration.
---

# Hook Library

Build and browse a library of powerful opening lines to hook your audience.

## When to Activate

- User says `/hook-library` or `/hooks`
- User says `/hooks add "{hook}"`
- User asks "give me a good opening line"
- User asks "how should I start this post?"
- Referenced by content-writer for hook inspiration

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- `~/.content-autopilot/hook-library.json` (created automatically)

## Commands

### `/hooks` — Browse the hook library
### `/hooks {category}` — Browse hooks by category (surprise/empathy/question/data/story)
### `/hooks add "{hook}"` — Manually add a hook
### `/hooks generate {topic}` — Generate new hooks for a specific topic
### `/hooks best` — Show top-performing hooks (if performance data exists)

## Hook Categories

| Category | Description | Best For | Example |
|----------|------------|----------|---------|
| Surprise | Counterintuitive claim that challenges assumptions | TOFU, X | "The most productive people don't use to-do lists." |
| Empathy | Relatable pain point or shared experience | Instagram, note | "If you've ever stared at a blank screen for 30 minutes..." |
| Question | Provocative question that triggers metacognition | X, Instagram | "What if everything you know about productivity is wrong?" |
| Data | Specific statistic or number that shocks | X, note | "87% of AI projects fail. Here's why yours won't." |
| Story | Mini-narrative that pulls the reader in | note, Instagram | "Last Tuesday, a single email changed how I work forever." |
| Authority | Expert credential or social proof | note (paid) | "After training 500+ companies on AI..." |
| Urgency | Time-sensitive or FOMO-triggering | X, Instagram | "In 6 months, this skill will be mandatory. Most people aren't ready." |

## Data: hook-library.json

Location: `~/.content-autopilot/hook-library.json`

```json
{
  "version": "1.0",
  "hooks": [
    {
      "id": "hook-001",
      "text": "87% of AI projects fail. Here's why yours won't.",
      "category": "data",
      "platform": "x",
      "topic_tags": ["AI", "business", "productivity"],
      "title_logics": ["Numbers", "Paradox"],
      "source": "manual",
      "added_at": "2026-03-20",
      "performance": null
    }
  ]
}
```

## Workflow

### Browse Hooks (`/hooks`)

```
============================================
  Hook Library ({total_count} hooks)
============================================

--- Surprise ({count}) ---
1. "The most productive people don't use to-do lists."
   Platform: X | Tags: productivity
2. "AI won't take your job. But someone using AI will."
   Platform: X, Instagram | Tags: AI, career

--- Empathy ({count}) ---
1. "If you've ever spent 3 hours on a post that got 2 likes..."
   Platform: Instagram | Tags: content-creation, SNS

--- Question ({count}) ---
1. "What if your worst content idea is actually your best?"
   Platform: X | Tags: content-creation

--- Data ({count}) ---
1. "87% of AI projects fail. Here's why yours won't."
   Platform: X, note | Tags: AI, business

--- Story ({count}) ---
1. "Last Tuesday, a single email changed how I work forever."
   Platform: note | Tags: productivity

Filter: /hooks {category} | Add: /hooks add "{text}"
============================================
```

### Generate Hooks (`/hooks generate {topic}`)

Generate 10 hooks across all categories for a given topic:

```
Generated hooks for "{topic}":

Surprise:
  1. "{hook}"
  2. "{hook}"

Empathy:
  1. "{hook}"
  2. "{hook}"

Question:
  1. "{hook}"

Data:
  1. "{hook}"
  2. "{hook}"

Story:
  1. "{hook}"

Authority:
  1. "{hook}"

Urgency:
  1. "{hook}"

Save all to library? (yes / select numbers / no)
```

### Add Hook (`/hooks add "{hook}"`)

```
Hook added to library:
  Text: "{hook}"

  Auto-detected:
    Category: {auto-detected category}
    Platform: {suggested platform}
    Tags: {auto-detected topic tags}

  Correct? (yes / edit category/platform/tags)
```

## Auto-Population from Content History

When content-history.json has entries:
1. Extract the first line/sentence of each content piece
2. Score each as a potential hook (is it attention-grabbing?)
3. High-scoring hooks are auto-added with `"source": "auto"`
4. User can remove auto-added hooks they don't like

## Integration with Other Skills

- **content-writer**: Step 4 references hook-library for the selected topic/platform
  - Shows 2-3 relevant hooks as inspiration before writing
  - Can directly use a library hook as the opening line
- **series-designer**: Uses hooks for each part's opening concept
- **engagement-templates**: Conversation starters can draw from hook patterns

## Quality Gate

Before delivering:
- [ ] Hooks are genuinely attention-grabbing (not generic)
- [ ] Categories are correctly assigned
- [ ] Platform recommendations match the hook style
- [ ] No duplicate hooks in the library
- [ ] Auto-populated hooks are actually good (scored above threshold)
- [ ] Generated hooks follow bestseller title logic patterns
