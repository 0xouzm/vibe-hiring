"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";
import type { Question, Answer, DNAScoreResponse } from "@/lib/types";
import { useQuestionnaire } from "@/hooks/useQuestionnaire";
import { Button } from "@/components/ui/Button";
import { Card, CardContent } from "@/components/ui/Card";
import { ProgressHeader } from "@/components/questionnaire/ProgressHeader";
import { QuestionCard } from "@/components/questionnaire/QuestionCard";
import { RankQuestion } from "@/components/questionnaire/RankQuestion";
import { BudgetQuestion } from "@/components/questionnaire/BudgetQuestion";

/* ── Career DNA Questionnaire Page ─────────────────────────────────── */

export default function QuestionnairePage() {
  const router = useRouter();
  const [questions, setQuestions] = useState<Question[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<DNAScoreResponse | null>(null);

  // Load questions
  useEffect(() => {
    api
      .get<Question[]>("/questions/career-dna")
      .then((data) => {
        setQuestions(data);
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load questions. Is the backend running?");
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4">
        <p className="text-rose text-sm">{error}</p>
        <Button variant="secondary" onClick={() => window.location.reload()}>
          Retry
        </Button>
      </div>
    );
  }

  if (questions.length === 0) {
    return (
      <div className="text-center py-16">
        <p className="text-text-dim">No questions available yet.</p>
      </div>
    );
  }

  if (result) {
    return <CompletionView result={result} onContinue={() => router.push("/candidate/dashboard")} />;
  }

  return (
    <QuestionnaireFlow
      questions={questions}
      onComplete={(res) => setResult(res)}
    />
  );
}

/* ── Active questionnaire flow ─────────────────────────────────────── */

function QuestionnaireFlow({
  questions,
  onComplete,
}: {
  questions: Question[];
  onComplete: (res: DNAScoreResponse) => void;
}) {
  const q = useQuestionnaire(questions, "/answers/career-dna");

  const handleSubmit = async () => {
    try {
      const res = await q.submitAnswers();
      onComplete(res);
    } catch {
      // Error handled by hook
    }
  };

  if (!q.currentQuestion) return null;

  const question = q.currentQuestion;
  const hasAnswer = q.currentAnswer !== undefined;

  return (
    <div className="max-w-2xl mx-auto">
      <ProgressHeader
        currentIndex={q.currentIndex}
        totalQuestions={q.totalQuestions}
        progress={q.progress}
        answeredCount={q.answeredCount}
      />

      <Card>
        <CardContent>
          {/* Question title */}
          <h2 className="text-lg font-semibold font-display text-text mb-4">
            {question.title}
          </h2>

          {/* Render by type */}
          <QuestionRenderer
            question={question}
            answer={q.currentAnswer}
            onAnswer={q.setAnswer}
          />

          {/* Navigation buttons */}
          <div className="flex items-center justify-between mt-8 pt-6 border-t border-glass-border">
            <Button
              variant="ghost"
              onClick={q.goPrev}
              disabled={q.isFirst}
            >
              Previous
            </Button>

            {q.isLast ? (
              <Button
                onClick={handleSubmit}
                loading={q.isSubmitting}
                disabled={!hasAnswer}
              >
                Submit
              </Button>
            ) : (
              <Button onClick={q.goNext} disabled={!hasAnswer}>
                Next
              </Button>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

/* ── Question type router ──────────────────────────────────────────── */

function QuestionRenderer({
  question,
  answer,
  onAnswer,
}: {
  question: Question;
  answer: Answer | undefined;
  onAnswer: (a: Answer) => void;
}) {
  switch (question.type) {
    case "choice":
      return (
        <QuestionCard
          question={question}
          selectedKey={
            answer?.type === "choice" ? answer.selected_key : undefined
          }
          onSelect={onAnswer}
        />
      );
    case "ranking":
      return (
        <RankQuestion
          question={question}
          currentRanking={
            answer?.type === "ranking" ? answer.ranking : undefined
          }
          onRank={onAnswer}
        />
      );
    case "budget":
      return (
        <BudgetQuestion
          question={question}
          currentAllocations={
            answer?.type === "budget" ? answer.allocations : undefined
          }
          onAllocate={onAnswer}
        />
      );
    default:
      return <p className="text-text-dim">Unknown question type.</p>;
  }
}

/* ── Completion view ───────────────────────────────────────────────── */

function CompletionView({
  result,
  onContinue,
}: {
  result: DNAScoreResponse;
  onContinue: () => void;
}) {
  return (
    <div className="max-w-md mx-auto text-center py-12">
      <div className="w-16 h-16 rounded-full bg-emerald/10 flex items-center justify-center mx-auto mb-6">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#10B981" strokeWidth="2">
          <path d="M20 6L9 17l-5-5" />
        </svg>
      </div>
      <h2 className="text-2xl font-bold font-display text-text mb-2">
        Career DNA Complete!
      </h2>
      <p className="text-text-dim text-sm mb-2">
        Your consistency score:{" "}
        <span className="font-semibold text-indigo">
          {Math.round(result.consistency * 100)}%
        </span>
      </p>
      <p className="text-text-muted text-xs mb-8">
        Your profile is ready. View your dashboard to see your full DNA breakdown.
      </p>
      <Button size="lg" onClick={onContinue}>
        Go to Dashboard
      </Button>
    </div>
  );
}
