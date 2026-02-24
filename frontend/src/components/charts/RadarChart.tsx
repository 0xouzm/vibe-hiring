"use client";

import type { DimensionScores } from "@/lib/types";
import { DIMENSIONS, DIMENSION_LABELS, type DimensionKey } from "@/lib/constants";

/* ── Types ──────────────────────────────────────────── */

interface RadarChartProps {
  scores: DimensionScores;
  compareScores?: DimensionScores;
  size?: number;
  className?: string;
}

/* ── Geometry helpers ───────────────────────────────── */

const AXIS_COUNT = DIMENSIONS.length;

function polarToXY(
  cx: number,
  cy: number,
  radius: number,
  index: number,
): [number, number] {
  const angle = (Math.PI * 2 * index) / AXIS_COUNT - Math.PI / 2;
  return [cx + radius * Math.cos(angle), cy + radius * Math.sin(angle)];
}

function buildPolygonPoints(
  cx: number,
  cy: number,
  scores: DimensionScores,
  maxRadius: number,
): string {
  return DIMENSIONS.map((dim, i) => {
    const value = scores[dim] ?? 0;
    const r = (value / 100) * maxRadius;
    const [x, y] = polarToXY(cx, cy, r, i);
    return `${x},${y}`;
  }).join(" ");
}

/* ── Grid rings ─────────────────────────────────────── */

const RINGS = [20, 40, 60, 80, 100];

function GridRings({ cx, cy, maxRadius }: { cx: number; cy: number; maxRadius: number }) {
  return (
    <>
      {RINGS.map((ringValue) => {
        const r = (ringValue / 100) * maxRadius;
        const points = Array.from({ length: AXIS_COUNT }, (_, i) =>
          polarToXY(cx, cy, r, i),
        )
          .map(([x, y]) => `${x},${y}`)
          .join(" ");
        return (
          <polygon
            key={ringValue}
            points={points}
            fill="none"
            stroke="#E2E8F0"
            strokeWidth="1"
            opacity={0.6}
          />
        );
      })}
    </>
  );
}

/* ── Axis lines ─────────────────────────────────────── */

function AxisLines({ cx, cy, maxRadius }: { cx: number; cy: number; maxRadius: number }) {
  return (
    <>
      {DIMENSIONS.map((_, i) => {
        const [x, y] = polarToXY(cx, cy, maxRadius, i);
        return (
          <line
            key={i}
            x1={cx}
            y1={cy}
            x2={x}
            y2={y}
            stroke="#E2E8F0"
            strokeWidth="1"
            opacity={0.6}
          />
        );
      })}
    </>
  );
}

/* ── Labels ─────────────────────────────────────────── */

function AxisLabels({ cx, cy, maxRadius }: { cx: number; cy: number; maxRadius: number }) {
  const labelOffset = 18;
  return (
    <>
      {DIMENSIONS.map((dim, i) => {
        const [x, y] = polarToXY(cx, cy, maxRadius + labelOffset, i);
        return (
          <text
            key={dim}
            x={x}
            y={y}
            textAnchor="middle"
            dominantBaseline="central"
            fontSize="11"
            fill="#64748B"
            fontFamily="var(--font-body)"
          >
            {DIMENSION_LABELS[dim as DimensionKey]}
          </text>
        );
      })}
    </>
  );
}

/* ── Data polygon ───────────────────────────────────── */

interface DataAreaProps {
  cx: number;
  cy: number;
  scores: DimensionScores;
  maxRadius: number;
  fillColor: string;
  strokeColor: string;
}

function DataArea({ cx, cy, scores, maxRadius, fillColor, strokeColor }: DataAreaProps) {
  const points = buildPolygonPoints(cx, cy, scores, maxRadius);
  return (
    <>
      <polygon
        points={points}
        fill={fillColor}
        stroke={strokeColor}
        strokeWidth="2"
      />
      {/* Dots on vertices */}
      {DIMENSIONS.map((dim, i) => {
        const value = scores[dim] ?? 0;
        const r = (value / 100) * maxRadius;
        const [x, y] = polarToXY(cx, cy, r, i);
        return (
          <circle
            key={dim}
            cx={x}
            cy={y}
            r="3.5"
            fill={strokeColor}
            stroke="white"
            strokeWidth="1.5"
          />
        );
      })}
    </>
  );
}

/* ── Main Component ─────────────────────────────────── */

export function RadarChart({
  scores,
  compareScores,
  size = 320,
  className = "",
}: RadarChartProps) {
  const cx = size / 2;
  const cy = size / 2;
  const maxRadius = size / 2 - 40;

  return (
    <svg
      width={size}
      height={size}
      viewBox={`0 0 ${size} ${size}`}
      className={className}
    >
      <GridRings cx={cx} cy={cy} maxRadius={maxRadius} />
      <AxisLines cx={cx} cy={cy} maxRadius={maxRadius} />
      <AxisLabels cx={cx} cy={cy} maxRadius={maxRadius} />

      {/* Compare data (behind) */}
      {compareScores && (
        <DataArea
          cx={cx}
          cy={cy}
          scores={compareScores}
          maxRadius={maxRadius}
          fillColor="rgba(249, 115, 22, 0.12)"
          strokeColor="#F97316"
        />
      )}

      {/* Primary data (front) */}
      <DataArea
        cx={cx}
        cy={cy}
        scores={scores}
        maxRadius={maxRadius}
        fillColor="rgba(99, 102, 241, 0.15)"
        strokeColor="#6366f1"
      />
    </svg>
  );
}
