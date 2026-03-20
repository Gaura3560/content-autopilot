---
name: course-builder
description: Transform your content archive into a structured online course — auto-analyze content-history to identify teachable modules, generate curriculum, lesson scripts, quizzes, and assignments. You've already written the course — this skill reveals it.
---

# Course Builder

Your articles ARE a course — you just haven't organized them yet.

## When to Activate

- User says `/course-builder` or `/course`
- User asks "can I turn my content into a course?"
- User wants to create an online course or workshop

## Commands

### `/course` — Analyze content archive and propose course structure
### `/course {topic}` — Build course on specific topic
### `/course lesson {N}` — Generate detailed lesson content

## Workflow

### Step 1: Content Archive Analysis

Scan content-history.json and cluster articles by topic:

```
Course Potential Analysis:
============================================

Your content archive: {N} articles

Identified course candidates:

1. "{Course Title}" — {N} articles form a natural curriculum
   Coverage: beginner → advanced progression exists
   Modules: {N} modules, {N} lessons estimated
   Gap: {missing topics to fill}
   Revenue potential: ¥{estimate} (based on pricing-strategy data)

2. "{Course Title}" — {N} articles
   ...

Recommended: Course #1 — strongest curriculum with fewest gaps

============================================
```

### Step 2: Generate Curriculum

```
Course: "{Title}"
============================================

Module 1: {Foundation}
  Lesson 1.1: "{title}" — based on: {existing_article}
  Lesson 1.2: "{title}" — based on: {existing_article}
  Lesson 1.3: "{title}" — NEW (gap to fill)
  Quiz: {3-5 questions testing Module 1 concepts}

Module 2: {Core Skills}
  Lesson 2.1-2.4...
  Assignment: {practical exercise}

Module 3: {Advanced Application}
  Lesson 3.1-3.3...
  Assignment: {real-world project}

Module 4: {Mastery}
  Lesson 4.1-4.2...
  Final project: {capstone assignment}

--- Course Metrics ---
Total lessons: {N} ({existing} from archive + {new} to create)
Estimated creation time: {hours} hours (for new content only)
Pricing recommendation: ¥{price} (from /pricing research)
Platform: Udemy / Teachable / note membership / standalone

============================================
```

### Step 3: Generate Lesson Content

For each lesson, create:
- Video script (from voice-script patterns)
- Slide outline (from slide-deck patterns)
- Downloadable resource (from lead-magnet-creator patterns)
- Quiz questions
- Action items for students

## Quality Gate

- [ ] Curriculum has logical progression (beginner → advanced)
- [ ] Existing content reused efficiently (not recreating)
- [ ] Gaps identified and creation plan included
- [ ] Each module has assessment (quiz/assignment)
- [ ] Pricing based on market research
