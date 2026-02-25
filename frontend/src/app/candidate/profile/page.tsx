"use client";

import { useState, useEffect, useRef } from "react";
import { api } from "@/lib/api";
import { useAuth } from "@/hooks/useAuth";
import type { UserProfile } from "@/lib/types";
import { Card, CardHeader, CardContent } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";

export default function CandidateProfilePage() {
  const { user } = useAuth();
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const [uploading, setUploading] = useState(false);
  const fileRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (!user) return;
    api
      .getProfile(user.id)
      .then(setProfile)
      .catch(() => setProfile(null))
      .finally(() => setLoading(false));
  }, [user]);

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setUploading(true);
    try {
      const updated = await api.upload<UserProfile>("/resume/upload", file);
      setProfile(updated);
    } catch {
      // silently fail for demo
    } finally {
      setUploading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="w-8 h-8 border-2 border-indigo border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  return (
    <div className="max-w-3xl">
      <div className="mb-8">
        <h1 className="text-2xl font-bold font-display text-text">个人档案</h1>
        <p className="text-sm text-text-dim mt-1">
          你的综合职业画像 — 由 AI 对话、简历解析和问卷数据汇总
        </p>
      </div>

      {/* Resume upload */}
      <Card className="mb-6">
        <CardHeader>
          <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
            简历上传
          </h2>
        </CardHeader>
        <CardContent>
          <div className="flex items-center gap-4">
            <input
              ref={fileRef}
              type="file"
              accept=".pdf,.txt,.doc,.docx"
              className="hidden"
              onChange={handleUpload}
            />
            <Button
              variant="secondary"
              onClick={() => fileRef.current?.click()}
              disabled={uploading}
            >
              {uploading ? "解析中..." : "上传简历"}
            </Button>
            <span className="text-xs text-text-muted">
              支持 PDF、TXT 格式，最大 10MB
            </span>
          </div>
          {profile?.resume_text && (
            <p className="text-xs text-emerald mt-2">简历已上传并解析完成</p>
          )}
        </CardContent>
      </Card>

      {!profile ? (
        <EmptyProfileState />
      ) : (
        <>
          <BasicInfoCard profile={profile} />
          <SkillsCard skills={profile.skills} />
          <EducationCard education={profile.education} />
          {profile.chat_summary && <ChatSummaryCard summary={profile.chat_summary} />}
        </>
      )}
    </div>
  );
}

function BasicInfoCard({ profile }: { profile: UserProfile }) {
  return (
    <Card className="mb-6">
      <CardHeader>
        <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
          基本信息
        </h2>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-2 gap-4">
          <InfoItem label="职位" value={profile.title} />
          <InfoItem label="工作年限" value={profile.years_experience ? `${profile.years_experience} 年` : undefined} />
          <InfoItem label="所在地" value={profile.location} />
          <InfoItem label="办公偏好" value={profile.remote_preference} />
        </div>
        {profile.bio && (
          <p className="mt-4 text-sm text-text-dim leading-relaxed">{profile.bio}</p>
        )}
      </CardContent>
    </Card>
  );
}

function SkillsCard({ skills }: { skills: string[] }) {
  if (!skills.length) return null;
  return (
    <Card className="mb-6">
      <CardHeader>
        <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
          技能标签
        </h2>
      </CardHeader>
      <CardContent>
        <div className="flex flex-wrap gap-2">
          {skills.map((skill) => (
            <Badge key={skill} variant="default">{skill}</Badge>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}

function EducationCard({ education }: { education: Array<{ degree: string; school: string; major: string }> }) {
  if (!education.length) return null;
  return (
    <Card className="mb-6">
      <CardHeader>
        <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
          教育背景
        </h2>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          {education.map((edu, i) => (
            <div key={i} className="text-sm">
              <span className="text-text font-medium">{edu.school}</span>
              <span className="text-text-dim ml-2">{edu.degree} · {edu.major}</span>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}

function ChatSummaryCard({ summary }: { summary: string }) {
  return (
    <Card className="mb-6">
      <CardHeader>
        <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
          AI 对话摘要
        </h2>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-text-dim leading-relaxed">{summary}</p>
      </CardContent>
    </Card>
  );
}

function InfoItem({ label, value }: { label: string; value?: string | null }) {
  return (
    <div>
      <span className="text-xs text-text-muted">{label}</span>
      <p className="text-sm text-text mt-0.5">{value || "—"}</p>
    </div>
  );
}

function EmptyProfileState() {
  return (
    <Card>
      <CardContent>
        <div className="text-center py-8">
          <p className="text-text-dim text-sm">
            你的档案尚未建立。试试上传简历或与 AI 对话来开始。
          </p>
        </div>
      </CardContent>
    </Card>
  );
}
