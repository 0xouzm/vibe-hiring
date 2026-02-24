import type { ReactNode } from "react";

type BadgeVariant = "default" | "success" | "warning" | "danger";

const variantStyles: Record<BadgeVariant, string> = {
  default: "bg-indigo/10 text-indigo",
  success: "bg-emerald/10 text-emerald",
  warning: "bg-amber/10 text-amber",
  danger: "bg-rose/10 text-rose",
};

interface BadgeProps {
  variant?: BadgeVariant;
  className?: string;
  children: ReactNode;
}

export function Badge({
  variant = "default",
  className = "",
  children,
}: BadgeProps) {
  return (
    <span
      className={[
        "inline-flex items-center px-2.5 py-0.5",
        "text-xs font-medium rounded-full",
        variantStyles[variant],
        className,
      ].join(" ")}
    >
      {children}
    </span>
  );
}

export type { BadgeVariant };
