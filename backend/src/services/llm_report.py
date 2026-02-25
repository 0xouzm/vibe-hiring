"""LLM-driven match report generation — replaces template reports."""

import json

from openai import AsyncOpenAI

from src.core.config import settings
from src.models.dna_score import DIMENSIONS, DimensionScores
from src.services.report import generate_simple_report

REPORT_PROMPT = """你是知遇（TalentDrop）的匹配分析师。请根据以下数据生成一份深度匹配报告。

## 候选人信息
- 姓名：{candidate_name}
- 职位：{candidate_title}
- 技能：{candidate_skills}
- 简介：{candidate_bio}

## 企业/岗位信息
- 公司：{company_name}
- 岗位：{role_title}
- 岗位要求：{role_skills}
- 岗位描述：{role_description}

## DNA 匹配数据
- 总体匹配度：{match_score}%
- 各维度对比（候选人 vs 企业）：
{dimension_comparison}

## 报告要求

请用中文输出以下三个部分的报告：

### 1. 匹配亮点
分析 2-3 个匹配度最高的维度，解释为什么这些方面高度契合。结合候选人的实际背景和岗位需求给出具体洞察。

### 2. 需要探索的方面
分析 1-2 个差异较大的维度，不要用负面措辞。而是提出建设性的问题或建议，帮助双方在面试中深入了解。

### 3. 深度洞察
基于候选人的整体画像和公司文化，给出一段综合性的分析。这段应该是最有价值的：预测候选人在这个环境中可能的表现、成长路径、以及需要的支持。

请用 Markdown 格式输出。"""


async def generate_llm_report(
    candidate_name: str,
    company_name: str,
    match_score: float,
    candidate_dna: DimensionScores,
    company_dna: DimensionScores,
    consistency: float = 0.85,
    candidate_title: str | None = None,
    candidate_skills: list[str] | None = None,
    candidate_bio: str | None = None,
    role_title: str | None = None,
    role_skills: list[str] | None = None,
    role_description: str | None = None,
) -> str:
    """Generate a match report using LLM.

    Falls back to template report if no API key is configured.
    """
    if not settings.openai_api_key:
        dim_dict = {d: getattr(candidate_dna, d) for d in DIMENSIONS}
        return generate_simple_report(
            candidate_name=candidate_name,
            company_name=company_name,
            match_score=match_score,
            dimension_scores=dim_dict,
            candidate_dna=candidate_dna,
            company_dna=company_dna,
            consistency=consistency,
        )

    # Build dimension comparison text
    dim_lines: list[str] = []
    dim_labels = {
        "pace": "工作节奏", "collab": "协作模式", "decision": "决策风格",
        "expression": "表达风格", "unc": "不确定性容忍", "growth": "成长路径",
        "motiv": "驱动力", "execution": "执行风格",
    }
    for dim in DIMENSIONS:
        c_val = getattr(candidate_dna, dim)
        j_val = getattr(company_dna, dim)
        diff = abs(c_val - j_val)
        dim_lines.append(
            f"  - {dim_labels[dim]}: 候选人 {c_val} vs 企业 {j_val} (差距 {diff})"
        )

    prompt = REPORT_PROMPT.format(
        candidate_name=candidate_name,
        candidate_title=candidate_title or "未提供",
        candidate_skills=", ".join(candidate_skills) if candidate_skills else "未提供",
        candidate_bio=candidate_bio or "未提供",
        company_name=company_name,
        role_title=role_title or "未提供",
        role_skills=", ".join(role_skills) if role_skills else "未提供",
        role_description=role_description or "未提供",
        match_score=match_score,
        dimension_comparison="\n".join(dim_lines),
    )

    client = AsyncOpenAI(api_key=settings.openai_api_key)
    response = await client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": "你是一位专业的人才匹配分析师。"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=1200,
    )

    return response.choices[0].message.content or "报告生成失败"
