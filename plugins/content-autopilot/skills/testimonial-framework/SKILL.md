---
name: testimonial-framework
description: Social proof collection and formatting — create testimonial request templates, format received testimonials for different platforms, and strategically place them in content. Social proof increases conversion by 270%.
---

# Testimonial Framework

Collect, format, and deploy social proof — the #1 conversion driver you're probably underusing.

## When to Activate

- User says `/testimonial` or `/testimonials`
- User says `/testimonial request` to create request templates
- User says `/testimonial format` to format received testimonials
- User wants to add social proof to content or launch

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/testimonial request` — Generate testimonial request templates
### `/testimonial format "{text}"` — Format a testimonial for use
### `/testimonial place {file}` — Suggest where to add testimonials in content
### `/testimonial library` — View all saved testimonials

## Data: testimonials.json

Location: `~/.content-autopilot/testimonials.json`

```json
{
  "version": "1.0",
  "testimonials": [
    {
      "id": "test-001",
      "from": "Reader A",
      "platform": "note",
      "original_text": "This article changed how I...",
      "formatted": {
        "short": "\"Changed how I work\" — Reader A",
        "medium": "\"This article changed how I approach AI. Saved me 3 hours.\" — Reader A",
        "long": "Full quote with context..."
      },
      "topic_tags": ["AI", "productivity"],
      "type": "result",
      "received_at": "2026-03-21",
      "used_in": []
    }
  ]
}
```

## Testimonial Types

| Type | Power | Example | Best Placement |
|------|-------|---------|---------------|
| Result | Highest | "Saved me 3 hours/day" | Sales pages, launches |
| Transformation | High | "Before: confused → After: confident" | note articles |
| Emotional | Medium | "This was exactly what I needed" | Instagram, note |
| Authority | High | "As a {credential}, I recommend..." | Paid content |
| Specific | High | Numbers, dates, concrete outcomes | Anywhere |

## Workflow: Request Templates (`/testimonial request`)

```
Testimonial Request Templates:
============================================

--- X DM Template ---
{name}さん、{article/content}を読んでいただきありがとうございます。

もし参考になっていたら、一言感想をいただけると嬉しいです。
他の読者の参考になるので...！

例えばこんな感じで：
「{topic}について{何が変わった/何が得られた}」

--- note Comment Prompt (in article) ---
この記事が参考になった方、コメントで教えてください：
・どの部分が一番参考になりましたか？
・実際に試してみた結果はどうでしたか？

いただいた感想は（許可をいただいた上で）
今後の記事で紹介させていただくことがあります。

--- Direct Request (for specific results) ---
{name}さん

以前{topic}の記事を参考にしてくださったとお聞きしました。
具体的にどんな変化がありましたか？

差し支えなければ、以下の形式で教えていただけると助かります：
1. 記事を読む前の状況：
2. 実践した内容：
3. その結果：

匿名/実名どちらでもOKです。

============================================
```

### Workflow: Format (`/testimonial format`)

```
/testimonial format "This AI article was amazing. I used the 3-step method and saved 2 hours on my first day. Now I use it every morning."

Formatted versions:

Short (for bios/CTAs):
  "Saved 2 hours on day one" — Reader

Medium (for articles/social):
  "3ステップを初日に試したら2時間の節約に。今は毎朝使っています" — Reader

Long (for sales pages):
  "このAI記事は素晴らしかったです。3ステップの方法を使ったら初日で
  2時間節約できました。今では毎朝のルーティンになっています" — Reader

Save to testimonial library? (yes / edit / no)
Topic tags: AI, productivity, time-saving (auto-detected)
Type: result (specific outcome mentioned)
```

### Workflow: Strategic Placement (`/testimonial place`)

```
/testimonial place note_2026-03-20.md

Suggested testimonial placements for "{article_title}":

1. After introduction (trust signal early):
   Insert: "{short_testimonial}" — builds immediate credibility

2. Before paid section paywall:
   Insert: "{result_testimonial}" — justifies the purchase

3. In conclusion/CTA:
   Insert: "{transformation_testimonial}" — motivates action

4. As pull quote (visual break):
   Insert: > "{medium_testimonial}"

Available testimonials matching this topic: {count}
Auto-insert all? (yes / select positions / skip)
```

## Integration with Other Skills

- **launch-sequence**: Testimonials placed in launch day content
- **content-writer**: Suggests testimonial insertion points
- **lead-magnet-creator**: Include testimonials in guides
- **newsletter-generator**: Feature testimonials in emails
- **pricing-strategy**: Testimonials support price justification

## Quality Gate

- [ ] Permission obtained before using testimonials
- [ ] Testimonials are real (not fabricated)
- [ ] Multiple format lengths available for flexibility
- [ ] Strategic placement suggestions are natural (not forced)
- [ ] Topic tags enable accurate matching to content
