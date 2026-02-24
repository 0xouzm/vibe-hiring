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
  pace: "Work Pace",
  collab: "Collaboration",
  decision: "Decision Style",
  expression: "Expression",
  unc: "Uncertainty Tolerance",
  growth: "Growth Path",
  motiv: "Motivation",
  execution: "Execution Style",
};

export const DIMENSION_SPECTRUM: Record<DimensionKey, [string, string]> = {
  pace: ["Deep & Thorough", "Fast & Iterative"],
  collab: ["Independent", "Team-driven"],
  decision: ["Intuition-led", "Data-driven"],
  expression: ["Strategic & Subtle", "Direct & Open"],
  unc: ["Clarity-seeking", "Ambiguity-embracing"],
  growth: ["Deep Specialist", "Broad Generalist"],
  motiv: ["Reward-driven", "Mission-driven"],
  execution: ["Flexible & Adaptive", "Planned & Structured"],
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
