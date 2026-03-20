---
name: content-memoir
description: Auto-generate your content creation story from history data — the narrative of your journey as a creator. Use as "about me" content, book introduction, or personal motivation when you forget how far you've come.
---

# Content Memoir

Your data tells a story. This skill writes it.

## Commands

### `/memoir` — Generate your content creation story
### `/memoir short` — 500-char version (for bios)
### `/memoir chapter {period}` — Detailed chapter for a time period

## Output

```
============================================
  Your Content Memoir
============================================

Chapter 1: The Beginning ({first_date})
  "It started with a single note article: '{first_title}'.
  {N} characters of uncertainty..."

Chapter 2: Finding a Voice ({month range})
  "By {month}, a pattern emerged. {topic} wasn't just a topic — it was your thing.
  {N} articles in, the DNA started to show: {signature_pattern}..."

Chapter 3: The Breakthrough ({date of first viral/milestone})
  "'{breakthrough_title}' changed everything. {metrics}.
  For the first time, strangers were sharing your words..."

Chapter 4: Building the System ({date range})
  "You went from sporadic posting to {frequency}.
  Revenue appeared: first ¥{first_sale}, then ¥{monthly_avg}/month..."

Chapter 5: Where You Are Now ({current_date})
  "{total_articles} articles. {total_revenue} earned. {followers} people who care.
  Your content DNA: {signature formula}.
  The journey continues."

============================================

Use this as:
  - note "about me" article
  - Book introduction
  - Personal motivation when you doubt yourself
```

Integrates with: content-history, monetize-data, milestone-tracker, content-dna.
