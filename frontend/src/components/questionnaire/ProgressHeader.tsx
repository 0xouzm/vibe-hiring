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
          Question {currentIndex + 1} of {totalQuestions}
        </span>
        <span className="text-sm font-medium text-indigo">
          {answeredCount} / {totalQuestions} answered
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
