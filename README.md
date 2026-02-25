# 职遇 (TalentDrop)

AI 驱动的深度人才匹配平台。告别海投简历，候选人和企业各自完成深度问卷（Career DNA / Company DNA），算法每周自动「投递」高匹配机会。

## 项目概述

职遇借鉴 Date Drop 的深度匹配算法理念，将其应用于招聘场景：

- **Career DNA**：通过 8 个核心维度（节奏、协作、决策、表达、不确定性、成长、动机、执行）描绘候选人画像，所有维度均为光谱式分布，没有"正确答案"
- **三层问卷架构**：平台标准题（30 题，权重 60%）→ 岗位类型题（15 题，25%）→ 企业自定义题（≤5 题，15%）
- **双向发现机制**：候选人收到匹配岗位，企业收到匹配候选人，双方独立做出 接受/跳过 决策 → 双向匹配
- **每周 Drop**：每周二晚 9 点揭晓本周匹配结果，附带兼容性分析报告

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Next.js 16 + React 19 + TypeScript + Tailwind CSS v4 |
| 后端 | Python 3.11+ / FastAPI + Pydantic v2 |
| 数据库 | SQLite (aiosqlite) |
| AI | OpenAI API（对话画像 / 简历解析 / 匹配报告）+ LightRAG 知识图谱引擎，支持 mock 回退 |
| 包管理 | uv (Python) / npm (Node.js) |
| 部署 | Docker Compose |

## 主要功能

- **候选人侧**：Career DNA 问卷、每周 Drop 匹配揭晓、匹配报告（雷达图 + 知识图谱 + 匹配漏斗）、AI 对话画像、简历上传解析、个人档案管理
- **企业侧**：Company DNA 问卷、岗位管理（CRUD）、每周 Drop 候选人推荐、匹配详情与维度对比
- **匹配引擎**：L1 硬性筛选 → L2 DNA 兼容度（详见下方核心算法章节）
- **可视化**：力导向知识图谱、匹配漏斗图、维度对比条形图、DNA 雷达图
- **互动演示**：`/demo` 页面包含 6 个互动分区，展示平台理论基础

## 核心算法：三阶段匹配流水线

匹配计算是一条 **DNA 计分 → L1 硬过滤 → L2 DNA 兼容度** 的三阶段流水线。

### Stage 1 — DNA 画像计算

候选人和企业各自完成问卷后，系统通过 3 种题型的差异化计分策略，将主观作答转化为 8 维客观画像：

| 题型 | 计分策略 | 原理 |
|------|----------|------|
| **单选题** | 预定义映射表，每个选项对各维度有固定贡献分值 | 直接测量偏好 |
| **排序题** | **Borda 计数法** — 排第 1 得 N 分，末位得 1 分，归一化到 0-100 | 揭示优先级权重 |
| **预算分配题** | 分配百分比直接映射为维度分值 | 捕捉资源取舍倾向 |

每个维度汇总多道题的分值后取**平均值**，产出 8 维 `DimensionScores`（0-100 光谱值）。

同时计算**一致性系数**：

```
consistency = 1 - mean(各维度标准差) / 50
```

该系数衡量作答的自洽程度 — 越自洽，最终匹配分越有信心。

**企业侧的额外处理：**
- **多人聚合**：多位填写者的分数按角色加权（HR 权重 0.5、员工权重 1.0），N≥7 时去极端值，取**加权中位数**
- **CAS 文化真实性评分**：`CAS = 0.55 × 内部一致性 + 0.45 × HR-员工认知偏差`，分 Gold / Silver / Bronze 三档，量化企业文化描述的可信度

### Stage 2 — L1 硬约束过滤

布尔门槛，不通过则匹配分直接为 0：

| 过滤条件 | 逻辑 |
|----------|------|
| 远程政策 | `remote` 岗位所有候选人自动通过 |
| 地点匹配 | `onsite` 岗位要求城市精确匹配 |
| 技能交集 | 候选人技能集与岗位要求至少 1 个交集 |

### Stage 3 — L2 DNA 兼容度计算

通过 L1 后，进入核心匹配公式：

```
每个维度 d：  compat_d = 1 - |候选人_d - 企业_d| / 100
最终匹配分：  score = mean(compat_d) × consistency × 100
```

**本质上是 8 维向量的归一化曼哈顿距离，再乘以答题一致性作为置信度衰减。** 结果 clamp 到 0-100，越高代表"职场基因"越吻合。

## LightRAG 知识引擎：从结构化匹配到语义理解

职遇引入 [LightRAG](https://github.com/HKUDS/LightRAG)（港大 HKUDS，EMNLP 2025）作为匹配引擎的 **Layer 0 — 上下文理解层**。它不替代上述匹配算法，而是让算法真正"读懂"非结构化信息。

### 解决什么问题

传统招聘匹配只能处理结构化字段（技能标签、学历、薪资）。但真正决定匹配质量的信息往往藏在非结构化文本中 — 候选人的 Dream Role 描述、AI 对话记录、简历项目经历、员工匿名评价等。LightRAG 将这些文本自动转化为可检索、可推理的知识图谱。

### 数据流程

**写入阶段（索引构建）：**

```
问卷答案 / 简历文本 / AI 对话记录 / 员工评价
        ↓
    文本化（结构化数据转为自然语言描述）
        ↓
    LightRAG.insert()
        ↓
    自动处理：分块 → LLM 实体抽取 → 关系抽取 → 知识图谱构建 + 向量化存储
```

**查询阶段（检索增强生成）：**

```
用户请求（如"生成匹配报告" / "为什么推荐这个岗位"）
        ↓
    LightRAG.query(question, mode="hybrid")
        ↓
    双路检索：
      低级 → 向量相似度搜索，找到相关文本块
      高级 → 图谱遍历，通过实体关系发现隐含关联
        ↓
    合并 context + LLM 生成 → 有知识支撑的报告/回答
```

### 集成前后对比

| 场景 | 无 LightRAG（当前） | 有 LightRAG |
|------|---------------------|-------------|
| **匹配报告** | 分数直传 OpenAI，LLM 缺乏上下文 | 检索候选人简历 + 对话 + DNA，报告有据可查 |
| **知识图谱** | 手动从数据库拼装节点 | 自动从非结构化文本抽取实体和关系，图谱更丰富 |
| **AI 对话** | 无记忆，不跨轮次关联 | 对话持续索引，后续问题能关联之前的上下文 |
| **跨实体推理** | 无法实现 | 图谱可发现"候选人 A 的项目经验与岗位 B 的技术栈高度关联"等隐含匹配 |

### 知识图谱实体设计

| 实体类型 | 示例 | 关系 |
|---------|------|------|
| Person | 候选人、员工、推荐人 | `-[masters]→` Skill |
| Skill | React、财务建模、团队管理 | `-[related_to]→` Skill |
| Value | 自主性、使命驱动 | `-[complements]→` Culture |
| Culture | 扁平管理、快速迭代 | `-[embodies]←` Team |
| Outcome | 入职、留存、高绩效 | `-[led_to]←` Match |

### 三阶段进化路线

```
Phase 1（当前 — 冷启动）
  ✅ 问卷 + 匹配引擎 + 模板报告端到端跑通
  ✅ OpenAI 直调生成匹配报告，手动构建知识图谱可视化

Phase 2（数据积累）
  → LightRAG 正式接管上下文理解
  → 非结构化文本（对话/简历/评价）自动入图
  → 匹配报告由知识图谱双层检索 + LLM 联合生成
  → 增量更新：新数据直接并入已有图谱，无需重建

Phase 3（智能进化）
  → 90 天入职结果数据回传，新增 Outcome 节点
  → 图谱支持多跳推理：Match → led_to → Outcome → 反向推导成功因素
  → 协同过滤 + 知识图谱双引擎持续调优匹配权重
```

> 依赖已安装（`lightrag-hku>=1.0.0`），架构设计完成 — 可随时启动 Phase 2 集成。

## 快速开始

### 环境要求

- Python 3.11+、[uv](https://docs.astral.sh/uv/)
- Node.js 18+、npm
- （可选）Docker & Docker Compose
- （可选）OpenAI API Key（不配置则使用 mock 数据）

### 方式一：本地开发

```bash
# 1. 克隆项目
git clone <repo-url> && cd vibe-hiring

# 2. 启动后端（自动创建虚拟环境 + 安装依赖）
./scripts/dev-backend.sh

# 3. 初始化演示数据（另开终端）
./scripts/seed-db.sh

# 4. 启动前端（另开终端）
./scripts/dev-frontend.sh
```

后端运行在 `http://localhost:8000`，前端运行在 `http://localhost:3000`。

### 方式二：Docker Compose

```bash
# 一键启动前后端
./scripts/docker-up.sh
```

### 环境变量（可选）

```bash
export OPENAI_API_KEY="sk-..."       # 启用 AI 功能（对话/简历解析/报告）
export JWT_SECRET="your-secret"      # JWT 签名密钥（默认 demo-secret-key）
```

## 项目结构

```
vibe-hiring/
├── backend/           # FastAPI 后端（API / 模型 / 服务 / 数据）
├── frontend/          # Next.js 前端（页面 / 组件 / 工具库）
├── scripts/           # 开发与部署脚本
├── discuss/           # 产品设计文档
└── docker-compose.yml
```

## 演示账号

运行 `./scripts/seed-db.sh` 后，所有账号使用统一密码：`demo123`

> 首页（`http://localhost:3000`）内置快速登录按钮，点击姓名即可一键登录，无需手动输入。

### 候选人

| 姓名 | 邮箱 | 简介 |
|------|------|------|
| Alex Chen | `alex@example.com` | 高级前端，6年，杭州，快节奏/独立型 |
| Maria Santos | `maria@example.com` | 全栈，4年，北京，协作/使命驱动 |
| James Wright | `james@example.com` | 后端，8年，上海，数据驱动/计划有序 |
| Priya Sharma | `priya@example.com` | 产品工程师，3年，北京，使命驱动/团队 |
| David Kim | `david@example.com` | DevOps，5年，上海，数据驱动 |
| Sophie Zhang | `sophie@example.com` | 初级，1年，南京，广博通才 |

### 企业 HR

| 公司 | 邮箱 |
|------|------|
| Velocity Labs | `hr@velocity-labs.example.com` |
| Meridian Financial | `hr@meridian-financial.example.com` |
| Bloom Education | `hr@bloom-education.example.com` |

### 高匹配验证对照

| 候选人 | 公司 | 预期匹配度 |
|--------|------|-----------|
| Alex Chen | Velocity Labs | ~91% |
| James Wright | Meridian Financial | ~92% |
| Priya Sharma | Bloom Education | ~93% |
| Maria Santos | Bloom Education | ~89% |

## 许可证

私有项目，仅供内部使用。
