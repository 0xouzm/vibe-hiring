import {
  BIG_FIVE_MAP,
  PAIN_POINTS,
  LAYERS,
  ENGINE_LAYERS,
} from "./section-data";

/* ── 行业痛点 ─────────────────────────────────────────────────────── */

export function PainSection() {
  return (
    <div className="grid grid-cols-2 sm:grid-cols-5 gap-3">
      {PAIN_POINTS.map((p) => (
        <div key={p.label} className="text-center p-4 rounded-xl border border-white/10 bg-white/5">
          <div className="text-2xl font-bold font-display mb-1" style={{ color: "#ff6b4a" }}>{p.pct}</div>
          <div className="text-sm font-semibold text-white mb-1">{p.label}</div>
          <div className="text-xs text-white/50">{p.desc}</div>
        </div>
      ))}
    </div>
  );
}

/* ── Career DNA 理论框架 ──────────────────────────────────────────── */

export function DnaSection() {
  return (
    <div>
      <div className="overflow-x-auto rounded-xl border border-white/10">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-white/10 text-left text-white/50">
              <th className="px-4 py-2">Big Five 来源</th>
              <th className="px-4 py-2">Career DNA 维度</th>
              <th className="px-4 py-2">测量内容</th>
            </tr>
          </thead>
          <tbody>
            {BIG_FIVE_MAP.map((r, i) => (
              <tr key={r.dim} className={i % 2 === 0 ? "bg-white/5" : ""}>
                <td className="px-4 py-2 text-white/60">{r.big5}</td>
                <td className="px-4 py-2 font-semibold" style={{ color: "#6366f1" }}>{r.dim}</td>
                <td className="px-4 py-2 text-white/80">{r.measure}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="mt-4 text-center text-sm text-white/60 italic">
        &quot;所有维度都是光谱，两端都合理，没有正确答案&quot;
      </p>
    </div>
  );
}

/* ── 三层问卷架构 ─────────────────────────────────────────────────── */

export function ArchSection() {
  return (
    <div className="space-y-4">
      <div className="flex gap-3 justify-center flex-wrap">
        {LAYERS.map((l) => (
          <div key={l.name} className="flex-1 min-w-[140px] p-4 rounded-xl border border-white/10 bg-white/5 text-center">
            <div className="text-lg font-bold font-display" style={{ color: l.color }}>{l.count}</div>
            <div className="text-sm text-white font-medium">{l.name}</div>
            <div className="text-xs text-white/50 mt-1">权重 {l.weight}</div>
          </div>
        ))}
      </div>
      <div className="p-3 rounded-xl border border-white/10 bg-white/5 text-center">
        <span className="text-sm text-white/70">反作弊机制：</span>
        <span className="text-sm text-white/90">行为场景 · 强制排序 · 交叉验证 · 一致性评分</span>
      </div>
    </div>
  );
}

/* ── 匹配引擎 ─────────────────────────────────────────────────────── */

export function EngineSection() {
  return (
    <div className="space-y-2">
      {ENGINE_LAYERS.map((l) => (
        <div key={l.id} className="flex items-center gap-4 p-3 rounded-xl border border-white/10 bg-white/5">
          <span className="text-xs font-bold px-2 py-1 rounded-md shrink-0" style={{ background: l.color, color: "#070b1a" }}>{l.id}</span>
          <div>
            <div className="text-sm font-semibold text-white">{l.name}</div>
            <div className="text-xs text-white/50">{l.desc}</div>
          </div>
        </div>
      ))}
    </div>
  );
}

/* ── 双向发现 ─────────────────────────────────────────────────────── */

const FLOW_CARDS = [
  { role: "候选人", color: "#6366f1", steps: ["填写 Career DNA", "每周收到 1-3 个匹配岗位", "查看兼容性报告 → 接受 / 跳过"] },
  { role: "企业", color: "#f59e0b", steps: ["填写 Company DNA", "发布岗位 → 自动匹配", "每周收到 3-5 位候选人推荐"] },
  { role: "Mutual Match", color: "#10b981", steps: ["双方都选择「接受」", "开启沟通通道", "面试 → 入职 → 90 天追踪"] },
];

export function FlowSection() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {FLOW_CARDS.map((c) => (
        <div key={c.role} className="p-4 rounded-xl border border-white/10 bg-white/5">
          <div className="text-sm font-bold font-display mb-3" style={{ color: c.color }}>{c.role}</div>
          <ol className="space-y-2">
            {c.steps.map((s, i) => (
              <li key={i} className="flex items-start gap-2 text-xs text-white/70">
                <span className="shrink-0 w-5 h-5 flex items-center justify-center rounded-full text-[10px] font-bold" style={{ background: c.color, color: "#070b1a" }}>{i + 1}</span>
                {s}
              </li>
            ))}
          </ol>
        </div>
      ))}
    </div>
  );
}

/* ── 数据飞轮 ─────────────────────────────────────────────────────── */

const FLYWHEEL_STEPS = ["匹配落地", "90 天追踪", "知识图谱更新", "算法进化", "更精准匹配"];

export function FlywheelSection() {
  return (
    <div className="flex flex-col items-center gap-6">
      <div className="flex flex-wrap justify-center gap-3">
        {FLYWHEEL_STEPS.map((step, i, arr) => (
          <div key={step} className="flex items-center gap-2">
            <span className="px-3 py-2 rounded-lg text-sm font-medium border border-white/10 bg-white/5 text-white">{step}</span>
            {i < arr.length - 1 && <span className="text-white/30 text-lg">&rarr;</span>}
          </div>
        ))}
      </div>
      <p className="text-lg font-display font-semibold text-center" style={{ color: "#ff6b4a" }}>
        &quot;职遇，让招聘回归双向奔赴&quot;
      </p>
    </div>
  );
}
