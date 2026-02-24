"use client";

import { useState, useCallback, useMemo } from "react";
import type { Question, Answer } from "@/lib/types";
import { api } from "@/lib/api";
import type { DNAScoreResponse } from "@/lib/types";

interface QuestionnaireState {
  questions: Question[];
  currentIndex: number;
  answers: Map<string, Answer>;
  isSubmitting: boolean;
  isComplete: boolean;
}

interface QuestionnaireActions {
  setAnswer: (answer: Answer) => void;
  goNext: () => void;
  goPrev: () => void;
  goTo: (index: number) => void;
  submitAnswers: () => Promise<DNAScoreResponse>;
}

interface QuestionnaireReturn extends QuestionnaireActions {
  currentQuestion: Question | undefined;
  currentAnswer: Answer | undefined;
  currentIndex: number;
  totalQuestions: number;
  progress: number;
  answeredCount: number;
  isFirst: boolean;
  isLast: boolean;
  isSubmitting: boolean;
  isComplete: boolean;
}

export function useQuestionnaire(
  questions: Question[],
  submitPath: string,
): QuestionnaireReturn {
  const [state, setState] = useState<QuestionnaireState>({
    questions,
    currentIndex: 0,
    answers: new Map(),
    isSubmitting: false,
    isComplete: false,
  });

  const currentQuestion = state.questions[state.currentIndex];
  const currentAnswer = currentQuestion
    ? state.answers.get(currentQuestion.id)
    : undefined;

  const totalQuestions = state.questions.length;
  const answeredCount = state.answers.size;
  const progress =
    totalQuestions > 0 ? Math.round((answeredCount / totalQuestions) * 100) : 0;
  const isFirst = state.currentIndex === 0;
  const isLast = state.currentIndex === totalQuestions - 1;

  const setAnswer = useCallback((answer: Answer) => {
    setState((prev) => {
      const next = new Map(prev.answers);
      next.set(answer.question_id, answer);
      return { ...prev, answers: next };
    });
  }, []);

  const goNext = useCallback(() => {
    setState((prev) => ({
      ...prev,
      currentIndex: Math.min(prev.currentIndex + 1, prev.questions.length - 1),
    }));
  }, []);

  const goPrev = useCallback(() => {
    setState((prev) => ({
      ...prev,
      currentIndex: Math.max(prev.currentIndex - 1, 0),
    }));
  }, []);

  const goTo = useCallback(
    (index: number) => {
      if (index >= 0 && index < totalQuestions) {
        setState((prev) => ({ ...prev, currentIndex: index }));
      }
    },
    [totalQuestions],
  );

  const submitAnswers = useCallback(async (): Promise<DNAScoreResponse> => {
    setState((prev) => ({ ...prev, isSubmitting: true }));
    try {
      const answersArray = Array.from(state.answers.values());
      const result = await api.post<DNAScoreResponse>(submitPath, {
        answers: answersArray,
      });
      setState((prev) => ({
        ...prev,
        isSubmitting: false,
        isComplete: true,
      }));
      return result;
    } catch (error) {
      setState((prev) => ({ ...prev, isSubmitting: false }));
      throw error;
    }
  }, [state.answers, submitPath]);

  return useMemo(
    () => ({
      currentQuestion,
      currentAnswer,
      currentIndex: state.currentIndex,
      totalQuestions,
      progress,
      answeredCount,
      isFirst,
      isLast,
      isSubmitting: state.isSubmitting,
      isComplete: state.isComplete,
      setAnswer,
      goNext,
      goPrev,
      goTo,
      submitAnswers,
    }),
    [
      currentQuestion,
      currentAnswer,
      state.currentIndex,
      totalQuestions,
      progress,
      answeredCount,
      isFirst,
      isLast,
      state.isSubmitting,
      state.isComplete,
      setAnswer,
      goNext,
      goPrev,
      goTo,
      submitAnswers,
    ],
  );
}
