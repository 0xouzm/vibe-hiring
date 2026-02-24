"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { AuthProvider, useAuth } from "@/hooks/useAuth";
import { PageContainer } from "@/components/layout/PageContainer";

/* -- Auth guard -- redirect if not logged-in or not HR role ----------- */

function CompanyAuthGuard({ children }: { children: React.ReactNode }) {
  const { user, isLoading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (isLoading) return;
    if (!user) {
      router.replace("/");
      return;
    }
    if (user.role !== "hr") {
      router.replace("/candidate/dashboard");
    }
  }, [user, isLoading, router]);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (!user || user.role !== "hr") return null;

  return <PageContainer>{children}</PageContainer>;
}

/* -- Layout ----------------------------------------------------------- */

export default function CompanyLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <AuthProvider>
      <CompanyAuthGuard>{children}</CompanyAuthGuard>
    </AuthProvider>
  );
}
