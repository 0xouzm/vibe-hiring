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

/* -- Company DNA Questionnaire Page ----------------------------------- */

export default function CompanyQuestionnairePage() {
  const router = useRouter();
  const [questions, setQuestions] = useState<Question[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<DNAScoreResponse | null>(null);

  useEffect(() => {
    api
      .get<Question[]>("/questions/company-dna")
      .then((data) => {
        setQuestions(data);
        setLoading(false);
      })
      .catch(() => {
        setError("加载题目失败，请确认后端服务是否已启动。");
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
          重试
        </Button>
      </div>
    );
  }

  if (questions.length === 0) {
    return (
      <div className="text-center py-16">
        <p className="text-text-dim">暂无可用题目。</p>
      </div>
    );
  }

  if (result) {
    return (
      <CompletionView
        result={result}
        onContinue={() => router.push("/company/dashboard")}
      />
    );
  }

  return (
    <QuestionnaireFlow
      questions={questions}
      onComplete={(res) => setResult(res)}
    />
  );
}

/* -- Active questionnaire flow ---------------------------------------- */

function QuestionnaireFlow({
  questions,
  onComplete,
}: {
  questions: Question[];
  onComplete: (res: DNAScoreResponse) => void;
}) {
  const q = useQuestionnaire(questions, "/answers/company-dna");

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

      <div className="mb-6">
        <h1 className="text-2xl font-bold font-display text-text">
          企业 DNA 测评
        </h1>
        <p className="text-sm text-text-dim mt-1">
          通过行为场景定义企业文化画像
        </p>
      </div>

      <Card>
        <CardContent>
          <h2 className="text-lg font-semibold font-display text-text mb-4">
            {question.title}
          </h2>

          <QuestionRenderer
            question={question}
            answer={q.currentAnswer}
            onAnswer={q.setAnswer}
          />

          <div className="flex items-center justify-between mt-8 pt-6 border-t border-glass-border">
            <Button
              variant="ghost"
              onClick={q.goPrev}
              disabled={q.isFirst}
            >
              上一题
            </Button>

            {q.isLast ? (
              <Button
                onClick={handleSubmit}
                loading={q.isSubmitting}
                disabled={!hasAnswer}
              >
                提交
              </Button>
            ) : (
              <Button onClick={q.goNext} disabled={!hasAnswer}>
                下一题
              </Button>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

/* -- Question type router --------------------------------------------- */

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
      return <p className="text-text-dim">未知题目类型。</p>;
  }
}

/* -- Completion view -------------------------------------------------- */

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
        <svg
          width="32"
          height="32"
          viewBox="0 0 24 24"
          fill="none"
          stroke="#10B981"
          strokeWidth="2"
        >
          <path d="M20 6L9 17l-5-5" />
        </svg>
      </div>
      <h2 className="text-2xl font-bold font-display text-text mb-2">
        企业 DNA 测评完成！
      </h2>
      <p className="text-text-dim text-sm mb-2">
        一致性分数：{" "}
        <span className="font-semibold text-indigo">
          {Math.round(result.consistency * 100)}%
        </span>
      </p>
      <p className="text-text-muted text-xs mb-8">
        企业文化画像已生成，前往仪表盘查看完整的 DNA 分析和 CAS 评分。
      </p>
      <Button size="lg" onClick={onContinue}>
        前往仪表盘
      </Button>
    </div>
  );
}
