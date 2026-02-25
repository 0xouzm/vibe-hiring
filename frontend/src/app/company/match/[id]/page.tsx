"use client";

import { useState, useEffect, use } from "react";
import { useRouter } from "next/navigation";
import { api, ApiError } from "@/lib/api";
import type { MatchResponse, UserProfile } from "@/lib/types";
import { MATCH_STATUS_LABELS, MATCH_STATUS_COLORS } from "@/lib/constants";
import { RadarChart } from "@/components/charts/RadarChart";
import { Card, CardHeader, CardContent } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { Badge } from "@/components/ui/Badge";

/* ── Company Match Detail Page ───────────────────────────────────── */

export default function CompanyMatchDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = use(params);
  const router = useRouter();
  const [match, setMatch] = useState<MatchResponse | null>(null);
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [actionLoading, setActionLoading] = useState(false);

  useEffect(() => {
    const loadData = async () => {
      try {
        const matchData = await api.get<MatchResponse>(`/matching/results/${id}`);
        setMatch(matchData);
        // 尝试获取候选人档案，404 时静默处理
        try {
          setProfile(await api.getProfile(matchData.candidate_id));
        } catch (err) {
          if (!(err instanceof ApiError && err.status === 404)) console.warn("获取候选人档案失败", err);
        }
      } catch {
        setError("加载匹配详情失败，请稍后重试。");
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, [id]);

  const handleAction = async (action: "accept" | "pass") => {
    setActionLoading(true);
    try {
      const updated = await api.companyAction(id, action);
      setMatch((prev) => prev ? { ...prev, status: updated.status, company_action: action } : prev);
    } catch { /* 静默处理 */ } finally {
      setActionLoading(false);
    }
  };

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
        <Button variant="secondary" onClick={() => router.push("/company/drop")}>返回推荐页</Button>
      </div>
    );
  }

  const scorePct = Math.round(match.score);
  const scoreVariant = scorePct >= 80 ? "success" : scorePct >= 60 ? "warning" : "danger";
  const isMutual = match.status === "mutual";
  const hasActed = match.company_action === "accept" || match.company_action === "pass";

  return (
    <div className="max-w-4xl mx-auto">
      {/* ── Header ─────────────────────────────────────── */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <button
            onClick={() => router.push("/company/drop")}
            className="text-sm text-text-dim hover:text-text mb-2 flex items-center gap-1 cursor-pointer"
          >
            <BackArrow /> 返回推荐页
          </button>
          <h1 className="text-2xl font-bold font-display text-text">
            {match.role_title || "未指定岗位"}
          </h1>
          <p className={`text-sm mt-1 ${MATCH_STATUS_COLORS[match.status] || "text-text-dim"}`}>
            {MATCH_STATUS_LABELS[match.status] || match.status}
          </p>
        </div>
        <div className="text-center">
          <div className="text-5xl font-bold font-display text-indigo">{scorePct}%</div>
          <Badge variant={scoreVariant} className="mt-1">
            {scorePct >= 80 ? "高度匹配" : scorePct >= 60 ? "良好匹配" : "部分匹配"}
          </Badge>
        </div>
      </div>

      {/* ── Mutual match banner ────────────────────────── */}
      {isMutual && (
        <div className="flex items-center gap-2 mb-6 px-4 py-3 rounded-lg bg-emerald/10 text-emerald text-sm font-medium">
          <SparkleIcon />
          双向匹配成功！候选人也接受了这次匹配。
        </div>
      )}

      {/* ── Candidate profile card ─────────────────────── */}
      {profile && <CandidateCard profile={profile} />}

      {/* ── DNA radar comparison ───────────────────────── */}
      <Card className="mb-6">
        <CardHeader>
          <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">DNA 对比</h2>
          <div className="flex gap-4 mt-2">
            <Legend color="#6366f1" label="候选人 DNA" />
            <Legend color="#F97316" label="岗位匹配维度" />
          </div>
        </CardHeader>
        <CardContent className="flex items-center justify-center">
          <RadarChart scores={match.dimension_scores} size={360} />
        </CardContent>
      </Card>

      {/* ── Report section ─────────────────────────────── */}
      {match.report && (
        <Card className="mb-6">
          <CardHeader>
            <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">匹配报告</h2>
          </CardHeader>
          <CardContent>
            <SimpleMarkdown text={match.report} />
          </CardContent>
        </Card>
      )}

      {/* ── Action buttons ─────────────────────────────── */}
      <ActionSection
        hasActed={hasActed}
        isMutual={isMutual}
        companyAction={match.company_action}
        loading={actionLoading}
        onAccept={() => handleAction("accept")}
        onPass={() => handleAction("pass")}
      />
    </div>
  );
}

/* ── Candidate Profile Card ──────────────────────────────────────── */

function CandidateCard({ profile }: { profile: UserProfile }) {
  return (
    <Card className="mb-6">
      <CardContent>
        <h3 className="text-lg font-semibold font-display text-text">候选人档案</h3>
        {profile.title && <p className="text-sm text-indigo mt-1">{profile.title}</p>}
        {profile.years_experience != null && (
          <p className="text-xs text-text-dim mt-1">{profile.years_experience} 年工作经验</p>
        )}
        {profile.skills.length > 0 && (
          <div className="flex flex-wrap gap-1.5 mt-3">
            {profile.skills.map((s) => <Badge key={s}>{s}</Badge>)}
          </div>
        )}
        {profile.bio && (
          <p className="text-sm text-text-dim mt-3 leading-relaxed">{profile.bio}</p>
        )}
      </CardContent>
    </Card>
  );
}

/* ── Action Section ──────────────────────────────────────────────── */

function ActionSection({ hasActed, isMutual, companyAction, loading, onAccept, onPass }: {
  hasActed: boolean;
  isMutual: boolean;
  companyAction?: string;
  loading: boolean;
  onAccept: () => void;
  onPass: () => void;
}) {
  if (isMutual) {
    return (
      <div className="text-center py-8">
        <p className="text-lg font-semibold text-emerald">双向匹配成功！可以开始沟通了。</p>
      </div>
    );
  }
  if (hasActed) {
    return (
      <div className="text-center py-8">
        <p className="text-sm text-text-dim">
          {companyAction === "accept" ? "已接受该候选人" : "已跳过该候选人"}
        </p>
      </div>
    );
  }
  return (
    <div className="flex items-center justify-center gap-4 py-8">
      <Button variant="ghost" size="lg" loading={loading} onClick={onPass}>跳过</Button>
      <Button size="lg" loading={loading} onClick={onAccept}>接受候选人</Button>
    </div>
  );
}

/* ── Simple Markdown Renderer ────────────────────────────────────── */

function SimpleMarkdown({ text }: { text: string }) {
  return (
    <div className="prose-sm space-y-2">
      {text.split("\n").map((line, i) => {
        const t = line.trim();
        if (!t) return <div key={i} className="h-2" />;
        if (t.startsWith("### ")) return <h4 key={i} className="text-sm font-bold text-text mt-4 mb-1">{t.slice(4)}</h4>;
        if (t.startsWith("## ")) return <h3 key={i} className="text-base font-bold font-display text-text mt-4 mb-1">{t.slice(3)}</h3>;
        if (t.startsWith("# ")) return <h2 key={i} className="text-lg font-bold font-display text-text mt-4 mb-1">{t.slice(2)}</h2>;
        if (t.startsWith("- ") || t.startsWith("* "))
          return <li key={i} className="text-sm text-text-dim ml-4 list-disc">{renderBold(t.slice(2))}</li>;
        return <p key={i} className="text-sm text-text-dim leading-relaxed">{renderBold(t)}</p>;
      })}
    </div>
  );
}

function renderBold(text: string) {
  return text.split(/(\*\*[^*]+\*\*)/g).map((part, i) =>
    part.startsWith("**") && part.endsWith("**")
      ? <strong key={i} className="font-semibold text-text">{part.slice(2, -2)}</strong>
      : part,
  );
}

/* ── Small Icons ─────────────────────────────────────────────────── */

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
      <span className="w-3 h-3 rounded-full" style={{ backgroundColor: color }} />
      <span className="text-xs text-text-dim">{label}</span>
    </div>
  );
}

function SparkleIcon() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M12 3l1.912 5.813a2 2 0 001.275 1.275L21 12l-5.813 1.912a2 2 0 00-1.275 1.275L12 21l-1.912-5.813a2 2 0 00-1.275-1.275L3 12l5.813-1.912a2 2 0 001.275-1.275L12 3z" />
    </svg>
  );
}
