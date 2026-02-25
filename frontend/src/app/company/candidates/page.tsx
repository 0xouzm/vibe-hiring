"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";
import type { CompanyMatchResponse, DimensionScores } from "@/lib/types";
import { useAuth } from "@/hooks/useAuth";
import {
  DIMENSIONS,
  DIMENSION_LABELS,
  DIMENSION_COLORS,
  type DimensionKey,
} from "@/lib/constants";
import { Card, CardHeader, CardContent } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";

/* -- Matched Candidates Page ------------------------------------------ */

export default function CandidatesPage() {
  const { user } = useAuth();
  const router = useRouter();
  const [matches, setMatches] = useState<CompanyMatchResponse[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const companyId = user?.company_id;

  useEffect(() => {
    if (!companyId) return;
    api
      .get<CompanyMatchResponse[]>(`/companies/${companyId}/matches`)
      .then(setMatches)
      .catch(() =>
        setError("加载匹配失败，请稍后重试。"),
      )
      .finally(() => setLoading(false));
  }, [companyId]);

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
        <p className="text-rose text-sm">{error}</p>
        <Button variant="secondary" onClick={() => window.location.reload()}>
          重试
        </Button>
      </div>
    );
  }

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold font-display text-text">
          匹配候选人
        </h1>
        <p className="text-sm text-text-dim mt-1">
          共 {matches.length} 位候选人与你的企业文化匹配
        </p>
      </div>

      {matches.length === 0 ? (
        <EmptyState />
      ) : (
        <div className="grid gap-4">
          {matches.map((match, index) => (
            <CandidateCard
              key={match.id}
              match={match}
              index={index + 1}
              onViewReport={() =>
                router.push(`/company/candidates/${match.id}`)
              }
            />
          ))}
        </div>
      )}
    </div>
  );
}

/* -- Empty state ------------------------------------------------------ */

function EmptyState() {
  return (
    <Card>
      <CardContent className="py-12 text-center">
        <p className="text-text-dim text-sm mb-2">
          暂无匹配候选人。
        </p>
        <p className="text-text-muted text-xs">
          匹配结果在每周推荐周期中生成，请确保企业 DNA 测评已完成。
        </p>
      </CardContent>
    </Card>
  );
}

/* -- Candidate match card --------------------------------------------- */

function CandidateCard({
  match,
  index,
  onViewReport,
}: {
  match: CompanyMatchResponse;
  index: number;
  onViewReport: () => void;
}) {
  const scorePct = Math.round(match.score);
  const scoreVariant: "success" | "warning" | "danger" =
    scorePct >= 80 ? "success" : scorePct >= 60 ? "warning" : "danger";

  return (
    <Card>
      <CardContent className="py-5">
        <div className="flex items-start justify-between gap-4">
          {/* Left: candidate info */}
          <div className="flex-1">
            <div className="flex items-center gap-3 mb-3">
              <div className="w-10 h-10 rounded-full bg-indigo/10 flex items-center justify-center text-indigo font-bold text-sm">
                #{index}
              </div>
              <div>
                <h3 className="text-base font-semibold text-text">
                  候选人 #{index}
                </h3>
                <Badge variant={scoreVariant}>
                  {scorePct}% 匹配
                </Badge>
              </div>
            </div>

            {/* Mini dimension comparison */}
            <MiniDimensions scores={match.dimension_scores} />
          </div>

          {/* Right: action */}
          <div className="shrink-0 flex flex-col items-end gap-2">
            <StatusBadge status={match.status} />
            <Button variant="secondary" size="sm" onClick={onViewReport}>
              查看报告
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

/* -- Status badge ----------------------------------------------------- */

function StatusBadge({ status }: { status: string }) {
  const variants: Record<string, "success" | "warning" | "danger"> = {
    accepted: "success",
    pending: "warning",
    passed: "danger",
  };
  const labels: Record<string, string> = {
    accepted: "已接受",
    pending: "待处理",
    passed: "已跳过",
  };

  return (
    <Badge variant={variants[status] ?? "warning"}>
      {labels[status] ?? status}
    </Badge>
  );
}

/* -- Mini dimension bars ---------------------------------------------- */

function MiniDimensions({
  scores,
}: {
  scores: DimensionScores;
}) {
  return (
    <div className="grid grid-cols-4 gap-x-4 gap-y-2">
      {DIMENSIONS.map((dim) => {
        const value = scores[dim] ?? 0;
        const color = DIMENSION_COLORS[dim as DimensionKey];
        return (
          <div key={dim}>
            <div className="flex items-center justify-between mb-0.5">
              <span className="text-[10px] text-text-muted truncate">
                {DIMENSION_LABELS[dim as DimensionKey]}
              </span>
              <span
                className="text-[10px] font-semibold"
                style={{ color }}
              >
                {value}
              </span>
            </div>
            <div className="h-1 w-full rounded-full bg-surface-light overflow-hidden">
              <div
                className="h-full rounded-full transition-all duration-500"
                style={{
                  width: `${value}%`,
                  backgroundColor: color,
                }}
              />
            </div>
          </div>
        );
      })}
    </div>
  );
}
