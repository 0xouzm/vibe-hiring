"use client";

import { useEffect, useRef, useState } from "react";

/* ── Types ───────────────────────────────────────────── */

interface GraphNode {
  id: string;
  label: string;
  type: "person" | "company" | "role" | "skill" | "requirement" | "dimension";
  size: number;
  x?: number;
  y?: number;
  vx?: number;
  vy?: number;
}

interface GraphEdge {
  source: string;
  target: string;
  weight: number;
  type?: string;
}

interface KnowledgeGraphProps {
  nodes: GraphNode[];
  edges: GraphEdge[];
  width?: number;
  height?: number;
}

/* ── Colors by node type ─────────────────────────────── */

const TYPE_COLORS: Record<string, string> = {
  person: "#6366f1",
  company: "#F97316",
  role: "#F59E0B",
  skill: "#10B981",
  requirement: "#06B6D4",
  dimension: "#8B5CF6",
};

/* ── Simple force simulation ─────────────────────────── */

function initPositions(nodes: GraphNode[], w: number, h: number): GraphNode[] {
  const cx = w / 2;
  const cy = h / 2;
  return nodes.map((n, i) => ({
    ...n,
    x: cx + (Math.cos((i / nodes.length) * Math.PI * 2) * w * 0.3),
    y: cy + (Math.sin((i / nodes.length) * Math.PI * 2) * h * 0.3),
    vx: 0,
    vy: 0,
  }));
}

function simulate(nodes: GraphNode[], edges: GraphEdge[], steps: number = 80) {
  const nodeMap = new Map(nodes.map((n) => [n.id, n]));

  for (let step = 0; step < steps; step++) {
    const alpha = 1 - step / steps;

    // Repulsion between all nodes
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i];
        const b = nodes[j];
        const dx = (b.x ?? 0) - (a.x ?? 0);
        const dy = (b.y ?? 0) - (a.y ?? 0);
        const dist = Math.max(Math.sqrt(dx * dx + dy * dy), 1);
        const force = (200 * alpha) / dist;
        const fx = (dx / dist) * force;
        const fy = (dy / dist) * force;
        a.vx = (a.vx ?? 0) - fx;
        a.vy = (a.vy ?? 0) - fy;
        b.vx = (b.vx ?? 0) + fx;
        b.vy = (b.vy ?? 0) + fy;
      }
    }

    // Attraction along edges
    for (const edge of edges) {
      const a = nodeMap.get(edge.source);
      const b = nodeMap.get(edge.target);
      if (!a || !b || a.id === b.id) continue;
      const dx = (b.x ?? 0) - (a.x ?? 0);
      const dy = (b.y ?? 0) - (a.y ?? 0);
      const dist = Math.max(Math.sqrt(dx * dx + dy * dy), 1);
      const force = (dist - 100) * 0.02 * alpha * edge.weight;
      const fx = (dx / dist) * force;
      const fy = (dy / dist) * force;
      a.vx = (a.vx ?? 0) + fx;
      a.vy = (a.vy ?? 0) + fy;
      b.vx = (b.vx ?? 0) - fx;
      b.vy = (b.vy ?? 0) - fy;
    }

    // Apply velocities
    for (const node of nodes) {
      node.x = (node.x ?? 0) + (node.vx ?? 0) * 0.3;
      node.y = (node.y ?? 0) + (node.vy ?? 0) * 0.3;
      node.vx = (node.vx ?? 0) * 0.8;
      node.vy = (node.vy ?? 0) * 0.8;
    }
  }

  return nodes;
}

/* ── Component ───────────────────────────────────────── */

export function KnowledgeGraph({
  nodes: rawNodes,
  edges,
  width = 600,
  height = 400,
}: KnowledgeGraphProps) {
  const [positioned, setPositioned] = useState<GraphNode[]>([]);
  const [hoveredNode, setHoveredNode] = useState<string | null>(null);

  useEffect(() => {
    if (rawNodes.length === 0) return;
    const init = initPositions([...rawNodes], width, height);
    const result = simulate(init, edges);
    setPositioned(result);
  }, [rawNodes, edges, width, height]);

  if (positioned.length === 0) {
    return (
      <div className="flex items-center justify-center" style={{ width, height }}>
        <p className="text-text-muted text-sm">暂无图谱数据</p>
      </div>
    );
  }

  const nodeMap = new Map(positioned.map((n) => [n.id, n]));

  return (
    <svg width={width} height={height} className="select-none">
      {/* Edges */}
      {edges.map((edge, i) => {
        const a = nodeMap.get(edge.source);
        const b = nodeMap.get(edge.target);
        if (!a || !b || a.id === b.id) return null;
        const isHighlighted =
          hoveredNode === edge.source || hoveredNode === edge.target;
        return (
          <line
            key={`e-${i}`}
            x1={a.x} y1={a.y} x2={b.x} y2={b.y}
            stroke={isHighlighted ? "#6366f1" : "#374151"}
            strokeWidth={isHighlighted ? 2 : 1}
            strokeOpacity={isHighlighted ? 0.8 : 0.3}
          />
        );
      })}

      {/* Nodes */}
      {positioned.map((node) => {
        const color = TYPE_COLORS[node.type] ?? "#6B7280";
        const isHovered = hoveredNode === node.id;
        return (
          <g
            key={node.id}
            onMouseEnter={() => setHoveredNode(node.id)}
            onMouseLeave={() => setHoveredNode(null)}
            className="cursor-pointer"
          >
            <circle
              cx={node.x} cy={node.y}
              r={isHovered ? node.size * 0.6 : node.size * 0.5}
              fill={color}
              fillOpacity={isHovered ? 0.9 : 0.6}
              stroke={color}
              strokeWidth={isHovered ? 2 : 1}
            />
            <text
              x={node.x} y={(node.y ?? 0) + node.size * 0.5 + 14}
              textAnchor="middle"
              fill="#9CA3AF"
              fontSize={isHovered ? 12 : 10}
              fontWeight={isHovered ? 600 : 400}
            >
              {node.label}
            </text>
          </g>
        );
      })}
    </svg>
  );
}
