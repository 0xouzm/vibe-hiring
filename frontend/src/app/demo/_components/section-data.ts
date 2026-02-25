/* ── Section 常量数据 ──────────────────────────────────────────────── */

export const BIG_FIVE_MAP = [
  { big5: "外向性 Extraversion", dim: "Pace 节奏", measure: "快节奏冲刺 vs 稳步推进" },
  { big5: "宜人性 Agreeableness", dim: "Collab 协作", measure: "独立深耕 vs 团队协同" },
  { big5: "开放性 Openness", dim: "Decision 决策", measure: "数据驱动 vs 直觉判断" },
  { big5: "宜人性+神经质", dim: "Expression 表达", measure: "直言不讳 vs 委婉含蓄" },
  { big5: "开放性 Openness", dim: "Uncertainty 不确定性", measure: "拥抱模糊 vs 需要明确" },
  { big5: "开放性 Openness", dim: "Growth 成长", measure: "广泛探索 vs 深度专精" },
  { big5: "尽责性 Conscientiousness", dim: "Motivation 驱动力", measure: "使命驱动 vs 回报驱动" },
  { big5: "尽责性 Conscientiousness", dim: "Execution 执行", measure: "严谨计划 vs 灵活应变" },
];

export const PAIN_POINTS = [
  { label: "简历黑洞", desc: "投了 100 封，回复 3 封", pct: "97%" },
  { label: "面试马拉松", desc: "8 轮面试只为一个 offer", pct: "8轮" },
  { label: "文化错配", desc: "入职 3 个月才发现不合适", pct: "90天" },
  { label: "算法偏见", desc: "关键词匹配 ≠ 真正匹配", pct: "≠" },
  { label: "信息不对称", desc: "候选人猜公司文化，公司猜候选人能力", pct: "??" },
];

export const LAYERS = [
  { name: "平台标准层", count: "30 题", weight: "60%", color: "#6366f1" },
  { name: "岗位专属层", count: "15 题", weight: "25%", color: "#f59e0b" },
  { name: "企业定制层", count: "≤5 题", weight: "15%", color: "#10b981" },
];

export const ENGINE_LAYERS = [
  { id: "L1", name: "LightRAG 语义理解", desc: "知识图谱 + 上下文增强检索", color: "#6366f1" },
  { id: "L2", name: "DNA 兼容性", desc: "8 维光谱距离 + 权重优化", color: "#ff6b4a" },
  { id: "L3", name: "技能匹配", desc: "硬技能 + 软实力向量相似度", color: "#f59e0b" },
  { id: "L4", name: "Gale-Shapley 稳定匹配", desc: "双向偏好的博弈论最优解", color: "#10b981" },
  { id: "L5", name: "几何均值聚合", desc: "防止单维过高掩盖短板", color: "#6366f1" },
  { id: "L6-L7", name: "进化反馈回路", desc: "90 天追踪 → 算法自适应", color: "#ff6b4a" },
];

/* ── Date Drop 对比数据 ───────────────────────────────────────────── */

export const DATE_DROP_STATS = [
  { label: "用户规模", value: "5,000+", desc: "活跃用户" },
  { label: "转化率", value: "10x", desc: "vs Tinder 等平台" },
  { label: "问卷深度", value: "~50 题", desc: "心理+社会学" },
  { label: "推荐频率", value: "每周 1 人", desc: "深度匹配" },
];

export const COMPARISON_ROWS = [
  {
    dim: "问卷设计",
    dateDrop: "~50 题，心理学 + 社会学量表",
    zhiyu: "30+ 题 Career DNA 8 维 + 三层架构（标准/岗位/企业）",
    highlight: true,
  },
  {
    dim: "AI 对话",
    dateDrop: "语音对话提取择偶偏好",
    zhiyu: "文本对话提取职业画像 + 简历解析双通道",
    highlight: false,
  },
  {
    dim: "匹配算法",
    dateDrop: "监督学习预测 + Gale-Shapley",
    zhiyu: "L1-L5 五层渐进式匹配引擎",
    highlight: true,
  },
  {
    dim: "推荐机制",
    dateDrop: "每周二 Drop 1 人",
    zhiyu: "每周二 Drop — 候选人 1-3 / 企业 3-5",
    highlight: true,
  },
  {
    dim: "反馈闭环",
    dateDrop: "约会结果 → 模型调优",
    zhiyu: "90 天入职追踪 → 权重 + 题库 + 图谱全链路进化",
    highlight: false,
  },
  {
    dim: "知识图谱",
    dateDrop: "无",
    zhiyu: "LightRAG 上下文理解 + 多跳推理",
    highlight: true,
  },
];

/* ── Section 定义 ────────────────────────────────────────────────── */

export interface SectionDef {
  id: string;
  icon: string;
  title: string;
  color: string;
}

export const SECTION_DEFS: SectionDef[] = [
  { id: "pain", icon: "⚡", title: "行业痛点", color: "#ff6b4a" },
  { id: "dna", icon: "🧬", title: "Career DNA 理论框架", color: "#6366f1" },
  { id: "arch", icon: "📋", title: "三层问卷架构", color: "#f59e0b" },
  { id: "compare", icon: "📊", title: "与 Date Drop 的对标", color: "#a855f7" },
  { id: "engine", icon: "⚙️", title: "三层匹配引擎", color: "#10b981" },
  { id: "flow", icon: "🔄", title: "双向发现机制", color: "#6366f1" },
  { id: "flywheel", icon: "🚀", title: "数据飞轮", color: "#ff6b4a" },
];
