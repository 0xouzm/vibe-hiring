import type { HTMLAttributes, ReactNode } from "react";

/* ── Card ───────────────────────────────────────────── */

interface CardProps extends HTMLAttributes<HTMLDivElement> {
  glass?: boolean;
}

export function Card({
  glass = false,
  className = "",
  children,
  ...props
}: CardProps) {
  const base = [
    "rounded-[var(--radius-xl)]",
    "border border-glass-border",
    "overflow-hidden",
  ];

  const style = glass
    ? [...base, "glass"]
    : [...base, "bg-surface", "shadow-sm"];

  return (
    <div className={[...style, className].join(" ")} {...props}>
      {children}
    </div>
  );
}

/* ── Card Header ────────────────────────────────────── */

interface CardSectionProps {
  className?: string;
  children: ReactNode;
}

export function CardHeader({ className = "", children }: CardSectionProps) {
  return (
    <div className={`px-6 pt-6 pb-2 ${className}`}>
      {children}
    </div>
  );
}

/* ── Card Content ───────────────────────────────────── */

export function CardContent({ className = "", children }: CardSectionProps) {
  return (
    <div className={`px-6 py-4 ${className}`}>
      {children}
    </div>
  );
}

/* ── Card Footer ────────────────────────────────────── */

export function CardFooter({ className = "", children }: CardSectionProps) {
  return (
    <div
      className={`px-6 py-4 border-t border-glass-border ${className}`}
    >
      {children}
    </div>
  );
}
