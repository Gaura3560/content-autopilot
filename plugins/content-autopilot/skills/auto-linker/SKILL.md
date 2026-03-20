---
name: auto-linker
description: Automatic internal link insertion — scan content for opportunities to link to your other articles, improving SEO and reader retention. Analyzes content-history for topic matches and suggests optimal link placement with anchor text.
---

# Auto Internal Linker

Never miss a link opportunity — automatically connect your content for better SEO and reader flow.

## When to Activate

- User says `/auto-link {file_path}`
- User asks "add internal links to this article"
- User asks "what should I link to?"
- Auto-suggested by seo-optimizer and pre-publish

## Prerequisites

- `~/.content-autopilot/content-history.json` (to know what articles exist)
- Content file to add links to

## Commands

### `/auto-link {file_path}` — Find and suggest internal links
### `/auto-link map` — Show full internal link map across all content
### `/auto-link orphans` — Find articles with zero incoming links

## Workflow

### Step 1: Build Link Graph

Read content-history.json and map all existing articles:
- Extract topics, keywords, titles
- Build a topic→article index

### Step 2: Scan Content for Opportunities

Read the target file and identify:
- Mentions of topics covered in other articles
- Concepts that have dedicated articles
- "Learn more about X" opportunities
- Natural transition points between paragraphs

### Step 3: Suggest Links

```
Auto-Link Suggestions: "{title}"
============================================

Found {N} internal link opportunities:

1. Line {N}: "{anchor_text}"
   Link to: "{related_article_title}" ({date})
   Context: This paragraph discusses {topic}, which is covered in depth in the linked article
   Suggested insertion:
     Before: "...{surrounding text}..."
     After: "...{text with [anchor_text](note_url)} inserted..."

2. Line {N}: "{anchor_text}"
   Link to: "{related_article_title}" ({date})
   Context: {reason this link adds value}
   Suggested insertion: "...{modified text}..."

3. Line {N}: "{anchor_text}"
   ...

--- Link Quality ---
  Natural fit: {count} links (reads naturally)
  Forced fit: {count} links (might feel unnatural — optional)

--- Recommended (top 3-5 links) ---
  Most valuable links to add:
  1. {link} — highest SEO value (related keyword cluster)
  2. {link} — highest reader value (answers likely next question)
  3. {link} — freshest content (recent, keeps readers in ecosystem)

Apply all recommended links? (yes / select / no)
============================================
```

### Step 4: Orphan Detection

`/auto-link orphans`:
```
Orphan Articles (0 incoming links):
  1. "{title}" ({date}) — no other article links to this
     Fix: Add link from "{best_candidate_article}"
  2. "{title}" ({date})
     Fix: Add link from "{best_candidate}"

Well-connected articles (5+ links):
  1. "{title}" — {N} incoming links (hub article)

Link health: {percentage}% of articles have at least 1 incoming link
Target: 100% — every article should be reachable from at least one other
```

## Integration with Other Skills

- **seo-optimizer**: Internal links are a major SEO factor
- **content-cluster**: Cluster structure defines link architecture
- **content-writer**: Suggest links during content creation
- **content-refresh**: Add new links when refreshing old content
- **pre-publish**: Check for link opportunities before publishing

## Quality Gate

- [ ] Suggested links are genuinely relevant (not forced)
- [ ] Anchor text is natural within the sentence
- [ ] Not over-linking (max 3-5 internal links per article)
- [ ] Links point to existing, accessible content
- [ ] Orphan detection covers all content in history
