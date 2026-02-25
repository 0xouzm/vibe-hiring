import type { ChatMessage as ChatMessageType } from "@/lib/types";
import { Badge } from "@/components/ui/Badge";

/* ── Entity label translation ──────────────────────────────────────── */

const ENTITY_LABELS: Record<string, string> = {
  skills: "技能",
  values: "价值观",
  experience: "经验",
  education: "教育",
  location: "地点",
  salary: "薪资",
  industry: "行业",
  role: "角色",
};

/* ── Chat message bubble ───────────────────────────────────────────── */

interface ChatMessageProps {
  message: ChatMessageType;
  isUser: boolean;
}

export function ChatMessage({ message, isUser }: ChatMessageProps) {
  // Backend may return { entities: { skills: [], ... } } or flat { skills: [], ... }
  const raw = message.extracted_entities;
  const entities: Record<string, unknown> | null =
    raw && typeof raw === "object" && "entities" in raw && typeof raw.entities === "object"
      ? (raw.entities as Record<string, unknown>)
      : raw ?? null;
  // Filter out empty arrays to only show meaningful entities
  const visibleEntries = entities
    ? Object.entries(entities).filter(
        ([, v]) => v && (!Array.isArray(v) || v.length > 0),
      )
    : [];
  const hasEntities = visibleEntries.length > 0;

  return (
    <div
      className={`flex ${isUser ? "justify-end" : "justify-start"} mb-3`}
    >
      <div
        className={[
          "max-w-[75%] rounded-[var(--radius-xl)] px-4 py-3",
          isUser
            ? "bg-indigo/20 text-text rounded-br-sm"
            : "bg-surface-light text-text rounded-bl-sm",
        ].join(" ")}
      >
        <p className="text-sm leading-relaxed whitespace-pre-wrap">
          {message.content}
        </p>

        {hasEntities && (
          <div className="flex flex-wrap gap-1.5 mt-2 pt-2 border-t border-glass-border">
            {visibleEntries.map(([key, value]) => {
              const display = Array.isArray(value) ? value.join("、") : String(value);
              return (
                <Badge key={key} variant="default">
                  {ENTITY_LABELS[key] ?? key}:&nbsp;
                  <span className="font-medium">{display}</span>
                </Badge>
              );
            })}
          </div>
        )}

        <p className="text-[10px] text-text-muted mt-1.5">
          {new Date(message.created_at).toLocaleTimeString("zh-CN", {
            hour: "2-digit",
            minute: "2-digit",
          })}
        </p>
      </div>
    </div>
  );
}
