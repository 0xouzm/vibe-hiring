"use client";

import { useState, useEffect } from "react";
import { api } from "@/lib/api";
import { Card, CardHeader, CardContent } from "@/components/ui/Card";
import { KnowledgeGraph } from "@/components/charts/KnowledgeGraph";
import { MatchFunnel } from "@/components/charts/MatchFunnel";
import { DimensionCompare } from "@/components/charts/DimensionCompare";

/* ── Types ───────────────────────────────────────────── */

interface GraphData {
  nodes: Array<{
    id: string;
    label: string;
    type: string;
    size: number;
  }>;
  edges: Array<{
    source: string;
    target: string;
    weight: number;
    type?: string;
  }>;
}

interface PipelineData {
  funnel: { total_candidates: number; l1_passed: number; l2_top: number };
  dimensions: {
    candidate: Record<string, number>;
    company: Record<string, number>;
    compatibility: Record<string, number>;
  };
  formula: { consistency: number; raw_average: number; final_score: number };
}

/* ── Tab Selector ────────────────────────────────────── */

type TabKey = "graph" | "pipeline";

const TABS: { key: TabKey; label: string }[] = [
  { key: "graph", label: "知识图谱" },
  { key: "pipeline", label: "匹配过程" },
];

/* ── Main Component ──────────────────────────────────── */

export function MatchVisualization({ matchId }: { matchId: string }) {
  const [activeTab, setActiveTab] = useState<TabKey>("graph");
  const [graphData, setGraphData] = useState<GraphData | null>(null);
  const [pipelineData, setPipelineData] = useState<PipelineData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      api.get<GraphData>(`/graph/match/${matchId}`).catch(() => null),
      api.get<PipelineData>(`/graph/pipeline/${matchId}`).catch(() => null),
    ]).then(([g, p]) => {
      setGraphData(g);
      setPipelineData(p);
      setLoading(false);
    });
  }, [matchId]);

  if (loading) {
    return (
      <Card className="mb-6">
        <CardContent>
          <div className="flex items-center justify-center h-32">
            <div className="w-6 h-6 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="mb-6">
      <CardHeader>
        {/* Tab bar */}
        <div className="flex gap-1 bg-surface-light rounded-[var(--radius-lg)] p-1">
          {TABS.map((tab) => (
            <button
              key={tab.key}
              onClick={() => setActiveTab(tab.key)}
              className={[
                "px-4 py-1.5 rounded-[var(--radius-md)] text-sm font-medium transition-colors cursor-pointer",
                activeTab === tab.key
                  ? "bg-indigo/20 text-indigo"
                  : "text-text-dim hover:text-text",
              ].join(" ")}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </CardHeader>
      <CardContent>
        {activeTab === "graph" && <GraphTab data={graphData} />}
        {activeTab === "pipeline" && <PipelineTab data={pipelineData} />}
      </CardContent>
    </Card>
  );
}

/* ── Graph Tab ───────────────────────────────────────── */

function GraphTab({ data }: { data: GraphData | null }) {
  if (!data || data.nodes.length === 0) {
    return <EmptyState text="暂无知识图谱数据" />;
  }

  return (
    <div className="flex flex-col items-center">
      <KnowledgeGraph
        nodes={data.nodes as never}
        edges={data.edges as never}
        width={560}
        height={380}
      />
      <Legend />
    </div>
  );
}

/* ── Pipeline Tab ────────────────────────────────────── */

function PipelineTab({ data }: { data: PipelineData | null }) {
  if (!data) {
    return <EmptyState text="暂无匹配流程数据" />;
  }

  return (
    <div className="space-y-6">
      {/* Funnel */}
      <div className="flex justify-center">
        <MatchFunnel funnel={data.funnel} width={440} height={200} />
      </div>

      {/* Dimension comparison */}
      <div>
        <h3 className="text-sm font-semibold text-text-dim mb-3">
          维度级对比
        </h3>
        <DimensionCompare
          candidate={data.dimensions.candidate}
          company={data.dimensions.company}
          compatibility={data.dimensions.compatibility}
          width={520}
        />
      </div>

      {/* Score formula */}
      <div className="bg-surface-light rounded-[var(--radius-lg)] p-4">
        <h3 className="text-sm font-semibold text-text-dim mb-2">
          评分公式
        </h3>
        <p className="text-xs text-text-muted font-mono">
          最终分数 = 维度均值 × 一致性系数
        </p>
        <p className="text-sm text-text mt-1 font-mono">
          <span className="text-indigo">{data.formula.raw_average}</span>
          {" × "}
          <span className="text-amber-400">{data.formula.consistency}</span>
          {" = "}
          <span className="text-emerald font-bold">{data.formula.final_score}</span>
        </p>
      </div>
    </div>
  );
}

/* ── Legend ───────────────────────────────────────────── */

function Legend() {
  const items = [
    { color: "#6366f1", label: "候选人" },
    { color: "#F97316", label: "公司" },
    { color: "#F59E0B", label: "岗位" },
    { color: "#10B981", label: "技能" },
    { color: "#8B5CF6", label: "DNA 维度" },
  ];
  return (
    <div className="flex flex-wrap gap-3 mt-4 justify-center">
      {items.map((item) => (
        <div key={item.label} className="flex items-center gap-1.5">
          <span className="w-3 h-3 rounded-full" style={{ backgroundColor: item.color }} />
          <span className="text-xs text-text-dim">{item.label}</span>
        </div>
      ))}
    </div>
  );
}

/* ── Empty State ─────────────────────────────────────── */

function EmptyState({ text }: { text: string }) {
  return (
    <div className="flex items-center justify-center h-48">
      <p className="text-text-muted text-sm">{text}</p>
    </div>
  );
}
