---
name: daily-capture
description: Quick-capture ideas from daily life — one-line memos of observations, conversations, frustrations, and discoveries that become content seeds. The best content ideas come from real life — but you forget them in 10 minutes. Never lose an idea again.
---

# Daily Capture

The best content idea you had today? You already forgot it. Unless you captured it.

## When to Activate

- User says `/capture "{memo}"` or `/cap "{memo}"`
- User says `/capture` to review captured ideas
- User says "I just noticed something interesting"

## Data: captures.json

```json
{
  "version": "1.0",
  "captures": [
    {
      "id": "cap-001",
      "text": "Coffee shop: overheard someone struggling with AI tools for 30 min — there's clearly a gap in beginner content",
      "captured_at": "2026-03-21T14:30:00Z",
      "tags": ["AI", "beginners", "observation"],
      "status": "unprocessed",
      "promoted_to": null
    }
  ]
}
```

## Commands

### `/cap "{memo}"` — Quick capture (1 line)
### `/capture` — Review all unprocessed captures
### `/capture process` — Turn captures into content ideas
### `/capture stats` — How many captures → content pieces

## Workflow

### Quick Capture

```
/cap "Client asked me 'what's the simplest AI tool?' — maybe everyone wants simple, not powerful"

Captured! ✓
  Tags (auto): AI, simplicity, audience-insight
  Time: {timestamp}

Your capture bank: {N} unprocessed ideas
Process them with /capture process
```

### Process Captures

```
/capture process

Unprocessed captures ({N}):

1. "Coffee shop AI struggle observation" ({date})
   Content potential: HIGH
   → Article: "Why AI Tools Fail Beginners (And What to Do Instead)"
   → Format: note article (MOFU) + X thread
   → Add to pipeline? (yes / skip)

2. "Client wants simple not powerful" ({date})
   Content potential: HIGH
   → Article: "The Simplicity Trap: Why the 'Easiest' AI Tool Wins"
   → Format: X thread + Instagram carousel
   → Connects to: capture #1 (combine?)
   → Add to pipeline? (yes / skip)

3. "Saw competitor post about {topic}" ({date})
   Content potential: LOW — already covered this
   → Archive

Processed: {count} | Added to pipeline: {count} | Archived: {count}
```

### Capture → Content Stats

```
Capture conversion rate:
  Total captures: {N}
  → Became content: {N} ({percentage}%)
  → Best capture-to-content: "{capture}" → "{article_title}" ({engagement})

  Insight: Your best content ideas come from {category} captures
```

## Integration

- **pipeline-view**: Processed captures enter pipeline as "idea" stage
- **mind-map**: Expand a capture into full mind map
- **story-bank**: Personal captures become stories
- **content-writer**: Captures referenced during topic selection

## Quality Gate

- [ ] Capture is instant (< 5 seconds to save)
- [ ] Auto-tagging is accurate
- [ ] Processing suggests specific content ideas (not generic)
- [ ] Connection between related captures detected
- [ ] Stats track capture-to-published conversion
