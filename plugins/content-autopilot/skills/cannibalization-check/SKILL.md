---
name: cannibalization-check
description: SEO keyword cannibalization detector — find articles competing for the same search keywords, weakening each other's ranking. Suggests merging, differentiating, or canonicalizing conflicting pages. Critical for note SEO strategy.
---

# Cannibalization Check

Stop your own articles from competing against each other in search results.

## When to Activate

- User says `/cannibalization` or `/cannibal-check`
- User asks "are my articles competing with each other?"
- Auto-suggested by seo-optimizer and content-cluster
- Run periodically (monthly) for SEO health

## Prerequisites

- `~/.content-autopilot/content-history.json` with note article data

## Commands

### `/cannibal-check` — Scan all note articles for cannibalization
### `/cannibal-check {keyword}` — Check specific keyword
### `/cannibal-check fix` — Show fix recommendations

## Workflow

### Step 1: Build Keyword Map

For each note article in content-history:
- Extract title keywords
- Extract H2 heading keywords
- Extract first-paragraph keywords
- Identify primary target keyword

### Step 2: Detect Overlaps

```
============================================
  Cannibalization Report
  Scanned: {N} note articles
============================================

CANNIBALIZATION DETECTED:

1. [HIGH] Keyword: "AI自動化"
   Competing articles:
     a) "{title_1}" ({date}) — targets "AI自動化" in title + H2
     b) "{title_2}" ({date}) — targets "AI自動化" in title + body
     c) "{title_3}" ({date}) — targets "AI 自動化 ツール" (overlap)

   Impact: These 3 articles split search authority — none ranks well

   Fix options:
     A) MERGE: Combine into one comprehensive article (strongest SEO)
     B) DIFFERENTIATE: Change keywords
        - Article a: keep "AI自動化" (broadest)
        - Article b: retarget to "AI自動化 初心者" (beginner angle)
        - Article c: retarget to "AI自動化ツール 比較" (comparison angle)
     C) CANONICAL: Keep one as primary, others link to it

2. [MEDIUM] Keyword: "生産性 向上"
   Competing articles:
     a) "{title}" ({date})
     b) "{title}" ({date})

   Fix options: {same structure}

NO ISSUES:
  {N} keywords have unique targeting — no cannibalization

--- Summary ---
  High severity: {count} keyword groups
  Medium severity: {count}
  Clean: {count} keywords

  Estimated SEO impact: {count} articles underperforming due to cannibalization

============================================
```

### Step 3: Generate Fix Plan

```
Recommended fix plan (priority order):

1. Merge "{title_a}" + "{title_b}" into one pillar article
   New title: "{suggested_merged_title}"
   Action: /refresh to merge + /auto-link to redirect

2. Retarget "{title_c}" from "AI自動化" to "AI自動化ツール 比較"
   Action: /seo "{title_c}" with new keyword

3. Add internal links between related but non-competing articles
   Action: /auto-link for the cluster

Estimated ranking improvement: {estimate}
```

## Integration with Other Skills

- **seo-optimizer**: Cannibalization check is part of SEO audit
- **content-cluster**: Cluster design prevents future cannibalization
- **content-refresh**: Merge articles through refresh process
- **auto-linker**: Fix redirects and internal links after merging
- **content-calendar**: Plan future content to avoid creating new overlaps

## Quality Gate

- [ ] All note articles scanned for keyword overlap
- [ ] Severity accurately reflects the impact
- [ ] Fix options are practical (merge/differentiate/canonical)
- [ ] Future prevention strategy included
- [ ] Doesn't flag intentionally different angles on the same broad topic
