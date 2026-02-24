# TalentDrop Demo 数据集

> 用途：Demo 演示匹配算法的输入数据
> 包含：3 家虚构公司 Company DNA + 6 名虚构候选人 Career DNA + 匹配矩阵 + 3 份匹配报告样本

---

## 一、虚构公司 Company DNA 评分

### Company A: Velocity Labs

**简介**: 50 人快速增长的 B2B SaaS 初创公司，刚完成 Series B 融资。产品迭代极快，工程文化自由，远程优先。

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 82 | 快速迭代：周部署，先 ship 后完善 |
| Collab | 40 | 偏独立：小团队各自负责，异步沟通为主 |
| Decision | 55 | 中间：有数据就看数据，没数据就凭经验 |
| Expression | 78 | 偏直接：鼓励公开质疑，CEO 亲自做 Ask Me Anything |
| Unc | 75 | 高容忍：需求常变，拥抱模糊是常态 |
| Growth | 35 | 偏专精：深度技术专家被高度重视 |
| Motiv | 70 | 偏使命：团队因"改变行业"的愿景聚在一起 |
| Execution | 30 | 偏灵活：轻流程，适应性强，少文档 |

**CAS**: 81（Silver — 员工一致性较高，HR 略偏乐观）

**HR-员工偏差**: Expression 维度 HR 填 88 vs 员工聚合 78（HR 高估了直接程度 10 分）

---

### Company B: Meridian Financial Systems

**简介**: 2000 人上市金融科技公司。产品服务银行和保险公司，合规要求高。工程团队稳定，混合办公。

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 32 | 偏打磨：季度发布，充分测试后上线 |
| Collab | 68 | 偏协作：跨团队评审、设计委员会常态化 |
| Decision | 80 | 强数据驱动：决策必须有 metrics 支持 |
| Expression | 45 | 中间偏含蓄：尊重层级，重大分歧通常私下提 |
| Unc | 25 | 低容忍：明确 spec、完整 PRD 后才启动开发 |
| Growth | 55 | 中间：既需要深度专家也需要跨团队协调人 |
| Motiv | 40 | 中间偏回报：竞争力薪酬、稳定晋升是核心吸引力 |
| Execution | 82 | 强计划：详细项目跟踪、严格里程碑、合规文档 |

**CAS**: 88（Gold — 员工高度一致，HR-员工偏差小）

**HR-员工偏差**: 各维度偏差均 < 10 分

---

### Company C: Bloom Education

**简介**: 120 人教育科技公司，使命驱动。产品帮助K-12学校个性化教学。工程团队年轻、充满激情，办公室优先。

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 60 | 平衡：两周 sprint，但关键功能会多打磨一轮 |
| Collab | 75 | 强协作：Pair programming 常态化，团队决策 |
| Decision | 48 | 中间偏直觉：教育领域数据少，很多靠教育学直觉 |
| Expression | 72 | 偏直接：每周 retrospective 鼓励坦诚反馈 |
| Unc | 58 | 中等：接受一定模糊但喜欢大方向明确 |
| Growth | 70 | 偏广泛：鼓励跨职能、工程师参与产品和教研 |
| Motiv | 88 | 强使命：几乎所有人因"教育改变世界"留下 |
| Execution | 55 | 中间：有基本流程但不死板 |

**CAS**: 74（Silver — 员工总体一致，Execution 维度内部分歧较大）

**HR-员工偏差**: Execution 维度 HR 填 70 vs 员工聚合 55（HR 高估了流程化程度）

---

## 二、虚构候选人 Career DNA 评分

### Candidate 1: Alex Chen — Senior Frontend Engineer

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 78 | 快速迭代：喜欢先 ship 再优化 |
| Collab | 45 | 偏独立：享受 deep work，异步沟通优先 |
| Decision | 60 | 中间偏数据：喜欢 A/B 测试但也信任经验 |
| Expression | 75 | 直接：会在 PR 里逐条回复，公开表达观点 |
| Unc | 70 | 高容忍：喜欢从零到一的项目 |
| Growth | 30 | 强专精：想成为前端架构领域专家 |
| Motiv | 55 | 中间：技术挑战和使命都重要 |
| Execution | 35 | 偏灵活：轻量跟踪，反感过多流程 |

**一致性分数**: 0.91（高 — 交叉验证题目高度一致）

---

### Candidate 2: Maria Santos — Full-Stack Engineer

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 55 | 平衡：可以快也可以慢，取决于上下文 |
| Collab | 72 | 偏协作：喜欢 pair programming 和团队讨论 |
| Decision | 50 | 中间：会看数据但也重视团队共识 |
| Expression | 65 | 中等偏直接：有意见会说但方式温和 |
| Unc | 50 | 中间：喜欢有大方向但接受细节模糊 |
| Growth | 75 | 偏广泛：喜欢跨领域学习，从前端到后端到 DevOps |
| Motiv | 82 | 强使命驱动：曾在 NGO 工作，看重社会影响 |
| Execution | 60 | 中间偏计划：用看板但不会过度流程化 |

**一致性分数**: 0.87（较高）

---

### Candidate 3: James Wright — Backend Engineer

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 28 | 深度打磨：宁可慢也要架构做对 |
| Collab | 60 | 中间偏协作：喜欢设计评审和深度技术讨论 |
| Decision | 85 | 强数据驱动：一切基于 metrics 和基准测试 |
| Expression | 55 | 中间：有层级意识，公开场合措辞谨慎 |
| Unc | 20 | 低容忍：喜欢明确 spec、完整文档 |
| Growth | 25 | 强专精：分布式系统领域深耕 8 年 |
| Motiv | 35 | 偏回报：薪酬、稳定性和技术声誉 |
| Execution | 85 | 强计划：详细技术设计文档、严格代码评审 |

**一致性分数**: 0.94（非常高）

---

### Candidate 4: Priya Sharma — Product Engineer

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 68 | 中等偏快：喜欢两周 sprint 的节奏 |
| Collab | 80 | 强协作：喜欢跨职能合作，经常和产品/设计配对 |
| Decision | 42 | 中间偏直觉：教育背景让她信任定性研究 |
| Expression | 70 | 偏直接：retrospective 积极发言 |
| Unc | 62 | 中等偏高：喜欢探索但需要大方向 |
| Growth | 80 | 强广泛：从前端到用户研究到数据分析 |
| Motiv | 90 | 强使命驱动：以前在教育领域工作 |
| Execution | 50 | 中间：适应团队的流程风格 |

**一致性分数**: 0.89（较高）

---

### Candidate 5: David Kim — DevOps Engineer

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 50 | 平衡：基础设施需要稳健但也要自动化提速 |
| Collab | 35 | 偏独立：基础设施工作大部分是独立的 |
| Decision | 75 | 偏数据驱动：监控、SLA、性能指标驱动一切 |
| Expression | 40 | 偏含蓄：技术写作清晰但当面沟通低调 |
| Unc | 30 | 偏低容忍：基础设施需要可预测性 |
| Growth | 40 | 偏专精：深耕 Kubernetes 和云原生生态 |
| Motiv | 45 | 中间：技术挑战 + 合理薪酬 |
| Execution | 78 | 偏计划：自动化、监控、runbook、严格变更管理 |

**一致性分数**: 0.92（高）

---

### Candidate 6: Sophie Zhang — Junior Engineer

| 维度 | 评分 | 解读 |
|------|------|------|
| Pace | 72 | 偏快：年轻有冲劲，喜欢快速出成果 |
| Collab | 70 | 偏协作：喜欢有人带，乐于结对 |
| Decision | 45 | 中间偏直觉：经验不足以形成强数据驱动 |
| Expression | 50 | 中间：想发言但对资深同事会犹豫 |
| Unc | 65 | 中等偏高：对新事物好奇但需要指导 |
| Growth | 85 | 强广泛：什么都想学，对任何新领域都兴奋 |
| Motiv | 75 | 偏使命：选 offer 时会看公司做什么 |
| Execution | 45 | 中间偏灵活：还在形成自己的工作方法论 |

**一致性分数**: 0.78（中等 — 部分维度的交叉题答案有波动，可能还在探索阶段）

---

## 三、匹配矩阵

### L2 DNA 兼容性评分（简化版：单维度距离加权平均）

```
公式: Match(C, J) = 1 - Σ(|C_d - J_d| × w_d) / Σ(w_d × 100)
权重: 所有维度等权 w_d = 1（冷启动默认）
```

| 候选人 \ 公司 | Velocity Labs | Meridian Financial | Bloom Education |
|--------------|:------------:|:-----------------:|:--------------:|
| Alex Chen | **91%** | 52% | 72% |
| Maria Santos | 72% | 65% | **89%** |
| James Wright | 48% | **92%** | 55% |
| Priya Sharma | 74% | 58% | **93%** |
| David Kim | 56% | **83%** | 60% |
| Sophie Zhang | 76% | 54% | **81%** |

> 粗体 = 最佳匹配

### 匹配结果摘要

**Velocity Labs** 最佳匹配：
1. Alex Chen (91%) — 快节奏 + 独立 + 灵活执行 完美契合
2. Sophie Zhang (76%) — 节奏匹配但经验不足

**Meridian Financial** 最佳匹配：
1. James Wright (92%) — 数据驱动 + 计划严谨 + 深度专精 完美契合
2. David Kim (83%) — 稳健 + 结构化 + 低不确定性容忍

**Bloom Education** 最佳匹配：
1. Priya Sharma (93%) — 使命驱动 + 协作 + 跨领域 完美契合
2. Maria Santos (89%) — 使命驱动 + 协作 + 广泛学习
3. Sophie Zhang (81%) — 好奇心强 + 协作 + 使命认同

---

## 四、匹配报告样本

### 样本 1: Alex Chen × Velocity Labs — 91%

```
┌──────────────────────────────────────────────────┐
│  Match Report: Alex Chen × Velocity Labs          │
│  Overall Match: 91%                               │
│  ████████████████████░░                           │
├──────────────────────────────────────────────────┤
│                                                    │
│  ── Why You're a Great Fit ──                      │
│                                                    │
│  1. Work Pace Alignment (96%)                      │
│     You both thrive in fast-iteration              │
│     environments. Velocity ships weekly —           │
│     matching your "ship first, polish later"        │
│     instinct.                                      │
│                                                    │
│  2. Independence & Autonomy (95%)                  │
│     You prefer deep work and async comms.           │
│     Velocity's small-team, remote-first            │
│     structure gives you exactly that.              │
│                                                    │
│  3. Expression Style Match (97%)                   │
│     You're direct in code reviews and meetings.     │
│     Velocity's culture actively encourages          │
│     open challenge — even to the CEO.              │
│                                                    │
│  ── Something to Explore ──                        │
│                                                    │
│  Your strong preference for specialization          │
│  (Growth: 30) is a great fit for their deep-       │
│  expertise culture (35). However, as a 50-          │
│  person startup, you may occasionally need to       │
│  wear multiple hats. Worth discussing how they      │
│  protect focus time for specialists.               │
│                                                    │
│  ── Confidence Note ──                             │
│  Your DNA consistency: 0.91 (High)                 │
│  Company culture verification: Silver (CAS 81)     │
│  Note: Team members' views on communication         │
│  openness are slightly more reserved than the       │
│  company profile suggests.                         │
│                                                    │
└──────────────────────────────────────────────────┘
```

### 样本 2: James Wright × Meridian Financial — 92%

```
┌──────────────────────────────────────────────────┐
│  Match Report: James Wright × Meridian Financial   │
│  Overall Match: 92%                               │
│  █████████████████████░                           │
├──────────────────────────────────────────────────┤
│                                                    │
│  ── Why You're a Great Fit ──                      │
│                                                    │
│  1. Execution Style Alignment (97%)                │
│     You thrive with structured planning,            │
│     detailed design docs, and rigorous review.      │
│     Meridian's compliance-driven engineering        │
│     culture is built exactly this way.             │
│                                                    │
│  2. Decision Making Match (95%)                    │
│     You're strongly data-driven. Meridian           │
│     requires metrics-backed decisions — your        │
│     natural instinct is their requirement.         │
│                                                    │
│  3. Uncertainty Tolerance (95%)                    │
│     You prefer clear specs and thorough docs.       │
│     Meridian's PRD-first development process        │
│     means you'll rarely face ambiguity.            │
│                                                    │
│  ── Something to Explore ──                        │
│                                                    │
│  Your work pace (28) is even more deliberate        │
│  than Meridian's already careful pace (32).         │
│  This is a strong alignment, but ensure the         │
│  quarterly release cycle gives you enough time      │
│  for the depth you value, rather than feeling       │
│  rushed by multiple parallel compliance tracks.     │
│                                                    │
│  ── Confidence Note ──                             │
│  Your DNA consistency: 0.94 (Very High)            │
│  Company culture verification: Gold (CAS 88)       │
│  High confidence in this match.                    │
│                                                    │
└──────────────────────────────────────────────────┘
```

### 样本 3: Priya Sharma × Bloom Education — 93%

```
┌──────────────────────────────────────────────────┐
│  Match Report: Priya Sharma × Bloom Education      │
│  Overall Match: 93%                               │
│  █████████████████████░                           │
├──────────────────────────────────────────────────┤
│                                                    │
│  ── Why You're a Great Fit ──                      │
│                                                    │
│  1. Mission Alignment (98%)                        │
│     You're deeply mission-driven (90) and have      │
│     previous education sector experience.           │
│     Bloom's team stays because they believe in      │
│     transforming K-12 education (88).              │
│                                                    │
│  2. Collaboration Style (95%)                      │
│     You love cross-functional pairing (80).         │
│     Bloom pair-programs daily and makes             │
│     decisions as a team (75). You'll feel           │
│     right at home.                                 │
│                                                    │
│  3. Growth Path Match (90%)                        │
│     You want to explore across domains (80).        │
│     Bloom actively encourages engineers to           │
│     participate in product and pedagogy              │
│     research (70). Your curiosity is their asset.   │
│                                                    │
│  ── Something to Explore ──                        │
│                                                    │
│  Bloom's execution style scored 55 (moderate),      │
│  but there's internal disagreement — HR says 70     │
│  while employees say 55. This suggests processes    │
│  may be aspirational rather than established.       │
│  Ask about how the team actually tracks work        │
│  and handles missed deadlines.                     │
│                                                    │
│  ── Confidence Note ──                             │
│  Your DNA consistency: 0.89 (High)                 │
│  Company culture verification: Silver (CAS 74)     │
│  Note: Execution style has higher internal          │
│  variance — explore in interviews.                 │
│                                                    │
└──────────────────────────────────────────────────┘
```

---

## 五、弱匹配样本（用于对比演示）

### Alex Chen × Meridian Financial — 52%

```
┌──────────────────────────────────────────────────┐
│  Match Report: Alex Chen × Meridian Financial      │
│  Overall Match: 52%                               │
│  ███████████░░░░░░░░░░░                           │
├──────────────────────────────────────────────────┤
│                                                    │
│  ── Potential Friction Points ──                   │
│                                                    │
│  1. Work Pace Mismatch (50 pt gap)                 │
│     You ship weekly; they release quarterly.        │
│     Your fast-iteration instinct may feel           │
│     constrained by their deliberate cadence.       │
│                                                    │
│  2. Execution Style Clash (47 pt gap)              │
│     You prefer lightweight tracking and             │
│     flexibility. Meridian requires detailed         │
│     project plans, compliance docs, and             │
│     formal change management.                      │
│                                                    │
│  3. Uncertainty Tolerance Gap (45 pt gap)           │
│     You thrive in ambiguity; they eliminate it.     │
│     Their spec-first process may feel like          │
│     unnecessary overhead to you.                   │
│                                                    │
│  ── Where You Do Align ──                          │
│                                                    │
│  Decision making (15 pt gap) is your closest        │
│  match — you both respect data, though Meridian     │
│  takes it further than you might prefer.           │
│                                                    │
└──────────────────────────────────────────────────┘
```

---

## 六、维度评分速查表

```
         Pace  Collab  Decision  Expression  Unc  Growth  Motiv  Execution
VeloLabs   82     40       55         78     75      35     70       30
Meridian   32     68       80         45     25      55     40       82
Bloom      60     75       48         72     58      70     88       55

Alex       78     45       60         75     70      30     55       35
Maria      55     72       50         65     50      75     82       60
James      28     60       85         55     20      25     35       85
Priya      68     80       42         70     62      80     90       50
David      50     35       75         40     30      40     45       78
Sophie     72     70       45         50     65      85     75       45
```
