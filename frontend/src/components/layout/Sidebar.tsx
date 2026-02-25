"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useAuth } from "@/hooks/useAuth";

/* ── Navigation items per role ──────────────────────── */

interface NavItem {
  label: string;
  href: string;
  icon: string;
}

const candidateNav: NavItem[] = [
  { label: "仪表盘", href: "/candidate/dashboard", icon: "grid" },
  { label: "AI 对话", href: "/candidate/chat", icon: "chat" },
  { label: "个人档案", href: "/candidate/profile", icon: "profile" },
  { label: "我的 DNA", href: "/candidate/questionnaire", icon: "dna" },
  { label: "每周推荐", href: "/candidate/drop", icon: "sparkle" },
];

const hrNav: NavItem[] = [
  { label: "仪表盘", href: "/company/dashboard", icon: "grid" },
  { label: "企业 DNA", href: "/company/questionnaire", icon: "building" },
  { label: "岗位管理", href: "/company/roles", icon: "briefcase" },
  { label: "每周推荐", href: "/company/drop", icon: "sparkle" },
  { label: "候选人", href: "/company/candidates", icon: "users" },
  { label: "邀请成员", href: "/company/invite", icon: "mail" },
];

/* ── Component ──────────────────────────────────────── */

export function Sidebar() {
  const { user } = useAuth();
  const pathname = usePathname();

  if (!user) return null;

  const navItems = user.role === "hr" ? hrNav : candidateNav;

  return (
    <aside className="fixed top-16 left-0 bottom-0 w-60 border-r border-glass-border bg-surface z-30">
      <nav className="flex flex-col gap-1 p-4">
        {navItems.map((item) => {
          const isActive = pathname.startsWith(item.href);
          return (
            <Link
              key={item.href}
              href={item.href}
              className={[
                "flex items-center gap-3 px-3 py-2.5",
                "rounded-[var(--radius-lg)] text-sm font-medium",
                "transition-colors",
                isActive
                  ? "bg-indigo/10 text-indigo"
                  : "text-text-dim hover:text-text hover:bg-surface-light",
              ].join(" ")}
            >
              <NavIcon name={item.icon} />
              {item.label}
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}

/* ── Simple icon set ────────────────────────────────── */

function NavIcon({ name }: { name: string }) {
  const props = {
    width: 20,
    height: 20,
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 2,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
  };

  switch (name) {
    case "grid":
      return (
        <svg {...props}>
          <rect x="3" y="3" width="7" height="7" rx="1" />
          <rect x="14" y="3" width="7" height="7" rx="1" />
          <rect x="3" y="14" width="7" height="7" rx="1" />
          <rect x="14" y="14" width="7" height="7" rx="1" />
        </svg>
      );
    case "chat":
      return (
        <svg {...props}>
          <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" />
        </svg>
      );
    case "profile":
      return (
        <svg {...props}>
          <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2" />
          <circle cx="12" cy="7" r="4" />
        </svg>
      );
    case "dna":
      return (
        <svg {...props}>
          <path d="M2 15c6.667-6 13.333 0 20-6" />
          <path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993" />
          <path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993" />
          <path d="M17 6l-2.5 2.5" />
          <path d="M14 8l-1.5 1.5" />
          <path d="M7 18l2.5-2.5" />
          <path d="M3.5 14.5l.5-.5" />
          <path d="M20 9l.5-.5" />
          <path d="M2 15c6.667-6 13.333 0 20-6" />
        </svg>
      );
    case "sparkle":
      return (
        <svg {...props}>
          <path d="M12 3l1.912 5.813a2 2 0 001.275 1.275L21 12l-5.813 1.912a2 2 0 00-1.275 1.275L12 21l-1.912-5.813a2 2 0 00-1.275-1.275L3 12l5.813-1.912a2 2 0 001.275-1.275L12 3z" />
        </svg>
      );
    case "building":
      return (
        <svg {...props}>
          <rect x="4" y="2" width="16" height="20" rx="2" />
          <path d="M9 22v-4h6v4" />
          <path d="M8 6h.01M16 6h.01M12 6h.01M8 10h.01M16 10h.01M12 10h.01M8 14h.01M16 14h.01M12 14h.01" />
        </svg>
      );
    case "briefcase":
      return (
        <svg {...props}>
          <rect x="2" y="7" width="20" height="14" rx="2" />
          <path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2" />
          <path d="M12 12h.01" />
        </svg>
      );
    case "users":
      return (
        <svg {...props}>
          <path d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2" />
          <circle cx="9" cy="7" r="4" />
          <path d="M22 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75" />
        </svg>
      );
    case "mail":
      return (
        <svg {...props}>
          <rect x="2" y="4" width="20" height="16" rx="2" />
          <path d="M22 7l-10 7L2 7" />
        </svg>
      );
    default:
      return <span className="w-5 h-5" />;
  }
}
