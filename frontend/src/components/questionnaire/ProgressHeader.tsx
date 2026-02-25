"use client";

/* ── Progress header for questionnaire ─────────────────────────────── */

interface ProgressHeaderProps {
  currentIndex: number;
  totalQuestions: number;
  progress: number;
  answeredCount: number;
}

export function ProgressHeader({
  currentIndex,
  totalQuestions,
  progress,
  answeredCount,
}: ProgressHeaderProps) {
  return (
    <div className="mb-8">
      {/* Top labels */}
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm text-text-dim">
          第 {currentIndex + 1} 题 / 共 {totalQuestions} 题
        </span>
        <span className="text-sm font-medium text-indigo">
          已答 {answeredCount} / {totalQuestions} 题
        </span>
      </div>

      {/* Progress bar */}
      <div className="h-2 w-full rounded-full bg-surface-light overflow-hidden">
        <div
          className="h-full rounded-full bg-indigo transition-all duration-500 ease-out"
          style={{ width: `${progress}%` }}
        />
      </div>
    </div>
  );
}
