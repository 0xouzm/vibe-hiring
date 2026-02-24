# TalentDrop 第一层标准题库（30 题完整版）

> 设计方法论和维度模型详见 `question-bank-design.md`
> 本文档包含全部 30 道平台标准行为场景题，权重占总匹配的 60%

## 维度覆盖矩阵

```
维度                    | 主测题            | 交叉验证题        | 强排/预算题
------------------------|------------------|------------------|----------
工作节奏 (Pace)          | Q01, Q06         | Q12*, Q15*       | Q10
协作模式 (Collab)        | Q02, Q07         | Q16, Q23         | Q10
决策风格 (Decision)      | Q11, Q14         | Q01, Q17         | Q27
表达风格 (Expression)    | Q04, Q08         | Q17, Q18, Q30    | -
不确定性容忍 (Unc)       | Q03, Q06         | Q13, Q26         | -
成长路径 (Growth)        | Q22, Q25         | Q07, Q28         | Q24
驱动力来源 (Motiv)       | Q05, Q21         | Q09, Q29         | Q24
执行风格 (Execution)     | Q12*, Q19(新)    | Q15*, Q20(新)    | Q10
混合交叉                 | Q14, Q18         | Q23, Q24         | Q09, Q10, Q27

* Q12 和 Q15 同时服务于 Pace 和 Execution，为双归维题
```

---

## Q01 — Work Pace + Decision Style

You've picked up a new feature. The PM says "the sooner it ships, the better — let's see what users think." After assessing the work, you find the quick approach has obvious technical shortcomings but can ship in one week; the thorough approach takes three weeks but produces a cleaner architecture. You would:

- A. Ship the quick version, collect data, then decide whether to refactor
- B. Negotiate a middle ground with the PM: a workable version in two weeks
- C. Advocate for the thorough approach, using data to explain the long-term cost of tech debt
- D. Ship quick but simultaneously start a refactor plan so debt doesn't accumulate

> Measures: A/D = fast-iteration bias, C = depth-first bias, B = balanced negotiator
> Cross-validates: Q12, Q15

---

## Q02 — Collaboration Mode + Communication

Friday afternoon — you spot a production risk. It's not a critical bug, but if left alone it could cause issues next week. Most of the team has wrapped up for the day. You would:

- A. Fix it yourself in a couple of hours, then share what you did at Monday standup
- B. Post in the team channel explaining the issue, see if anyone wants to jump in
- C. Create a detailed ticket marked high-priority, tackle it first thing Monday
- D. Reach out directly to the colleague closest to that code, fix it together quickly

> Measures: A = independent action, B = open team collaboration, C = process-driven, D = targeted pairing
> Cross-validates: Q16, Q23

---

## Q03 — Uncertainty Tolerance

You've been assigned to a brand-new project. Your manager says "here's the rough direction — figure out how to get there." No spec, no reference implementation. Your first instinct is:

- A. Excitement — finally a chance to define something from zero
- B. Spend a few days researching comparable products and approaches before committing
- C. Go back to your manager and try to pin down requirements and boundaries
- D. Build a minimal prototype fast, then use it to drive a more concrete discussion

> Measures: A = high ambiguity embrace, D = action to resolve ambiguity, C = clarity-seeking, B = cautious research
> Cross-validates: Q13, Q26

---

## Q04 — Expression Style (primary)

During code review a senior colleague leaves extensive change requests on your PR. After careful reading, you believe most are stylistic preferences rather than genuine issues. You would:

- A. Reply point by point with your reasoning, linking docs or best practices to support your position
- B. Hop on a 15-minute call to talk through the key disagreements
- C. Accept most suggestions — they're more senior, and team harmony matters
- D. Accept the suggestions that have merit, and on pure style issues say "personal preference — keeping as-is"

> Measures: A = data-backed confrontation, B = direct + relationship-aware, C = conflict-avoidant / authority-deferring, D = principled boundary-setting
> Cross-validates: Q08, Q18, Q20

---

## Q05 — Motivation Source

Four offers are identical in pay, location, and title. The companies differ. Which do you lean toward?

- A. A company tackling climate change — technically challenging but the business model is still unproven
- B. A high-growth company that tripled revenue this year — equity could be very valuable
- C. A company with an exceptional engineering culture — several domain luminaries on the team
- D. A profitable, stable company with great work-life balance and predictable annual raises

> Measures: A = mission-driven, B = growth/reward-driven, C = craft/mastery-driven, D = stability/balance-driven
> Cross-validates: Q21, Q29

---

## Q06 — Work Pace + Uncertainty Tolerance

You're researching a technical approach and find two paths: Path A is battle-tested but mediocre performance; Path B comes from a recent paper with great theoretical results but zero production validation. The project deadline is three months away.

- A. Go with A — proven and low-risk, you'll hit the deadline comfortably
- B. Spend one week pressure-testing B; if it doesn't hold up, switch to A
- C. Go with B — three months is enough, and if it works it's a breakthrough
- D. Build on A as the main track, explore B on the side as a future optimization

> Measures: A = conservative, C = aggressive explorer, B = quick-validation thinker, D = pragmatic hedge

---

## Q07 — Collaboration Mode + Growth Path

A junior colleague keeps coming to you with similar questions in your area of expertise. You've already explained the same concept two or three times. You would:

- A. Write documentation or record a video so they can self-serve going forward
- B. Keep patiently answering — helping others deepens your own understanding too
- C. Point them toward a more systematic learning resource (course, book) to level up fundamentally
- D. Schedule a pair-programming session to walk through the problem-solving process end to end

> Measures: A = efficiency-first + system-builder, B = high empathy + collaborative, C = boundary-aware + growth-advisor, D = hands-on teaching + deep investment

---

## Q08 — Expression Style (primary)

During sprint planning, you believe a proposed technical approach has a serious flaw — but the proposal comes from the team lead. Eight people are in the room. You would:

- A. Raise your concern on the spot, backing it with clear reasoning
- B. Wait until after the meeting and bring it up privately with the lead
- C. Ask a gentle probing question in the meeting, seeing if the lead catches the issue themselves
- D. Stay quiet in the meeting, then send the lead a detailed written analysis afterward

> Measures: A = public directness, B = private diplomacy, C = socratic/high-EQ, D = deliberate written communicator
> Cross-validates: Q04, Q18, Q30

---

## Q09 — Motivation + Growth Path (Forced Ranking)

Rank these from most to least important to you:

- Becoming a recognized expert in a cutting-edge technical domain
- Leading an increasingly large team
- Working on a product that changes the world
- Earning exceptional financial compensation
- Having freedom and control over your time and energy

> Format: Forced ranking — no ties allowed
> Signal: Ranking pattern = career motivation fingerprint
> Cross-validates: Q05, Q21, Q24

---

## Q10 — Work Pace + Collaboration (Budget Allocation)

Distribute 100% of your ideal work energy:

- Solo execution (coding / design / analysis): ___%
- Team discussion, design review, pairing: ___%
- Cross-functional communication (PM, business): ___%
- Learning new tech or exploring new directions: ___%
- Documentation, knowledge management: ___%

> Format: Must total 100%. Reveals true time-allocation preference.
> Cross-validates: Q02, Q07, Q12

---

## Q11 — Decision Style

Your team is evaluating three vendors for a critical infrastructure migration. You have two weeks of trial data, industry benchmarks, and strong personal recommendations from trusted engineers at other companies. The quantitative data slightly favors Vendor A, but the engineers you respect are unanimously recommending Vendor B, saying "the numbers don't capture the developer experience." You would:

- A. Build a weighted scorecard from the data and benchmarks, present the quantitative ranking, flag anecdotal feedback as secondary
- B. Give significant weight to the engineers' lived experience — they've used these tools in production. Recommend Vendor B with their reasoning documented
- C. Design a one-week structured pilot where your own team uses both on a real task, generating first-party data that captures both metrics and experience
- D. Bring both data and recommendations to the team, facilitate discussion, let collective judgment drive the decision

> Measures: A = strong data-driven, B = high trust in expert intuition, C = empirical + experience-aware, D = consensus-seeking
> Cross-validates: Q01, Q14, Q27

---

## Q12 — Work Pace + Execution Style (dual-mapped)

You've just taken ownership of an internal tool used daily by ~40 people. There are 23 feature requests and 8 bug reports in the backlog. Your manager says you have full autonomy — no hard deadline, just "make it better." Your first two weeks look like:

- A. Pick the three most-requested quick fixes, ship them within days, use the momentum to learn what actually matters before planning bigger
- B. Interview power users and map workflows for a week, then create a prioritized roadmap that sequences changes toward a coherent improved experience
- C. Identify the single highest-impact architectural improvement that would make all future changes easier, and invest the full two weeks on that foundation
- D. Categorize everything by effort/impact, knock out all quick wins in week one, then reassess with a clearer picture of the codebase

> Measures: A = ship-to-learn, B = plan-then-execute, C = foundation-first depth, D = pragmatic velocity
> Cross-validates: Q01, Q15

---

## Q13 — Uncertainty Tolerance (cross-validation for Q03)

Your company is entering a new market. You're building a demo but nobody can specify which features prospects care about most. Two analyst reports disagree, and three prospect conversations each emphasized different pain points. You would:

- A. Pick the pain point that appeared in at least two conversations, build a focused demo around it, iterate based on real reactions
- B. Build a modular demo with three separate tracks so sales can adapt in real time depending on the audience
- C. Push back — schedule five more discovery calls before building anything. Building the wrong demo costs more than a two-week delay
- D. Design the demo around the problem framing the analysts agree on, trusting that analysts see market patterns individual buyers miss

> Measures: A = moderate tolerance — act on imperfect signal, B = high tolerance — hold multiple possibilities open, C = low tolerance — clarity before commitment, D = moderate — seeks structural certainty from authoritative sources
> Cross-validates: Q03, Q26

---

## Q14 — Decision Style + Uncertainty Tolerance

You're tech lead, six weeks into a project. Yesterday a competitor launched a product overlapping ~60% with yours. The CEO wants a same-day assessment: pivot, double down, or something else? You have gut instinct, team opinions, and could do rigorous analysis — but that would take three days. CEO needs your input by EOD.

- A. Share your honest instinct now — six weeks in this problem space makes your gut read informed, even without a spreadsheet. Speed matters
- B. Spend the day on rapid structured analysis — feature comparison, differentiation map, rough switching-cost estimates — present findings with explicit confidence levels
- C. Tell the CEO a same-day call on something this consequential will likely be wrong. Propose a 48-hour evaluation with a preliminary read clearly labeled as unreliable
- D. Convene a 90-minute team session to surface collective perspectives and blind spots, then present a team position rather than an individual one

> Measures: A = intuition-first under pressure, B = compressed analytics, C = quality over speed, D = distributed intelligence
> Cross-validates: Q11, Q03, Q13

---

## Q15 — Work Pace + Execution Style (dual-mapped, cross-validation)

Your team just finished a major release Friday. On Monday, your manager mentions optional interest in a technical retrospective at the company all-hands in two weeks. You would:

- A. Volunteer to put together a lightweight 10-minute retro yourself this week while details are fresh — good enough now beats polished later
- B. Propose the team spend one focused afternoon on a thorough internal retro, then distill it into a polished all-hands presentation the following week
- C. Suggest skipping the all-hands talk but running a quick async retro — everyone drops takeaways in a shared doc by Wednesday
- D. Advocate for a proper retrospective in the second week — gather cycle-time data, incident counts, and produce something genuinely reusable for other teams

> Measures: A = speed over polish, B = balanced quality, C = velocity-protective, D = depth-oriented
> Cross-validates: Q01, Q12

---

## Q16 — Collaboration Mode (cross-validation for Q02)

Your team just kicked off a high-priority project with a tight two-week deadline. Three separate modules can technically be developed in parallel. You're assigned one, but the overall architecture hasn't been clearly defined. You would:

- A. Start building your module based on your best interface assumptions, then align with others once you have something concrete
- B. Propose a half-day architecture session where all three module owners sketch interfaces together before anyone codes
- C. Draft the interface contracts yourself and share for async feedback — if no objections within a few hours, start building
- D. Pair up with the developer on the most tightly coupled module and design your two pieces together first, then loop in the third person

> Measures: A = build-first independence, B = team-first collaborative planning, C = initiative + structured async, D = selective pragmatic pairing
> Cross-validates: Q02, Q23

---

## Q17 — Expression Style (cross-validation for Q04) + Decision Style

You've been working on a feature for two weeks and just realized you'll likely miss the deadline by 3-4 days due to unforeseen technical complexity, not poor planning. There's still a week until the deadline. You would:

- A. Message your manager immediately: "Heads up — hitting complexity on X, likely 3-4 days late. Here's why and my adjusted plan."
- B. Finish working through the complexity first so you can present the problem alongside a concrete solution
- C. Bring it up casually at your next 1:1 or standup — not urgent enough for a special notification since there's still time
- D. Send a detailed written update to your manager and the broader team documenting the challenge, what you've tried, and the revised timeline

> Measures: A = fast, direct, minimal framing, B = solution-first communicator, C = low-ceremony/trusts organic channels, D = thorough + transparent
> Cross-validates: Q04, Q08

---

## Q18 — Expression Style (key cross-validation)

Your team has been debating two competing approaches for a system redesign for a week. The group is split 50/50 and the discussion is going in circles. You have a strong opinion. There's no designated decision-maker. You would:

- A. Write a structured comparison document with pros/cons and data, share it, and explicitly call for a final decision by end of week
- B. Suggest the team just pick one and commit — indecision costs more than picking the "slightly wrong" approach
- C. Talk privately with key people on the other side to understand their concerns, then propose a modified version of your approach that addresses them
- D. Propose a time-boxed spike: each side builds a small proof-of-concept in two days, then decide based on concrete results

> Measures: A = structured confrontation + written, B = action-biased resolution, C = diplomatic coalition-building, D = empirical conflict resolution
> Cross-validates: Q04, Q08 — tests whether conflict style is consistent in peer-level (no hierarchy) debates

---

## Q19 — Execution Style (primary)

You're leading a feature that involves coordinating work across three services. You've estimated it at six weeks. Your manager asks: "How will you track progress?"

- A. Set up a detailed project tracker with weekly milestones, dependency maps, and a risk register. Schedule brief daily syncs with contributors for the first two weeks
- B. Create a lightweight shared doc listing the three key milestones and their target dates. Check in with contributors as each milestone approaches
- C. Keep it informal — you know the people involved. Ping them in Slack when you need updates, and flag risks in your weekly 1:1 with your manager
- D. Define the end state and first milestone clearly. Re-plan the rest after milestone one lands, when you'll know more about actual complexity

> Measures: A = highly structured/high discipline, B = moderately structured/balanced, C = flexible/low structure, D = iterative planning/adaptive
> Design note: No time pressure (doesn't pollute Pace), no data-vs-intuition choice (doesn't pollute Decision), coordination is constant (doesn't pollute Collab), no interpersonal conflict (doesn't pollute Expression)
> Cross-validates: Q12, Q15, Q20

---

## Q20 — 执行风格 Execution Style（交叉验证）

你向 team lead 承诺了周四交付一个组件。周二晚上你发现低估了工作量——要在周四交付就必须牺牲测试覆盖和错误处理的质量。如果做到位，周一才能交付。你会：

- A. 立刻发消息给 lead："修正估期为周一。以下是我低估的部分和调整后的计划。" 周一交付高质量版本
- B. 全力冲刺周四——加班也行。承诺就是承诺，可靠性意味着说到做到
- C. 周四先交付已完成的部分，附上一份清晰的"已知缺口"清单，然后周一补齐剩余质量工作
- D. 先确认是否真的有人需要周四拿到，还是这个 deadline 本来就是软性的。如果有弹性，悄悄改到周一

> 测量：A = 高责任感/主动透明/质量优先，B = 承诺必达/可靠性驱动，C = 务实增量交付，D = 灵活务实/低仪式感
> 交叉验证逻辑：
>   · 与 Q12（接手工具怎么开始）形成规划维度的交叉检测
>   · 与 Q15（回顾总结深度）形成完善度维度的交叉检测
>   · 与 Q10（文档/知识管理预算分配）形成隐式一致性校验

---

## Q21 — Motivation Source (cross-validation for Q05)

You've been at your company for two years, performing well. A recruiter contacts you about a new role — same salary, same commute, equivalent title. Which single factor would most likely make you seriously consider leaving?

- A. The new company is working on a problem you find deeply meaningful — climate, healthcare, or education — and your work directly contributes to that mission
- B. The new role offers a clear, accelerated promotion path: formal senior-title review within 12 months with a compensation bump
- C. The team is led by someone widely regarded as one of the best mentors in your field — former reports credit her with transforming their careers
- D. The company gives every employee 20% discretionary time and a $10K annual budget to explore any project or skill, no questions asked

> Measures: A = purpose-driven, B = extrinsic reward/status, C = relational/developmental, D = autonomy/curiosity
> Cross-validates: Q05 (choosing vs. leaving — higher-stakes reveal), Q09

---

## Q22 — Growth Path (primary)

Your company gives you a full week of paid professional development. No strings — no expectation to report back or apply it immediately. How do you spend it?

- A. Intensive advanced workshop in your core skill area — move from "good" to "exceptional" in what you already do
- B. Something deliberately outside your domain — a UX sprint if you're a developer, a data science bootcamp if you're in marketing
- C. Shadow three different senior leaders — sit in their meetings, understand how they make decisions, see the organizational big picture
- D. Skip courses entirely. Identify a real unsolved problem at your company and spend the week building a working prototype

> Measures: A = specialist depth, B = cross-domain breadth, C = strategic/systemic, D = applied/pragmatic learning
> Cross-validates: Q25, Q28, Q09

---

## Q23 — Collaboration Mode (cross-validation, growth lens)

A colleague from another department invites you to co-lead a new internal initiative. The project is interesting but ambiguous — no playbook, and leadership will leave you two to figure it out. You both have roughly equal expertise. How do you structure the partnership?

- A. Divide into two distinct halves based on strengths. Each owns their section end-to-end, sync weekly. Clear boundaries, clear ownership
- B. Work on everything together — pair on key deliverables, joint meetings, shared documents. Slower but deeply collaborative output
- C. One of you takes the lead, the other supports. You're fine being either — what matters is a clear decision-maker
- D. Intensive co-working session at the start to align on vision, then split off independently for the bulk, reconvene for final integration

> Measures: A = independent-parallel, B = deep-integration, C = hierarchy-preference, D = hybrid-adaptive
> Cross-validates: Q02, Q16, Q10

---

## Q24 — Motivation + Growth Path combined (Forced Ranking)

Rank these role configurations from most to least appealing (1 = most, 4 = least):

- A. **Deep Impact Specialist** — Single high-stakes problem affecting thousands of users. Narrow scope, irreplaceable expertise. Success = tangible difference in people's lives
- B. **Rapid-Growth Generalist** — Rotate across three functions in two years. Each rotation is a stretch assignment. Success = speed of effectiveness in unfamiliar territory
- C. **Mastery-Track Expert** — Go deep with the best training, conferences, mentors. In two years, among the top practitioners in your specialty. Success = peer recognition and craft excellence
- D. **High-Leverage Operator** — Cross-functional, high-visibility, direct access to senior leadership. Broad, sometimes chaotic. Success = business outcomes and expanding scope

> Format: Forced ranking — reveals dominant motivation-growth combination
> Measures: A = mission + specialist, B = curiosity + generalist, C = mastery + depth, D = reward + breadth through influence
> Cross-validates: Q05, Q09, Q22, Q25

---

## Q25 — Growth Path (cross-validation, specialist vs. generalist)

You're five years in and have a strong reputation in your primary skill. A restructuring creates two new positions; you're the top candidate for either:

**Role X:** Go-to authority for your discipline company-wide. Set standards, review critical work, mentor specialists. Depth deepens, scope stays within your domain. In three years: industry-level expert.

**Role Y:** Hybrid role combining your skill with two adjacent areas you've never formally worked in. First year you'll often be the least experienced person in the room. In three years: a unique cross-functional perspective few possess.

- A. Role X, without hesitation — depth is rare, being the best at one thing is career-proof
- B. Role Y, without hesitation — breadth creates opportunities depth can't, being a beginner again is worth the long-term versatility
- C. Role X, but with some reluctance — you'd negotiate for occasional cross-functional projects to stay rounded
- D. Role Y, but with some reluctance — you'd negotiate to keep a small advisory role in your original domain

> Measures: A = strong specialist, B = strong generalist, C = specialist-leaning with breadth anxiety, D = generalist-leaning with depth anxiety
> Cross-validates: Q22, Q24, Q28

---

## Q26 — Uncertainty Tolerance (cross-validation)

Your company just acquired a startup. You're assigned to integrate their product, but leadership provides only a high-level vision — no roadmap, no success metrics, and the acquired team has conflicting ideas. Your first month:

- A. Start building based on your best interpretation, course-correct as you learn from real results
- B. Spend two weeks interviewing stakeholders on both sides, synthesize a unified direction document before coding
- C. Propose a small reversible pilot integration to test assumptions, use outcomes to negotiate a clearer mandate
- D. Escalate that the project needs defined scope and success criteria before meaningful work can begin

> Measures: A = high ambiguity tolerance, B = moderate (resolves via social info-gathering), C = moderate (resolves via experimentation), D = low (requires structural clarity)
> Cross-validates: Q03, Q13 — tests behavior when ambiguity is organizational rather than technical

---

## Q27 — Decision Style (Budget Allocation)

Allocate **100 points** across these inputs when making a major decision — reflect how you actually weigh each, not how you think you should:

- A. **Quantitative evidence** — metrics, A/B tests, benchmarks, market data: ___ pts
- B. **Pattern recognition** — past experience and gut sense of what works: ___ pts
- C. **Stakeholder consensus** — alignment among affected people: ___ pts
- D. **First-principles reasoning** — logical deduction from fundamental constraints: ___ pts

> Format: Must total 100. A flat 25/25/25/25 itself signals contextual flexibility.
> Measures: Heavy A = data rationalist, heavy B = experienced-intuition, heavy C = consensus-oriented, heavy D = analytical-independent
> Cross-validates: Q11, Q14 — exposes inconsistencies if scenario choices don't match abstract self-assessment

---

## Q28 — Growth Path (cross-validation)

You receive two internal transfer offers on the same day. Identical compensation, title, and team quality.

**Offer X:** Senior role on a team working in the exact tech stack you've spent 4 years mastering. You'd become the undisputed domain expert, mentor juniors, own the technical roadmap.

**Offer Y:** Senior role on a newly formed team exploring a domain you've never touched. You'd be the least experienced person, spend 6+ months ramping up, but gain entirely different exposure.

- A. Take X — depth creates irreplaceable value, there's always more to master even in a "known" domain
- B. Take Y — growth comes from discomfort, being a beginner again keeps you sharp and versatile
- C. Take X but negotiate 20% time to cross-train with the Y team on the side
- D. Take Y but only if you can bring one project from your current domain to maintain continuity

> Measures: A = specialist depth, B = generalist breadth, C = specialist-anchored hedge, D = generalist-anchored hedge
> Cross-validates: Q22, Q25 — removes career-advancement framing, isolates pure preference

---

## Q29 — Motivation Source (cross-validation)

Your team just shipped a major feature after a grueling 3-month push. Your manager asks each person to pick one reward. All genuinely offered, no judgment:

- A. A public shout-out from the VP at the all-hands, recognizing you by name for your specific contribution
- B. A $5,000 spot bonus deposited in your next paycheck, no ceremony
- C. Three extra PTO days to use however you want this quarter
- D. The right to choose what you work on next — full autonomy over your next project for one quarter

> Measures: A = recognition/visibility-driven, B = financial/extrinsic, C = well-being/balance, D = autonomy/intrinsic
> Cross-validates: Q05, Q21 — concrete reward selection exposes gaps between stated values and revealed preferences

---

## Q30 — Expression Style, cross-functional (cross-validation)

Marketing has promised a major client that a feature will be ready in 6 weeks. You're the engineering lead; your honest estimate is 10-12 weeks. A press release has already gone out. The sales VP is furious at the idea of walking it back. The client is a top-3 revenue account. You would:

- A. Meet privately with the marketing lead and sales VP together, lay out the technical reality, collaboratively renegotiate the timeline before anyone talks to the client
- B. Commit to the 6-week deadline but immediately cut scope — ship a minimal version on time, frame it as "Phase 1"
- C. Escalate to your shared executive (CTO/CEO), present the tradeoffs transparently, let leadership decide how to handle the external commitment
- D. Go directly to the client with the sales VP, honestly explain the revised timeline, and offer a concrete interim solution to maintain trust

> Measures: A = collaborative-diplomatic (private multi-party alignment), B = pragmatic-accommodating (absorbs conflict by reshaping deliverable), C = hierarchical-transparent (defers to authority), D = direct-external (bypasses internal politics for client trust)
> Cross-validates: Q04, Q08, Q18 — specifically tests conflict style across departmental boundaries with revenue-facing stakes

---

## 交叉验证逻辑总结

### 一致性检测示例：表达风格维度 (Expression)

```
Q04  (Code Review 分歧，对平级)        → 选 A (逐条回复理由) → 直接开放
Q08  (Sprint Planning 反对 Lead)       → 选 B (私下沟通)     → 策略含蓄
Q17  (进度延迟沟通)                     → 选 A (立刻通知)     → 直接开放
Q18  (团队 50/50 分歧，无层级)          → 选 A (写对比文档)   → 直接开放
Q30  (跨部门冲突，外部客户压力)          → 选 A (私下多方协商) → 策略协商

分析：
- Q04→A + Q08→B = 合理变化 (对平级直接，对上级含蓄) ✅
- Q04→A + Q17→A + Q18→A = 一致 ✅
- Q04→A + Q08→C + Q18→C = Q04 可能是伪装 ⚠️ 降低置信度
- Q04→A + Q30→D = 有趣信号 (内部谨慎，对外直接) — 标记为"外向直接型" ✅
```

### 一致性检测示例：执行风格维度 (Execution) — 新增

```
Q12 (接手内部工具)  → 选 B (先访谈再做路线图) → 结构化规划
Q19 (跟踪项目进度)  → 选 A (详细项目跟踪器)  → 高度结构化
Q15 (回顾总结)      → 选 D (收集数据做正式回顾) → 高完善度
Q20 (承诺交付)      → 选 A (主动修改估期+高质量) → 高责任感

分析：4 题全部指向"计划严谨" → 高置信度 ✅

如果 Q12→A (快速ship) 但 Q19→A (详细跟踪) 但 Q20→D (deadline灵活处理)：
→ Q12 说"先做再说"，Q19 说"详细规划"——矛盾
→ 该维度置信度低 ⚠️
→ 可能是随意作答或策略性伪装
```

### 一致性检测示例：成长路径维度 (Growth)

```
Q22 (自由发展周) → 选 A (深耕核心技能)
Q25 (选 Role X/Y) → 选 A (坚定选 X — 专精)
Q28 (内部转岗)    → 选 A (深度不可替代)
Q24 (强制排序)    → Mastery-Track Expert 排第一

分析：4 题全部指向"专精深耕" → 高置信度 ✅

如果 Q22→A 但 Q25→B 但 Q28→D:
→ 三道题结论矛盾 → 该维度置信度低 ⚠️
→ 可能是随意作答或刻意伪装
```

### 一致性检测示例：驱动力维度 (Motiv)

```
Q05 (选 Offer)   → 选 A (使命驱动公司)
Q21 (离职动机)    → 选 A (使命驱动)
Q29 (选奖励)      → 选 B ($5000 奖金)
Q09 (强制排序)    → "经济回报" 排第二

分析：
- Q05/Q21 声称使命驱动，但 Q29 面对真实奖励选了钱 → 有意思的信号
- 不一定是"作假" —— 可能是"使命驱动但务实" → 细化画像
- 但如果 Q09 也把经济回报排第一 → Q05/Q21 的使命选择可信度降低 ⚠️
```
