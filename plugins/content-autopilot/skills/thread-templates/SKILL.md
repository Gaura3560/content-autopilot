---
name: thread-templates
description: Structured X thread templates — 12 proven thread formats (listicle, story, how-to, contrarian, etc.) with fill-in frameworks. Select a template, input your topic, and get a complete thread skeleton. Integrates with hook-library.
---

# Thread Templates

Write viral X threads faster with proven structural templates.

## When to Activate

- User says `/threads` or `/threads {template_name}`
- User says `/threads {topic}` to auto-select best template
- User asks "what thread format should I use?"
- User wants to write an X thread with a proven structure

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/threads` — Show all 12 templates
### `/threads {template}` — Use a specific template (e.g., `/threads listicle`)
### `/threads {topic}` — Auto-select best template for the topic
### `/threads fill {template} {topic}` — Generate a complete thread

## 12 Thread Templates

### 1. Listicle Thread
```
Structure: "X things about {topic}"
Tweets: 7-10
Best for: Tips, tools, habits, resources

Tweet 1: "{N} {things} that {outcome}:" [Hook with number]
Tweet 2: "1. {point}" [Most surprising first]
Tweet 3: "2. {point}"
...
Tweet N: "{N}. {point}" [Strongest last]
Tweet N+1: "Which one surprised you most? RT if useful" [CTA]
```

### 2. Story Thread
```
Structure: Personal narrative with lesson
Tweets: 5-8
Best for: Case studies, experiences, transformations

Tweet 1: "{Time reference}, {dramatic event happened}." [Story hook]
Tweet 2: "Here's what happened:" [Setup]
Tweet 3: "{Conflict/challenge}" [Rising action]
Tweet 4: "{Turning point}" [Climax]
Tweet 5: "{Resolution}" [What changed]
Tweet 6: "The lesson:" [Takeaway]
Tweet 7: "{Broader application for the reader}" [Universal truth]
Tweet 8: [CTA]
```

### 3. How-To Thread
```
Structure: Step-by-step guide
Tweets: 7-12
Best for: Tutorials, processes, workflows

Tweet 1: "How to {achieve outcome} in {timeframe}:" [Promise]
Tweet 2: "Step 1: {step}" [Most important first]
Tweet 3: "Step 2: {step}"
...
Tweet N: "Step {N}: {step}"
Tweet N+1: "That's it. {Timeframe} to {outcome}. Bookmark this." [CTA]
```

### 4. Contrarian Thread
```
Structure: Challenge conventional wisdom
Tweets: 5-7
Best for: Hot takes, thought leadership, debate

Tweet 1: "Unpopular opinion: {bold claim}" [Controversial hook]
Tweet 2: "Here's why everyone gets this wrong:" [Setup]
Tweet 3: "{Evidence/reasoning 1}" [Support]
Tweet 4: "{Evidence/reasoning 2}" [Build case]
Tweet 5: "Instead, do {alternative}:" [Your solution]
Tweet 6: "{Proof it works}" [Credibility]
Tweet 7: "Agree or disagree? Quote-tweet your take." [Engagement CTA]
```

### 5. Before/After Thread
```
Structure: Transformation showcase
Tweets: 6-8
Best for: Results, case studies, tool comparisons

Tweet 1: "{Topic}: Before vs After" [Visual hook]
Tweet 2: "BEFORE: {pain state}" [Relatable problem]
Tweet 3: "I was {specific struggle}..." [Personal touch]
Tweet 4: "Then I discovered {solution}:" [Turning point]
Tweet 5: "AFTER: {improved state}" [Transformation]
Tweet 6: "Specific results: {data}" [Proof]
Tweet 7: "Here's exactly how to make the switch:" [Actionable]
Tweet 8: [CTA]
```

### 6. Myth Buster Thread
```
Structure: Debunk common beliefs
Tweets: 7-10

Tweet 1: "{N} {topic} myths that are costing you {negative outcome}:" [Pain hook]
Tweet 2: "Myth 1: '{common belief}' Reality: {truth}"
...
Tweet N+1: "Stop believing these. Start doing {correct approach}." [CTA]
```

### 7. Data Thread
```
Structure: Statistics with insights
Tweets: 6-8

Tweet 1: "I analyzed {data source}. The results surprised me:" [Curiosity]
Tweet 2: "Finding 1: {stat}" [Most shocking first]
Tweet 3: "What this means: {insight}" [Interpretation]
...
Tweet N: "The biggest takeaway: {conclusion}" [Synthesis]
```

### 8. Prediction Thread
```
Structure: Future-looking analysis
Tweets: 6-8

Tweet 1: "{N} predictions for {topic} in {year/timeframe}:" [Forward-looking hook]
Tweet 2-N: "Prediction {N}: {prediction + reasoning}"
Tweet N+1: "Which prediction do you agree with? Which did I miss?" [Engagement]
```

### 9. Resource Thread
```
Structure: Curated collection
Tweets: 8-12

Tweet 1: "{N} free {resources} that are worth more than paid courses:" [Value hook]
Tweet 2-N: "{Resource name} — {what it does + why it's valuable} {link}"
Tweet N+1: "Bookmark this thread. You'll need it." [Save CTA]
```

### 10. Framework Thread
```
Structure: Mental model or framework
Tweets: 6-8

Tweet 1: "The {framework name} changed how I think about {topic}:" [Coined concept]
Tweet 2: "Here's the framework:" [Overview]
Tweet 3-5: "{Component 1/2/3 of the framework}" [Detail each part]
Tweet 6: "How to apply it today:" [Practical application]
Tweet 7: "Use this framework next time you {situation}." [CTA]
```

### 11. Comparison Thread
```
Structure: A vs B analysis
Tweets: 6-8

Tweet 1: "{A} vs {B} — which is better for {outcome}?" [Debate hook]
Tweet 2: "{A}: Pros"
Tweet 3: "{A}: Cons"
Tweet 4: "{B}: Pros"
Tweet 5: "{B}: Cons"
Tweet 6: "The verdict: {recommendation with nuance}" [Answer]
Tweet 7: "Which do you prefer? Reply with your choice." [Engagement]
```

### 12. Lesson Thread
```
Structure: Lessons from experience
Tweets: 7-10

Tweet 1: "{N} lessons from {experience/timeframe/project}:" [Experience hook]
Tweet 2-N: "Lesson {N}: {lesson} — {brief context/story}"
Tweet N+1: "The hardest lesson was #{N}. What's yours?" [Engagement]
```

## Auto-Select Logic

When user provides a topic, auto-recommend:

| Topic Type | Recommended Template | Why |
|-----------|---------------------|-----|
| Tips/advice | Listicle or How-To | Highest save rate |
| Personal experience | Story or Before/After | Emotional connection |
| Hot take | Contrarian | Maximizes engagement/debate |
| Industry analysis | Data or Prediction | Authority building |
| Tool recommendation | Resource or Comparison | Utility value |
| Teaching a concept | Framework or How-To | Educational |

## Integration with Other Skills

- **hook-library**: Pulls relevant hooks for Tweet 1
- **content-writer**: Uses thread templates when generating X content
- **repurpose**: `/repurpose note→x` auto-selects best thread template
- **batch-generator**: Varies thread structures across the week

## Quality Gate

- [ ] Template matches the topic type
- [ ] Tweet 1 is a genuine scroll-stopper
- [ ] Each tweet adds value (no filler tweets)
- [ ] Thread length matches content depth (not padded)
- [ ] CTA drives engagement (reply/RT/bookmark)
- [ ] All tweets ≤ 280 chars
