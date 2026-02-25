"""Resume parsing service — extract structured data from PDF/text resumes."""

import json
import re

from openai import AsyncOpenAI

from src.core.config import settings

PARSE_PROMPT = """从以下简历文本中提取结构化信息，以 JSON 格式返回：

```json
{
  "title": "当前职位",
  "years_experience": 数字,
  "skills": ["技能1", "技能2"],
  "education": [{"degree": "学位", "school": "学校", "major": "专业"}],
  "bio": "一句话职业总结"
}
```

只返回 JSON，不要其他文字。

简历内容：
"""


async def parse_resume_text(text: str) -> dict:
    """Parse resume text into structured profile data.

    Uses OpenAI if API key is available, otherwise falls back to regex extraction.
    """
    if not settings.openai_api_key:
        return _regex_extract(text)

    client = AsyncOpenAI(api_key=settings.openai_api_key)
    response = await client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": "你是一个简历解析助手。只输出 JSON。"},
            {"role": "user", "content": PARSE_PROMPT + text[:3000]},
        ],
        temperature=0,
        max_tokens=500,
    )

    content = response.choices[0].message.content or "{}"
    # Extract JSON from response
    try:
        # Try to find JSON block
        json_match = re.search(r"\{[\s\S]*\}", content)
        if json_match:
            return json.loads(json_match.group())
    except json.JSONDecodeError:
        pass

    return _regex_extract(text)


def _regex_extract(text: str) -> dict:
    """Simple regex-based extraction as fallback."""
    # Extract email-like skills
    skill_keywords = [
        "Python", "Java", "JavaScript", "TypeScript", "React", "Vue",
        "Node.js", "Go", "Rust", "C++", "SQL", "PostgreSQL", "MongoDB",
        "Docker", "Kubernetes", "AWS", "GCP", "Azure", "Git",
        "Machine Learning", "AI", "TensorFlow", "PyTorch",
        "Spring Boot", "FastAPI", "Django", "Flask",
        "Next.js", "Tailwind", "GraphQL", "Redis", "Kafka",
    ]

    found_skills = [
        s for s in skill_keywords
        if s.lower() in text.lower()
    ]

    # Try to find years of experience
    years_match = re.search(r"(\d+)\s*[+年]?\s*(years?|年)", text, re.IGNORECASE)
    years = int(years_match.group(1)) if years_match else None

    return {
        "skills": found_skills,
        "years_experience": years,
        "title": None,
        "education": [],
        "bio": None,
    }


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract text from PDF bytes.

    Uses pdfplumber if available, otherwise returns a placeholder.
    """
    try:
        import pdfplumber
        import io
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            pages = [page.extract_text() or "" for page in pdf.pages]
            return "\n\n".join(pages)
    except ImportError:
        # pdfplumber not installed — return raw text attempt
        text = pdf_bytes.decode("utf-8", errors="ignore")
        # Filter out binary garbage
        text = re.sub(r"[^\x20-\x7e\u4e00-\u9fff\n]", "", text)
        return text[:5000]
