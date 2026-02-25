"use client";

import { useEffect, useRef, type ReactNode } from "react";

/* ── Scroll fade-in hook ──────────────────────────────────────────── */

export function useScrollFadeIn() {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const observer = new IntersectionObserver(
      (entries) =>
        entries.forEach((e) => {
          if (e.isIntersecting)
            e.target.classList.add("opacity-100", "translate-y-0");
        }),
      { threshold: 0.15 },
    );
    const children = el.querySelectorAll("[data-fade]");
    children.forEach((c) => observer.observe(c));
    return () => observer.disconnect();
  }, []);
  return ref;
}

/* ── Section shell ────────────────────────────────────────────────── */

interface SectionShellProps {
  id: string;
  index: number;
  title: string;
  color: string;
  children: ReactNode;
}

export function SectionShell({ id, index, title, color, children }: SectionShellProps) {
  return (
    <section
      id={id}
      data-fade
      className="opacity-0 translate-y-8 transition-all duration-700 ease-out rounded-2xl p-6 md:p-8 border border-white/10"
      style={{ background: "rgba(255,255,255,0.03)", backdropFilter: "blur(12px)" }}
    >
      <div className="flex items-center gap-3 mb-6">
        <span
          className="text-xs font-bold px-2 py-1 rounded-md"
          style={{ background: color, color: "#070b1a" }}
        >
          0{index + 1}
        </span>
        <h2
          className="text-xl md:text-2xl font-bold font-display"
          style={{ color }}
        >
          {title}
        </h2>
      </div>
      {children}
    </section>
  );
}
