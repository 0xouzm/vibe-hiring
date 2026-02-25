"use client";

import Link from "next/link";
import { SECTION_DEFS } from "./_components/section-data";
import { useScrollFadeIn, SectionShell } from "./_components/SectionRenderer";
import {
  PainSection,
  DnaSection,
  ArchSection,
  EngineSection,
  FlowSection,
  FlywheelSection,
} from "./_components/ExistingSections";
import { DateDropComparison } from "./_components/DateDropComparison";

/* ── Section id → content 映射 ────────────────────────────────────── */

const CONTENT_MAP: Record<string, React.ReactNode> = {
  pain: <PainSection />,
  dna: <DnaSection />,
  arch: <ArchSection />,
  compare: <DateDropComparison />,
  engine: <EngineSection />,
  flow: <FlowSection />,
  flywheel: <FlywheelSection />,
};

/* ── Page ─────────────────────────────────────────────────────────── */

export default function DemoTheoryPage() {
  const containerRef = useScrollFadeIn();

  return (
    <div
      ref={containerRef}
      className="min-h-screen text-white overflow-x-hidden"
      style={{ background: "#070b1a" }}
    >
      {/* Hero */}
      <header className="flex flex-col items-center justify-center text-center px-6 pt-24 pb-16">
        <h1
          className="text-5xl md:text-7xl font-bold font-display mb-4"
          style={{ color: "#6366f1" }}
        >
          职遇
        </h1>
        <p className="text-xl md:text-2xl text-white/70 max-w-2xl leading-relaxed">
          AI 驱动的深度人才匹配平台 — 理论基础与技术架构
        </p>
        <div className="mt-8 flex gap-2 flex-wrap justify-center">
          {SECTION_DEFS.map((s) => (
            <a
              key={s.id}
              href={`#${s.id}`}
              className="px-3 py-1.5 rounded-full text-xs font-medium border border-white/10 hover:border-white/30 text-white/60 hover:text-white"
            >
              {s.icon} {s.title}
            </a>
          ))}
        </div>
      </header>

      {/* Sections */}
      <main className="max-w-4xl mx-auto px-6 pb-24 space-y-12">
        {SECTION_DEFS.map((s, i) => (
          <SectionShell key={s.id} id={s.id} index={i} title={s.title} color={s.color}>
            {CONTENT_MAP[s.id]}
          </SectionShell>
        ))}

        {/* CTA */}
        <div data-fade className="opacity-0 translate-y-8 transition-all duration-700 ease-out text-center pt-8">
          <Link
            href="/"
            className="inline-block px-8 py-4 rounded-2xl text-lg font-bold font-display text-white hover:scale-105 transition-transform"
            style={{ background: "linear-gradient(135deg, #6366f1, #ff6b4a)" }}
          >
            开始体验 Demo &rarr;
          </Link>
        </div>
      </main>
    </div>
  );
}
