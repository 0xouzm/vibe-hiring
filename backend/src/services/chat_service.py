"""AI chat service — conversational profiling with entity extraction."""

import json

from openai import AsyncOpenAI

from src.core.config import settings

SYSTEM_PROMPT = """你是职遇（TalentDrop）的 AI 职业顾问。你的目标是通过自然对话了解候选人的背景信息。

对话策略：
1. 先了解当前职位和工作经历
2. 探索技术技能和专长领域
3. 了解职业价值观和工作偏好
4. 询问期望的工作环境和团队文化

风格要求：
- 友好、专业、不像面试官
- 每次只问 1-2 个问题
- 根据对方回答自然追问
- 适当给出积极反馈

在每次回复的最后，用 JSON 格式提取实体信息（用户看不到这部分）：
```json
{"entities": {"skills": [], "experience": [], "values": [], "preferences": []}}
```
如果本轮对话没有新实体，返回空数组即可。"""


def _get_client() -> AsyncOpenAI:
    return AsyncOpenAI(api_key=settings.openai_api_key)


async def chat_completion(
    messages: list[dict[str, str]],
) -> tuple[str, dict | None]:
    """Send messages to OpenAI and return (response_text, extracted_entities).

    Falls back to a mock response if no API key is configured.
    """
    if not settings.openai_api_key:
        return _mock_response(messages)

    client = _get_client()
    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    response = await client.chat.completions.create(
        model=settings.openai_model,
        messages=full_messages,
        temperature=0.7,
        max_tokens=800,
    )

    content = response.choices[0].message.content or ""
    entities = _extract_entities(content)
    clean_text = _strip_entity_json(content)

    return clean_text, entities


def _extract_entities(text: str) -> dict | None:
    """Try to extract JSON entity block from response."""
    try:
        start = text.rfind('{"entities"')
        if start == -1:
            start = text.rfind("```json")
            if start != -1:
                start = text.index("{", start)
                end = text.index("}", start) + 1
                return json.loads(text[start:end])
            return None
        end = text.index("}", start) + 1
        # Handle nested braces
        depth = 0
        for i, ch in enumerate(text[start:], start):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        return json.loads(text[start:end])
    except (json.JSONDecodeError, ValueError):
        return None


def _strip_entity_json(text: str) -> str:
    """Remove the entity JSON block from user-visible text."""
    # Remove ```json...``` blocks
    import re
    text = re.sub(r"```json\s*\{.*?\}\s*```", "", text, flags=re.DOTALL)
    # Remove standalone {"entities"...} at end
    text = re.sub(r'\{"entities".*\}\s*$', "", text, flags=re.DOTALL)
    return text.strip()


def _mock_response(
    messages: list[dict[str, str]],
) -> tuple[str, dict | None]:
    """Provide a mock response when no API key is available."""
    turn = len([m for m in messages if m["role"] == "user"])

    mock_responses = [
        (
            "你好！欢迎来到职遇 🎯 我是你的 AI 职业顾问。\n\n"
            "在开始之前，能简单介绍一下你目前的工作情况吗？"
            "比如你现在的职位、所在行业、工作了多长时间？",
            None,
        ),
        (
            "听起来你的经历很丰富！你在技术方面有哪些核心技能和专长？"
            "平时最喜欢用哪些技术栈？",
            {"entities": {"skills": [], "experience": ["software engineering"],
                          "values": [], "preferences": []}},
        ),
        (
            "非常不错的技术栈！最后想了解一下你对未来工作的期望。"
            "你更看重什么——技术挑战、团队氛围、还是使命感？"
            "对远程办公有偏好吗？",
            {"entities": {"skills": ["Python", "React"], "experience": [],
                          "values": [], "preferences": []}},
        ),
        (
            "谢谢你的分享！我已经对你有了比较全面的了解。\n\n"
            "接下来你可以上传简历让我进一步分析，"
            "或者直接开始 Career DNA 测评来精确定位你的职业画像。",
            {"entities": {"skills": [], "experience": [],
                          "values": ["technical challenge", "team culture"],
                          "preferences": ["remote"]}},
        ),
    ]

    idx = min(turn, len(mock_responses) - 1)
    return mock_responses[idx]
