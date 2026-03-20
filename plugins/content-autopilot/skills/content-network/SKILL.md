---
name: content-network
description: Visualize your entire content ecosystem as a living network — nodes (articles) with energy (performance), connections (links), age (freshness), and clusters (topics). See which nodes are thriving, dying, or isolated. Manage content as an ecosystem, not a list.
---

# Content Network

Your content isn't a list. It's a living ecosystem. See it that way.

## When to Activate

- User says `/network` or `/content-network`
- User asks "show me my content ecosystem"
- User wants a holistic view of their content

## Commands

### `/network` — Full network visualization
### `/network health` — Ecosystem health report
### `/network dead-nodes` — Find dying/dead content
### `/network bridges` — Find connection opportunities

## Workflow

```
============================================
  Content Network — Ecosystem View
  Nodes: {N} | Links: {N} | Clusters: {N}
============================================

--- Network Map ---

Cluster: "{topic_1}" ({N} nodes)
  ● "{title}" — Energy: HIGH (500 PV/month, growing)
  ● "{title}" — Energy: MEDIUM (200 PV, stable)
  ○ "{title}" — Energy: LOW (50 PV, declining)
  ◌ "{title}" — Energy: DEAD (5 PV, no links in)
  Links within cluster: {N}

Cluster: "{topic_2}" ({N} nodes)
  ● "{title}" — Energy: HIGH
  ○ "{title}" — Energy: LOW
  Links within cluster: {N}

Isolated nodes (no cluster):
  ◌ "{title}" — no links, no cluster
  ◌ "{title}" — orphaned content

--- Ecosystem Health ---

Overall health: {score}/100

  Connectivity: {score}/25
    {N}% of nodes have incoming links
    {N} orphan nodes (no connections)

  Energy distribution: {score}/25
    {N} high-energy nodes (hub articles)
    {N} dead nodes (need refresh or removal)

  Cluster balance: {score}/25
    {N} clusters active
    Largest: "{topic}" ({N} nodes)
    Smallest: "{topic}" ({N} nodes)

  Freshness: {score}/25
    Avg node age: {days} days
    {N} nodes past expiry date

--- Recommended Actions ---

1. REVIVE dead node: "{title}" — /refresh or /recycle
2. BRIDGE clusters: Link "{cluster_A}" to "{cluster_B}" via "{common_topic}"
3. GROW weakest cluster: "{topic}" needs {N} more articles
4. PRUNE: "{title}" has zero value — consider removing
5. STRENGTHEN hub: "{title}" is your highest-energy node — create more links TO it

============================================

Think of your content as a garden:
  ● Thriving plants (high-energy nodes) — water them (promote, update)
  ○ Struggling plants (low-energy) — assess: revive or remove
  ◌ Dead plants (zero traffic) — compost (recycle content) or clear
  Bridges (links) — connect related plants for mutual benefit
  Clusters (beds) — organized by topic for SEO authority

============================================
```

## Quality Gate

- [ ] Network based on actual content data and links
- [ ] Energy levels from real performance data where available
- [ ] Cluster identification is logical
- [ ] Recommendations are specific and prioritized
- [ ] Ecosystem metaphor makes the data intuitive
