"use client";

import { useState, useEffect, useCallback } from "react";
import { api } from "@/lib/api";
import type { Role, RoleCreate } from "@/lib/types";
import { useAuth } from "@/hooks/useAuth";
import { REMOTE_POLICY_LABELS, LEVEL_LABELS } from "@/lib/constants";
import { Card, CardContent } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { CreateRoleForm } from "./_components/CreateRoleForm";

/* ── 主页面 ─────────────────────────────────────────── */

export default function RolesPage() {
  const { user } = useAuth();
  const companyId = user?.company_id;

  const [roles, setRoles] = useState<Role[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);

  const fetchRoles = useCallback(() => {
    if (!companyId) return;
    setLoading(true);
    api
      .getRoles(companyId)
      .then(setRoles)
      .catch(() => setError("加载岗位列表失败，请稍后重试。"))
      .finally(() => setLoading(false));
  }, [companyId]);

  useEffect(() => {
    fetchRoles();
  }, [fetchRoles]);

  const handleCreate = async (data: RoleCreate) => {
    await api.createRole(data);
    setShowForm(false);
    fetchRoles();
  };

  const handleDeactivate = async (roleId: string) => {
    await api.deleteRole(roleId);
    fetchRoles();
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4">
        <p className="text-rose text-sm">{error}</p>
        <Button variant="secondary" onClick={fetchRoles}>
          重试
        </Button>
      </div>
    );
  }

  return (
    <div>
      {/* 页面标题 */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold font-display text-text">
            岗位管理
          </h1>
          <p className="text-sm text-text-dim mt-1">
            共 {roles.length} 个在招岗位
          </p>
        </div>
        <Button onClick={() => setShowForm(!showForm)}>
          {showForm ? "取消" : "新建岗位"}
        </Button>
      </div>

      {/* 创建表单（展开区域） */}
      {showForm && (
        <CreateRoleForm
          onSubmit={handleCreate}
          onCancel={() => setShowForm(false)}
        />
      )}

      {/* 岗位列表 */}
      {roles.length === 0 ? (
        <EmptyState />
      ) : (
        <div className="grid gap-4">
          {roles.map((role) => (
            <RoleCard
              key={role.id}
              role={role}
              onDeactivate={() => handleDeactivate(role.id)}
            />
          ))}
        </div>
      )}
    </div>
  );
}

/* ── 空状态 ─────────────────────────────────────────── */

function EmptyState() {
  return (
    <Card>
      <CardContent className="py-12 text-center">
        <p className="text-text-dim text-sm mb-2">暂无岗位。</p>
        <p className="text-text-muted text-xs">
          点击「新建岗位」添加第一个招聘岗位。
        </p>
      </CardContent>
    </Card>
  );
}

/* ── 岗位卡片 ───────────────────────────────────────── */

function RoleCard({
  role,
  onDeactivate,
}: {
  role: Role;
  onDeactivate: () => void;
}) {
  const salaryText =
    role.salary_range && role.salary_range.min > 0
      ? `${role.salary_range.min / 1000}k - ${role.salary_range.max / 1000}k ${role.salary_range.currency}`
      : null;

  return (
    <Card>
      <CardContent className="py-5">
        <div className="flex items-start justify-between gap-4">
          <div className="flex-1 min-w-0">
            {/* 标题行 */}
            <div className="flex items-center gap-2 mb-2 flex-wrap">
              <h3 className="text-base font-semibold text-text">
                {role.title}
              </h3>
              {role.level && (
                <Badge>{LEVEL_LABELS[role.level] ?? role.level}</Badge>
              )}
              {!role.is_active && <Badge variant="danger">已停用</Badge>}
            </div>

            {/* 技能标签 */}
            {role.skills.length > 0 && (
              <div className="flex flex-wrap gap-1.5 mb-3">
                {role.skills.map((skill) => (
                  <span
                    key={skill}
                    className="px-2 py-0.5 text-xs rounded-full bg-surface-light text-text-dim"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            )}

            {/* 信息行 */}
            <div className="flex items-center gap-4 text-xs text-text-muted flex-wrap">
              {role.location && <span>{role.location}</span>}
              {role.remote_policy && (
                <span>
                  {REMOTE_POLICY_LABELS[role.remote_policy] ??
                    role.remote_policy}
                </span>
              )}
              {salaryText && <span>{salaryText}</span>}
            </div>
          </div>

          {/* 操作按钮 */}
          <div className="shrink-0">
            {role.is_active && (
              <Button variant="ghost" size="sm" onClick={onDeactivate}>
                停用
              </Button>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
