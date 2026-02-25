"use client";

import { ChatWindow } from "@/components/chat/ChatWindow";

/* ── AI Career Advisor Chat Page ───────────────────────────────────── */

export default function CandidateChatPage() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold font-display text-text">
          AI 职业顾问
        </h1>
        <p className="text-sm text-text-dim mt-1">
          通过对话帮你梳理职业背景，提炼关键信息，完善个人档案
        </p>
      </div>

      <ChatWindow />
    </div>
  );
}
