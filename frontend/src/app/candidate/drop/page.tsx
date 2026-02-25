"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";
import type { DropResponse, MatchResponse } from "@/lib/types";
import { Card, CardContent } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";

/* ── Weekly Drop Page ──────────────────────────────────────────────── */

export default function WeeklyDropPage() {
  const router = useRouter();
  const [drop, setDrop] = useState<DropResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api
      .get<DropResponse>("/drops/current")
      .then(setDrop)
      .catch(() => setError("加载每周推荐失败。"))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4">
        <p className="text-text-dim text-sm">{error}</p>
        <Button variant="secondary" onClick={() => window.location.reload()}>
          重试
        </Button>
      </div>
    );
  }

  if (!drop || drop.matches.length === 0) {
    return <EmptyDropState />;
  }

  return (
    <div>
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-2xl font-bold font-display text-text">
          每周匹配推荐
        </h1>
        <p className="text-sm text-text-dim mt-1">
          {drop.week} — 共找到 {drop.matches.length} 个匹配
        </p>
      </div>

      {/* Match cards */}
      <div className="grid gap-6">
        {drop.matches.slice(0, 3).map((match) => (
          <MatchCard
            key={match.id}
            match={match}
            onViewReport={() => router.push(`/candidate/match/${match.id}`)}
          />
        ))}
      </div>
    </div>
  );
}

/* ── Match preview card ────────────────────────────────────────────── */

function MatchCard({
  match,
  onViewReport,
}: {
  match: MatchResponse;
  onViewReport: () => void;
}) {
  const scorePct = Math.round(match.score);
  const scoreVariant =
    scorePct >= 80 ? "success" : scorePct >= 60 ? "warning" : "danger";

  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardContent>
        <div className="flex items-center justify-between">
          {/* Left: company info */}
          <div className="flex-1">
            <h3 className="text-lg font-semibold font-display text-text">
              {match.company_name}
            </h3>

            {/* Mini dimension bars */}
            <div className="mt-3 grid grid-cols-4 gap-x-4 gap-y-2">
              {(Object.entries(match.dimension_scores) as [string, number][])
                .slice(0, 8)
                .map(([dim, val]) => (
                  <MiniDimBar key={dim} label={dim} value={val as number} />
                ))}
            </div>
          </div>

          {/* Right: score + CTA */}
          <div className="flex flex-col items-center gap-3 ml-8">
            <div className="text-center">
              <div className="text-4xl font-bold font-display text-indigo">
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
            <Button size="sm" onClick={onViewReport}>
              查看报告
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

/* ── Mini dimension bar ────────────────────────────────────────────── */

function MiniDimBar({ label, value }: { label: string; value: number }) {
  return (
    <div>
      <span className="text-[10px] text-text-muted uppercase">{label}</span>
      <div className="h-1.5 w-full rounded-full bg-surface-light overflow-hidden mt-0.5">
        <div
          className="h-full rounded-full bg-indigo/60"
          style={{ width: `${Math.round(value)}%` }}
        />
      </div>
    </div>
  );
}

/* ── Empty state ───────────────────────────────────────────────────── */

function EmptyDropState() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] text-center">
      <div className="w-16 h-16 rounded-full bg-surface-light flex items-center justify-center mb-6">
        <svg
          width="32"
          height="32"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.5"
          className="text-text-muted"
        >
          <path d="M12 3l1.912 5.813a2 2 0 001.275 1.275L21 12l-5.813 1.912a2 2 0 00-1.275 1.275L12 21l-1.912-5.813a2 2 0 00-1.275-1.275L3 12l5.813-1.912a2 2 0 001.275-1.275L12 3z" />
        </svg>
      </div>
      <h2 className="text-xl font-bold font-display text-text mb-2">
        暂无推荐
      </h2>
      <p className="text-sm text-text-dim max-w-sm">
        下一次每周推荐将于周二晚 9 点送达。
        请确保你的职业 DNA 测评已完成，以便接收匹配。
      </p>
    </div>
  );
}
