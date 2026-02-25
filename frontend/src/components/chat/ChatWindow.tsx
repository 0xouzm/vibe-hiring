"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import { api } from "@/lib/api";
import { useAuth } from "@/hooks/useAuth";
import type {
  ChatMessage as ChatMessageType,
  ChatHistoryResponse,
} from "@/lib/types";
import { ChatMessage } from "./ChatMessage";

/* ── Chat Window ───────────────────────────────────────────────────── */

export function ChatWindow() {
  const { user } = useAuth();
  const [messages, setMessages] = useState<ChatMessageType[]>([]);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);
  const [loading, setLoading] = useState(true);
  const scrollRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = useCallback(() => {
    requestAnimationFrame(() => {
      scrollRef.current?.scrollTo({
        top: scrollRef.current.scrollHeight,
        behavior: "smooth",
      });
    });
  }, []);

  useEffect(() => {
    if (!user) return;
    api
      .get<ChatHistoryResponse>("/chat/history")
      .then((res) => setMessages(res.messages))
      .catch(() => setMessages([]))
      .finally(() => setLoading(false));
  }, [user]);

  useEffect(() => {
    if (!loading) scrollToBottom();
  }, [messages, loading, scrollToBottom]);

  const handleSend = async () => {
    const content = input.trim();
    if (!content || sending) return;

    setInput("");
    setSending(true);

    const tempId = `temp-${Date.now()}`;
    const tempMsg: ChatMessageType = {
      id: tempId,
      user_id: user?.id ?? "",
      role: "user",
      content,
      created_at: new Date().toISOString(),
    };
    setMessages((prev) => [...prev, tempMsg]);

    try {
      // Backend returns only the assistant message; user msg is already shown
      const assistantMsg = await api.post<ChatMessageType>("/chat/profile", { content });
      // Replace temp user msg with a confirmed version, add assistant reply
      setMessages((prev) => [
        ...prev.map((m) =>
          m.id === tempId ? { ...m, id: `usr-${assistantMsg.id}` } : m,
        ),
        assistantMsg,
      ]);
    } catch {
      setMessages((prev) => prev.filter((m) => m.id !== tempId));
    } finally {
      setSending(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  return (
    <div className="flex flex-col h-[calc(100vh-220px)] border border-glass-border rounded-[var(--radius-xl)] bg-surface overflow-hidden">
      {/* Messages */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto p-4">
        {messages.length === 0 && (
          <p className="text-center text-text-muted text-sm mt-12">
            你好！我是你的 AI 职业顾问，可以帮你梳理职业背景和求职偏好。
            <br />
            试试告诉我你的工作经历或理想岗位吧。
          </p>
        )}
        {messages.map((msg) => (
          <ChatMessage key={msg.id} message={msg} isUser={msg.role === "user"} />
        ))}
        {sending && <TypingIndicator />}
      </div>

      {/* Input */}
      <div className="border-t border-glass-border p-3 bg-surface-light">
        <div className="flex gap-2 items-end">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="输入你的消息..."
            rows={1}
            className="flex-1 resize-none px-3 py-2 rounded-[var(--radius-lg)] border border-glass-border bg-surface text-text text-sm placeholder:text-text-muted focus:outline-2 focus:outline-offset-0 focus:outline-indigo"
          />
          <button
            onClick={handleSend}
            disabled={!input.trim() || sending}
            className="h-10 px-4 rounded-[var(--radius-lg)] text-sm font-medium bg-indigo text-white cursor-pointer hover:bg-indigo/90 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            发送
          </button>
        </div>
      </div>
    </div>
  );
}

/* ── Typing indicator ──────────────────────────────────────────────── */

function TypingIndicator() {
  return (
    <div className="flex justify-start mb-3">
      <div className="bg-surface-light rounded-[var(--radius-xl)] rounded-bl-sm px-4 py-3">
        <div className="flex gap-1.5">
          <span className="w-2 h-2 bg-text-muted rounded-full animate-bounce" />
          <span className="w-2 h-2 bg-text-muted rounded-full animate-bounce [animation-delay:0.15s]" />
          <span className="w-2 h-2 bg-text-muted rounded-full animate-bounce [animation-delay:0.3s]" />
        </div>
      </div>
    </div>
  );
}
