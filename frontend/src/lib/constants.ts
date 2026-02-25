export const DIMENSIONS = [
  "pace",
  "collab",
  "decision",
  "expression",
  "unc",
  "growth",
  "motiv",
  "execution",
] as const;

export type DimensionKey = (typeof DIMENSIONS)[number];

export const DIMENSION_LABELS: Record<DimensionKey, string> = {
  pace: "工作节奏",
  collab: "协作模式",
  decision: "决策风格",
  expression: "表达风格",
  unc: "不确定性容忍",
  growth: "成长路径",
  motiv: "驱动力",
  execution: "执行风格",
};

export const DIMENSION_SPECTRUM: Record<DimensionKey, [string, string]> = {
  pace: ["深度打磨", "快速迭代"],
  collab: ["独立自主", "团队驱动"],
  decision: ["直觉主导", "数据驱动"],
  expression: ["策略含蓄", "直接开放"],
  unc: ["追求确定", "拥抱模糊"],
  growth: ["深耕专家", "广博通才"],
  motiv: ["回报驱动", "使命驱动"],
  execution: ["灵活应变", "计划有序"],
};

export const DIMENSION_COLORS: Record<DimensionKey, string> = {
  pace: "#6366f1",
  collab: "#F97316",
  decision: "#F59E0B",
  expression: "#10B981",
  unc: "#F43F5E",
  growth: "#8B5CF6",
  motiv: "#06B6D4",
  execution: "#EC4899",
};
