"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";
import type { DNAScoreResponse, CASResponse } from "@/lib/types";
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

/* -- CAS tier badge variant mapping ----------------------------------- */

function casTierVariant(tier: string): "success" | "warning" | "danger" {
  if (tier === "gold") return "success";
  if (tier === "silver") return "warning";
  return "danger";
}

function casTierLabel(tier: string): string {
  const labels: Record<string, string> = {
    gold: "Gold",
    silver: "Silver",
    bronze: "Bronze",
    none: "N/A",
  };
  return labels[tier] ?? tier;
}

/* -- Company Dashboard ------------------------------------------------ */

export default function CompanyDashboard() {
  const { user } = useAuth();
  const router = useRouter();
  const [dna, setDna] = useState<DNAScoreResponse | null>(null);
  const [cas, setCas] = useState<CASResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!user?.company_id) return;

    const companyId = user.company_id;

    Promise.all([
      api
        .get<DNAScoreResponse>(`/scores/company/${companyId}`)
        .catch(() => null),
      api
        .get<CASResponse>(`/companies/${companyId}/cas`)
        .catch(() => null),
    ])
      .then(([dnaRes, casRes]) => {
        if (!dnaRes) {
          setError(
            "No Company DNA profile found. Complete the questionnaire first.",
          );
        }
        setDna(dnaRes);
        setCas(casRes);
      })
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
        <p className="text-text-dim text-sm">{error ?? "No DNA data."}</p>
        <Button onClick={() => router.push("/company/questionnaire")}>
          Take Company DNA Assessment
        </Button>
      </div>
    );
  }

  return (
    <div>
      {/* Page title + CAS badge */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold font-display text-text">
            Company DNA
          </h1>
          <p className="text-sm text-text-dim mt-1">
            Aggregated culture profile based on team responses
          </p>
        </div>
        {cas && cas.tier !== "none" && (
          <Badge variant={casTierVariant(cas.tier)}>
            CAS: {casTierLabel(cas.tier)}
          </Badge>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Radar chart + CAS summary */}
        <div className="flex flex-col gap-6">
          <Card>
            <CardHeader>
              <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
                DNA Overview
              </h2>
            </CardHeader>
            <CardContent className="flex items-center justify-center pb-6">
              <RadarChart scores={dna.scores} size={320} />
            </CardContent>
          </Card>

          {cas && <CASCard cas={cas} />}
        </div>

        {/* Dimension breakdown */}
        <Card>
          <CardHeader>
            <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
              Dimension Breakdown
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

      {/* CTAs */}
      <div className="mt-8 flex items-center justify-center gap-4">
        <Button size="lg" onClick={() => router.push("/company/candidates")}>
          View Matched Candidates
        </Button>
        <Button
          variant="secondary"
          size="lg"
          onClick={() => router.push("/company/invite")}
        >
          Invite Team Members
        </Button>
      </div>
    </div>
  );
}

/* -- CAS score card --------------------------------------------------- */

function CASCard({ cas }: { cas: CASResponse }) {
  const scorePct = Math.round(cas.score * 100);

  return (
    <Card>
      <CardHeader>
        <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
          Culture Authenticity Score
        </h2>
      </CardHeader>
      <CardContent>
        <div className="flex items-center gap-6 mb-4">
          <div className="text-4xl font-bold font-display text-text">
            {scorePct}
          </div>
          <Badge variant={casTierVariant(cas.tier)}>
            {casTierLabel(cas.tier)} Tier
          </Badge>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="text-xs text-text-muted mb-1">
              Internal Consistency
            </p>
            <div className="h-2 w-full rounded-full bg-surface-light overflow-hidden">
              <div
                className="h-full rounded-full bg-indigo transition-all duration-700"
                style={{ width: `${Math.round(cas.internal_consistency * 100)}%` }}
              />
            </div>
            <p className="text-xs text-text-dim mt-0.5">
              {Math.round(cas.internal_consistency * 100)}%
            </p>
          </div>
          <div>
            <p className="text-xs text-text-muted mb-1">
              HR-Employee Alignment
            </p>
            <div className="h-2 w-full rounded-full bg-surface-light overflow-hidden">
              <div
                className="h-full rounded-full bg-emerald transition-all duration-700"
                style={{ width: `${Math.round(cas.hr_employee_alignment * 100)}%` }}
              />
            </div>
            <p className="text-xs text-text-dim mt-0.5">
              {Math.round(cas.hr_employee_alignment * 100)}%
            </p>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

/* -- Dimension row with spectrum labels ------------------------------- */

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
