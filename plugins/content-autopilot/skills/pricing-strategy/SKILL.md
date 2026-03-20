---
name: pricing-strategy
description: Paid content pricing strategy — research competitor pricing, analyze value perception, design pricing tiers, and plan price testing. Covers note paid articles, memberships, ebooks, and courses. Data-driven pricing decisions.
---

# Pricing Strategy

Set the right price for your paid content — backed by market research and value analysis.

## When to Activate

- User says `/pricing` or `/pricing {product_type}`
- User asks "how much should I charge?"
- User asks "what's the right price for my paid article?"
- User wants to optimize pricing for monetization

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Knowledge of the product/content to price

## Commands

### `/pricing` — Interactive pricing strategy session
### `/pricing {product_type}` — Price a specific product type
### `/pricing research {keyword}` — Research competitor pricing
### `/pricing test` — Design a price testing plan

## Workflow

### Step 1: Understand the Product

```
What are you pricing?

1. note paid article (single purchase)
2. note membership/magazine (recurring)
3. Ebook / PDF guide
4. Online course / video content
5. Consulting / coaching session
6. Other (describe)

Select (1-6):
```

### Step 2: Market Research

Use WebSearch to gather pricing data:

```
Search: "note 有料記事 {niche} 価格"
Search: "note メンバーシップ {niche} 月額"
Search: "{niche} オンライン講座 価格"
Search: "note.com {keyword}" — check actual prices of similar content
```

Present findings:
```
Market Research: {product_type} in {niche}
============================================

Competitor Pricing:
  1. "{title}" by {author} — ¥{price}
     Content: {brief description}
     Estimated sales: {if visible}

  2. "{title}" by {author} — ¥{price}
     Content: {brief description}

  3. "{title}" by {author} — ¥{price}
     Content: {brief description}

Market Summary:
  Price range: ¥{min} — ¥{max}
  Average: ¥{avg}
  Median: ¥{median}
  Most common price point: ¥{mode}

============================================
```

### Step 3: Value Assessment

```
Value Assessment: Your Content
============================================

Value Factors:                        Score
  Unique data/research:               {1-5}/5
  Actionable templates/tools:         {1-5}/5
  Time savings for reader:            {1-5}/5
  Expertise/authority level:          {1-5}/5
  Depth beyond free content:          {1-5}/5

Total value score: {total}/25

Value positioning:
  {score < 10}: Entry-level pricing (¥100-300)
  {10-15}: Standard pricing (¥300-700)
  {15-20}: Premium pricing (¥700-1,500)
  {20-25}: High-value pricing (¥1,500-5,000)

============================================
```

### Step 4: Pricing Recommendation

```
Pricing Recommendation
============================================

Product: {product_name}
Type: {product_type}

Recommended price: ¥{price}

Reasoning:
  - Market average: ¥{avg} → your content is {above/at/below} average quality
  - Value score: {score}/25 → positions in {tier} range
  - Audience willingness: {audience_type} typically pays ¥{range}
  - Psychological pricing: ¥{price} hits the "{anchor}" sweet spot

Alternative strategies:
  1. Launch price: ¥{lower_price} (first 50 buyers)
     → Build momentum, collect reviews, raise later
  2. Premium price: ¥{higher_price}
     → If you add {bonus_suggestion} as a bonus
  3. Bundle price: ¥{bundle_price} for {N} articles
     → Higher total revenue per customer

--- For Membership/Recurring ---
  Monthly: ¥{monthly}
  Annual: ¥{annual} (¥{monthly_equivalent}/month — {discount}% savings)
  Recommendation: Offer both, highlight annual savings

============================================
```

### Step 5: Price Testing Plan

```
Price Testing Plan
============================================

Test A: ¥{price_A} (lower)
Test B: ¥{price_B} (higher)
Duration: 2 weeks each
Metric: Total revenue (not just units sold)

Week 1-2: Sell at ¥{price_A}
  Record: units sold, total revenue, conversion rate

Week 3-4: Sell at ¥{price_B}
  Record: units sold, total revenue, conversion rate

Compare:
  ¥{price_A} × {units_A} = ¥{revenue_A}
  ¥{price_B} × {units_B} = ¥{revenue_B}

Winner: Higher total revenue wins (not higher unit sales)

Track with: /monetize add sale {date} {amount}
Review with: /monetize (revenue dashboard)
============================================
```

## Pricing Psychology Tips (built into recommendations)

1. **Charm pricing**: ¥480 feels cheaper than ¥500
2. **Anchor pricing**: Show the "real value" before the price
3. **Bundle savings**: "3 articles for ¥1,200 (save ¥300)"
4. **Price anchoring**: Compare to alternatives ("a ¥5,000 course covers the same content")
5. **Decoy pricing**: 3 tiers where the middle one is the best value

## Quality Gate

- [ ] Recommendations based on actual market data
- [ ] Value assessment is honest (not inflated)
- [ ] Price testing plan is practical and measurable
- [ ] Psychology tips are ethical (no dark patterns)
- [ ] Multiple price points offered for different strategies
