"use client";

import { useState } from "react";
import type { RoleCreate } from "@/lib/types";
import { REMOTE_POLICY_LABELS, LEVEL_LABELS } from "@/lib/constants";
import { Card, CardHeader, CardContent } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";

/* ── 表单初始值 ─────────────────────────────────────── */

const EMPTY_FORM: RoleCreate = {
  title: "",
  level: "mid",
  skills: [],
  nice_to_have: [],
  salary_range: { min: 0, max: 0, currency: "CNY" },
  location: "",
  remote_policy: "onsite",
  description: "",
};

/* ── 选择器样式（共用） ───────────────────────────────── */

const selectClass = [
  "w-full h-10 px-3 rounded-[var(--radius-lg)]",
  "border border-glass-border bg-surface text-text",
  "focus:outline-2 focus:outline-offset-0 focus:outline-indigo",
].join(" ");

const numberInputClass = [
  "w-full h-10 px-3 rounded-[var(--radius-lg)]",
  "border border-glass-border bg-surface text-text",
  "placeholder:text-text-muted",
  "focus:outline-2 focus:outline-offset-0 focus:outline-indigo",
].join(" ");

/* ── 创建岗位表单 ───────────────────────────────────── */

export function CreateRoleForm({
  onSubmit,
  onCancel,
}: {
  onSubmit: (data: RoleCreate) => Promise<void>;
  onCancel: () => void;
}) {
  const [form, setForm] = useState<RoleCreate>({ ...EMPTY_FORM });
  const [skillsInput, setSkillsInput] = useState("");
  const [submitting, setSubmitting] = useState(false);

  const update = <K extends keyof RoleCreate>(key: K, val: RoleCreate[K]) =>
    setForm((prev) => ({ ...prev, [key]: val }));

  const handleSubmit = async () => {
    if (!form.title.trim()) return;
    setSubmitting(true);
    const skills = skillsInput
      .split(/[,，]/)
      .map((s) => s.trim())
      .filter(Boolean);
    try {
      await onSubmit({ ...form, skills });
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Card className="mb-6">
      <CardHeader>
        <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
          新建岗位
        </h2>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Input
            label="岗位名称"
            placeholder="如：高级前端工程师"
            value={form.title}
            onChange={(e) => update("title", e.target.value)}
          />

          <SelectField
            label="级别"
            value={form.level ?? "mid"}
            options={LEVEL_LABELS}
            onChange={(v) => update("level", v)}
          />

          <Input
            label="技能要求（逗号分隔）"
            placeholder="如：React, TypeScript, Node.js"
            value={skillsInput}
            onChange={(e) => setSkillsInput(e.target.value)}
          />

          <Input
            label="工作地点"
            placeholder="如：北京 / 上海"
            value={form.location ?? ""}
            onChange={(e) => update("location", e.target.value)}
          />

          <SelectField
            label="办公方式"
            value={form.remote_policy ?? "onsite"}
            options={REMOTE_POLICY_LABELS}
            onChange={(v) => update("remote_policy", v)}
          />

          {/* 薪资区间 */}
          <div className="w-full">
            <label className="block text-sm font-medium text-text mb-1.5">
              薪资范围（元/月）
            </label>
            <div className="flex items-center gap-2">
              <input
                type="number"
                placeholder="最低"
                value={form.salary_range?.min || ""}
                onChange={(e) =>
                  update("salary_range", {
                    min: Number(e.target.value),
                    max: form.salary_range?.max ?? 0,
                    currency: form.salary_range?.currency ?? "CNY",
                  })
                }
                className={numberInputClass}
              />
              <span className="text-text-muted text-sm shrink-0">—</span>
              <input
                type="number"
                placeholder="最高"
                value={form.salary_range?.max || ""}
                onChange={(e) =>
                  update("salary_range", {
                    min: form.salary_range?.min ?? 0,
                    max: Number(e.target.value),
                    currency: form.salary_range?.currency ?? "CNY",
                  })
                }
                className={numberInputClass}
              />
            </div>
          </div>
        </div>

        {/* 岗位描述 */}
        <div className="mt-4">
          <label className="block text-sm font-medium text-text mb-1.5">
            岗位描述
          </label>
          <textarea
            rows={3}
            placeholder="岗位职责、工作内容等"
            value={form.description ?? ""}
            onChange={(e) => update("description", e.target.value)}
            className="w-full px-3 py-2 rounded-[var(--radius-lg)] border border-glass-border bg-surface text-text placeholder:text-text-muted focus:outline-2 focus:outline-offset-0 focus:outline-indigo resize-none"
          />
        </div>

        {/* 操作按钮 */}
        <div className="flex items-center justify-end gap-3 mt-5">
          <Button variant="ghost" onClick={onCancel}>
            取消
          </Button>
          <Button
            onClick={handleSubmit}
            loading={submitting}
            disabled={!form.title.trim()}
          >
            创建岗位
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}

/* ── 通用选择器字段 ─────────────────────────────────── */

function SelectField({
  label,
  value,
  options,
  onChange,
}: {
  label: string;
  value: string;
  options: Record<string, string>;
  onChange: (value: string) => void;
}) {
  return (
    <div className="w-full">
      <label className="block text-sm font-medium text-text mb-1.5">
        {label}
      </label>
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className={selectClass}
      >
        {Object.entries(options).map(([key, text]) => (
          <option key={key} value={key}>
            {text}
          </option>
        ))}
      </select>
    </div>
  );
}
