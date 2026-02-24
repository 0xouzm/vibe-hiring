# TalentDrop Demo Phase 1 — Gap Analysis

> 日期：2026-02-24
> 目标：梳理从"概念+原型"到"可演示 Demo"的全部缺口，按优先级排序
> 背景：当前已完成产品设计文档 + 静态原型，无应用代码

---

## 一、已完成清单

| # | 产出物 | 文件 | 状态 |
|---|--------|------|------|
| 1 | 核心产品概念（6 大机制、用户旅程、商业模式） | `discuss/brainstorm.md` | ✅ |
| 2 | 行业竞品调研（Eightfold, Pymetrics, Hinge, OkCupid, CMB 等） | `discuss/matching-algorithm-research.md` | ✅ |
| 3 | 题库设计方法论（心理测量学 + 博弈论） | `discuss/question-bank-design.md` | ✅ |
| 4 | Career DNA 候选人侧 30 题完整题库（8 维光谱） | `discuss/question-bank-full.md` | ✅ |
| 5 | 7 层反作弊机制设计 | `discuss/anti-gaming-mechanism.md` | ✅ |
| 6 | 3 层匹配引擎架构（LightRAG + 算法 + 进化） | `discuss/matching-architecture.md` | ✅ |
| 7 | Pitch Deck 理论基础（Career DNA 学术锚点） | `discuss/pitch-theoretical-foundation.md` | ✅ |
| 8 | 静态 HTML/CSS/JS 交互原型 | `prototype/index.html` | ✅ |
| 9 | Company DNA 设计方案（聚合算法 + 真实度验证） | `discuss/company-dna-design.md` | ✅ 本次 |
| 10 | Company DNA 20 题完整题库 | `discuss/company-dna-full.md` | ✅ 本次 |

---

## 二、P0 — Demo 阻塞项（必须完成才能 Demo）

> 没有这些，Demo 无法展示核心匹配逻辑

### G1: Company DNA 设计文档 ✅ 已完成

- **文件**: `discuss/company-dna-design.md`
- **内容**: 设计原则、维度映射、聚合算法、Culture Authenticity Score
- **状态**: 本次完成

### G2: Company DNA 20 题完整题库 ✅ 已完成

- **文件**: `discuss/company-dna-full.md`
- **内容**: 20 道完整英文场景题 + 维度映射 + 交叉验证逻辑
- **状态**: 本次完成

### G3: Demo 数据集（虚构公司 + 候选人）✅ 已完成

- **文件**: `discuss/demo-dataset.md`
- **内容**: 3 家虚构公司 + 6 名候选人 + 18 对匹配分矩阵 + 4 份匹配报告样本
- **状态**: 已完成

### G4: 原型维度命名同步 ✅ 已完成

- **内容**: `prototype/index.html` 中 Comms/Conflict → Expression/Execution，Q19/Q20 替换为新 Execution 题
- **状态**: 已完成

---

## 三、P1 — 提升 Demo 说服力（Demo 能跑但有这些更好）

> 有了这些，Demo 从"静态展示"升级为"交互演示"

### G5: 企业侧问卷原型页面

- **缺失原因**: 当前原型只有候选人旅程，没有企业侧
- **需要产出**:
  - Company DNA 问卷填写界面原型（20 题交互）
  - HR 邀请员工填写的流程页面
  - 聚合结果展示页面（雷达图 + CAS 评分）
- **工作量**: ~2 天
- **依赖**: G1, G2

### G6: 匹配报告动态计算

- **缺失原因**: 当前原型中的匹配报告是硬编码的静态内容
- **需要产出**:
  - 基于 G3 数据集的动态匹配分计算（至少 L2 层简化版）
  - 匹配报告根据维度差异动态生成文案
  - 前端展示"为什么你们适合"的动态雷达图对比
- **工作量**: ~3 天
- **依赖**: G3

### G7: 员工聚合与真实度验证 Demo

- **缺失原因**: Company DNA 的核心差异化（多人填写 + CAS）没有演示
- **需要产出**:
  - 模拟 HR + 5 名员工的填写数据
  - 去极值加权中位数聚合结果的可视化
  - HR-员工偏差的可视化对比
  - Culture Authenticity Score 的展示
- **工作量**: ~2 天
- **依赖**: G5

### G8: 雷达图维度更新

- **缺失原因**: 原型中的雷达图仍为旧维度模型
- **需要产出**:
  - 8 维雷达图（Pace, Collab, Decision, Expression, Unc, Growth, Motiv, Execution）
  - 候选人 vs 企业的双层雷达图叠加展示
  - 维度匹配度的颜色编码（绿色=高匹配，黄色=中等，红色=低匹配）
- **工作量**: ~1 天
- **依赖**: G4

---

## 四、P2 — 锦上添花（Demo 可展示更完整的产品蓝图）

> 有了这些，Demo 从"核心功能"升级为"完整产品愿景"

### G9: 第二层岗位定制题

- **缺失原因**: 三层题库架构中，第二层（岗位类型定制 15 题）只有 3 题示例
- **需要产出**:
  - 至少完成"工程师岗"完整 15 题
  - 展示三层架构如何协同工作
- **工作量**: ~2 天
- **依赖**: 无

### G10: 技术架构选型

- **缺失原因**: `matching-architecture.md` 给出了技术栈初步规划，但没有具体选型决策
- **需要产出**:
  - 前端：确认 Next.js 15+ 项目脚手架
  - 后端：确认 Python（uv + FastAPI）或 Node.js
  - 数据库：确认 PostgreSQL 方案
  - 部署：确认云平台和 CI/CD
- **工作量**: ~1 天
- **依赖**: 无

### G11: 数据模型设计

- **缺失原因**: 没有 ERD 或数据结构定义
- **需要产出**:
  - 用户（候选人 + 企业 + 员工）数据模型
  - Career DNA / Company DNA 评分存储结构
  - 匹配结果和 Weekly Drop 数据模型
  - 问卷回答的原始数据存储
- **工作量**: ~2 天
- **依赖**: G10

### G12: Pitch Deck 制作

- **缺失原因**: 理论基础文档已完成，但没有正式的演示幻灯片
- **需要产出**:
  - 10-15 页核心 Pitch Deck
  - 包含：问题 → 方案 → 产品演示 → 技术壁垒 → 商业模式 → 团队 → Ask
- **工作量**: ~2 天
- **依赖**: G6（需要动态 Demo 截图）

---

## 五、P3 — Phase 2 才需要

> 不影响 Demo，但实际运行时必须有

| # | 项目 | 说明 |
|---|------|------|
| G13 | AI 语音分析模块 | Career DNA 中的语音部分 |
| G14 | Play Recruiter 推荐系统 | 内推机制 |
| G15 | Team Chemistry 互补度计算 | 团队级匹配 |
| G16 | 90 天追踪与反馈闭环 | 结果数据收集 |
| G17 | L6 协同过滤 + L7 公平性审计 | 进化层 |
| G18 | Glassdoor/Blind 数据接入 | 第三方真实度验证 |
| G19 | 企业自定义题审核系统 | 第三层题库的 AI 质量审核 |

---

## 六、建议执行顺序

```
Sprint 0（立即，0.5 天）
  └── G4: 原型维度命名同步
        原因：修改量最小，消除所有文档和原型的不一致

Sprint 1（1-2 天）
  └── G3: Demo 数据集
        原因：P0 阻塞项中唯一剩余，且为 G6 前置依赖
        产出：3 家公司 + 5-8 名候选人的完整假数据

Sprint 2（3-4 天）
  ├── G8: 雷达图维度更新（依赖 G4）
  └── G5: 企业侧问卷原型页面（依赖 G1, G2）
        原因：两项可并行，快速补齐企业侧视觉

Sprint 3（3-4 天）
  ├── G6: 匹配报告动态计算（依赖 G3）
  └── G7: 员工聚合与真实度验证 Demo（依赖 G5）
        原因：这是 Demo 的"wow moment"

Sprint 4（可选，3-4 天）
  ├── G10: 技术架构选型
  ├── G9: 第二层岗位定制题
  └── G11: 数据模型设计（依赖 G10）

Sprint 5（可选，2 天）
  └── G12: Pitch Deck 制作（依赖 G6 截图）
```

### 时间线总结

| 里程碑 | 累计时间 | 可演示内容 |
|--------|---------|-----------|
| Sprint 0 完成 | 0.5 天 | 原型维度一致 |
| Sprint 1 完成 | 2.5 天 | 假数据就绪，可手动演示匹配 |
| Sprint 2 完成 | 6.5 天 | 企业侧问卷可交互 + 新雷达图 |
| Sprint 3 完成 | 10.5 天 | **核心 Demo 完成** — 动态匹配 + CAS |
| Sprint 4 完成 | 14.5 天 | 技术蓝图 + 数据模型就绪 |
| Sprint 5 完成 | 16.5 天 | Pitch Deck 就绪 |

> **最小可行 Demo = Sprint 0-3 ≈ 2 周**
> 包含：候选人问卷 + 企业问卷 + 动态匹配报告 + 文化真实度验证
