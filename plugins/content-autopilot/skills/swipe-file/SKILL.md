---
name: swipe-file
description: Curated swipe file of inspiring content — save URLs or text of content you admire, auto-analyze structure and hooks, tag by category and technique. A searchable inspiration database that content-writer and hook-library can reference.
---

# Swipe File

Build your personal library of content inspiration — analyzed and ready to reference.

## When to Activate

- User says `/swipe-file add {url}` or `/swipe add {url}`
- User says `/swipe` to browse
- User says `/swipe search {keyword}`
- User asks "save this for inspiration"

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Data: swipe-file.json

Location: `~/.content-autopilot/swipe-file.json`

```json
{
  "version": "1.0",
  "entries": [
    {
      "id": "swipe-001",
      "added_at": "2026-03-21",
      "url": "https://x.com/user/status/123",
      "platform": "x",
      "author": "@username",
      "content_preview": "First 200 chars...",
      "full_text": "...",
      "analysis": {
        "hook_type": "data",
        "hook_text": "87% of...",
        "structure": "listicle",
        "emotional_trigger": "curiosity",
        "title_logics": ["Numbers", "Paradox"],
        "viral_pattern": "data_storytelling",
        "key_technique": "Specific number + contrarian claim"
      },
      "tags": ["AI", "productivity", "thread"],
      "notes": "Great hook structure — use for tech topics",
      "used_count": 0
    }
  ]
}
```

## Commands

### `/swipe add {url}` — Add and auto-analyze content
### `/swipe add` — Paste text to save (no URL)
### `/swipe` — Browse all entries
### `/swipe search {keyword}` — Search by tag, technique, or content
### `/swipe {category}` — Filter by hook type or structure
### `/swipe random` — Get random inspiration
### `/swipe stats` — Show swipe file statistics

## Workflow: Add Entry

### Step 1: Fetch Content

**If URL:**
- WebFetch to retrieve full content
- Auto-detect platform from URL

**If text:**
- Save the pasted text
- Ask which platform it's from

### Step 2: Auto-Analyze

Apply viral-reverse analysis (lightweight version):
- Hook type classification
- Structure identification
- Emotional trigger detection
- Title logic extraction
- Key technique summary

### Step 3: Tag and Save

```
Saved to swipe file:

Author: {author}
Platform: {platform}
Hook: "{first_line}" [{hook_type}]
Structure: {structure}
Technique: {key_technique}

Auto-tags: {tag1}, {tag2}, {tag3}
Add custom tags? (enter tags or "done"):
Add personal notes? (enter note or "skip"):

Entry saved! (#{entry_number} in your swipe file)
```

## Workflow: Browse

```
============================================
  Swipe File ({total} entries)
============================================

Filter by: hook type | structure | platform | tag

Recent additions:
1. [{platform}] "{preview}" — {hook_type} hook, {structure}
   by {author} | Tags: {tags}
2. [{platform}] "{preview}" — {hook_type} hook
   by {author} | Tags: {tags}
3. ...

--- By Hook Type ---
Surprise: {count} | Data: {count} | Story: {count}
Question: {count} | Empathy: {count} | Authority: {count}

--- By Structure ---
Thread: {count} | Article: {count} | Carousel: {count}
Single post: {count}

Search: /swipe search {keyword}
Random: /swipe random
============================================
```

## Workflow: Search

`/swipe search AI` or `/swipe search data hook`:

```
Search results for "{query}":

1. [{platform}] "{preview}" — {technique}
   Relevance: {why this matches}
   Use for: {suggestion}

2. [{platform}] "{preview}" — {technique}
   Relevance: {why}

{count} results found
```

## Integration with Other Skills

- **content-writer**: "Looking for inspiration? You have {N} swipe entries tagged '{topic}'"
- **hook-library**: Auto-extracts hooks from swipe entries
- **viral-reverse**: Full analysis saved directly to swipe file
- **content-dna**: Compares your DNA with swipe file patterns to identify gaps
- **thread-templates**: Swipe entries inform which templates to recommend

## Quality Gate

- [ ] Auto-analysis is accurate (hook type, structure correctly identified)
- [ ] Tags are useful for searching
- [ ] Content is stored for reference (not just URLs that may break)
- [ ] No copyright issues (stored for personal reference only)
- [ ] Search returns relevant results
