"use client";

import { useEffect, useRef } from "react";
import Link from "next/link";

/* ── Section data ─────────────────────────────────────────────────── */

interface Section {
  id: string;
  icon: string;
  title: string;
  color: string;
  content: React.ReactNode;
}

const BIG_FIVE_MAP = [
  { big5: "外向性 Extraversion", dim: "Pace 节奏", measure: "快节奏冲刺 vs 稳步推进" },
  { big5: "宜人性 Agreeableness", dim: "Collab 协作", measure: "独立深耕 vs 团队协同" },
  { big5: "开放性 Openness", dim: "Decision 决策", measure: "数据驱动 vs 直觉判断" },
  { big5: "宜人性+神经质", dim: "Expression 表达", measure: "直言不讳 vs 委婉含蓄" },
  { big5: "开放性 Openness", dim: "Uncertainty 不确定性", measure: "拥抱模糊 vs 需要明确" },
  { big5: "开放性 Openness", dim: "Growth 成长", measure: "广泛探索 vs 深度专精" },
  { big5: "尽责性 Conscientiousness", dim: "Motivation 驱动力", measure: "使命驱动 vs 回报驱动" },
  { big5: "尽责性 Conscientiousness", dim: "Execution 执行", measure: "严谨计划 vs 灵活应变" },
];

const PAIN_POINTS = [
  { label: "简历黑洞", desc: "投了 100 封，回复 3 封", pct: "97%" },
  { label: "面试马拉松", desc: "8 轮面试只为一个 offer", pct: "8轮" },
  { label: "文化错配", desc: "入职 3 个月才发现不合适", pct: "90天" },
  { label: "算法偏见", desc: "关键词匹配 ≠ 真正匹配", pct: "≠" },
  { label: "信息不对称", desc: "候选人猜公司文化，公司猜候选人能力", pct: "??" },
];

const LAYERS = [
  { name: "平台标准层", count: "30 题", weight: "60%", color: "#6366f1" },
  { name: "岗位专属层", count: "15 题", weight: "25%", color: "#f59e0b" },
  { name: "企业定制层", count: "≤5 题", weight: "15%", color: "#10b981" },
];

const ENGINE_LAYERS = [
  { id: "L1", name: "LightRAG 语义理解", desc: "知识图谱 + 上下文增强检索", color: "#6366f1" },
  { id: "L2", name: "DNA 兼容性", desc: "8 维光谱距离 + 权重优化", color: "#ff6b4a" },
  { id: "L3", name: "技能匹配", desc: "硬技能 + 软实力向量相似度", color: "#f59e0b" },
  { id: "L4", name: "Gale-Shapley 稳定匹配", desc: "双向偏好的博弈论最优解", color: "#10b981" },
  { id: "L5", name: "几何均值聚合", desc: "防止单维过高掩盖短板", color: "#6366f1" },
  { id: "L6-L7", name: "进化反馈回路", desc: "90 天追踪 → 算法自适应", color: "#ff6b4a" },
];

function buildSections(): Section[] {
  return [
    {
      id: "pain", icon: "⚡", title: "行业痛点", color: "#ff6b4a",
      content: (
        <div className="grid grid-cols-2 sm:grid-cols-5 gap-3">
          {PAIN_POINTS.map((p) => (
            <div key={p.label} className="text-center p-4 rounded-xl border border-white/10 bg-white/5">
              <div className="text-2xl font-bold font-display mb-1" style={{ color: "#ff6b4a" }}>{p.pct}</div>
              <div className="text-sm font-semibold text-white mb-1">{p.label}</div>
              <div className="text-xs text-white/50">{p.desc}</div>
            </div>
          ))}
        </div>
      ),
    },
    {
      id: "dna", icon: "🧬", title: "Career DNA 理论框架", color: "#6366f1",
      content: (
        <div>
          <div className="overflow-x-auto rounded-xl border border-white/10">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-white/10 text-left text-white/50">
                  <th className="px-4 py-2">Big Five 来源</th>
                  <th className="px-4 py-2">Career DNA 维度</th>
                  <th className="px-4 py-2">测量内容</th>
                </tr>
              </thead>
              <tbody>
                {BIG_FIVE_MAP.map((r, i) => (
                  <tr key={r.dim} className={i % 2 === 0 ? "bg-white/5" : ""}>
                    <td className="px-4 py-2 text-white/60">{r.big5}</td>
                    <td className="px-4 py-2 font-semibold" style={{ color: "#6366f1" }}>{r.dim}</td>
                    <td className="px-4 py-2 text-white/80">{r.measure}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="mt-4 text-center text-sm text-white/60 italic">
            &quot;所有维度都是光谱，两端都合理，没有正确答案&quot;
          </p>
        </div>
      ),
    },
    {
      id: "arch", icon: "📋", title: "三层问卷架构", color: "#f59e0b",
      content: (
        <div className="space-y-4">
          <div className="flex gap-3 justify-center flex-wrap">
            {LAYERS.map((l) => (
              <div key={l.name} className="flex-1 min-w-[140px] p-4 rounded-xl border border-white/10 bg-white/5 text-center">
                <div className="text-lg font-bold font-display" style={{ color: l.color }}>{l.count}</div>
                <div className="text-sm text-white font-medium">{l.name}</div>
                <div className="text-xs text-white/50 mt-1">权重 {l.weight}</div>
              </div>
            ))}
          </div>
          <div className="p-3 rounded-xl border border-white/10 bg-white/5 text-center">
            <span className="text-sm text-white/70">反作弊机制：</span>
            <span className="text-sm text-white/90">行为场景 · 强制排序 · 交叉验证 · 一致性评分</span>
          </div>
        </div>
      ),
    },
    {
      id: "engine", icon: "⚙️", title: "三层匹配引擎", color: "#10b981",
      content: (
        <div className="space-y-2">
          {ENGINE_LAYERS.map((l) => (
            <div key={l.id} className="flex items-center gap-4 p-3 rounded-xl border border-white/10 bg-white/5">
              <span className="text-xs font-bold px-2 py-1 rounded-md shrink-0" style={{ background: l.color, color: "#070b1a" }}>{l.id}</span>
              <div>
                <div className="text-sm font-semibold text-white">{l.name}</div>
                <div className="text-xs text-white/50">{l.desc}</div>
              </div>
            </div>
          ))}
        </div>
      ),
    },
    {
      id: "flow", icon: "🔄", title: "双向发现机制", color: "#6366f1",
      content: (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { role: "候选人", color: "#6366f1", steps: ["填写 Career DNA", "每周收到 1-3 个匹配岗位", "查看兼容性报告 → 接受 / 跳过"] },
            { role: "企业", color: "#f59e0b", steps: ["填写 Company DNA", "发布岗位 → 自动匹配", "每周收到 3-5 位候选人推荐"] },
            { role: "Mutual Match", color: "#10b981", steps: ["双方都选择「接受」", "开启沟通通道", "面试 → 入职 → 90 天追踪"] },
          ].map((c) => (
            <div key={c.role} className="p-4 rounded-xl border border-white/10 bg-white/5">
              <div className="text-sm font-bold font-display mb-3" style={{ color: c.color }}>{c.role}</div>
              <ol className="space-y-2">
                {c.steps.map((s, i) => (
                  <li key={i} className="flex items-start gap-2 text-xs text-white/70">
                    <span className="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-[10px] font-bold" style={{ background: c.color, color: "#070b1a" }}>{i + 1}</span>
                    {s}
                  </li>
                ))}
              </ol>
            </div>
          ))}
        </div>
      ),
    },
    {
      id: "flywheel", icon: "🚀", title: "数据飞轮", color: "#ff6b4a",
      content: (
        <div className="flex flex-col items-center gap-6">
          <div className="flex flex-wrap justify-center gap-3">
            {["匹配落地", "90 天追踪", "知识图谱更新", "算法进化", "更精准匹配"].map((step, i, arr) => (
              <div key={step} className="flex items-center gap-2">
                <span className="px-3 py-2 rounded-lg text-sm font-medium border border-white/10 bg-white/5 text-white">{step}</span>
                {i < arr.length - 1 && <span className="text-white/30 text-lg">→</span>}
              </div>
            ))}
          </div>
          <p className="text-lg font-display font-semibold text-center" style={{ color: "#ff6b4a" }}>
            &quot;知遇，让招聘回归双向奔赴&quot;
          </p>
        </div>
      ),
    },
  ];
}

/* ── Scroll fade-in hook ──────────────────────────────────────────── */

function useScrollFadeIn() {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((e) => {
        if (e.isIntersecting) e.target.classList.add("opacity-100", "translate-y-0");
      }),
      { threshold: 0.15 },
    );
    const children = el.querySelectorAll("[data-fade]");
    children.forEach((c) => observer.observe(c));
    return () => observer.disconnect();
  }, []);
  return ref;
}

/* ── Page component ───────────────────────────────────────────────── */

export default function DemoTheoryPage() {
  const containerRef = useScrollFadeIn();
  const sections = buildSections();

  return (
    <div
      ref={containerRef}
      className="min-h-screen text-white overflow-x-hidden"
      style={{ background: "#070b1a" }}
    >
      {/* Hero */}
      <header className="flex flex-col items-center justify-center text-center px-6 pt-24 pb-16">
        <h1 className="text-5xl md:text-7xl font-bold font-display mb-4" style={{ color: "#6366f1" }}>
          知遇
        </h1>
        <p className="text-xl md:text-2xl text-white/70 max-w-2xl leading-relaxed">
          AI 驱动的深度人才匹配平台 — 理论基础与技术架构
        </p>
        <div className="mt-8 flex gap-2 flex-wrap justify-center">
          {sections.map((s) => (
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
        {sections.map((s, i) => (
          <section
            key={s.id}
            id={s.id}
            data-fade
            className="opacity-0 translate-y-8 transition-all duration-700 ease-out rounded-2xl p-6 md:p-8 border border-white/10"
            style={{ background: "rgba(255,255,255,0.03)", backdropFilter: "blur(12px)" }}
          >
            <div className="flex items-center gap-3 mb-6">
              <span className="text-xs font-bold px-2 py-1 rounded-md" style={{ background: s.color, color: "#070b1a" }}>
                0{i + 1}
              </span>
              <h2 className="text-xl md:text-2xl font-bold font-display" style={{ color: s.color }}>
                {s.title}
              </h2>
            </div>
            {s.content}
          </section>
        ))}

        {/* CTA */}
        <div data-fade className="opacity-0 translate-y-8 transition-all duration-700 ease-out text-center pt-8">
          <Link
            href="/"
            className="inline-block px-8 py-4 rounded-2xl text-lg font-bold font-display text-white hover:scale-105 transition-transform"
            style={{ background: "linear-gradient(135deg, #6366f1, #ff6b4a)" }}
          >
            开始体验 Demo →
          </Link>
        </div>
      </main>
    </div>
  );
}
