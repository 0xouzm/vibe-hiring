"use client";

import { useState, useEffect, useCallback } from "react";
import type { Question, BudgetAnswer } from "@/lib/types";

/* ── Budget question — allocate 100 points across options ──────────── */

interface BudgetQuestionProps {
  question: Question;
  currentAllocations: Record<string, number> | undefined;
  onAllocate: (answer: BudgetAnswer) => void;
}

export function BudgetQuestion({
  question,
  currentAllocations,
  onAllocate,
}: BudgetQuestionProps) {
  const optionKeys = question.options.map((o) => o.key);
  const evenSplit = Math.floor(100 / optionKeys.length);
  const remainder = 100 - evenSplit * optionKeys.length;

  const [allocations, setAllocations] = useState<Record<string, number>>(() => {
    if (currentAllocations) return currentAllocations;
    const init: Record<string, number> = {};
    optionKeys.forEach((k, i) => {
      init[k] = evenSplit + (i === 0 ? remainder : 0);
    });
    return init;
  });

  // Sync when question changes
  useEffect(() => {
    if (currentAllocations) {
      setAllocations(currentAllocations);
    }
  }, [question.id, currentAllocations]);

  const total = Object.values(allocations).reduce((s, v) => s + v, 0);
  const isValid = total === 100;

  const emitAnswer = useCallback(
    (alloc: Record<string, number>) => {
      const sum = Object.values(alloc).reduce((s, v) => s + v, 0);
      if (sum === 100) {
        onAllocate({
          type: "budget",
          question_id: question.id,
          allocations: alloc,
        });
      }
    },
    [onAllocate, question.id],
  );

  const handleChange = (key: string, value: number) => {
    const clamped = Math.max(0, Math.min(100, value));
    const next = { ...allocations, [key]: clamped };
    setAllocations(next);
    emitAnswer(next);
  };

  const optionMap = new Map(question.options.map((o) => [o.key, o.text]));

  return (
    <div>
      <p className="text-text-dim text-sm leading-relaxed mb-2">
        {question.scenario}
      </p>
      <p className="text-xs text-text-muted mb-6">
        将 100 分精确分配到以下选项中。
      </p>

      <div className="grid gap-4">
        {optionKeys.map((key) => {
          const val = allocations[key] ?? 0;
          return (
            <div key={key}>
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-sm text-text">
                  {optionMap.get(key) ?? key}
                </span>
                <span className="text-sm font-medium text-indigo w-10 text-right">
                  {val}
                </span>
              </div>
              <input
                type="range"
                min={0}
                max={100}
                value={val}
                onChange={(e) => handleChange(key, Number(e.target.value))}
                className="w-full accent-indigo cursor-pointer"
              />
            </div>
          );
        })}
      </div>

      {/* Total indicator */}
      <div className="mt-6 flex items-center justify-between px-4 py-3 rounded-[var(--radius-lg)] border border-glass-border bg-surface">
        <span className="text-sm text-text-dim">总计</span>
        <span
          className={[
            "text-lg font-bold",
            isValid ? "text-emerald" : "text-rose",
          ].join(" ")}
        >
          {total} / 100
        </span>
      </div>
    </div>
  );
}
