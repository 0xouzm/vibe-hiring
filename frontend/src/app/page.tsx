"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { api, setToken } from "@/lib/api";
import type { TokenResponse } from "@/lib/types";
import { Button } from "@/components/ui/Button";

/* ── Seed user definitions ─────────────────────────────────────────── */

interface SeedUser {
  name: string;
  email: string;
  role: "candidate" | "hr";
  redirect: string;
}

const SEED_CANDIDATES: SeedUser[] = [
  { name: "Alex Chen", email: "alex@example.com", role: "candidate", redirect: "/candidate/dashboard" },
  { name: "Maria Santos", email: "maria@example.com", role: "candidate", redirect: "/candidate/dashboard" },
  { name: "James Wright", email: "james@example.com", role: "candidate", redirect: "/candidate/dashboard" },
  { name: "Priya Sharma", email: "priya@example.com", role: "candidate", redirect: "/candidate/dashboard" },
  { name: "David Kim", email: "david@example.com", role: "candidate", redirect: "/candidate/dashboard" },
  { name: "Sophie Zhang", email: "sophie@example.com", role: "candidate", redirect: "/candidate/dashboard" },
];

const SEED_HRS: SeedUser[] = [
  { name: "HR at Velocity Labs", email: "hr@velocity-labs.example.com", role: "hr", redirect: "/company/dashboard" },
  { name: "HR at Meridian Financial", email: "hr@meridian-financial.example.com", role: "hr", redirect: "/company/dashboard" },
  { name: "HR at Bloom Education", email: "hr@bloom-education.example.com", role: "hr", redirect: "/company/dashboard" },
];

const DEMO_PASSWORD = "demo123";

/* ── Landing Page ──────────────────────────────────────────────────── */

export default function LandingPage() {
  const router = useRouter();
  const [loading, setLoading] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleQuickLogin = async (user: SeedUser) => {
    setLoading(user.email);
    setError(null);
    try {
      const res = await api.post<TokenResponse>("/auth/login", {
        email: user.email,
        password: DEMO_PASSWORD,
      });
      setToken(res.access_token);
      localStorage.setItem("talentdrop_token", res.access_token);
      localStorage.setItem("talentdrop_user", JSON.stringify(res.user));
      router.push(user.redirect);
    } catch {
      setError(`Failed to login as ${user.name}. Is the backend running?`);
    } finally {
      setLoading(null);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-6 py-16">
      {/* ── Hero ────────────────────────────────────────── */}
      <div className="text-center max-w-2xl mb-16">
        <h1 className="text-6xl font-bold font-display text-indigo mb-4">
          TalentDrop
        </h1>
        <p className="text-xl text-text-dim leading-relaxed mb-8">
          Find where you truly belong.
        </p>
        <div className="flex gap-4 justify-center">
          <Button size="lg" onClick={() => router.push("/candidate/questionnaire")}>
            I&apos;m a Candidate
          </Button>
          <Button
            variant="secondary"
            size="lg"
            onClick={() => router.push("/company/questionnaire")}
          >
            I&apos;m Hiring
          </Button>
        </div>
      </div>

      {/* ── Decorative divider ──────────────────────────── */}
      <div className="w-full max-w-2xl border-t border-glass-border mb-12" />

      {/* ── Quick Login Section ─────────────────────────── */}
      <div className="w-full max-w-3xl">
        <h2 className="text-center text-sm font-medium text-text-dim uppercase tracking-wide mb-6">
          Demo Quick Login
        </h2>

        {error && (
          <p className="text-center text-sm text-rose mb-4">{error}</p>
        )}

        {/* Candidates */}
        <div className="mb-8">
          <h3 className="text-xs font-semibold text-text-muted uppercase tracking-wide mb-3">
            Candidates
          </h3>
          <div className="grid grid-cols-3 gap-2">
            {SEED_CANDIDATES.map((u) => (
              <SeedLoginButton
                key={u.email}
                user={u}
                loading={loading === u.email}
                onClick={() => handleQuickLogin(u)}
              />
            ))}
          </div>
        </div>

        {/* HR */}
        <div>
          <h3 className="text-xs font-semibold text-text-muted uppercase tracking-wide mb-3">
            Company HR
          </h3>
          <div className="grid grid-cols-3 gap-2">
            {SEED_HRS.map((u) => (
              <SeedLoginButton
                key={u.email}
                user={u}
                loading={loading === u.email}
                onClick={() => handleQuickLogin(u)}
              />
            ))}
          </div>
        </div>
      </div>

      {/* ── Feature cards ──────────────────────────────── */}
      <div className="grid grid-cols-3 gap-6 mt-16 w-full max-w-3xl">
        <FeatureCard
          title="Career DNA"
          desc="50+ dimension deep profile through behavioral scenarios"
        />
        <FeatureCard
          title="Weekly Drop"
          desc="Curated matches revealed every Tuesday at 9 PM"
        />
        <FeatureCard
          title="Smart Match"
          desc="AI-powered compatibility scoring with detailed reports"
        />
      </div>
    </div>
  );
}

/* ── Sub-components ─────────────────────────────────────────────────── */

function SeedLoginButton({
  user,
  loading,
  onClick,
}: {
  user: SeedUser;
  loading: boolean;
  onClick: () => void;
}) {
  return (
    <button
      onClick={onClick}
      disabled={loading}
      className={[
        "px-4 py-2.5 rounded-[var(--radius-lg)] text-sm font-medium",
        "border border-glass-border cursor-pointer",
        "hover:bg-surface-light disabled:opacity-50 disabled:cursor-not-allowed",
        user.role === "hr" ? "text-amber" : "text-indigo",
      ].join(" ")}
    >
      {loading ? "Logging in..." : user.name}
    </button>
  );
}

function FeatureCard({ title, desc }: { title: string; desc: string }) {
  return (
    <div className="p-4 rounded-[var(--radius-xl)] border border-glass-border bg-surface text-left">
      <h3 className="text-sm font-semibold font-display text-indigo mb-1">
        {title}
      </h3>
      <p className="text-xs text-text-dim leading-relaxed">{desc}</p>
    </div>
  );
}
