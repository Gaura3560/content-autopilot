---
name: engagement-templates
description: Pre-built engagement templates for audience interaction — comment replies, conversation starters, funnel nudges, and community building across X, note, and Instagram. Personalized to profile.json style and funnel settings.
---

# Engagement Templates

Generate ready-to-use reply and engagement templates to build your audience community.

## When to Activate

- User says `/engagement` or `/engagement {category}`
- User says `/engagement thank` for gratitude templates
- User says `/engagement funnel` for funnel nudge templates
- User asks "how should I reply to comments?"
- User wants templates for audience interaction

## Prerequisites

- `~/.content-autopilot/profile.json` must exist (for style and funnel settings)

## Template Categories

### 1. Comment Gratitude (`/engagement thank`)

Reply templates for when someone comments on or shares your content.

**X replies:**
```
Template 1 (Short):
{username}さん、ありがとうございます！{one-line response to their specific point}

Template 2 (Expand):
{username}さん、嬉しいコメントありがとうございます！
{reference their specific point}ですよね。
実は{related insight not in the original post}...深掘りしたnote記事もあるのでぜひ
→ {note_url}  ← only when funnel.enabled

Template 3 (Question):
{username}さん、ありがとうございます！
{their point}について、{follow-up question}？
ぜひ教えてください
```

**note replies:**
```
Template 1 (Warm):
コメントありがとうございます！{specific response to their feedback}
{their question}についてはまた別の記事で詳しく書きますね

Template 2 (Deep):
素晴らしい視点ですね！{expand on their point with additional insight}
このテーマは奥が深いので、{related topic}についても近々書く予定です

Template 3 (Redirect):
ありがとうございます！ちょうど{their question topic}について
詳しく書いた記事があります→「{related article title}」
```

**Instagram replies:**
```
Template 1 (Emoji-friendly):
{emoji} ありがとうございます！{short response}
{follow-up question}？

Template 2 (Story prompt):
嬉しいコメント！{reference their point}
あなたの{related experience question}もぜひ聞かせてください{emoji}

Template 3 (Save prompt):
ありがとうございます{emoji} 保存して後で見返してくださいね！
```

### 2. Conversation Starters (`/engagement converse`)

Follow-up templates to deepen engagement and spark discussion.

**X:**
```
Template 1 (Poll-style):
質問です：{topic}について、あなたはどちら派？
A) {option A}
B) {option B}
引用RTで教えてください

Template 2 (Experience sharing):
{topic}で一番{positive/negative experience}だったことは？
自分は{brief personal example}...
リプで教えてもらえると嬉しいです

Template 3 (Debate trigger):
「{controversial but respectful take}」
...と思ってるんですが、違う意見の方いますか？
建設的な議論大歓迎です
```

**note:**
```
Template 1 (End-of-article question):
---
この記事を読んで、あなたの{topic}体験はどうでしたか？
コメント欄で教えてください。次回の記事の参考にさせていただきます。

Template 2 (Challenge):
---
今日のアクションチャレンジ：
{specific small action related to article}を試してみて、結果をコメントで報告してください！
```

### 3. Funnel Nudge (`/engagement funnel`)

Templates designed to move audiences through your funnel.

> These templates are only generated when `funnel.enabled = true`.
> When funnel is disabled, this category is skipped with a message:
> "Funnel nudge templates require funnel mode. Enable with /setup-profile."

**X -> note (TOFU -> MOFU):**
```
Template 1 (Curiosity):
この続き、noteで3000字で詳しく解説しています
→ {note_url}
{specific detail they'll find in the article}がポイントです

Template 2 (Exclusive):
Xでは書けない{topic}の裏側、noteで公開中
→ {note_url}
フォロワーさん限定で{lead_magnet}も配布しています

Template 3 (Social proof):
この記事、すでに{N}人に読まれています
→ {note_url}
{key insight from the article}が特に反響大きかったです
```

**note free -> note paid (MOFU -> BOFU):**
```
Template 1 (Value preview):
この記事の続き（テンプレート＋実践ガイド付き）はこちら
→ {paid_article_url}
無料部分だけでも{specific value}は得られますが、
有料部分の{premium_value}が本当の差を生みます

Template 2 (Scarcity):
有料マガジン読者の方から「{positive feedback}」というお声をいただきました
月額{price}で{benefit description}
→ {membership_url}
```

**Instagram -> note:**
```
Template 1 (Bio link):
詳しくはプロフィールのリンクから！
noteで{article_count}本の無料記事を公開しています{emoji}

Template 2 (Story response):
ストーリーありがとうございます！
この内容、もっと詳しくnoteにまとめています
プロフのリンクからどうぞ{emoji}
```

### 4. Community Building (`/engagement community`)

Templates for building relationships and fostering a community feeling.

**Relationship building:**
```
Template 1 (Appreciation):
いつも見てくださってありがとうございます！
{username}さんの{specific thing you noticed about them}が素敵ですね

Template 2 (Collaboration):
{username}さんの{their content/post}、とても参考になりました
{specific point}について、一緒に深掘りしませんか？

Template 3 (Quote permission):
{username}さんのこのコメント、すごく的を射ていて
次回の記事で（匿名で）引用させていただいてもいいですか？
```

**Welcome new followers:**
```
Template 1 (X):
フォローありがとうございます！
{theme.main}について毎日発信しています
最近のおすすめ→「{recent_article_title}」{note_url}

Template 2 (note):
フォローありがとうございます！
{theme.main}について{frequency}で記事を書いています
まずはこちらがおすすめ→「{best_article_title}」
```

## Personalization

All templates are personalized based on `profile.json`:

- **Tone**: Match `style.tone` (casual/professional/storytelling/etc.)
- **Emoji**: Apply `style.emoji_usage` setting
  - `none`: No emoji in templates
  - `minimal`: 1-2 emoji per template
  - `moderate`: 3-5 emoji per template
  - `heavy`: Emoji-rich templates
- **First person**: Use `style.first_person` setting
- **Platform handles**: Use `funnel.x_handle`, `funnel.instagram_handle`
- **Content references**: Pull recent titles from content-history.json

## Workflow

### Step 1: Load Profile

Read `~/.content-autopilot/profile.json` for style and funnel settings.

### Step 2: Determine Category

If category is specified (`/engagement thank`), generate that category.
If no category (`/engagement`), show menu:

```
Engagement Template Categories:

1. Thank — Comment gratitude replies
2. Converse — Conversation starters & follow-up questions
3. Funnel — Nudge templates (X->note->paid)
4. Community — Relationship building & welcomes
5. All — Generate all categories

Select category (1-5):
```

### Step 3: Generate Templates

Generate 3-5 templates per platform for the selected category.
Personalize based on profile settings.

### Step 4: Display Templates

```
============================================
  Engagement Templates — {Category}
============================================

--- X ---
1. {template}
2. {template}
3. {template}

--- note ---
1. {template}
2. {template}
3. {template}

--- Instagram ---
1. {template}
2. {template}
3. {template}

============================================
Copy the template that fits your situation,
customize the {placeholders}, and send!
============================================
```

## Backward Compatibility

When `funnel.enabled = false`:
- Category 3 (Funnel Nudge) is unavailable — show message to enable funnel
- All other categories work normally
- CTAs in templates use traditional style (follow/like/share) instead of funnel flow
- No note referral URLs in X/Instagram templates

## Quality Gate

Before delivering:
- [ ] Templates match the user's tone from profile.json
- [ ] Emoji usage matches profile setting
- [ ] Platform conventions are respected (character limits, hashtags, etc.)
- [ ] Funnel templates only shown when funnel.enabled = true
- [ ] Placeholders are clearly marked with {} for easy customization
- [ ] Templates feel human and conversational, not robotic
- [ ] No generic filler — every template has a specific purpose and structure
