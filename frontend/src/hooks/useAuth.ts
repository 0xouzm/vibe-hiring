"use client";

import {
  createContext,
  useContext,
  useState,
  useEffect,
  useCallback,
  type ReactNode,
} from "react";
import { createElement } from "react";
import type { User, TokenResponse } from "@/lib/types";
import { api, setToken, clearToken } from "@/lib/api";

/* ── Types ──────────────────────────────────────────── */

interface AuthState {
  user: User | null;
  token: string | null;
  isLoading: boolean;
}

interface AuthActions {
  login: (email: string, password: string) => Promise<void>;
  register: (
    name: string,
    email: string,
    password: string,
    role: "candidate" | "hr",
    companyId?: string,
  ) => Promise<void>;
  logout: () => void;
}

type AuthContextValue = AuthState & AuthActions;

/* ── Constants ──────────────────────────────────────── */

const TOKEN_KEY = "talentdrop_token";
const USER_KEY = "talentdrop_user";

/* ── Context ────────────────────────────────────────── */

const AuthContext = createContext<AuthContextValue | null>(null);

/* ── Provider ───────────────────────────────────────── */

export function AuthProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<AuthState>({
    user: null,
    token: null,
    isLoading: true,
  });

  // Restore session on mount
  useEffect(() => {
    const token = localStorage.getItem(TOKEN_KEY);
    const userJson = localStorage.getItem(USER_KEY);

    if (token && userJson) {
      try {
        const user = JSON.parse(userJson) as User;
        setToken(token);
        setState({ user, token, isLoading: false });
      } catch {
        clearSession();
        setState({ user: null, token: null, isLoading: false });
      }
    } else {
      setState({ user: null, token: null, isLoading: false });
    }
  }, []);

  const persistSession = useCallback((token: string, user: User) => {
    localStorage.setItem(TOKEN_KEY, token);
    localStorage.setItem(USER_KEY, JSON.stringify(user));
    setToken(token);
    setState({ user, token, isLoading: false });
  }, []);

  const clearSession = useCallback(() => {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(USER_KEY);
    clearToken();
    setState({ user: null, token: null, isLoading: false });
  }, []);

  const login = useCallback(
    async (email: string, password: string) => {
      const res = await api.post<TokenResponse>("/auth/login", {
        email,
        password,
      });
      persistSession(res.access_token, res.user);
    },
    [persistSession],
  );

  const register = useCallback(
    async (
      name: string,
      email: string,
      password: string,
      role: "candidate" | "hr",
      companyId?: string,
    ) => {
      const res = await api.post<TokenResponse>("/auth/register", {
        name,
        email,
        password,
        role,
        company_id: companyId,
      });
      persistSession(res.access_token, res.user);
    },
    [persistSession],
  );

  const logout = useCallback(() => {
    clearSession();
  }, [clearSession]);

  const value: AuthContextValue = {
    ...state,
    login,
    register,
    logout,
  };

  return createElement(AuthContext.Provider, { value }, children);
}

/* ── Hook ───────────────────────────────────────────── */

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return ctx;
}
