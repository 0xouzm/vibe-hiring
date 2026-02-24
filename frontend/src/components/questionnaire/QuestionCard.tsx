"use client";

import type { Question, ChoiceAnswer } from "@/lib/types";

/* ── Choice question — select one option ───────────────────────────── */

interface QuestionCardProps {
  question: Question;
  selectedKey: string | undefined;
  onSelect: (answer: ChoiceAnswer) => void;
}

export function QuestionCard({
  question,
  selectedKey,
  onSelect,
}: QuestionCardProps) {
  const handleClick = (key: string) => {
    onSelect({
      type: "choice",
      question_id: question.id,
      selected_key: key,
    });
  };

  return (
    <div>
      {/* Scenario */}
      <p className="text-text-dim text-sm leading-relaxed mb-6">
        {question.scenario}
      </p>

      {/* Options grid */}
      <div className="grid gap-3">
        {question.options.map((opt) => {
          const isSelected = selectedKey === opt.key;
          return (
            <button
              key={opt.key}
              onClick={() => handleClick(opt.key)}
              className={[
                "w-full text-left px-5 py-4 rounded-[var(--radius-lg)]",
                "border cursor-pointer transition-all",
                isSelected
                  ? "border-indigo bg-indigo/5 text-text shadow-sm shadow-indigo/10"
                  : "border-glass-border bg-surface text-text-dim hover:border-indigo/40 hover:bg-surface-light",
              ].join(" ")}
            >
              <div className="flex items-start gap-3">
                {/* Radio indicator */}
                <span
                  className={[
                    "mt-0.5 w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0",
                    isSelected ? "border-indigo" : "border-glass-border",
                  ].join(" ")}
                >
                  {isSelected && (
                    <span className="w-2.5 h-2.5 rounded-full bg-indigo" />
                  )}
                </span>

                <span className="text-sm leading-relaxed">{opt.text}</span>
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
}
