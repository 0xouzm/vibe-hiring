# TalentDrop Question Bank Design

## Design Methodology

### Who Designs the Questions?

The platform designs them centrally — not by gut feeling, but grounded in three intersecting disciplines:

1. **Organizational Behavior** — determines "what dimensions to measure"
2. **Psychometrics** — determines "how to measure effectively"
3. **Game Theory** — determines "how to prevent gaming"

In practice, this requires collaboration among organizational psychologists, data scientists, and product designers. For the MVP, we can rapidly build v1 based on established academic models (e.g., Big Five, Schwartz Values), then iterate with real-world data.

### How Do We Ensure Quality?

Four validation criteria:

| Criterion | Meaning | How to Verify |
|---|---|---|
| **Validity** | We're actually measuring what we intend to | High-scorers genuinely have higher 90-day retention |
| **Reliability** | Same person's results are stable over time | Test-retest correlation > 0.7 after two weeks |
| **Discrimination** | Different people actually answer differently | No single option selected by > 60% of respondents |
| **Gaming resistance** | No option yields "better" results through guessing | Match success rates show no statistical difference across options |

### Iteration Mechanism

The question bank is not a one-time design:
- Quarterly analysis of question performance data (declining discrimination → replace)
- If a specific question gets widely discussed on social media → immediately swap in a variant
- A/B test new questions vs. old questions on match effectiveness
- Reverse-optimize question weights based on 90-day retention data

---

## Measurement Dimension Model

Based on organizational behavior research, we define 8 core dimensions (each is a spectrum — no good or bad):

```
Dimension 1: Work Pace          — Fast Iteration ←→ Deep Craftsmanship
Dimension 2: Collaboration Mode — Independent Driver ←→ Team Collaborator
Dimension 3: Decision Style     — Data-Driven ←→ Intuition-Led
Dimension 4: Communication      — Direct & Frank ←→ Diplomatic & Nuanced
Dimension 5: Uncertainty Tolerance — Embrace Ambiguity ←→ Seek Clarity
Dimension 6: Growth Path        — Deep Specialist ←→ Broad Generalist
Dimension 7: Motivation Source  — Mission & Purpose ←→ Reward & Recognition
Dimension 8: Conflict Resolution — Direct Confrontation ←→ Indirect Navigation
```

Key: **Both ends of every dimension are valid.** A fast-iteration person in a deep-craftsmanship team will be miserable — and vice versa.

---

## Layer 1: Platform Standard Behavioral Scenario Questions (30 Questions)

### Design Principles

1. Each question maps to 1-2 dimensions
2. Each dimension is covered by at least 3 questions (cross-validation)
3. All options are "reasonable good answers" — they just reflect different styles
4. Scenarios are specific enough to prevent generic posturing

### Question Examples

---

**Q01 [Dimensions: Work Pace + Decision Style]**

You've picked up a new feature. The PM says "the sooner it ships, the better — let's see what users think." After assessing the work, you find the quick approach has obvious technical shortcomings but can ship in one week; the thorough approach takes three weeks but produces a cleaner architecture. You would:

- A. Ship the quick version, collect data, then decide whether to refactor
- B. Negotiate a middle ground with the PM: a workable version in two weeks
- C. Advocate for the thorough approach, using data to explain the long-term cost of tech debt
- D. Ship quick but simultaneously start a refactor plan so debt doesn't accumulate

> Measures: A/D = fast-iteration bias, C = depth-first bias, B = balanced negotiator
> Anti-gaming: All options "look professional" — candidates can't guess the company's preference

---

**Q02 [Dimensions: Collaboration Mode + Communication]**

Friday afternoon — you spot a production risk. It's not a critical bug, but if left alone it could cause issues next week. Most of the team has wrapped up for the day. You would:

- A. Fix it yourself in a couple of hours, then share what you did at Monday standup
- B. Post in the team channel explaining the issue, see if anyone wants to jump in
- C. Create a detailed ticket marked high-priority, tackle it first thing Monday
- D. Reach out directly to the colleague closest to that code, fix it together quickly

> Measures: A = independent action, B = open team collaboration, C = process-driven, D = targeted pairing
> Cross-validates: Compared with Q14 (team communication frequency preference)

---

**Q03 [Dimension: Uncertainty Tolerance]**

You've been assigned to a brand-new project. Your manager says "here's the rough direction — figure out how to get there." No spec, no reference. Your first instinct is:

- A. Excitement — finally a chance to define something from zero
- B. Spend a few days researching comparable products and approaches before committing
- C. Go back to your manager and try to pin down requirements and boundaries
- D. Build a minimal prototype fast, then use it to drive a more concrete discussion

> Measures: A = high ambiguity embrace, D = action to resolve ambiguity, C = clarity-seeking, B = cautious research
> Note: Every team needs different types — there is no right or wrong

---

**Q04 [Dimensions: Conflict Resolution + Communication]**

During code review a senior colleague leaves extensive change requests on your PR. After careful reading, you believe most are stylistic preferences rather than genuine issues. You would:

- A. Reply point by point with your reasoning, linking docs or best practices
- B. Hop on a 15-minute call to talk through the key disagreements
- C. Accept most suggestions — they're more senior, and team harmony matters
- D. Accept the valid ones; on pure style issues, say "personal preference — keeping as-is"

> Measures: A = data-backed confrontation, B = direct + relationship-aware,
> C = conflict-avoidant / authority-deferring, D = principled boundary-setting
> Cross-validates: Compared with Q18 (team disagreement handling)

---

**Q05 [Dimension: Motivation Source]**

Four offers are identical in pay, location, and title. The companies differ. Which do you lean toward?

- A. A company tackling climate change — technically challenging but business model still unproven
- B. A high-growth company that tripled revenue this year — equity could be very valuable
- C. A company with exceptional engineering culture — several domain luminaries on the team
- D. A profitable, stable company with great work-life balance and predictable annual raises

> Measures: A = mission-driven, B = growth/reward-driven, C = craft/mastery-driven, D = stability/balance-driven
> Forced to pick one — reveals true priority

---

**Q06-Q10:** See complete question bank in `question-bank-full.md`

---

### Full 30-Question Coverage Matrix

```
Dimension            | Primary Questions | Cross-Validation | Forced Rank/Budget
---------------------|-------------------|-----------------|-------------------
Work Pace            | Q01, Q06          | Q15, Q22        | Q10
Collaboration Mode   | Q02, Q07          | Q16, Q23        | Q10
Decision Style       | Q01, Q11          | Q17, Q24        | Q27
Communication        | Q04, Q08          | Q18, Q25        | -
Uncertainty Tolerance| Q03, Q06          | Q19, Q26        | -
Growth Path          | Q07, Q09          | Q20, Q28        | Q09
Motivation Source    | Q05, Q09          | Q21, Q29        | Q09
Conflict Resolution  | Q04, Q08          | Q18, Q30        | -
```

Each dimension is covered by 4-5 questions from different angles, ensuring effective consistency detection.

---

## Layer 2: Role-Specific Questions (15 Questions)

Auto-configured by job family. Candidates and companies answer the same set.

### Engineering Roles (3 Examples)

**E01 [Technical Decision Style]**

The team needs to pick a new core framework. Two options: Framework X has an active community, great docs, but average performance. Framework Y has excellent performance but is newer with a small community. You lean toward:

- A. Choose X — team efficiency and maintenance costs matter more
- B. Choose Y — performance is the competitive edge, the community will grow
- C. Run a one-week benchmark, let data decide
- D. Start with X, but design key modules with swappable interfaces for future migration

**E02 [Code Philosophy]**

A piece of working but inelegant code has been running stable in production for a year. A new requirement needs to build on it. You would:

- A. Take the opportunity to refactor the whole thing — new feature + tech improvement together
- B. Only change what's absolutely necessary — if it's working, don't touch it
- C. Write an adapter layer wrapping the old code, develop the new feature on top
- D. Assess the situation — if the old code is truly terrible, rewrite; otherwise, build on it

**E03 [Debugging Mindset]**

A production bug appears intermittently — 3 occurrences in 10 days, no clear trace in logs. Your first step:

- A. Add extensive logging and monitoring, wait for it to happen again to catch it in the act
- B. Hypothesize trigger conditions from the timing pattern, try to reproduce locally
- C. Pull in the person who knows this code best, review suspicious logic together
- D. Check recent commit history — see if a specific change introduced it

### Designer, Product, Operations roles each have their corresponding 15 questions (omitted here).

---

## Layer 3: Company Custom Questions (5 Max)

### Strict Constraints

Company-designed questions must satisfy:

1. **Balanced options:** At least 3 options, all reasonable
2. **No leading language:** No questions like "do you agree with our XX culture"
3. **AI quality review:** Checked for leading/discriminatory language after submission
4. **Low weight:** This layer accounts for no more than 15% of total match scoring
5. **Candidate reporting:** Anonymous reporting of perceived bias is available

### Acceptable Custom Question (Example)

**"We're a 12-person early-stage team. Which work state resonates with you most?"**

- A. Constantly switching roles throughout the day — coding in the morning, customer calls in the afternoon, revising plans at night
- B. Focused deep work on one core direction — other tasks handled by teammates
- C. Doing a bit of everything, but primarily concentrating on your strongest area

### Unacceptable Custom Questions (Examples)

```
"Do you identify with hustle culture?" → Leading — implies the company expects overwork
"Are you willing to sacrifice personal time for the company mission?" → Leading + coercive
"Do you think remote work is productive?" → Implies a "correct answer"
```

---

## Cross-Validation Example

### Conflict Resolution Dimension

A candidate's answers across 4 questions should be broadly consistent:

```
Q04 (code review disagreement)     → Selected A (reply with reasoning point by point)
Q08 (sprint planning — disagree with lead) → Selected A (raise concern on the spot)
Q18 (team direction split)         → Should also lean toward direct confrontation
Q30 (cross-department conflict)    → Should also lean toward direct communication

If Q04 → A (direct confrontation) but Q08 → B (private discussion):
→ Reasonable variation — direct with peers, diplomatic with superiors
→ Consistency score: moderate (acceptable variation, no penalty)

If Q04 → A (direct confrontation) but Q08 → C (stay silent) and Q18 → C (avoid conflict):
→ Q04 may have been faked
→ Consistency score: low → reduce confidence for this dimension
```

---

## Summary

| Layer | Questions | Designer | Weight | Core Function |
|---|---|---|---|---|
| Layer 1 Standard | 30 | Platform (org psychologists) | 60% | Behavioral scenarios + forced ranking + cross-validation |
| Layer 2 Role-specific | 15 | Platform (auto-configured by role) | 25% | Professional capability matching + work philosophy |
| Layer 3 Company Custom | ≤ 5 | Company (with review constraints) | 15% | Custom culture fit |
| **Total** | **≤ 50** | | **100%** | |

**MVP Action Items:**
1. Complete the full design of all 30 Layer 1 standard questions
2. Run validity/reliability testing with 100 participants (same person retakes after two weeks, verify stability)
3. Analyze answer distributions, eliminate low-discrimination questions (any option selected by > 60%)
4. Post-launch: continuously optimize question weights using 90-day retention data
