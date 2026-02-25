"use client";

import { DIMENSION_LABELS, type DimensionKey } from "@/lib/constants";

/* ── Types ───────────────────────────────────────────── */

interface DimensionCompareProps {
  candidate: Record<string, number>;
  company: Record<string, number>;
  compatibility: Record<string, number>;
  width?: number;
}

/* ── Dimension Comparison Bar Chart ──────────────────── */

export function DimensionCompare({
  candidate,
  company,
  compatibility,
  width = 500,
}: DimensionCompareProps) {
  const dimensions = Object.keys(candidate) as DimensionKey[];
  const barHeight = 28;
  const gap = 8;
  const labelWidth = 100;
  const valueWidth = 40;
  const barAreaWidth = width - labelWidth - valueWidth * 2 - 20;
  const totalHeight = dimensions.length * (barHeight * 2 + gap + 16) + 40;

  return (
    <svg width={width} height={totalHeight}>
      {/* Legend */}
      <g transform="translate(0, 10)">
        <circle cx={labelWidth} cy={6} r={5} fill="#6366f1" />
        <text x={labelWidth + 12} y={10} fill="#9CA3AF" fontSize={11}>候选人</text>
        <circle cx={labelWidth + 80} cy={6} r={5} fill="#F97316" />
        <text x={labelWidth + 92} y={10} fill="#9CA3AF" fontSize={11}>企业</text>
        <circle cx={labelWidth + 140} cy={6} r={5} fill="#10B981" />
        <text x={labelWidth + 152} y={10} fill="#9CA3AF" fontSize={11}>兼容度</text>
      </g>

      {dimensions.map((dim, i) => {
        const y = 40 + i * (barHeight * 2 + gap + 16);
        const cVal = candidate[dim] ?? 0;
        const jVal = company[dim] ?? 0;
        const compatVal = compatibility[dim] ?? 0;
        const label = DIMENSION_LABELS[dim] ?? dim;

        return (
          <g key={dim}>
            {/* Dimension label */}
            <text
              x={labelWidth - 8}
              y={y + barHeight - 4}
              textAnchor="end"
              fill="#E5E7EB"
              fontSize={12}
              fontWeight={500}
            >
              {label}
            </text>

            {/* Candidate bar */}
            <rect
              x={labelWidth}
              y={y}
              width={Math.max(2, (cVal / 100) * barAreaWidth)}
              height={barHeight / 2 - 1}
              rx={3}
              fill="#6366f1"
              fillOpacity={0.7}
            />
            <text
              x={labelWidth + barAreaWidth + 8}
              y={y + barHeight / 2 - 3}
              fill="#9CA3AF"
              fontSize={10}
            >
              {Math.round(cVal)}
            </text>

            {/* Company bar */}
            <rect
              x={labelWidth}
              y={y + barHeight / 2 + 1}
              width={Math.max(2, (jVal / 100) * barAreaWidth)}
              height={barHeight / 2 - 1}
              rx={3}
              fill="#F97316"
              fillOpacity={0.7}
            />
            <text
              x={labelWidth + barAreaWidth + 8}
              y={y + barHeight - 1}
              fill="#9CA3AF"
              fontSize={10}
            >
              {Math.round(jVal)}
            </text>

            {/* Compatibility indicator */}
            <rect
              x={labelWidth}
              y={y + barHeight + 4}
              width={Math.max(2, (compatVal / 100) * barAreaWidth)}
              height={6}
              rx={3}
              fill="#10B981"
              fillOpacity={0.5}
            />
            <text
              x={labelWidth + barAreaWidth + 8}
              y={y + barHeight + 10}
              fill="#10B981"
              fontSize={10}
              fontWeight={600}
            >
              {Math.round(compatVal)}%
            </text>
          </g>
        );
      })}
    </svg>
  );
}
