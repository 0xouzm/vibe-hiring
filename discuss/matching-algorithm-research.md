# 人才匹配算法调研报告

> 调研日期：2026-02-24
> 调研目的：为 TalentDrop 的核心匹配算法设计提供技术参考

---

## 一、招聘领域的 AI 匹配产品

### 1.1 Eightfold AI — Talent Intelligence Platform

**核心架构：深度语义嵌入 + 技能图谱**

Eightfold 构建了目前业界最大的人才数据集（16 亿+ 职业画像、160 万+ 技能），其匹配系统的技术核心如下：

**（1）Token 级嵌入模型**
- 将技能（skills）、职位（titles）、公司（companies）、学位（degrees）、学校（schools）分别嵌入到 N 维向量空间
- 嵌入模型基于数亿条内部画像和职位文本 token 训练，并持续刷新
- 每个技能短语（如 "React"、"Kubernetes"、"Financial Modeling"）映射为一个 N 维向量
- 语义相近的技能在向量空间中距离更近：例如 "Pandas" 距 "Python" 比距 "Panda" 更近

**（2）相似度计算**
- 使用 **余弦相似度（Cosine Similarity）** 计算职位技能向量与候选人技能向量的匹配度
- 同时计算候选人**最近经历**的技能向量相似度，优先考虑近期技能使用情况

**（3）多维特征工程**
- 嵌入只是基础，还额外提取结构化字段中的丰富特征
- 为每个参与方（候选人、相似候选人、招聘经理）生成技能、职位、过往公司、经历的密集嵌入
- 然后在候选人画像与参考画像（理想候选人和招聘经理）之间计算多属性相似度

**（4）整体评分（Holistic Scoring）**
- 嵌入之外，还融入客观标量信号（如经历年限、职位层级等）
- 最终 Match Score 是一个综合信号，用于预测入职后的留存率和晋升率
- Eightfold 通过生存分析（Survival Analysis）验证了 Match Score 与实际职场结果的相关性

**（5）公平性约束**
- 使用 "Equal Opportunity Algorithms"，确保预测不因个人或人口统计特征产生偏见
- 多语言匹配支持全球化人才获取

**关键技术特征总结：**
```
候选人画像 → Token Embedding → N维向量
职位需求 → Token Embedding → N维向量
匹配分数 = f(cosine_similarity(技能向量), 结构化特征, 标量信号)
```

> 参考来源：[Eightfold 工程博客 - AI-powered talent matching](https://eightfold.ai/engineering-blog/ai-powered-talent-matching-the-tech-behind-smarter-and-fairer-hiring/)、[Eightfold Match Score 验证](https://eightfold.ai/engineering-blog/retaining-and-growing-talent-through-skills-based-hiring-insights-from-eightfold-ais-match-score/)

---

### 1.2 Pymetrics（现 Harver）— 神经科学游戏化评估

**核心架构：行为经济学实验范式 + 集成学习匹配**

Pymetrics 由哈佛和 MIT 的神经科学家创立，其技术路线与 Eightfold 的 NLP/嵌入路线截然不同——基于认知神经科学实验范式直接测量行为特征。

**（1）12 个神经科学迷你游戏**

每个游戏对应经典的实验心理学范式：

| 游戏 | 对应范式 | 测量维度 |
|------|----------|----------|
| Balloon Game | BART（气球模拟风险任务，Lejuez et al., 2002） | 风险容忍度、决策风格 |
| Money Exchange | 经典独裁者博弈 / 最后通牒博弈 | 公平感、慷慨度 |
| Keypress Game | Go/No-Go 任务 | 注意力控制、冲动性 |
| Card Game | Iowa Gambling Task（爱荷华赌博任务） | 学习能力、风险收益权衡 |
| Digits Memory | N-back 工作记忆任务 | 工作记忆容量 |
| Arrows Game | Flanker 任务 / Stroop 任务变体 | 注意力集中、干扰抑制 |
| Faces Game | 微表情识别任务 | 情绪智力、社会认知 |
| Towers Game | 伦敦塔/河内塔问题 | 规划能力、问题解决 |
| ... | ... | ... |

**（2）91 个特征、9 大类别**
- 注意力（Attention）、决策（Decision Making）、努力（Effort）、情绪（Emotion）、公平（Fairness）、专注（Focus）、风险容忍（Risk Tolerance）、慷慨度（Generosity）、学习（Learning）
- 每个特征是**连续谱**，没有"对错"之分
- 测试是**计算机自适应**的——根据行为实时调整游戏条件

**（3）匹配算法**
- 采用**集成学习（Ensemble Learning）**架构，组合多种建模方法
- 训练数据来源：目标岗位的高绩效员工完成同样游戏后的行为画像
- 将候选人的特征画像与高绩效员工画像进行匹配
- 不使用任何人口统计信息进行预测

**（4）公平性保障 — Audit-AI 开源工具**
- Pymetrics 开源了 [audit-ai](https://github.com/pymetrics/audit-ai) 偏见检测工具
- 核心方法：统计显著性检验（p < 0.05）+ 4/5 规则（最低通过组的通过率 >= 最高通过组的 4/5）
- 去偏流程：从 15 万+ 自愿提供人口统计信息的样本中建立"去偏集"
- 任何导致受保护群体差异的因素都会被从模型中移除

**关键数学思路：**
```
候选人游戏行为 → 提取 91 维特征向量 P_candidate
高绩效员工基准 → 聚合 91 维特征向量 P_benchmark
匹配度 = EnsembleModel(P_candidate, P_benchmark)
约束条件：∀ 受保护群体 g, PassRate(g) >= 0.8 × max(PassRate)
```

> 参考来源：[Pymetrics 技术分析](https://digidai.github.io/2025/07/26/pymetrics-comprehensive-analysis/)、[audit-ai GitHub](https://github.com/pymetrics/audit-ai)、[Harvard 案例](https://d3.harvard.edu/platform-digit/submission/pymetrics-using-neuroscience-ai-to-change-the-age-old-hiring-process/)

---

### 1.3 HireVue — AI 视频面试评估

**核心架构：NLP（RoBERTa）+ 静态确定性评估模型**

**（1）数据处理管线**
- 语音转文字：使用 Rev.ai 进行高精度语音转录（支持多口音）
- NLP 模型：基于 **RoBERTa** 的语言模型，经过微调用于面试文本分析
- 每段视频面试提取最多 **25,000 个数据点**

**（2）模型构建生命周期**
```
岗位分析 → 确定胜任力模型 → 设计面试问题
    ↓
数据收集 → 现有员工或候选人完成评估 + 绩效基准
    ↓
模型训练 → 预测绩效指标的机器学习模型
    ↓
部署 → 静态 & 确定性模型（锁定后不在线学习）
    ↓
持续监控 → 定期检查预测准确性和偏见
```

**（3）关键技术决策**
- **静态部署**：模型训练完成后锁定，不在生产环境中继续学习——确保可复现性
- **确定性输出**：同一输入永远产生相同输出
- **2020 年移除面部分析**：因争议移除了面部表情分析功能，现仅基于语言内容
- 偏见缓解：同时优化预测准确性并惩罚人口统计群体差异（类似多目标优化）

**（4）偏见缓解的数学框架**
```
Loss = L_prediction(y, ŷ) + λ × L_fairness(demographic_groups)
其中：
- L_prediction: 预测岗位胜任力的准确性损失
- L_fairness: 不同人口统计群体通过率差异的惩罚项
- λ: 公平性权重超参数
```

> 参考来源：[HireVue AI 系统报告](https://www.paradigmpress.org/ist/article/download/1204/1065/1376)、[HireVue 模型训练流程](https://www.hirevue.com/blog/hiring/train-validate-re-train-how-we-build-hirevue-assessments-models)、[CDT 分析](https://cdt.org/insights/hirevue-ai-explainability-statement-mostly-fails-to-explain-what-it-does/)

---

### 1.4 Plum.io — 工业心理学评估匹配

**核心架构：Big Five 人格模型 + I/O 心理学算法**

**（1）评估内容（25 分钟在线评估）**
- 第 1 & 3 节：人格评估（强制选择法 — 选择"最像我"和"最不像我"的描述）
- 第 2 & 4 节：问题解决能力（图形推理 — 矩阵推理题）
- 第 5 节：社会智力（职场情境判断）

**（2）10 项 Plum Talents**
- 基于 **Big Five 人格模型** 定义
- 每项 Talent 由多个底层特质（traits）通过 I/O 心理学家开发的算法组合而成
- Talent = f(personality_traits, cognitive_ability, social_intelligence)

**（3）岗位需求定义**
- 3-8 位岗位专家完成 8 分钟调查，选择"对成功最重要"和"最不重要"的行为
- 聚合结果，识别出**排名最高的 5 项 Talents** 作为岗位匹配标准

**（4）匹配评分**
- Match Score（30-99）= 候选人在 5 项岗位关键 Talent 上的综合表现
- 声称比简历筛选的预测准确性高 4 倍

**关键模型简化表示：**
```
岗位需求：T_job = {t1, t2, t3, t4, t5}  （5项最重要Talent）
候选人画像：T_candidate = {t1_score, t2_score, ..., t10_score}
Match Score = Σ(weight_i × T_candidate[t_i]) for t_i in T_job
范围：30-99
```

> 参考来源：[Plum 科学基础](https://www.plum.io/plum-science)、[Plum Discovery Survey](https://help.plum.io/hc/en-us/articles/360002490414-What-does-the-Discovery-Survey-measure)

---

## 二、约会/社交领域的深度匹配算法

### 2.1 Hinge — "Most Compatible"（Gale-Shapley 稳定匹配）

**核心算法：机器学习 + Gale-Shapley 延迟接受算法**

**（1）经典 Gale-Shapley 算法原理**

Gale 和 Shapley 于 1962 年发表，Shapley 因此获得 2012 年诺贝尔经济学奖。

```
算法：延迟接受（Deferred Acceptance）
输入：两组参与者，每人对对方组有一个偏好排序
输出：稳定匹配

while 存在未匹配的提议方:
    每个未匹配的提议方 → 向其最偏好的（尚未被拒绝的）对象提议
    每个接收方 → 从所有提议中选择最偏好的，回复"暂时接受"
                    对其余所有提议者回复"拒绝"

时间复杂度：O(n²)
关键性质：产生的匹配一定是"稳定"的
    — 不存在一对 (A, B) 使得 A 和 B 互相偏好对方胜过各自当前匹配
```

**（2）Hinge 的关键改造**

| 原始算法 | Hinge 改造 |
|----------|-----------|
| 显式偏好排序 | 机器学习从历史行为推断偏好 |
| 二元性别分组 | 取消性别分组，采用"稳定室友问题"变体 |
| 全量匹配 | Dealbreaker 硬性过滤预处理 |
| 一次性匹配 | 迭代式，每天推荐一个"Most Compatible" |

**（3）偏好推断的机器学习模型**
- 分析用户在平台上的历史行为（点赞、跳过、互动类型等）
- 预测用户最可能互动的画像
- 用推断出的偏好数据驱动 Gale-Shapley 迭代

**（4）效果**
- 早期测试中，Most Compatible 推荐的约会成功率（交换电话号码）是其他推荐的 **8 倍**

**（5）算法的内在权衡**
- Gale-Shapley 的提议方获得最优匹配，接收方获得最差稳定匹配
- Hinge 通过取消性别分组和随机化提议方来缓解这一不对等

> 参考来源：[Cornell 网络课程博客](https://blogs.cornell.edu/info2040/2021/09/30/hinge-and-its-implementation-of-the-gale-shapley-algorithm/)、[TechCrunch 报道](https://techcrunch.com/2018/07/11/hinge-employs-new-algorithm-to-find-your-most-compatible-match-for-you/)、[Gale-Shapley 维基百科](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm)

---

### 2.2 Coffee Meets Bagel — 深度神经网络 + 协同过滤

**核心架构：深度神经网络 + 基于物品的协同过滤 + 100 维隐因子**

**（1）双模管线**

```
┌─────────────────────────────────────────────────────────┐
│                    离线批处理组件                         │
│  Apache Spark + NumPy + Pandas + S3/Parquet             │
│  → 训练推荐模型、提取特征                                 │
│  → 每个用户生成 100 个隐因子（float）                     │
│  → 训练耗时 6-7 小时/天                                  │
│  → 结果以 JSON 格式存入 ElastiCache (Redis)              │
├─────────────────────────────────────────────────────────┤
│                    在线服务组件                           │
│  Django + Redis                                         │
│  → 对每对候选匹配进行实时评分                              │
│  → 维护每用户的推荐队列（Redis Sorted Sets）               │
│  → Web 应用从推荐数据存储中读取并服务推荐                    │
└─────────────────────────────────────────────────────────┘
```

**（2）隐因子（Latent Features）**
- 每用户计算 **100 个隐因子**，以浮点数表示
- 通过分析数百天的匹配历史学习得来
- 使用**基于物品的协同过滤**预测用户群体之间的相似性
- 隐因子比人工定义的元数据特征更具预测力

**（3）多层过滤**
- 用户设定的偏好作为 "must-haves" 硬性过滤
- 算法额外使用兴趣、社交圈、教育程度等信息
- 性别差异化推荐（基于行为数据：男性平均想要 17 个/天，女性想要 4 个高质量/天）

**（4）持续学习**
- 算法根据用户的点赞/跳过行为不断更新对用户偏好的理解
- 自适应调整，不是静态模型

> 参考来源：[AWS re:Invent 2017 演讲](https://www.slideshare.net/AmazonWebServices/dating-and-data-science-how-coffee-meets-bagel-uses-amazon-elasticache-to-deliver-highquality-match-recommendations-dat323-reinvent-2017)、[AWS 博客](https://aws.amazon.com/blogs/database/powering-recommendation-models-using-amazon-elasticache-for-redis-at-coffee-meets-bagel/)、[CMB Medium](https://coffeemeetsbagel.medium.com/the-science-behind-setting-your-preferences-liking-bagels-b0b84551e421)

---

### 2.3 OkCupid — 加权兼容性评分系统

**核心算法：加权问答 + 几何平均数**

OkCupid 的算法是所有调研对象中**公式最透明**的，其完整数学模型如下：

**（1）三维问答数据收集**
每个问题收集三个值：
- 你的回答 A_self
- 你希望对方怎么回答 A_desired
- 这个问题对你有多重要 W（权重）

**（2）权重体系**
```
Irrelevant     = 0
A little       = 1
Somewhat       = 10
Very important = 50
Mandatory      = 250
```

注意：权重呈指数级增长（大约 0, 1, 10, 50, 250），这意味着一个 "Mandatory" 问题的权重等于 250 个 "A little" 问题。

**（3）满意度计算**

对于用户 A 和用户 B 之间共同回答的 n 个问题：

```
Score_A→B = Σ(W_A_i × match_i) / Σ(W_A_i)
其中：match_i = 1 如果 B 的回答在 A 的可接受范围内，否则 = 0
W_A_i = A 对第 i 个问题赋予的重要性权重

Score_B→A = Σ(W_B_i × match_i) / Σ(W_B_i)
其中：match_i = 1 如果 A 的回答在 B 的可接受范围内，否则 = 0
```

**（4）几何平均数合成**

```
Match% = √(Score_A→B × Score_B→A)
```

**为什么用几何平均而非算术平均？**
- 算术平均：(0% + 100%) / 2 = 50% — 即使一方完全不满意
- 几何平均：√(0% × 100%) = 0% — 正确反映了"吸引力必须是双向的"
- 几何平均能更好地处理值域宽泛、代表不同属性的数值组合

**（5）误差修正**
- 当共同问题数量少时，加入保守的误差修正
- 始终显示可能的最低匹配百分比
- 例如：如果只有 2 个共同问题，误差率为 50%

**（6）完整公式**
```
令 S_A = A 对 B 的满意度, S_B = B 对 A 的满意度
令 n = 共同回答的问题数
Match% = √(S_A × S_B) × (1 - margin_of_error(n))
```

> 参考来源：[AMS 数学博客](https://blogs.ams.org/mathgradblog/2016/06/08/okcupid-math-online-dating/)、[HackerEarth 技术解析](https://www.hackerearth.com/practice/notes/okcupids-matching-algorithm-1/)、[OkCupid 官方指南](https://okcupid-app.zendesk.com/hc/en-us/articles/22982200783771)、[GitHub 算法实现](https://github.com/adi3/okcupid_matching)

---

## 三、心理测量学在匹配中的应用

### 3.1 Big Five / OCEAN 人格模型

**五大人格维度：**
| 维度 | 英文 | 含义 | 与工作绩效的关系 |
|------|------|------|-----------------|
| 开放性 | Openness | 创造力、好奇心 | 创新型岗位的正向预测因子 |
| 尽责性 | Conscientiousness | 自律、勤勉 | **几乎所有岗位的最强预测因子** |
| 外向性 | Extraversion | 社交性、果断性 | 销售/管理岗位的正向预测因子 |
| 宜人性 | Agreeableness | 善良、合作性 | 团队合作的正向预测因子 |
| 神经质 | Neuroticism | 情绪不稳定性 | 工作满意度的负向预测因子 |

**在匹配算法中的应用方式：**

**(a) 距离/相似度法**
```python
# 欧几里得距离
distance = √(Σ(P_candidate_i - P_ideal_i)²)  for i in [O, C, E, A, N]

# 余弦相似度
similarity = (P_candidate · P_ideal) / (||P_candidate|| × ||P_ideal||)

# 皮尔逊相关系数
correlation = cov(P_candidate, P_ideal) / (σ_candidate × σ_ideal)
```

**(b) 机器学习法（2023-2025 最新研究）**
- Francis, Back & Matz (2024, Frontiers in Social Psychology)：使用 ML 模型从简历和短文本中预测 Big Five 人格特质
- 多种模型对比：Naive Bayes、LR、SVM、Random Forest、XGBoost、CNN、CNN-LSTM、Bi-LSTM、GRU
- 深度学习方法普遍优于基于距离的简单方法

---

### 3.2 Person-Organization Fit（P-O Fit）理论

**（1）两种契合类型**

| 类型 | 英文 | 核心逻辑 |
|------|------|----------|
| 补充型契合 | Supplementary Fit | 人的特征与组织特征相似（价值观一致、人格相似） |
| 互补型契合 | Complementary Fit | 人的特征弥补了组织所缺少的（需求-供给匹配） |

**（2）Edwards 多项式回归模型（1993）— 学术界测量 P-E Fit 的标准方法**

传统的差值法（|P - E|）被证明存在严重的统计问题，Edwards 提出用多项式回归替代：

```
Z = b₀ + b₁P + b₂E + b₃PE + b₄P² + b₅E² + ε

其中：
Z = 结果变量（如工作满意度、留任意愿）
P = 个人变量（如个人价值观分数）
E = 环境变量（如组织价值观分数）
PE = 人-环境交互项
P², E² = 二次项（捕捉曲线关系）
```

**响应面分析（Response Surface Analysis）的关键参数：**
```
沿 P=E 线（一致性线）：
  斜率 = b₁ + b₂        （契合度增加时，结果如何变化）
  曲率 = b₃ + b₄ + b₅   （是否存在最优契合点）

沿 P=-E 线（不一致线）：
  斜率 = b₁ - b₂        （不契合的方向是否重要）
  曲率 = b₃ - b₄ + b₅   （不契合的程度效应）
```

当曲率为负且显著时，响应面呈倒 U 形 → 说明存在最优契合点。

**核心学术文献：**
- Kristof (1996): P-O Fit 的整合综述（Personnel Psychology）
- Edwards & Parry (1993): 多项式回归替代差值法（Academy of Management Journal）
- Schneider (1987): "The people make the place" — ASA 框架
- Kristof-Brown, Schneider & Su (2023): P-O Fit 理论最新回顾（Personnel Psychology）

---

### 3.3 协同过滤 vs 基于内容的匹配在人才领域的适用性

**（1）三种匹配范式对比**

| 维度 | 基于内容的过滤（CBF） | 协同过滤（CF） | 混合方法 |
|------|---------------------|---------------|---------|
| **核心思路** | 比较候选人属性与职位需求的相似度 | 找到"相似候选人"看他们匹配了什么 | 两者结合 |
| **数学方法** | TF-IDF + 余弦相似度、BERT 嵌入 | 矩阵分解、隐因子模型 | SRL、混合损失函数 |
| **优势** | 可解释性强、无冷启动（对新职位） | 能发现非显式特征的匹配模式 | 互补优势 |
| **劣势** | 过度依赖显式特征、不能发现隐式模式 | 冷启动问题严重、数据稀疏 | 复杂度高 |
| **人才领域特殊挑战** | 简历/JD 文本质量参差不齐 | 一个人入职后很久才换工作→数据极稀疏 | 需要大量标注数据 |

**（2）学术界的关键发现**

**混合方法显著优于单一方法**（来自 Springer 2025 年系统文献综述）：

Diaby et al. (2017, ScienceDirect) 提出了一种混合模型：
```
目标关系：Match(User, Job)
方法：关系函数梯度提升（Relational Functional Gradient Boosting, RFGB）

CBF 分支：分析用户画像与职位描述的内容相似度
CF 分支：分析相似用户的申请历史
SRL 整合：通过统计关系学习（SRL）直接表示相关对象之间的概率依赖关系
```

**冷启动问题在人才领域尤为严重：**
- 一个人获得职位后不太可能很快获得新职位 → 传统协同过滤数据极为有限
- 解决方案：融入内容特征、利用嵌入迁移、引入外部知识图谱

**（3）最新深度学习方法（2021-2025）**

| 方法 | 技术 | 来源 |
|------|------|------|
| KG-DPJF | BERT + 知识图谱 + 多层注意力 | Wang et al. 2021, Complexity |
| ConFit v2 | Siamese BERT + 假设简历嵌入 | arXiv 2502.12361, 2025 |
| GNN 匹配 | 图神经网络二部图 | Springer 2025 |
| Two-Tower | 双塔模型 + 余弦相似度 | 业界主流架构 |
| Smart-Hiring | all-MiniLM-L6-v2 + 余弦相似度 | arXiv 2511.02537, 2025 |

> 参考来源：[Springer 系统文献综述](https://link.springer.com/article/10.1186/s40537-025-01173-y)、[ScienceDirect 混合方法](https://www.sciencedirect.com/science/article/abs/pii/S095070511730374X)、[Frontiers in AI 可解释性调研](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1660548/full)

---

## 四、对 TalentDrop 的启发与建议

### 4.1 算法架构矩阵

将上述调研产品/理论按两个维度分类：

```
              显式特征（问卷/游戏/简历）
                    ↑
     Plum.io    Pymetrics      TalentDrop (目标定位)
     OkCupid      ↑               ↑
                   |               |
←—— 规则/公式 ——————————————————————————→ 机器学习/深度学习
                   |               |
     Hinge(GS)     ↓               ↓
     CMB        Eightfold      HireVue
                    ↓
              隐式特征（行为数据/交互历史）
```

### 4.2 TalentDrop 可借鉴的技术路线

| 借鉴来源 | 可借鉴的核心技术 | 如何应用到 TalentDrop |
|----------|----------------|---------------------|
| **OkCupid** | 加权问答 + 几何平均数 | Career DNA 问卷的基础评分框架 |
| **Pymetrics** | 行为场景 + 连续谱特征 | 行为情境题设计思路、无"对错"的特征空间 |
| **Hinge** | Gale-Shapley 稳定匹配 | Weekly Drop 的候选人-职位双向匹配 |
| **Eightfold** | 技能嵌入 + 余弦相似度 | 技能维度的语义匹配 |
| **Edwards P-E Fit** | 多项式回归 + 响应面分析 | 人-组织契合度的理论基础和数学模型 |
| **CMB** | 隐因子协同过滤 | 随平台积累匹配数据后引入 CF 分支 |
| **Plum.io** | Big Five + 岗位专家标定 | Company DNA 的岗位需求定义流程 |

### 4.3 推荐的 TalentDrop 匹配算法分层架构

```
Layer 1: 硬性过滤（Dealbreakers）
  → 地点、薪资范围、签证要求等不可协商条件
  → 类似 Hinge Dealbreaker 机制

Layer 2: Career DNA 兼容性评分（OkCupid 式加权几何平均）
  → 8 个核心维度的连续谱匹配
  → 双向评分：候选人对公司的满意度 × 公司对候选人的满意度
  → Match% = √(Score_C→J × Score_J→C)

Layer 3: 技能语义匹配（Eightfold 式嵌入）
  → 将技能嵌入向量空间，计算余弦相似度
  → 考虑技能新鲜度（最近经历的权重更高）

Layer 4: 文化/价值观契合（Edwards P-E Fit 多项式回归）
  → Company DNA vs Career DNA 在价值观维度的契合度
  → 使用简化的距离度量或多项式回归模型

Layer 5: 稳定匹配优化（Hinge 式 Gale-Shapley）
  → 在 Layer 2-4 得分基础上，进行双向偏好的稳定匹配
  → 确保 Weekly Drop 的推荐结果对双方都是"稳定"的

Layer 6: 协同过滤增强（CMB 式隐因子模型）
  → 冷启动阶段依赖 Layer 2-5
  → 积累足够交互数据后引入 CF 分支
  → 发现问卷无法捕捉的隐式匹配模式

Layer 7: 公平性约束（Pymetrics Audit-AI 式偏见检测）
  → 持续监控不同人口统计群体的匹配率
  → 4/5 规则 + 统计显著性检验
  → 移除任何导致系统性偏见的特征
```

---

## 五、核心参考文献汇总

### 学术论文
1. Gale, D. & Shapley, L. (1962). "College Admissions and the Stability of Marriage." *American Mathematical Monthly*
2. Edwards, J.R. & Parry, M.E. (1993). "On the use of polynomial regression equations as an alternative to difference scores." *Academy of Management Journal*
3. Kristof, A.L. (1996). "Person-Organization Fit: An Integrative Review." *Personnel Psychology*
4. Lejuez, C.W. et al. (2002). "Evaluation of a Behavioral Measure of Risk Taking: The Balloon Analogue Risk Task (BART)." *Journal of Experimental Psychology: Applied*
5. Diaby, M. et al. (2017). "Combining content-based and collaborative filtering for job recommendation system." *Knowledge-Based Systems* (ScienceDirect)
6. Wang et al. (2021). "A Deep-Learning-Inspired Person-Job Matching Model." *Complexity* (Wiley)
7. Francis, Back & Matz (2024). "Machine learning in recruiting: predicting personality from CVs." *Frontiers in Social Psychology*
8. Ashlagi, Chen, Roghani & Saberi (2025). "Stable Matching with Interviews." *arXiv:2501.12503*

### 技术博客与产品文档
9. [Eightfold AI 工程博客](https://eightfold.ai/engineering-blog/ai-powered-talent-matching-the-tech-behind-smarter-and-fairer-hiring/) (2025)
10. [Pymetrics audit-ai GitHub](https://github.com/pymetrics/audit-ai)
11. [Torre.ai Job Matching Model](https://torre.ai/jobmatchingmodel)
12. [CMB AWS re:Invent 2017 演讲](https://www.slideshare.net/AmazonWebServices/dating-and-data-science-how-coffee-meets-bagel-uses-amazon-elasticache-to-deliver-highquality-match-recommendations-dat323-reinvent-2017)
13. [OkCupid 算法数学解析](https://blogs.ams.org/mathgradblog/2016/06/08/okcupid-math-online-dating/)
14. [HireVue 模型训练流程](https://www.hirevue.com/blog/hiring/train-validate-re-train-how-we-build-hirevue-assessments-models)
