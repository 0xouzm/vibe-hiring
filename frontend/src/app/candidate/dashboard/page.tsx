"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";
import type { DNAScoreResponse } from "@/lib/types";
import { useAuth } from "@/hooks/useAuth";
import {
  DIMENSIONS,
  DIMENSION_LABELS,
  DIMENSION_SPECTRUM,
  DIMENSION_COLORS,
  type DimensionKey,
} from "@/lib/constants";
import { RadarChart } from "@/components/charts/RadarChart";
import { Card, CardHeader, CardContent } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";

/* ── Candidate Dashboard ───────────────────────────────────────────── */

export default function CandidateDashboard() {
  const { user } = useAuth();
  const router = useRouter();
  const [dna, setDna] = useState<DNAScoreResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!user) return;
    api
      .get<DNAScoreResponse>(`/scores/candidate/${user.id}`)
      .then(setDna)
      .catch(() => setError("未找到 DNA 画像，请先完成问卷测评。"))
      .finally(() => setLoading(false));
  }, [user]);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (error || !dna) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4">
        <p className="text-text-dim text-sm">{error ?? "暂无 DNA 数据。"}</p>
        <Button onClick={() => router.push("/candidate/questionnaire")}>
          开始测评
        </Button>
      </div>
    );
  }

  const consistencyPct = Math.round(dna.consistency * 100);
  const consistencyVariant =
    consistencyPct >= 85 ? "success" : consistencyPct >= 70 ? "warning" : "danger";

  return (
    <div>
      {/* Page title */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold font-display text-text">
            你的职业 DNA
          </h1>
          <p className="text-sm text-text-dim mt-1">
            基于问卷回答的 8 维度行为画像
          </p>
        </div>
        <Badge variant={consistencyVariant}>
          一致性：{consistencyPct}%
        </Badge>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Radar chart */}
        <Card>
          <CardHeader>
            <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
              DNA 概览
            </h2>
          </CardHeader>
          <CardContent className="flex items-center justify-center pb-6">
            <RadarChart scores={dna.scores} size={320} />
          </CardContent>
        </Card>

        {/* Dimension list */}
        <Card>
          <CardHeader>
            <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
              维度详情
            </h2>
          </CardHeader>
          <CardContent>
            <div className="grid gap-4">
              {DIMENSIONS.map((dim) => (
                <DimensionRow
                  key={dim}
                  dim={dim}
                  value={dna.scores[dim]}
                />
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      {/* CTA */}
      <div className="mt-8 text-center">
        <Button size="lg" onClick={() => router.push("/candidate/drop")}>
          查看每周推荐
        </Button>
      </div>
    </div>
  );
}

/* ── Dimension row with spectrum labels ────────────────────────────── */

function DimensionRow({ dim, value }: { dim: DimensionKey; value: number }) {
  const [low, high] = DIMENSION_SPECTRUM[dim];
  const color = DIMENSION_COLORS[dim];

  return (
    <div>
      <div className="flex items-center justify-between mb-1">
        <span className="text-sm font-medium text-text">
          {DIMENSION_LABELS[dim]}
        </span>
        <span className="text-sm font-bold" style={{ color }}>
          {value}
        </span>
      </div>
      <div className="h-2 w-full rounded-full bg-surface-light overflow-hidden">
        <div
          className="h-full rounded-full transition-all duration-700 ease-out"
          style={{ width: `${value}%`, backgroundColor: color }}
        />
      </div>
      <div className="flex items-center justify-between mt-0.5">
        <span className="text-[10px] text-text-muted">{low}</span>
        <span className="text-[10px] text-text-muted">{high}</span>
      </div>
    </div>
  );
}
