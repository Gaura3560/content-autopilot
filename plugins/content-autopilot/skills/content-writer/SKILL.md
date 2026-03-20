---
name: content-writer
description: Platform-native content generation for note, X, and Instagram. Creates completely different content per platform using the user's style profile. Applies bestseller title logic (9 categories) for maximum engagement. Includes note paid/free content judgment, cross-platform funnel CTAs (X/Instagram → note → monetization), A/B title tracking, and series mode with hooks/callbacks/cliffhangers.
---

# Content Writer

Generate platform-native content for note, X, and Instagram — each version unique, not cross-posted.

## When to Activate

- User says `/content-writer`
- Called automatically by `daily-autopilot` after topic selection
- User wants to write content for specific platforms
- User asks "write this for note/X/Instagram"

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- A selected topic (from `trend-scout` or user-provided)

## Workflow

### Step 1: Load Context

Read `~/.content-autopilot/profile.json` and extract:
- `style` — writing voice, tone, sentence patterns
- `platforms` — which platforms to generate for
- `audience` — who is reading
- `theme` — topic domain
- `brand` — for visual consistency references

Also receive from `trend-scout` or user:
- Selected topic title and angle
- Source URL(s) for reference
- Category (trending / overseas / evergreen)
- Funnel stage (TOFU / MOFU / BOFU) — if funnel is enabled

**Funnel context (if `profile.funnel.enabled` is true):**
- `funnel.note_url` — for cross-platform CTAs pointing to note
- `funnel.x_handle` — for X attribution
- `funnel.instagram_handle` — for Instagram attribution
- `funnel.monetization.type` — determines note CTA strategy
- `funnel.monetization.lead_magnet` — for lead capture CTAs

### Step 2: Research the Topic

If source URLs are provided:
1. Use WebSearch or WebFetch to gather detailed information
2. Extract key facts, data points, quotes, and examples
3. Identify the core insight to build content around

### Step 3: Generate Titles (Bestseller Logic)

Generate 3 title candidates using the Bestseller Title Logic system.

#### Quick Reference: 9 Title Logic Categories

| # | Logic | Description | Best For |
|---|-------|-------------|----------|
| 1 | Paradox | Flip reader's existing belief | Self-help, psychology |
| 2 | Numbers + Assertion | Specific numbers + confident promise | Universal (strongest) |
| 3 | Unexpected Combination | Collide unrelated concepts | Ads, brand names |
| 4 | Name the Enemy | Identify reader's obstacle | Business, money |
| 5 | Ideal Self | Show aspirational identity | Long-sellers, seminars |
| 6 | Hint at Secrets | Suggest hidden knowledge | Childcare, psychology |
| 7 | Extreme Simplicity | Surprisingly low effort for big result | Health, cooking, LPs |
| 8 | Coined Term | Create memorable new concept | Science, business |
| 9 | Question Format | Trigger metacognition | Seminars, psychology |

#### Title Generation Rules

1. **Always use 2-3 combined logics** (combined titles sell ~3x more than single-logic)
2. **Match logic to the topic's genre** using the genre compatibility table:
   - Self-help: Numbers + Paradox (S+)
   - Business: Enemy + Coined Term (S+)
   - Health: Numbers + Simplicity (S+)
   - AI/Tech: Simplicity + Paradox (S+)
3. **Avoid saturated patterns**: "XX's 9 割", "XX's 品格", "もしXX"
4. **Odd numbers outperform even** (+higher CTR)
5. **One negative word boosts CTR by +2.3%** (Nature 2023)

#### Platform-Specific Title Optimization

| Platform | Max Length | Priority Logics | Notes |
|----------|-----------|-----------------|-------|
| note | No limit | All 9 valid, prefer combined | Long titles OK (like book titles) |
| X | ~50 chars effective | Numbers, Simplicity, Paradox | Impact in first 28 chars |
| Instagram | ~40 chars visible | Simplicity, Question, Paradox | Must work as image overlay text |

**A/B Title History Check (NEW):**

If `~/.content-autopilot/content-history.json` has 10+ entries with `ab_titles.winner` data:
1. Calculate win rates per title logic combination
2. Prioritize logics with higher win rates in generation
3. Note the recommendation:
```
Based on your A/B history: {logic1} + {logic2} has a {X}% win rate.
Prioritizing this combination for today's titles.
```

Present 3 title candidates with which logics are used:
```
Title Candidates:
1. "7日で変わるAI仕事術 — まだ手作業で消耗してるの？"
   [Numbers + Simplicity + Enemy] — genre match: AI/Tech(S)
2. "AIが仕事を奪う」は嘘だった — 本当に危ないのは○○"
   [Paradox + Enemy + Secret] — genre match: Business(A)
3. "たった1つのAI習慣が、あなたの生産性を5倍にする理由"
   [Simplicity + Numbers + Question] — genre match: AI/Tech(S+)

Which title? (1 / 2 / 3 / or suggest your own)
```

**A/B Title Recording (NEW):**

After the user selects a title:
1. Record the chosen title as `ab_titles.chosen`
2. Record the next-best candidate as `ab_titles.alternative`
3. Both are stored in content-history.json by daily-autopilot (Step 6.5)
4. User can later mark the winner with `/title-winner {date} {A|B}`

### Step 4: Generate Platform-Native Content

Generate completely different content for each selected platform. Never copy-paste across platforms.

---

#### note Content

**Format specifications:**
- Length: 2,000-5,000 characters
- Structure: Title → Lead → H2 sections (3-5) → Conclusion → CTA
- Use `##` for section headings
- Short paragraphs (2-3 sentences max)
- Include 1-2 data points or specific examples per section

**Paid/Free Judgment:**

Evaluate the content against this decision table:

| Criterion | Free | Paid |
|-----------|------|------|
| Contains original research/data | No | Yes |
| Step-by-step actionable method | General | Detailed |
| Personal experience/case study | Surface | Deep |
| Templates or tools included | No | Yes |
| Topic depth | Overview | Expert-level |
| Reproducible results | Vague | Specific |

If 3+ criteria fall in "Paid" column, recommend paid content:

```
Recommendation: Paid content (4/6 paid criteria met)

Suggested split point:
--- Free section (visible to all) ---
[Introduction + Problem statement + Overview of the method]
--- Paid section (behind paywall) ---
[Detailed steps + Templates + Case study + Results data]

Free section should be ~40% of total, giving enough value to
demonstrate expertise while leaving the actionable details behind
the paywall.
```

**note Output Template:**
```markdown
# {Title}

{Lead paragraph — hook the reader in 2-3 sentences}

## {Section 1 heading}
{Content with specific examples}

## {Section 2 heading}
{Content with data points}

## {Section 3 heading}
{Content with actionable advice}

## まとめ
{Key takeaways — 3 bullet points}

---
# If funnel.enabled = true:
この記事が参考になったら「スキ」をお願いします

▼ さらに深掘りした内容はこちら
→ 「{related content title}」{URL}

▼ 「{funnel.monetization.lead_magnet}」を無料で配布中

# If funnel.enabled = false (traditional):
{CTA: follow, like, share, or link to related content}
```

---

#### X (Twitter) Content

**Format specifications:**
- Single tweet: max 280 characters (4,000 for Premium)
- Thread: 3-10 tweets, each self-contained but connected
- First tweet = hook (strongest statement)
- Last tweet = CTA

**Decision: Single vs Thread:**
| Content Type | Format |
|-------------|--------|
| One insight or opinion | Single tweet |
| Step-by-step method | Thread (5-7 tweets) |
| Story or case study | Thread (3-5 tweets) |
| Data or statistics | Single tweet + image |
| Announcement | Single tweet |

**Thread structure:**
```
Tweet 1 (Hook): Bold claim or surprising fact — stop the scroll
Tweet 2-N (Body): One point per tweet, concrete and specific
Tweet N+1 (CTA): Follow, retweet, or link
```

**X Output Template:**
```
--- Tweet 1 ---
{Hook: bold statement or surprising data}

--- Tweet 2 ---
{First key point with example}

--- Tweet 3 ---
{Second key point with evidence}

--- Tweet 4 ---
{Third key point or counter-intuitive insight}

--- Tweet 5 (CTA) ---
# If funnel.enabled = true:
もっと詳しく知りたい方はこちら
→ {funnel.note_url}

{funnel.x_handle} をフォローして最新の{theme.main}をチェック

# If funnel.enabled = false (traditional):
Like + RT if useful
Follow @{username} for more {theme}
```

---

#### Instagram Content

**Format specifications:**
- Caption: 300-500 characters (recommended for engagement; platform limit is 2,200 chars)
- Heavy line breaks for readability
- Up to 30 hashtags (mix of big/medium/niche)
- Emoji usage per profile.json style settings

**Instagram Output Template:**
```
{Hook line — first line visible before "more"}

.
{Main content — 3-5 short paragraphs}
.
{Key takeaway or call to action}
.
# If funnel.enabled = true:
詳しくはプロフィールのリンクから
→ noteで完全版を公開中
.
.
{Hashtags — 3 tiers}
#big_hashtag #big_hashtag #big_hashtag
#medium_hashtag #medium_hashtag #medium_hashtag
#niche_hashtag #niche_hashtag #niche_hashtag
```

**Hashtag strategy:**
- 10 big (100K+ posts): broad discovery
- 10 medium (10K-100K posts): niche visibility
- 10 niche (<10K posts): high ranking probability

### Step 4.5: Series Mode (NEW)

When content is being generated as part of an active series (series metadata passed from daily-autopilot):

**Add to each platform's content:**

1. **Hook** (opening): Use the series-defined hook as the opening line/concept
2. **Callback** (continuity): Add a reference to the previous part near the beginning
3. **Cliffhanger** (anticipation): Add a teaser for the next part at the end

**note content with series elements:**
```markdown
# {Title}

{Hook — series-defined opening concept}

{Callback — "In Part {N-1}, we covered {previous topic}. Today, we go deeper into..."}

## {Section 1}
{Content}

## {Section 2}
{Content}

## まとめ
{Key takeaways}

---
{Cliffhanger — "Next in the series: {Part N+1 teaser}. Coming {day}."}

{Standard CTA (funnel or traditional)}
```

**X thread with series elements:**
```
--- Tweet 1 ---
{Series title} Part {N}/{total}
{Hook}

--- Tweet 2 ---
{Callback: "Yesterday: {brief summary of Part N-1}"}
Today: {main point}

...

--- Last Tweet ---
{Cliffhanger: "Tomorrow: {Part N+1 teaser}"}
{CTA}
```

**Instagram with series elements:**
```
{Series title} Part {N}/{total} {emoji}
.
{Hook}
.
{Main content}
.
{Cliffhanger: "Next: {Part N+1 teaser}"}
.
{CTA + Hashtags}
```

If this is the last part of the series:
- Replace cliffhanger with a series wrap-up message
- Add CTA to the full series or next product/series

### Step 5: Output Files

Save generated content to `~/Desktop/content-autopilot-output/`:

```bash
mkdir -p ~/Desktop/content-autopilot-output
```

Files:
- `note_{date}.md` — note article
- `x_{date}.md` — X tweets/thread
- `instagram_{date}.md` — Instagram caption + hashtags

Also display all content directly in the terminal for easy copy-paste.

## Content Differentiation Rules

Each platform version MUST differ in:
1. **Opening** — different hooks per platform
2. **Depth** — note (deep) > Instagram (medium) > X (concise)
3. **Tone** — note (authoritative) / X (punchy) / Instagram (visual/emotional)
4. **Structure** — note (article) / X (thread) / Instagram (caption)
5. **CTA** — see Funnel CTA Strategy below (or traditional if funnel disabled)

## Funnel CTA Strategy

> **When `funnel.enabled = false`**: Use traditional CTAs — note (follow/paid) / X (RT/follow) / Instagram (save/share)

When `funnel.enabled = true`, all CTAs are designed to move the reader through the funnel:

### X CTA Strategy (TOFU — drive traffic to note)

```
Thread format (last tweet):
もっと詳しく知りたい方はこちら
→ {funnel.note_url}

{funnel.x_handle} をフォローして最新の{theme.main}をチェック
```

```
Single tweet format:
{content}

深掘りはプロフで → note
```

**30% Rule**: On X, reveal only 30% of the core insight. The remaining 70% lives on note. Create a curiosity gap — pose the "question" on X, provide the "answer" on note.

### Instagram CTA Strategy (TOFU — drive traffic to note)

```
{Main content}
.
詳しくはプロフィールのリンクから
→ noteで完全版を公開中
.
{Hashtags}
```

For Stories: use "swipe up" or "link in bio" template pointing to latest note article.

### note CTA Strategy (MOFU/BOFU — convert readers)

**Free article → Paid conversion:**
```markdown
---
この記事が参考になったら「スキ」をお願いします

▼ さらに深掘りした有料記事はこちら
→ 「{related paid article title}」

▼ 月額マガジンで毎週最新の{theme.main}をお届け
→ {membership URL}
```

**Lead magnet placement (in free articles):**
```markdown
▼ 「{funnel.monetization.lead_magnet}」を無料で配布中
→ {lead magnet URL or instructions}
```

**Paid article → Next conversion:**
```markdown
---
ここまで読んでくださりありがとうございます

▼ 次におすすめの記事
→ 「{next article title}」

▼ 全記事が読み放題のメンバーシップはこちら
→ {membership URL}
```

## Content Depth Differentiation (Funnel Mode)

When funnel is enabled, content depth varies by platform to create a natural pull toward note:

| Platform | Role | Information Depth | Purpose |
|----------|------|-------------------|---------|
| X | Teaser | 30% of core insight | Curiosity → drive to note |
| Instagram | Visual hook | 50% of core insight | Emotion → drive to note |
| note (free) | Value delivery | 80% of core insight | Trust building → paid conversion |
| note (paid) | Full version | 100% + bonus materials | Monetization |

**How to apply the depth rule:**

1. Write the note (free) version first as the "full" content
2. Extract the hook/surprising element for X (30%)
3. Extract the visual/emotional angle for Instagram (50%)
4. If paid: move the most actionable 20% behind the paywall

## Style Application

Apply the user's style from `profile.json`:
- Match `style.tone` across all platforms
- Use `style.sentence_length` as baseline
- Apply `style.emoji_usage` setting
- If `style.first_person` is true, write in first person
- If sample URLs exist in style, reference those patterns

## Quality Gate

Before delivering:
- [ ] Each platform version is genuinely different content (not reformatted)
- [ ] Titles use 2-3 combined bestseller logics
- [ ] note content is 2,000-5,000 chars with clear structure
- [ ] X content respects 280 char limit per tweet
- [ ] Instagram has ~30 relevant hashtags in 3 tiers (10 big + 10 medium + 10 niche)
- [ ] All content matches the user's style profile
- [ ] No generic hype language or filler
- [ ] Paid/free recommendation included for note (if applicable)
- [ ] Source attribution included where facts/data are cited
- [ ] If funnel enabled: X/Instagram CTAs point to note URL
- [ ] If funnel enabled: note CTAs point to paid content or lead magnet
- [ ] If funnel enabled: content depth follows 30%/50%/80%/100% rule
- [ ] If funnel disabled: traditional CTAs used (backward compatible)
- [ ] A/B titles recorded: chosen + alternative stored for later winner selection
- [ ] If series mode: hook, callback, and cliffhanger are included in content
- [ ] If series mode: part number and series title are visible
