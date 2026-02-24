# TalentDrop Company DNA 题库（20 题完整版）

> 设计方法论和聚合算法详见 `company-dna-design.md`
> 本文档包含全部 20 道 Company DNA 行为场景题
> 填写者：HR + 5 名以上同团队员工（匿名）

## 维度覆盖矩阵

```
维度                    | 主测题            | 交叉验证题        | 预算/排序题
------------------------|------------------|------------------|----------
工作节奏 (Pace)          | CQ01, CQ06       | CQ13             | CQ17
协作模式 (Collab)        | CQ02, CQ10       | CQ07, CQ16       | CQ17
决策风格 (Decision)      | CQ09             | CQ01             | CQ18
表达风格 (Expression)    | CQ04             | CQ02, CQ08, CQ16 | -
不确定性容忍 (Unc)       | CQ03, CQ06       | CQ09             | -
成长路径 (Growth)        | CQ11, CQ15       | CQ07             | CQ19
驱动力来源 (Motiv)       | CQ05, CQ12       | -                | CQ19
执行风格 (Execution)     | CQ14             | CQ08, CQ13       | CQ17
全维度交叉              | -                | -                | CQ20
```

---

## CQ01 — Pace + Decision

A feature is technically ready but has a few rough edges. The product lead says "let's get user feedback ASAP." In your team, the most likely outcome is:

- A. Ship it now, gather data, polish based on real feedback — speed is how we learn
- B. Take one more week to smooth the most visible rough edges, then ship — balance matters
- C. Hold until the experience is polished — we'd rather be late than ship something half-baked
- D. Ship to a small beta group first, validate, then roll out broadly — controlled velocity

> Measures: A = fast-iteration culture, C = depth-first culture, B/D = balanced
> Cross-validates: CQ13 (backlog handling), CQ06 (proven vs. novel)
> Career DNA mirror: Q01

---

## CQ02 — Collab + Expression

An engineer notices a non-urgent production risk on Friday afternoon. Most of the team has wrapped up for the week. In your team, what typically happens?

- A. They fix it themselves and mention it at Monday standup — individual initiative is valued
- B. They post in the team channel describing the issue, and whoever's around jumps in
- C. They create a detailed ticket marked high-priority — process ensures nothing is missed
- D. They ping the person closest to that code and pair-fix it quickly — targeted collaboration

> Measures: A = independent culture, B = open-collaborative, C = process-driven, D = selective pairing
> Cross-validates: CQ10 (parallel work style), CQ16 (cross-team communication)
> Career DNA mirror: Q02

---

## CQ03 — Uncertainty Tolerance

A new project lands with a rough direction but no spec, no wireframes, and no reference implementation. How does your team typically kick it off?

- A. Dive in — people start building prototypes and figure it out as they go
- B. Spend a few days researching comparable approaches, then align on a plan
- C. Push for a clearer brief before committing resources — ambiguity wastes effort
- D. Run a quick spike to surface unknowns, then regroup and plan properly

> Measures: A = high ambiguity embrace, B = research-first moderate, C = clarity-seeking, D = experiment-to-clarify
> Cross-validates: CQ06 (novel vs. proven), CQ09 (decisions under uncertainty)
> Career DNA mirror: Q03

---

## CQ04 — Expression

During a design review, a relatively junior team member disagrees with a senior colleague's approach. In your team's culture, what usually happens?

- A. They voice it directly in the meeting — everyone's opinion carries equal weight regardless of seniority
- B. They raise it diplomatically, often framing it as a question rather than a challenge
- C. They typically hold back in the meeting and mention it privately afterward
- D. They share their perspective in writing (comment, doc, or message) after reflecting

> Measures: A = direct-open culture, B = diplomatic-respectful, C = hierarchy-aware, D = written-deliberate
> Cross-validates: CQ02 (communication style), CQ08 (missed deadline response), CQ16 (conflict handling)
> Career DNA mirror: Q04, Q08

---

## CQ05 — Motivation

When you think about why your best-performing team members stay (beyond compensation), the primary reason is usually:

- A. The mission — they believe in what the company is trying to achieve in the world
- B. Growth trajectory — they see a clear path to bigger scope, title, and influence
- C. The craft — they get to work on technically challenging problems with talented peers
- D. The balance — predictable hours, manageable stress, and respect for personal life

> Measures: A = mission-driven culture, B = growth/ambition-driven, C = craft/mastery-driven, D = stability-driven
> Cross-validates: CQ12 (recognition style)
> Career DNA mirror: Q05

---

## CQ06 — Pace + Uncertainty Tolerance

Your team is evaluating two technical approaches: Path A is battle-tested with predictable results; Path B comes from recent research with better theoretical performance but zero production use. With a 3-month deadline, your team would most likely:

- A. Go with A — proven and reliable beats theoretical promise
- B. Spend a week stress-testing B; if it holds up, switch; if not, A is the fallback
- C. Go with B — three months is enough runway, and breakthrough results justify the risk
- D. Build on A as the main track while exploring B in parallel as a future option

> Measures: A = conservative, B = quick-validation, C = aggressive exploration, D = pragmatic hedge
> Cross-validates: CQ01 (shipping pace), CQ03 (ambiguity response)
> Career DNA mirror: Q06

---

## CQ07 — Collab + Growth

When a team member develops deep expertise in a specific area, how does the team typically share and leverage that knowledge?

- A. They write internal docs or record walkthroughs — scalable self-serve knowledge
- B. They become the go-to person; others simply ask them when needed — organic and personal
- C. They run occasional knowledge-sharing sessions or workshops for the broader team
- D. They pair with others on real tasks so knowledge transfers through practice

> Measures: A = systematic/documentation culture, B = informal/people-dependent, C = structured sharing, D = hands-on mentoring
> Cross-validates: CQ11 (learning culture), CQ15 (specialist vs. generalist)
> Career DNA mirror: Q07

---

## CQ08 — Expression + Execution

A team member misses a committed deadline by several days. No external factors — they simply underestimated the complexity. In your team, the typical response is:

- A. They proactively flag the delay early, share a revised plan, and the team adjusts — transparency is expected
- B. There's a retrospective to understand what happened and improve estimation going forward — process improvement
- C. It's handled quietly — deadlines shift, no big deal as long as quality is good
- D. There's visible frustration — commitments are taken seriously, and missing them has social consequences

> Measures: A = transparency-first culture, B = process-improvement culture, C = flexible/low-ceremony, D = accountability-driven
> Cross-validates: CQ04 (expression openness), CQ14 (project tracking)
> Career DNA mirror: Q17, Q20

---

## CQ09 — Decision + Uncertainty Tolerance

A high-stakes decision needs to be made this week. You have partial data, conflicting team opinions, and no time for thorough analysis. How does your team typically handle this?

- A. The most senior person makes the call based on experience — speed matters, and they've seen this before
- B. The team runs a rapid structured analysis — even compressed, data beats gut feel
- C. They convene a quick group discussion, surface perspectives, and go with the emerging consensus
- D. They choose the most reversible option — commit minimally, learn fast, adjust

> Measures: A = experience/intuition-driven, B = data-driven under pressure, C = consensus-driven, D = reversibility-driven
> Cross-validates: CQ01 (speed vs. quality tradeoff), CQ03 (ambiguity handling)
> Career DNA mirror: Q14

---

## CQ10 — Collaboration Mode

Three team members are building separate modules that need to integrate. No one has defined the interfaces yet. The deadline is tight. In your team, what usually happens?

- A. Each person starts building based on assumptions, then aligns when something concrete exists
- B. The team blocks out a half-day to design interfaces together before anyone writes code
- C. One person drafts the interface contracts and shares for async feedback — initiative-driven
- D. The two most tightly coupled modules pair up first; the third person joins once the core contract exists

> Measures: A = independent-first, B = collaborative planning, C = initiative + async, D = pragmatic pairing
> Cross-validates: CQ02 (collaboration pattern), CQ07 (knowledge sharing)
> Career DNA mirror: Q16

---

## CQ11 — Growth

Your company offers a full week of paid professional development per year with no strings attached. Most people on your team would choose to:

- A. Go deep — advanced workshop or certification in their core domain
- B. Go wide — explore something deliberately outside their daily work
- C. Go strategic — shadow leadership, attend strategy sessions, understand the bigger picture
- D. Go applied — skip courses and spend the week building a prototype for an unsolved internal problem

> Measures: A = specialist culture, B = breadth-seeking, C = strategic/leadership track, D = builder/pragmatic culture
> Cross-validates: CQ07 (knowledge sharing), CQ15 (specialist vs. generalist preference)
> Career DNA mirror: Q22

---

## CQ12 — Motivation

After shipping a major release following months of intense work, how does your team typically celebrate or recognize the effort?

- A. Public recognition — shout-outs at all-hands, leadership acknowledgment, visible praise
- B. Tangible rewards — bonuses, extra time off, team dinner funded by the company
- C. Autonomy — the team gets to choose what they work on next, a period of self-directed work
- D. Low-key acknowledgment — a brief "great job" in standup, then on to the next thing

> Measures: A = recognition-driven culture, B = reward-driven, C = autonomy-driven, D = heads-down culture
> Cross-validates: CQ05 (what makes people stay)
> Career DNA mirror: Q29

---

## CQ13 — Execution + Pace

A new team member inherits a project with 20+ open bugs and a long feature backlog. No hard deadline — management says "make it better." In your team's culture, the expected approach is:

- A. Start shipping quick wins immediately — visible progress builds momentum and trust
- B. Spend the first week understanding the full picture, then create a prioritized roadmap
- C. Identify the root architectural issue causing most bugs, fix that foundation first — even if nothing visible ships for weeks
- D. Categorize by effort/impact, clear all quick wins in week one, then reassess

> Measures: A = ship-first culture, B = plan-first, C = foundation-first depth, D = pragmatic velocity
> Cross-validates: CQ01 (shipping philosophy), CQ08 (deadline culture)
> Career DNA mirror: Q12

---

## CQ14 — Execution

For a cross-team project spanning 6+ weeks with multiple dependencies, how does your team typically track progress?

- A. Detailed project tracker with milestones, dependency maps, and regular syncs — structured and visible
- B. Lightweight shared doc with key milestones and target dates — check in as milestones approach
- C. Informal — people know what they're doing, progress surfaces through Slack and standups
- D. Adaptive — define the end state and first milestone clearly, re-plan after each milestone based on what we learned

> Measures: A = highly structured, B = moderately structured, C = low structure/trust-based, D = iterative/adaptive
> Cross-validates: CQ08 (accountability culture), CQ13 (backlog approach)
> Career DNA mirror: Q19

---

## CQ15 — Growth

If you had to fill one open headcount on your team right now, and two equally qualified candidates applied — one with 8 years of deep expertise in your exact domain, the other with 5 years across three different domains — your team would most likely prefer:

- A. The deep specialist — depth is hard to find, and we need someone who can own complex problems end-to-end
- B. The cross-domain generalist — versatility matters more; they'll bring fresh perspectives and adapt faster
- C. The specialist, but we'd want them to gradually broaden — T-shaped is the ideal
- D. The generalist, but only if they show the ability to go deep when needed — depth on demand

> Measures: A = specialist culture, B = generalist culture, C = specialist-leaning balanced, D = generalist-leaning balanced
> Cross-validates: CQ07 (knowledge sharing), CQ11 (learning preference)
> Career DNA mirror: Q25

---

## CQ16 — Expression + Collab

Another department promised a client that your team would deliver a feature in 6 weeks. Your honest estimate is 10 weeks. No one consulted your team before making the commitment. How would your team handle this?

- A. Arrange a private meeting with the other department, lay out the reality, and jointly renegotiate before telling the client
- B. Commit to the timeline but aggressively cut scope — deliver a "Phase 1" on time, full version later
- C. Escalate to shared leadership — present the trade-offs transparently and let executives decide
- D. Go directly to the client with the other department, explain the realistic timeline, and offer an interim plan

> Measures: A = collaborative-diplomatic, B = pragmatic-accommodating, C = hierarchical-transparent, D = direct-external
> Cross-validates: CQ04 (expression culture), CQ02 (collaboration pattern)
> Career DNA mirror: Q30

---

## CQ17 — Pace + Collab + Execution (Budget Allocation)

Distribute 100% to reflect how your team actually spends its collective energy in a typical sprint:

- Heads-down execution (coding / designing / building): ___%
- Internal team discussion, review, and pairing: ___%
- Cross-functional communication (PM, stakeholders, other teams): ___%
- Learning, research, and exploration: ___%
- Documentation, process improvement, and knowledge management: ___%

> Format: Must total 100%. Reveals actual time allocation culture.
> No "correct" distribution — a team that spends 70% heads-down isn't better or worse than one at 40%.
> Cross-validates: CQ01 (pace), CQ10 (collaboration), CQ14 (execution style)
> Career DNA mirror: Q10

---

## CQ18 — Decision (Budget Allocation)

Allocate 100 points to reflect how your team actually weighs these inputs when making major decisions — not how you think you should, but how it really works:

- Quantitative evidence — metrics, benchmarks, A/B test results: ___ pts
- Experience and pattern recognition — "we've seen this before": ___ pts
- Stakeholder alignment — getting buy-in from affected people: ___ pts
- First-principles reasoning — working from fundamentals and constraints: ___ pts

> Format: Must total 100. A flat 25/25/25/25 signals contextual flexibility.
> Measures: Heavy quantitative = data-rationalist culture, heavy experience = intuition-trusting, heavy stakeholder = consensus-oriented, heavy first-principles = analytical-independent
> Cross-validates: CQ09 (decision under pressure)
> Career DNA mirror: Q27

---

## CQ19 — Motiv + Growth (Forced Ranking)

Rank these descriptions of your team's culture from most accurate to least accurate (1 = most, 5 = least):

- **Mission-Driven** — People are here because they believe in the impact we're making
- **Growth Engine** — People are here because they're growing faster than anywhere else
- **Craft Culture** — People are here because they get to do the best work of their careers
- **Well-Compensated** — People are here because the total compensation is genuinely competitive
- **Life-Friendly** — People are here because the work-life integration is genuinely respected

> Format: Forced ranking — no ties allowed
> Signal: Ranking pattern reveals the dominant cultural value proposition
> Cross-validates: CQ05 (why people stay), CQ12 (how effort is recognized)
> Career DNA mirror: Q09

---

## CQ20 — Full Cross-Dimension (Forced Ranking)

Think about the last few successful hires on your team — the people who ramped up fastest and fit in best. Rank these traits from most important to least important for thriving on your team:

- **Speed-to-Impact** — Gets things done quickly; ships and iterates rather than perfecting
- **Structured Thinker** — Plans carefully, tracks commitments, brings order to ambiguity
- **Candid Communicator** — Says what they think directly, even when it's uncomfortable
- **Independent Operator** — Takes ownership without much hand-holding; figures things out alone
- **Curious Learner** — Picks up new domains fast; comfortable being a beginner

> Format: Forced ranking — no ties allowed
> Signal: Each trait maps to 1-2 dimensions, making this a full-spectrum cross-validation
>   Speed-to-Impact → Pace + Execution (flexible end)
>   Structured Thinker → Execution (planned end) + Unc (clarity-seeking)
>   Candid Communicator → Expression (direct end)
>   Independent Operator → Collab (independent end) + Decision
>   Curious Learner → Growth (breadth end) + Unc (ambiguity-embracing)
> Cross-validates: All dimensions — each option is a "micro-profile" that implies a position on multiple spectrums
> This is the highest-signal question in the Company DNA battery

---

## 交叉验证逻辑总结

### 一致性检测示例：企业工作节奏维度 (Pace)

```
CQ01 (功能上线做法)    → 多数选 A (快速上线) → 快速迭代
CQ06 (成熟 vs 新方案)  → 多数选 B (快速验证) → 偏快但审慎
CQ13 (积压任务处理)    → 多数选 A (先 ship)   → 快速迭代
CQ17 (精力分配)        → 60% heads-down      → 高执行密度

分析：4 题全部偏向"快速迭代" → 高置信度 ✅

如果 CQ01→A (快速上线) 但 CQ13→C (先修基础架构再说)：
→ CQ01 说"快速上线"，CQ13 说"先打地基"——矛盾
→ 该维度置信度低 ⚠️
→ 可能是 HR 美化（CQ01）vs 员工实际感受（CQ13）差异
```

### 一致性检测示例：企业表达风格维度 (Expression)

```
CQ04 (初级员工反对资深)  → 多数选 A (直接提出) → 直接开放
CQ02 (周五发现问题)      → 多数选 B (频道发布) → 开放沟通
CQ08 (错过 deadline)     → 多数选 A (主动透明) → 直接开放
CQ16 (跨部门冲突)        → 多数选 A (私下协商) → 外交型

分析：3 题指向"直接开放"，1 题指向"外交型" → 合理变化 ✅
（对内直接，对外协商是正常的文化特征）

如果 CQ04→A 但 CQ08→C (悄悄调整) 且 CQ16→C (上报领导)：
→ CQ04 声称"直接表达"，但实际行为却回避沟通 → 可能是文化美化 ⚠️
```

### HR-员工偏差检测示例

```
HR 填写：
  CQ04 → A (鼓励直接表达)
  CQ08 → A (主动透明是期望)
  CQ14 → A (详细项目跟踪)

员工聚合：
  CQ04 → C (大多数人会私下说)
  CQ08 → C (deadline 经常悄悄调)
  CQ14 → C (靠 Slack 和 standup)

分析：
  Expression 维度 HR-员工偏差 = 35 分 → 超过 25 分阈值 ⚠️
  Execution 维度 HR-员工偏差 = 30 分 → 超过 25 分阈值 ⚠️
  → HREmployeeAlignment 显著偏低
  → 匹配报告将标注：
    "Note: Team members' views on communication openness differ from the
     company profile. Worth exploring during interviews."
```
