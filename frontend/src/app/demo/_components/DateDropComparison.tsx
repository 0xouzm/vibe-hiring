import { DATE_DROP_STATS, COMPARISON_ROWS } from "./section-data";

/* ── Date Drop 对标 section ───────────────────────────────────────── */

export function DateDropComparison() {
  return (
    <div className="space-y-8">
      {/* 1 — Date Drop 概况四宫格 */}
      <div>
        <h3 className="text-sm font-semibold text-white/60 uppercase tracking-wide mb-3">
          Date Drop 核心数据
        </h3>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          {DATE_DROP_STATS.map((s) => (
            <div
              key={s.label}
              className="text-center p-4 rounded-xl border border-white/10 bg-white/5"
            >
              <div
                className="text-2xl font-bold font-display mb-1"
                style={{ color: "#a855f7" }}
              >
                {s.value}
              </div>
              <div className="text-sm font-semibold text-white mb-0.5">
                {s.label}
              </div>
              <div className="text-xs text-white/50">{s.desc}</div>
            </div>
          ))}
        </div>
      </div>

      {/* 2 — 维度对比表格 */}
      <div className="overflow-x-auto rounded-xl border border-white/10">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-white/10 text-left">
              <th className="px-4 py-3 text-white/50 w-[100px]">维度</th>
              <th className="px-4 py-3 text-white/50">
                Date Drop（约会）
              </th>
              <th className="px-4 py-3" style={{ color: "#a855f7" }}>
                职遇（招聘）
              </th>
            </tr>
          </thead>
          <tbody>
            {COMPARISON_ROWS.map((row, i) => (
              <tr
                key={row.dim}
                className={i % 2 === 0 ? "bg-white/5" : ""}
              >
                <td className="px-4 py-2.5 text-white/70 font-medium">
                  {row.dim}
                </td>
                <td className="px-4 py-2.5 text-white/60">{row.dateDrop}</td>
                <td className="px-4 py-2.5">
                  {row.highlight ? (
                    <span className="font-semibold" style={{ color: "#a855f7" }}>
                      {row.zhiyu}
                    </span>
                  ) : (
                    <span className="text-white/80">{row.zhiyu}</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* 3 — 底部总结 */}
      <div className="p-4 rounded-xl border border-white/10 bg-white/5 text-center space-y-2">
        <p className="text-sm text-white/80 leading-relaxed">
          Date Drop 已在约会场景验证了<strong className="text-white">「深度问卷 + 每周 Drop + 双向选择」</strong>的模式可行性，
          实现了 <strong className="text-white">10 倍于 Tinder</strong> 的成功配对率。
        </p>
        <p className="text-sm leading-relaxed" style={{ color: "#a855f7" }}>
          职遇将这一范式迁移到招聘领域，并以三层问卷架构、五层匹配引擎和 LightRAG 知识图谱做出核心差异化。
        </p>
      </div>
    </div>
  );
}
