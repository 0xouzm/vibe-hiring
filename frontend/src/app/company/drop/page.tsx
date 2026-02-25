"use client";

import { useState, useEffect, useCallback, useMemo } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";
import { useAuth } from "@/hooks/useAuth";
import type { CompanyDropResponse, CompanyMatchResponse } from "@/lib/types";
import { MATCH_STATUS_LABELS, DIMENSION_LABELS, type DimensionKey } from "@/lib/constants";
import { Card, CardContent } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { Badge } from "@/components/ui/Badge";

/* ── Company Weekly Drop Page ─────────────────────────────────────── */

export default function CompanyDropPage() {
  const router = useRouter();
  const { user } = useAuth();
  const [drop, setDrop] = useState<CompanyDropResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [actionLoading, setActionLoading] = useState<string | null>(null);

  useEffect(() => {
    api
      .getCompanyDrop()
      .then(setDrop)
      .catch(() => setError("加载每周推荐失败，请稍后再试。"))
      .finally(() => setLoading(false));
  }, []);

  const handleAction = useCallback(
    async (matchId: string, action: "accept" | "pass") => {
      setActionLoading(matchId);
      try {
        const updated = await api.companyAction(matchId, action);
        setDrop((prev) => {
          if (!prev) return prev;
          return {
            ...prev,
            matches: prev.matches.map((m) =>
              m.id === matchId
                ? { ...m, status: updated.status, company_action: action }
                : m,
            ),
          };
        });
      } catch {
        /* 静默处理，保持当前状态 */
      } finally {
        setActionLoading(null);
      }
    },
    [],
  );

  const groupedByRole = useMemo(() => {
    if (!drop) return new Map<string, CompanyMatchResponse[]>();
    const map = new Map<string, CompanyMatchResponse[]>();
    for (const match of drop.matches) {
      const key = match.role_title || "未指定岗位";
      const list = map.get(key) || [];
      list.push(match);
      map.set(key, list);
    }
    return map;
  }, [drop]);

  if (loading) return <LoadingState />;
  if (error) return <ErrorState message={error} />;
  if (!drop || drop.matches.length === 0) return <EmptyState />;

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold font-display text-text">每周人才推荐</h1>
        <p className="text-sm text-text-dim mt-1">
          {drop.week} — 共推荐 {drop.matches.length} 位候选人
        </p>
      </div>
      <div className="space-y-10">
        {[...groupedByRole.entries()].map(([roleTitle, matches]) => (
          <RoleSection
            key={roleTitle}
            roleTitle={roleTitle}
            matches={matches}
            actionLoading={actionLoading}
            onAction={handleAction}
            onView={(id) => router.push(`/company/match/${id}`)}
          />
        ))}
      </div>
    </div>
  );
}

/* ── Role Section ─────────────────────────────────────────────────── */

function RoleSection({
  roleTitle, matches, actionLoading, onAction, onView,
}: {
  roleTitle: string;
  matches: CompanyMatchResponse[];
  actionLoading: string | null;
  onAction: (id: string, action: "accept" | "pass") => void;
  onView: (id: string) => void;
}) {
  return (
    <section>
      <h2 className="text-lg font-semibold font-display text-text mb-4">
        {roleTitle}
        <span className="ml-2 text-sm font-normal text-text-dim">
          ({matches.length} 位候选人)
        </span>
      </h2>
      <div className="grid gap-4">
        {matches.map((match) => (
          <MatchCard
            key={match.id}
            match={match}
            isActionLoading={actionLoading === match.id}
            onAction={(action) => onAction(match.id, action)}
            onView={() => onView(match.id)}
          />
        ))}
      </div>
    </section>
  );
}

/* ── Match Card ───────────────────────────────────────────────────── */

function MatchCard({
  match, isActionLoading, onAction, onView,
}: {
  match: CompanyMatchResponse;
  isActionLoading: boolean;
  onAction: (action: "accept" | "pass") => void;
  onView: () => void;
}) {
  const scorePct = Math.round(match.score);
  const isMutual = match.status === "mutual";
  const hasActed = match.company_action === "accept" || match.company_action === "pass";
  const scoreVariant = scorePct >= 80 ? "success" : scorePct >= 60 ? "warning" : "danger";
  const statusLabel = MATCH_STATUS_LABELS[match.status] || match.status;

  return (
    <Card className={`hover:shadow-md transition-shadow ${isMutual ? "ring-1 ring-emerald/40" : ""}`}>
      <CardContent>
        {isMutual && <MutualBanner />}
        <div className="flex items-center justify-between gap-6">
          {/* 左侧：候选人信息 + 维度条 */}
          <div className="flex-1 min-w-0">
            <div className="flex items-center gap-3">
              <h3 className="text-lg font-semibold font-display text-text truncate">
                {match.candidate_name}
              </h3>
              <StatusBadge status={match.status} label={statusLabel} />
            </div>
            <div className="mt-3 grid grid-cols-4 gap-x-4 gap-y-2">
              {(Object.entries(match.dimension_scores) as [DimensionKey, number][])
                .slice(0, 8)
                .map(([dim, val]) => (
                  <MiniDimBar key={dim} dim={dim} value={val} />
                ))}
            </div>
          </div>
          {/* 右侧：匹配分数 + 操作按钮 */}
          <div className="flex flex-col items-center gap-3 shrink-0">
            <div className="text-center">
              <div className="text-4xl font-bold font-display text-indigo">{scorePct}%</div>
              <Badge variant={scoreVariant} className="mt-1">
                {scorePct >= 80 ? "高度匹配" : scorePct >= 60 ? "良好匹配" : "部分匹配"}
              </Badge>
            </div>
            <div className="flex flex-col gap-2 w-full">
              <Button size="sm" variant="secondary" onClick={onView}>查看详情</Button>
              {!hasActed && (
                <div className="flex gap-2">
                  <Button size="sm" loading={isActionLoading} onClick={() => onAction("accept")}>
                    接受
                  </Button>
                  <Button size="sm" variant="ghost" loading={isActionLoading} onClick={() => onAction("pass")}>
                    跳过
                  </Button>
                </div>
              )}
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

/* ── Sub-components ───────────────────────────────────────────────── */

function StatusBadge({ status, label }: { status: string; label: string }) {
  const variant = status === "mutual" ? "success" : status === "passed" ? "danger" : "default";
  return <Badge variant={variant}>{label}</Badge>;
}

function MutualBanner() {
  return (
    <div className="flex items-center gap-2 mb-3 px-3 py-2 rounded-lg bg-emerald/10 text-emerald text-sm font-medium">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M12 3l1.912 5.813a2 2 0 001.275 1.275L21 12l-5.813 1.912a2 2 0 00-1.275 1.275L12 21l-1.912-5.813a2 2 0 00-1.275-1.275L3 12l5.813-1.912a2 2 0 001.275-1.275L12 3z" />
      </svg>
      双向匹配成功！双方都接受了这次匹配。
    </div>
  );
}

function MiniDimBar({ dim, value }: { dim: DimensionKey; value: number }) {
  return (
    <div>
      <span className="text-[10px] text-text-muted uppercase">{DIMENSION_LABELS[dim] || dim}</span>
      <div className="h-1.5 w-full rounded-full bg-surface-light overflow-hidden mt-0.5">
        <div className="h-full rounded-full bg-indigo/60" style={{ width: `${Math.round(value)}%` }} />
      </div>
    </div>
  );
}

/* ── State screens ────────────────────────────────────────────────── */

function LoadingState() {
  return (
    <div className="flex items-center justify-center min-h-[60vh]">
      <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
    </div>
  );
}

function ErrorState({ message }: { message: string }) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4">
      <p className="text-text-dim text-sm">{message}</p>
      <Button variant="secondary" onClick={() => window.location.reload()}>重试</Button>
    </div>
  );
}

function EmptyState() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] text-center">
      <div className="w-16 h-16 rounded-full bg-surface-light flex items-center justify-center mb-6">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="text-text-muted">
          <path d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4-4v2" />
          <circle cx="9" cy="7" r="4" />
          <path d="M22 21v-2a4 4 0 00-3-3.87" />
          <path d="M16 3.13a4 4 0 010 7.75" />
        </svg>
      </div>
      <h2 className="text-xl font-bold font-display text-text mb-2">暂无人才推荐</h2>
      <p className="text-sm text-text-dim max-w-sm">
        下一次每周人才推荐将于周二晚 9 点送达。请确保企业文化 DNA 测评已完成并发布了岗位，以便接收匹配。
      </p>
    </div>
  );
}
