"use client";

/* ── Types ───────────────────────────────────────────── */

interface FunnelData {
  total_candidates: number;
  l1_passed: number;
  l2_top: number;
}

interface MatchFunnelProps {
  funnel: FunnelData;
  width?: number;
  height?: number;
}

/* ── Funnel Chart ────────────────────────────────────── */

export function MatchFunnel({ funnel, width = 400, height = 240 }: MatchFunnelProps) {
  const stages = [
    { label: "全部候选人", count: funnel.total_candidates, color: "#374151" },
    { label: "L1 硬性筛选通过", count: funnel.l1_passed, color: "#6366f1" },
    { label: "L2 DNA 匹配 Top", count: funnel.l2_top, color: "#10B981" },
  ];

  const maxCount = Math.max(...stages.map((s) => s.count), 1);
  const stageHeight = (height - 40) / stages.length;
  const minWidth = 80;
  const maxBarWidth = width - 120;

  return (
    <svg width={width} height={height}>
      {/* Title */}
      <text x={width / 2} y={16} textAnchor="middle" fill="#9CA3AF" fontSize={12}>
        匹配漏斗
      </text>

      {stages.map((stage, i) => {
        const ratio = stage.count / maxCount;
        const barWidth = Math.max(minWidth, maxBarWidth * ratio);
        const x = (width - barWidth) / 2;
        const y = 30 + i * stageHeight;
        const barH = stageHeight - 8;

        // Trapezoid shape for funnel
        const nextRatio = i < stages.length - 1 ? stages[i + 1].count / maxCount : ratio * 0.5;
        const nextWidth = Math.max(minWidth, maxBarWidth * nextRatio);
        const x1 = x;
        const x2 = x + barWidth;
        const x3 = (width + nextWidth) / 2;
        const x4 = (width - nextWidth) / 2;

        return (
          <g key={stage.label}>
            <polygon
              points={`${x1},${y} ${x2},${y} ${x3},${y + barH} ${x4},${y + barH}`}
              fill={stage.color}
              fillOpacity={0.3}
              stroke={stage.color}
              strokeWidth={1}
              strokeOpacity={0.6}
            />
            {/* Label */}
            <text
              x={width / 2}
              y={y + barH / 2 + 5}
              textAnchor="middle"
              fill="#E5E7EB"
              fontSize={13}
              fontWeight={600}
            >
              {stage.label}: {stage.count}
            </text>
          </g>
        );
      })}
    </svg>
  );
}
