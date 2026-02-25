"use client";

import { useState, useEffect, use } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";
import { useAuth } from "@/hooks/useAuth";
import type { MatchResponse, DNAScoreResponse } from "@/lib/types";
import { RadarChart } from "@/components/charts/RadarChart";
import { Card, CardHeader, CardContent } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";

/* ── Match Report Detail Page ──────────────────────────────────────── */

export default function MatchReportPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = use(params);
  const router = useRouter();
  const { user } = useAuth();
  const [match, setMatch] = useState<MatchResponse | null>(null);
  const [candidateDna, setCandidateDna] = useState<DNAScoreResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [actionState, setActionState] = useState<"idle" | "accepted" | "passed">("idle");

  useEffect(() => {
    const loadData = async () => {
      try {
        const [matchData, dnaData] = await Promise.all([
          api.get<MatchResponse>(`/matching/results/${id}`),
          user ? api.get<DNAScoreResponse>(`/scores/candidate/${user.id}`) : null,
        ]);
        setMatch(matchData);
        if (dnaData) setCandidateDna(dnaData);
      } catch {
        setError("加载匹配报告失败。");
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, [id, user]);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (error || !match) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4">
        <p className="text-text-dim text-sm">{error ?? "未找到匹配。"}</p>
        <Button variant="secondary" onClick={() => router.push("/candidate/drop")}>
          返回推荐页
        </Button>
      </div>
    );
  }

  const scorePct = Math.round(match.score);
  const scoreVariant =
    scorePct >= 80 ? "success" : scorePct >= 60 ? "warning" : "danger";

  const handleAction = async (action: "accept" | "pass") => {
    try {
      await api.post(`/matching/results/${id}/action`, { action });
      setActionState(action === "accept" ? "accepted" : "passed");
      if (action === "pass") {
        setTimeout(() => router.push("/candidate/drop"), 1200);
      }
    } catch {
      // silently fail for demo
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      {/* ── Header ─────────────────────────────────────── */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <button
            onClick={() => router.push("/candidate/drop")}
            className="text-sm text-text-dim hover:text-text mb-2 flex items-center gap-1 cursor-pointer"
          >
            <BackArrow /> 返回推荐页
          </button>
          <h1 className="text-2xl font-bold font-display text-text">
            {match.company_name}
          </h1>
        </div>
        <div className="text-center">
          <div className="text-5xl font-bold font-display text-indigo">
            {scorePct}%
          </div>
          <Badge variant={scoreVariant} className="mt-1">
            {scorePct >= 80
              ? "高度匹配"
              : scorePct >= 60
                ? "良好匹配"
                : "部分匹配"}
          </Badge>
        </div>
      </div>

      {/* ── Radar comparison ───────────────────────────── */}
      {candidateDna && (
        <Card className="mb-6">
          <CardHeader>
            <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
              DNA 对比
            </h2>
            <div className="flex gap-4 mt-2">
              <Legend color="#6366f1" label="你的 DNA" />
              <Legend color="#F97316" label={match.company_name} />
            </div>
          </CardHeader>
          <CardContent className="flex items-center justify-center">
            <RadarChart
              scores={candidateDna.scores}
              compareScores={match.dimension_scores}
              size={360}
            />
          </CardContent>
        </Card>
      )}

      {/* ── Report ─────────────────────────────────────── */}
      {match.report && (
        <Card className="mb-6">
          <CardHeader>
            <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
              匹配报告
            </h2>
          </CardHeader>
          <CardContent>
            <SimpleMarkdown text={match.report} />
          </CardContent>
        </Card>
      )}

      {/* ── Action buttons ─────────────────────────────── */}
      <ActionSection
        actionState={actionState}
        onAccept={() => handleAction("accept")}
        onPass={() => handleAction("pass")}
      />
    </div>
  );
}

/* ── Action section ────────────────────────────────────────────────── */

function ActionSection({
  actionState,
  onAccept,
  onPass,
}: {
  actionState: "idle" | "accepted" | "passed";
  onAccept: () => void;
  onPass: () => void;
}) {
  if (actionState === "accepted") {
    return (
      <div className="text-center py-8">
        <div className="w-12 h-12 rounded-full bg-emerald/10 flex items-center justify-center mx-auto mb-3">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10B981" strokeWidth="2">
            <path d="M20 6L9 17l-5-5" />
          </svg>
        </div>
        <p className="text-lg font-semibold text-emerald">
          连接请求已发送！
        </p>
        <p className="text-sm text-text-dim mt-1">
          企业将收到你的意向通知。
        </p>
      </div>
    );
  }

  if (actionState === "passed") {
    return (
      <div className="text-center py-8">
        <p className="text-sm text-text-dim">正在返回推荐页...</p>
      </div>
    );
  }

  return (
    <div className="flex items-center justify-center gap-4 py-8">
      <Button variant="secondary" size="lg" onClick={onPass}>
        跳过
      </Button>
      <Button size="lg" onClick={onAccept}>
        接受匹配
      </Button>
    </div>
  );
}

/* ── Simple markdown renderer ──────────────────────────────────────── */

function SimpleMarkdown({ text }: { text: string }) {
  const lines = text.split("\n");

  return (
    <div className="prose-sm space-y-2">
      {lines.map((line, i) => {
        const trimmed = line.trim();
        if (!trimmed) return <div key={i} className="h-2" />;
        if (trimmed.startsWith("### "))
          return (
            <h4 key={i} className="text-sm font-bold text-text mt-4 mb-1">
              {trimmed.slice(4)}
            </h4>
          );
        if (trimmed.startsWith("## "))
          return (
            <h3 key={i} className="text-base font-bold font-display text-text mt-4 mb-1">
              {trimmed.slice(3)}
            </h3>
          );
        if (trimmed.startsWith("# "))
          return (
            <h2 key={i} className="text-lg font-bold font-display text-text mt-4 mb-1">
              {trimmed.slice(2)}
            </h2>
          );
        if (trimmed.startsWith("- ") || trimmed.startsWith("* "))
          return (
            <li key={i} className="text-sm text-text-dim ml-4 list-disc">
              {renderInline(trimmed.slice(2))}
            </li>
          );
        return (
          <p key={i} className="text-sm text-text-dim leading-relaxed">
            {renderInline(trimmed)}
          </p>
        );
      })}
    </div>
  );
}

function renderInline(text: string) {
  // Simple bold: **text**
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  return parts.map((part, i) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return (
        <strong key={i} className="font-semibold text-text">
          {part.slice(2, -2)}
        </strong>
      );
    }
    return part;
  });
}

/* ── Small icons ───────────────────────────────────────────────────── */

function BackArrow() {
  return (
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M19 12H5M12 19l-7-7 7-7" />
    </svg>
  );
}

function Legend({ color, label }: { color: string; label: string }) {
  return (
    <div className="flex items-center gap-1.5">
      <span
        className="w-3 h-3 rounded-full"
        style={{ backgroundColor: color }}
      />
      <span className="text-xs text-text-dim">{label}</span>
    </div>
  );
}
