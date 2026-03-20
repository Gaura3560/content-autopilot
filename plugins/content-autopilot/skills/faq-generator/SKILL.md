---
name: faq-generator
description: FAQ content generator — compile questions from comments, niche monitoring, and search data into structured FAQ content for note articles, X pinned threads, and Instagram highlight stories. Includes schema markup suggestions for SEO.
---

# FAQ Generator

Turn your audience's questions into high-value, search-friendly content.

## When to Activate

- User says `/faq` or `/faq {topic}`
- User asks "create an FAQ"
- User asks "what questions do people ask about {topic}?"
- User wants to create FAQ content

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Optional: comment-insights.json, monitor-reports (for real audience questions)

## Commands

### `/faq {topic}` — Generate FAQ content for a topic
### `/faq compile` — Compile FAQs from all audience data sources
### `/faq {topic} {platform}` — FAQ formatted for specific platform

## Workflow

### Step 1: Gather Questions

**Source 1: Audience data (highest quality)**
- comment-insights.json — real questions from your readers
- monitor-keywords.json — questions found in niche monitoring

**Source 2: Search research**
```
Search: "{topic} よくある質問"
Search: "{topic} とは"
Search: "{topic} FAQ"
Search: "People Also Ask" for "{topic}"
```

**Source 3: Generate from expertise**
- Based on profile.json audience pain_points
- Common beginner questions for the topic

### Step 2: Organize and Answer

Group questions by category, then generate answers:

```
FAQ: "{topic}" — {N} questions
============================================

## Getting Started
Q1: {question}
A: {concise, helpful answer — 2-4 sentences}

Q2: {question}
A: {answer}

## Common Problems
Q3: {question}
A: {answer}

Q4: {question}
A: {answer}

## Advanced Topics
Q5: {question}
A: {answer}

...
============================================
```

### Step 3: Platform-Specific Formatting

**note FAQ article:**
```markdown
# {topic} よくある質問 {N}選

{Introduction — why these questions matter}

## Q1: {question}
{Detailed answer with examples}

## Q2: {question}
{Answer}
...

## まとめ
{Summary + CTA to related content}
```

**X pinned thread:**
```
Tweet 1: "{topic}についてよく聞かれる質問をまとめました (thread)"
Tweet 2: "Q: {question}" → "A: {brief answer}"
Tweet 3: "Q: {question}" → "A: {brief answer}"
...
Last tweet: "他に質問あればリプで！詳しくはnoteで → {url}"
```

**Instagram Stories highlight:**
```
Story 1: "FAQ: {topic}" (cover slide)
Story 2: Q: "{question}" (question sticker style)
Story 3: A: "{answer}" (answer reveal)
Story 4: Q: "{question}"
Story 5: A: "{answer}"
...
Last story: "More questions? DM me!" + link sticker
```

### Step 4: SEO Schema Suggestion

For note articles:
```
FAQ schema markup (for search engines):
This article could appear as FAQ rich snippets in Google.

Structured data:
  @type: FAQPage
  Questions: {N}

  Note: note.com doesn't support custom schema,
  but Google may still extract FAQ structure from
  well-formatted Q&A headings.
```

## Integration with Other Skills

- **comment-miner**: Primary source of real audience questions
- **niche-monitor**: Additional questions from niche conversations
- **seo-optimizer**: FAQ articles target "question" search queries
- **content-cluster**: FAQs serve as satellite content
- **content-writer**: FAQ format as content template option

## Quality Gate

- [ ] Questions represent real audience needs (not fabricated)
- [ ] Answers are concise yet complete
- [ ] Platform formatting is correct
- [ ] Questions are organized logically by category
- [ ] FAQ links to deeper content for complex topics
- [ ] SEO considerations applied (keyword-rich Q&A)
