"use client";

import { useState, useEffect } from "react";
import type { Question, RankingAnswer } from "@/lib/types";

/* ── Ranking question — reorder options via up/down buttons ────────── */

interface RankQuestionProps {
  question: Question;
  currentRanking: string[] | undefined;
  onRank: (answer: RankingAnswer) => void;
}

export function RankQuestion({
  question,
  currentRanking,
  onRank,
}: RankQuestionProps) {
  const [ranking, setRanking] = useState<string[]>(() =>
    currentRanking ?? question.options.map((o) => o.key),
  );

  // Sync if question changes
  useEffect(() => {
    setRanking(currentRanking ?? question.options.map((o) => o.key));
  }, [question.id, currentRanking, question.options]);

  const optionMap = new Map(question.options.map((o) => [o.key, o.text]));

  const moveUp = (index: number) => {
    if (index === 0) return;
    const next = [...ranking];
    [next[index - 1], next[index]] = [next[index], next[index - 1]];
    setRanking(next);
    emitAnswer(next);
  };

  const moveDown = (index: number) => {
    if (index === ranking.length - 1) return;
    const next = [...ranking];
    [next[index], next[index + 1]] = [next[index + 1], next[index]];
    setRanking(next);
    emitAnswer(next);
  };

  const emitAnswer = (order: string[]) => {
    onRank({
      type: "ranking",
      question_id: question.id,
      ranking: order,
    });
  };

  return (
    <div>
      <p className="text-text-dim text-sm leading-relaxed mb-2">
        {question.scenario}
      </p>
      <p className="text-xs text-text-muted mb-6">
        使用箭头调整排序，顶部 = 最重要。
      </p>

      <div className="grid gap-2">
        {ranking.map((key, idx) => (
          <div
            key={key}
            className="flex items-center gap-3 px-4 py-3 rounded-[var(--radius-lg)] border border-glass-border bg-surface"
          >
            {/* Rank number */}
            <span className="w-6 h-6 rounded-full bg-indigo/10 text-indigo text-xs font-bold flex items-center justify-center">
              {idx + 1}
            </span>

            {/* Label */}
            <span className="flex-1 text-sm text-text">
              {optionMap.get(key) ?? key}
            </span>

            {/* Up / Down buttons */}
            <div className="flex gap-1">
              <button
                onClick={() => moveUp(idx)}
                disabled={idx === 0}
                className="p-1 rounded text-text-dim hover:text-text disabled:opacity-25 cursor-pointer disabled:cursor-not-allowed"
                aria-label="上移"
              >
                <ArrowUp />
              </button>
              <button
                onClick={() => moveDown(idx)}
                disabled={idx === ranking.length - 1}
                className="p-1 rounded text-text-dim hover:text-text disabled:opacity-25 cursor-pointer disabled:cursor-not-allowed"
                aria-label="下移"
              >
                <ArrowDown />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ── Arrow icons ───────────────────────────────────────────────────── */

function ArrowUp() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M12 19V5M5 12l7-7 7 7" />
    </svg>
  );
}

function ArrowDown() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M12 5v14M19 12l-7 7-7-7" />
    </svg>
  );
}
