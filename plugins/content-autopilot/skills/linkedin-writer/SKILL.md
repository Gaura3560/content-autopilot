---
name: linkedin-writer
description: LinkedIn post and article generator — create platform-native LinkedIn content optimized for the professional audience algorithm. Story-format posts, carousel documents, and long-form articles with B2B engagement patterns.
---

# LinkedIn Writer

Reach decision-makers and professionals — LinkedIn's algorithm rewards different content than X or Instagram.

## When to Activate

- User says `/linkedin` or `/linkedin {topic}`
- User says `/linkedin {file_path}` to convert existing content
- User asks "write a LinkedIn post"
- User wants to reach a professional/B2B audience

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/linkedin {topic}` — Generate original LinkedIn post
### `/linkedin {file_path}` — Convert existing content for LinkedIn
### `/linkedin article {topic}` — Generate LinkedIn article (long-form)
### `/linkedin templates` — Show LinkedIn post templates

## LinkedIn Algorithm Essentials

| Factor | Impact | Strategy |
|--------|--------|----------|
| Dwell time | Highest | Long-form posts that keep people reading |
| Comments | High | End with a question to spark discussion |
| No external links | High | Links in comments, not in post body |
| First hour engagement | High | Post when your network is active |
| Story format | High | Personal narratives outperform everything |
| Carousel documents | High | PDF carousels get massive reach |

## Post Templates

### 1. Story Post (highest engagement)
```
{One-line hook that creates curiosity}

{Short paragraph setting the scene — personal experience}

{The challenge/problem you faced}

{What you learned/discovered}

{The insight that's valuable to others}

{3-5 bullet takeaways}

---

{Question to spark comments}

{No link in post — add link in first comment}
```

### 2. Framework Post
```
I've been {doing X} for {N} years.

Here's the framework that changed everything:

The {Framework Name}:

Step 1: {name}
→ {one-line explanation}

Step 2: {name}
→ {one-line explanation}

Step 3: {name}
→ {one-line explanation}

The result? {specific outcome}

Which step do you struggle with most?
```

### 3. Contrarian Post
```
Unpopular opinion:

{Bold claim that challenges industry conventional wisdom}

Here's why:

{Evidence point 1}

{Evidence point 2}

{Evidence point 3}

I know this is controversial.

But the data doesn't lie.

Agree or disagree? I'd love to hear your perspective.
```

## Workflow

### Step 1: Determine Content Type

```
LinkedIn content options for "{topic}":

1. Story post — personal experience angle (highest reach)
2. Framework post — teach a system/method
3. Contrarian post — challenge industry norms
4. Carousel document — visual slides (PDF)
5. Article — long-form thought leadership

Recommended: {recommendation based on topic type}
Select (1-5):
```

### Step 2: Generate Content

Apply LinkedIn-specific formatting:
- **Short paragraphs** (1-2 sentences, lots of white space)
- **No links in body** (kills reach — put in first comment)
- **Strong opening line** (visible in feed before "see more")
- **End with a question** (drives comments → algorithm boost)
- **Professional tone** but with personality
- **Hashtags**: 3-5 maximum, at the bottom

### Step 3: Generate First Comment

```
First comment (post immediately after publishing):

"{context or link}"
→ {note_url} (if funnel enabled)
→ {resource link}

This comment contains the link that would have killed your reach in the main post.
```

### Step 4: Save Output

```
~/Desktop/content-autopilot-output/
  linkedin_{date}.md           # Post text
  linkedin_comment_{date}.md   # First comment with links
  linkedin_carousel_{date}.md  # Carousel script (if applicable)
```

## LinkedIn → Funnel Integration

When `funnel.enabled = true`:
- LinkedIn becomes a new TOFU channel (professional audience)
- CTA in first comment points to note
- LinkedIn articles can link directly to note (long-form to long-form)

## Quality Gate

- [ ] Opening line is visible and compelling before "see more"
- [ ] No external links in post body (link in first comment)
- [ ] Professional tone maintained (not too casual)
- [ ] Ends with a discussion-sparking question
- [ ] Formatting uses plenty of white space
- [ ] Hashtags: 3-5 maximum, relevant to professional audience
- [ ] Content provides genuine professional value
