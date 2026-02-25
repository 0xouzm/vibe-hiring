"use client";

import { useAuth } from "@/hooks/useAuth";
import { Button } from "@/components/ui/Button";
import { Badge } from "@/components/ui/Badge";

export function Header() {
  const { user, logout } = useAuth();

  return (
    <header className="fixed top-0 left-0 right-0 z-40 h-16 glass">
      <div className="h-full flex items-center justify-between px-6">
        {/* Logo */}
        <div className="flex items-center gap-3">
          <span className="text-xl font-bold font-display text-indigo">
            TalentDrop
          </span>
        </div>

        {/* User info */}
        {user && (
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2">
              <span className="text-sm text-text">{user.name}</span>
              <Badge variant={user.role === "hr" ? "warning" : "default"}>
                {user.role === "hr" ? "HR" : "候选人"}
              </Badge>
            </div>
            <Button variant="ghost" size="sm" onClick={logout}>
              退出
            </Button>
          </div>
        )}
      </div>
    </header>
  );
}
