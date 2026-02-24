"use client";

import type { ReactNode } from "react";
import { Header } from "./Header";
import { Sidebar } from "./Sidebar";
import { useAuth } from "@/hooks/useAuth";

interface PageContainerProps {
  children: ReactNode;
}

export function PageContainer({ children }: PageContainerProps) {
  const { user, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="flex flex-col items-center gap-3">
          <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
          <span className="text-sm text-text-dim">Loading...</span>
        </div>
      </div>
    );
  }

  // No sidebar for unauthenticated users
  if (!user) {
    return (
      <div className="min-h-screen">
        <Header />
        <main className="pt-16">{children}</main>
      </div>
    );
  }

  return (
    <div className="min-h-screen">
      <Header />
      <Sidebar />
      <main className="pt-16 pl-60">
        <div className="p-6 max-w-6xl mx-auto">{children}</div>
      </main>
    </div>
  );
}
