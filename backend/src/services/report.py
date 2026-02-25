"""简单的模板式匹配报告生成器（Phase 1）。

生成无需 LLM 的人类可读兼容性报告。
Phase 2 将由 LightRAG 驱动的生成器替代。
"""

from src.models.dna_score import DIMENSIONS, DimensionScores

# 各维度的中文标签
_DIM_LABELS: dict[str, str] = {
    "pace": "工作节奏",
    "collab": "协作模式",
    "decision": "决策风格",
    "expression": "表达风格",
    "unc": "不确定性容忍",
    "growth": "成长路径",
    "motiv": "驱动力来源",
    "execution": "执行风格",
}

# 光谱两端描述（高分端 / 低分端）
_DIM_DESCRIPTIONS: dict[str, tuple[str, str]] = {
    "pace": ("快速行动、行动导向", "深思熟虑、有条不紊"),
    "collab": ("独立自主、自驱型", "高度协作、团队优先"),
    "decision": ("数据驱动、分析型", "直觉驱动、经验型"),
    "expression": ("直接透明", "含蓄委婉"),
    "unc": ("拥抱模糊性", "偏好结构和清晰"),
    "growth": ("广泛探索的通才", "深度钻研的专家"),
    "motiv": ("使命和目标驱动", "稳定和回报驱动"),
    "execution": ("结构化、系统性", "灵活自适应"),
}


def _sorted_dimensions_by_gap(
    candidate: DimensionScores,
    company: DimensionScores,
) -> list[tuple[str, float, float, float]]:
    """返回按绝对差值升序排列的维度列表。

    每个元组：(维度名, 候选人值, 公司值, 差值)。
    """
    items: list[tuple[str, float, float, float]] = []
    for dim in DIMENSIONS:
        c_val = getattr(candidate, dim)
        j_val = getattr(company, dim)
        items.append((dim, c_val, j_val, abs(c_val - j_val)))
    return sorted(items, key=lambda x: x[3])


def _describe_alignment(dim: str, c_val: float, j_val: float) -> str:
    """生成一句关于候选人与公司在该维度上契合度的描述。"""
    label = _DIM_LABELS[dim]
    high_desc, low_desc = _DIM_DESCRIPTIONS[dim]

    # 双方都倾向光谱的同一端
    if c_val >= 55 and j_val >= 55:
        return f"**{label}** — 你们都偏好{high_desc}的方式。"
    if c_val <= 45 and j_val <= 45:
        return f"**{label}** — 你们都倾向{low_desc}的风格。"
    return f"**{label}** — 你们的偏好高度一致。"


def _describe_gap(dim: str, c_val: float, j_val: float) -> str:
    """生成一句关于维度差异、值得探索的描述。"""
    label = _DIM_LABELS[dim]
    high_desc, low_desc = _DIM_DESCRIPTIONS[dim]

    if c_val > j_val:
        return (
            f"**{label}** — 你偏向{high_desc}，"
            f"而公司更倾向{low_desc}的环境。"
            f"建议在面试中了解团队实际的做法。"
        )
    return (
        f"**{label}** — 你偏好{low_desc}的方式，"
        f"而公司文化更{high_desc}。"
        f"建议在交流中了解灵活度。"
    )


def _confidence_note(consistency: float) -> str:
    """根据一致性评分生成置信度说明。"""
    if consistency >= 0.85:
        return (
            "你的作答高度一致，我们对这份匹配评估有很强的置信度。"
        )
    if consistency >= 0.65:
        return (
            "你的作答整体上保持了良好的一致性，"
            "这份匹配评估具有较高的可靠性。"
        )
    return (
        "你在部分相关题目上的作答存在一定波动，"
        "这份匹配结果应作为方向性参考而非最终结论。"
    )


def generate_simple_report(
    candidate_name: str,
    company_name: str,
    match_score: float,
    dimension_scores: dict[str, float],  # noqa: ARG001 — 为后续使用预留
    candidate_dna: DimensionScores,
    company_dna: DimensionScores,
    consistency: float = 0.85,
) -> str:
    """生成模板式兼容性报告。

    报告分三节：
        1. 为什么你是绝佳匹配 — 差距最小的前 3 个维度。
        2. 需要探索的方面 — 差距最大的前 2 个维度。
        3. 置信度说明 — 基于一致性评分。

    Args:
        candidate_name: 候选人展示名。
        company_name: 公司展示名。
        match_score: 总体匹配百分比 (0-100)。
        dimension_scores: 各维度兼容性（v1 暂未使用）。
        candidate_dna: 候选人 8 维 Career DNA。
        company_dna: 公司 8 维 Company DNA。
        consistency: 候选人作答一致性，范围 [0, 1]。

    Returns:
        Markdown 格式的报告字符串。
    """
    sorted_dims = _sorted_dimensions_by_gap(candidate_dna, company_dna)
    top_matches = sorted_dims[:3]
    top_gaps = sorted_dims[-2:]

    lines: list[str] = [
        f"# 匹配报告：{candidate_name} + {company_name}",
        f"**总体匹配度：{match_score}%**",
        "",
        "## 为什么你是绝佳匹配",
        "",
    ]

    for dim, c_val, j_val, _gap in top_matches:
        lines.append(f"- {_describe_alignment(dim, c_val, j_val)}")

    lines.extend([
        "",
        "## 需要探索的方面",
        "",
    ])

    for dim, c_val, j_val, _gap in top_gaps:
        lines.append(f"- {_describe_gap(dim, c_val, j_val)}")

    lines.extend([
        "",
        "## 置信度说明",
        "",
        _confidence_note(consistency),
    ])

    return "\n".join(lines)
