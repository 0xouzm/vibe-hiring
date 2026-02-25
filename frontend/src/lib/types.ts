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

/* ── Roles (Open Positions) ─────────────────────────── */

export interface SalaryRange {
  min: number;
  max: number;
  currency: string;
}

export interface Role {
  id: string;
  company_id: string;
  company_name: string;
  title: string;
  level?: string;
  skills: string[];
  nice_to_have: string[];
  salary_range?: SalaryRange;
  location?: string;
  remote_policy?: string;
  description?: string;
  is_active: boolean;
  created_at: string;
}

export interface RoleCreate {
  title: string;
  level?: string;
  skills?: string[];
  nice_to_have?: string[];
  salary_range?: SalaryRange;
  location?: string;
  remote_policy?: string;
  description?: string;
}

/* ── Matching ───────────────────────────────────────── */

export type MatchStatus =
  | "pending"
  | "candidate_accepted"
  | "company_accepted"
  | "mutual"
  | "passed"
  | "accepted"; // legacy

export interface MatchResponse {
  id: string;
  candidate_id: string;
  company_id: string;
  company_name: string;
  role_id?: string;
  role_title?: string;
  score: number;
  dimension_scores: DimensionScores;
  report?: string;
  status: MatchStatus;
  candidate_action?: string;
  company_action?: string;
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
  role_id?: string;
  role_title?: string;
  score: number;
  dimension_scores: DimensionScores;
  report?: string;
  status: MatchStatus;
  candidate_action?: string;
  company_action?: string;
}

export interface CompanyDropResponse {
  id: string;
  week: string;
  matches: CompanyMatchResponse[];
  revealed_at?: string;
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

/* ── User Profile ──────────────────────────────────── */

export interface UserProfile {
  id: string;
  user_id: string;
  title?: string;
  years_experience?: number;
  skills: string[];
  education: Array<{
    degree: string;
    school: string;
    major: string;
  }>;
  bio?: string;
  resume_text?: string;
  chat_summary?: string;
  location?: string;
  remote_preference?: string;
  salary_expectation?: SalaryRange;
  created_at: string;
  updated_at: string;
}

/* ── Chat ──────────────────────────────────────────── */

export interface ChatMessage {
  id: string;
  user_id: string;
  role: "user" | "assistant";
  content: string;
  extracted_entities?: Record<string, unknown>;
  created_at: string;
}

export interface ChatHistoryResponse {
  messages: ChatMessage[];
  total: number;
}

