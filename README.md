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
- **匹配引擎**：L1 硬性筛选（技能/地点）→ L2 DNA 兼容度（8 维向量距离 × 一致性系数）
- **可视化**：力导向知识图谱、匹配漏斗图、维度对比条形图、DNA 雷达图
- **互动演示**：`/demo` 页面包含 6 个互动分区，展示平台理论基础

## LightRAG 驱动的智能进化

职遇的核心技术差异化在于引入 [LightRAG](https://github.com/HKUDS/LightRAG)（港大 HKUDS，EMNLP 2025）作为匹配引擎的 **Layer 0 — 上下文理解层**。它不替代匹配算法本身，而是让算法真正"读懂"非结构化信息。

### 解决什么问题

传统招聘匹配只能处理结构化字段（技能标签、学历、薪资）。但真正决定匹配质量的信息往往藏在非结构化文本中 — 候选人的 Dream Role 描述、AI 对话转录、员工匿名评价、推荐信等。LightRAG 将这些文本转化为可检索、可推理的知识图谱。

### 知识图谱设计

| 实体类型 | 示例 | 关系 |
|---------|------|------|
| Person | 候选人、员工、推荐人 | `-[masters]→` Skill |
| Skill | React、财务建模、团队管理 | `-[related_to]→` Skill |
| Value | 自主性、使命驱动 | `-[complements]→` Culture |
| Culture | 扁平管理、快速迭代 | `-[embodies]←` Team |
| Outcome | 入职、留存、高绩效 | `-[led_to]←` Match |

### 双层检索

- **精确实体查询**：「候选人 A 擅长什么技术？」→ 沿图谱边遍历，自动扩展关联技能
- **宏观关系推理**：「什么特质的人在快速迭代文化中表现最好？」→ 跨实体多跳推理，发现隐式成功因素

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
  → 知识图谱成熟后支持多跳推理：
    Match → led_to → Outcome → 反向推导成功因素
  → 协同过滤 + 知识图谱双引擎持续调优匹配权重
```

> 依赖已安装（`lightrag-hku>=1.0.0`），环境变量与 Docker 配置就位，架构设计完成 — 可随时启动 Phase 2 集成。

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
