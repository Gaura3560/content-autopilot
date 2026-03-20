---
name: seo-optimizer
description: SEO optimization for note articles — keyword research, heading structure analysis, internal linking suggestions, meta description generation, and competitor SERP analysis. Maximizes organic search traffic to note content.
---

# SEO Optimizer

Maximize your note articles' search visibility with data-driven SEO optimization.

## When to Activate

- User says `/seo` or `/seo {file_path}`
- User asks "optimize this for search"
- User asks "what keywords should I target?"
- User wants more organic traffic to note articles

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Content file to optimize (note articles)

## Commands

### `/seo {file_path}` — Optimize a specific article
### `/seo keywords {topic}` — Research keywords for a topic
### `/seo audit` — Audit all recent note articles for SEO issues
### `/seo competitors {keyword}` — Analyze top-ranking articles for a keyword

## Workflow

### Step 1: Keyword Research

Use WebSearch to identify target keywords:

```
Search: "{topic} note.com" — see what ranks
Search: "{topic}" site:note.com — find competitor articles
Search: Google Suggest for "{topic}" — find related queries
Search: "{topic} とは" / "{topic} 方法" / "{topic} コツ" — long-tail variants
```

Present keyword opportunities:
```
Keyword Research: "{topic}"

Primary keyword: "{keyword}" — competition: {low/medium/high}
Secondary keywords:
  1. "{long_tail_1}" — {estimated_difficulty}
  2. "{long_tail_2}" — {estimated_difficulty}
  3. "{long_tail_3}" — {estimated_difficulty}

Related questions (People Also Ask):
  1. "{question_1}"
  2. "{question_2}"
  3. "{question_3}"

Recommendation: Target "{primary}" in title, use "{secondary}" in H2 headings
```

### Step 2: On-Page SEO Analysis

Analyze the article structure:

```
SEO Analysis: "{article_title}"
============================================

Title SEO:
  [ ] Primary keyword in title: {yes/no — where to add}
  [ ] Title length: {chars} chars ({optimal: 30-60 chars})
  [ ] Emotional trigger word present: {yes/no}
  Score: {score}/25

Heading Structure:
  [ ] H2 headings contain keywords: {count}/{total}
  [ ] Logical heading hierarchy: {yes/no}
  [ ] Heading count: {count} ({optimal: 3-7 for note})
  Suggested headings:
    H2: "{keyword-rich heading suggestion}"
    H2: "{keyword-rich heading suggestion}"
  Score: {score}/25

Content Optimization:
  [ ] Keyword in first 100 chars: {yes/no}
  [ ] Keyword density: {percentage}% ({optimal: 1-3%})
  [ ] LSI keywords present: {count} ({list})
  [ ] Content length: {chars} ({optimal: 2,000-5,000})
  Missing LSI keywords to add: {list}
  Score: {score}/25

Technical:
  [ ] Image alt text described: {yes/no — note doesn't support alt, but caption helps}
  [ ] Internal links to other articles: {count}
  [ ] External source citations: {count}
  [ ] Meta description (note excerpt): {quality assessment}
  Score: {score}/25

Overall SEO Score: {total}/100
============================================
```

### Step 3: Competitor SERP Analysis

For `/seo competitors {keyword}`:

```
Top-ranking articles for "{keyword}" on note:

1. "{title}" by {author}
   URL: {url}
   Length: ~{chars} chars | Headings: {count}
   Strengths: {what they do well}
   Gaps: {what they miss — your opportunity}

2. "{title}" by {author}
   ...

3. "{title}" by {author}
   ...

--- Your Differentiation Opportunities ---
1. {specific gap you can fill}
2. {angle not covered by top results}
3. {data/example you can add that they don't have}
```

### Step 4: Generate Optimized Version

If the user wants auto-optimization:

```
SEO Improvements Applied:

1. Title: "{original}" → "{optimized}"
   Reason: Added primary keyword + emotional trigger

2. Added keyword to first paragraph:
   Original: "{original_first_line}"
   Optimized: "{keyword-enriched_first_line}"

3. Heading optimization:
   H2: "{original}" → "{keyword-rich version}"
   H2: "{original}" → "{keyword-rich version}"

4. Added LSI keywords in body:
   - "{lsi_keyword_1}" added to Section 2
   - "{lsi_keyword_2}" added to Section 4

5. Meta description (note excerpt):
   "{optimized_excerpt_under_120_chars}"

6. Internal link suggestion:
   Link to "{related_article}" from Section 3

Original score: {before}/100 → Optimized score: {after}/100
```

### Step 5: Save Optimized Version

```
Save optimized version?
1. Replace original
2. Save as new file (seo_{filename})
3. Show diff only (don't save)
```

## SEO Audit (`/seo audit`)

Scan all note articles in content-history.json:

```
SEO Audit — {count} note articles scanned
============================================

High Priority (score < 50):
  1. "{title}" ({date}) — Score: {score}/100
     Issue: {main issue}
  2. "{title}" ({date}) — Score: {score}/100
     Issue: {main issue}

Medium Priority (score 50-70):
  3. "{title}" ({date}) — Score: {score}/100
  4. "{title}" ({date}) — Score: {score}/100

Good (score > 70):
  5. "{title}" ({date}) — Score: {score}/100

Quick wins (fix 1 thing for biggest impact):
  1. Add keyword to title of "{article}" → estimated +15 points
  2. Add H2 headings to "{article}" → estimated +10 points
  3. Extend "{article}" by 500 chars → estimated +8 points

Run /seo {file} to optimize any article.
============================================
```

## Quality Gate

- [ ] Keyword recommendations are based on actual search data
- [ ] Suggestions don't compromise readability for SEO
- [ ] Competitor analysis uses real top-ranking content
- [ ] Optimized version maintains the author's voice
- [ ] Score improvements are realistic and measurable
