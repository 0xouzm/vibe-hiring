/* ── User & Auth ─────────────────────────────────────── */

export type UserRole = "candidate" | "hr";

export interface User {
  id: string;
  email: string;
  name: string;
  role: UserRole;
  company_id?: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  user: User;
}

/* ── Questionnaire ──────────────────────────────────── */

export type QuestionType = "choice" | "ranking" | "budget";

export interface QuestionOption {
  key: string;
  text: string;
}

export interface Question {
  id: string;
  title: string;
  scenario: string;
  type: QuestionType;
  options: QuestionOption[];
  dimensions: string[];
}

/* ── Answers ────────────────────────────────────────── */

export interface ChoiceAnswer {
  type: "choice";
  question_id: string;
  selected_key: string;
}

export interface RankingAnswer {
  type: "ranking";
  question_id: string;
  ranking: string[];
}

export interface BudgetAnswer {
  type: "budget";
  question_id: string;
  allocations: Record<string, number>;
}

export type Answer = ChoiceAnswer | RankingAnswer | BudgetAnswer;

/* ── DNA Scores ─────────────────────────────────────── */

export interface DimensionScores {
  pace: number;
  collab: number;
  decision: number;
  expression: number;
  unc: number;
  growth: number;
  motiv: number;
  execution: number;
}

export interface DNAScoreResponse {
  entity_type: string;
  entity_id: string;
  scores: DimensionScores;
  consistency: number;
}

/* ── Matching ───────────────────────────────────────── */

export type MatchStatus = "pending" | "accepted" | "passed";

export interface MatchResponse {
  id: string;
  candidate_id: string;
  company_id: string;
  company_name: string;
  score: number;
  dimension_scores: DimensionScores;
  report?: string;
  status: MatchStatus;
}

export interface DropResponse {
  id: string;
  week: string;
  matches: MatchResponse[];
  revealed_at?: string;
}

/* ── Company Matches ───────────────────────────────── */

export interface CompanyMatchResponse {
  id: string;
  candidate_id: string;
  candidate_name: string;
  company_id: string;
  score: number;
  dimension_scores: DimensionScores;
  report?: string;
  status: MatchStatus;
}

/* ── Company ────────────────────────────────────────── */

export interface Company {
  id: string;
  name: string;
  industry: string;
  size: string;
  cas_score?: number;
  cas_tier?: string;
}

export interface CASResponse {
  company_id: string;
  score: number;
  tier: string;
  internal_consistency: number;
  hr_employee_alignment: number;
}
