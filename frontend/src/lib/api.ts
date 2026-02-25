import type {
  CompanyDropResponse,
  CompanyMatchResponse,
  DropResponse,
  MatchResponse,
  Role,
  RoleCreate,
  UserProfile,
} from "./types";

const API_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

const TOKEN_KEY = "talentdrop_token";

function getToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(TOKEN_KEY);
}

export function setToken(token: string): void {
  localStorage.setItem(TOKEN_KEY, token);
}

export function clearToken(): void {
  localStorage.removeItem(TOKEN_KEY);
}

class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

async function request<T>(
  path: string,
  options: RequestInit = {},
): Promise<T> {
  const token = getToken();
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...((options.headers as Record<string, string>) || {}),
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers,
  });

  if (!res.ok) {
    const body = await res.text();
    throw new ApiError(res.status, body);
  }

  if (res.status === 204) return undefined as T;
  return res.json() as Promise<T>;
}

async function uploadFile<T>(path: string, file: File): Promise<T> {
  const token = getToken();
  const formData = new FormData();
  formData.append("file", file);

  const headers: Record<string, string> = {};
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const res = await fetch(`${API_URL}${path}`, {
    method: "POST",
    headers,
    body: formData,
  });

  if (!res.ok) {
    const body = await res.text();
    throw new ApiError(res.status, body);
  }

  return res.json() as Promise<T>;
}

export const api = {
  get<T>(path: string): Promise<T> {
    return request<T>(path, { method: "GET" });
  },

  post<T>(path: string, body?: unknown): Promise<T> {
    return request<T>(path, {
      method: "POST",
      body: body ? JSON.stringify(body) : undefined,
    });
  },

  put<T>(path: string, body?: unknown): Promise<T> {
    return request<T>(path, {
      method: "PUT",
      body: body ? JSON.stringify(body) : undefined,
    });
  },

  patch<T>(path: string, body?: unknown): Promise<T> {
    return request<T>(path, {
      method: "PATCH",
      body: body ? JSON.stringify(body) : undefined,
    });
  },

  delete<T>(path: string): Promise<T> {
    return request<T>(path, { method: "DELETE" });
  },

  upload<T>(path: string, file: File): Promise<T> {
    return uploadFile<T>(path, file);
  },

  /* ── Roles ──────────────────────────────────────── */

  getRoles(companyId?: string): Promise<Role[]> {
    const query = companyId ? `?company_id=${companyId}` : "";
    return request<Role[]>(`/roles${query}`, { method: "GET" });
  },

  getRole(roleId: string): Promise<Role> {
    return request<Role>(`/roles/${roleId}`, { method: "GET" });
  },

  createRole(data: RoleCreate): Promise<Role> {
    return request<Role>("/roles", {
      method: "POST",
      body: JSON.stringify(data),
    });
  },

  updateRole(roleId: string, data: Partial<RoleCreate>): Promise<Role> {
    return request<Role>(`/roles/${roleId}`, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  },

  deleteRole(roleId: string): Promise<void> {
    return request<void>(`/roles/${roleId}`, { method: "DELETE" });
  },

  /* ── Matches (dual-action) ──────────────────────── */

  getMatch(matchId: string): Promise<MatchResponse> {
    return request<MatchResponse>(`/matches/results/${matchId}`, { method: "GET" });
  },

  candidateAction(matchId: string, action: "accept" | "pass"): Promise<MatchResponse> {
    return request<MatchResponse>(
      `/matches/results/${matchId}/candidate-action`,
      { method: "POST", body: JSON.stringify({ action }) },
    );
  },

  companyAction(matchId: string, action: "accept" | "pass"): Promise<MatchResponse> {
    return request<MatchResponse>(
      `/matches/results/${matchId}/company-action`,
      { method: "POST", body: JSON.stringify({ action }) },
    );
  },

  /* ── Drops ──────────────────────────────────────── */

  getCandidateDrop(): Promise<DropResponse> {
    return request<DropResponse>("/drops/current", { method: "GET" });
  },

  getCompanyDrop(): Promise<CompanyDropResponse> {
    return request<CompanyDropResponse>("/drops/company/current", { method: "GET" });
  },

  /* ── Company Matches ────────────────────────────── */

  getCompanyMatches(companyId: string): Promise<CompanyMatchResponse[]> {
    return request<CompanyMatchResponse[]>(
      `/companies/${companyId}/candidates`,
      { method: "GET" },
    );
  },

  /* ── Profile ────────────────────────────────────── */

  getProfile(userId: string): Promise<UserProfile> {
    return request<UserProfile>(`/profile/${userId}`, { method: "GET" });
  },

  updateProfile(data: Partial<UserProfile>): Promise<UserProfile> {
    return request<UserProfile>("/profile", {
      method: "PUT",
      body: JSON.stringify(data),
    });
  },
};

export { ApiError };
