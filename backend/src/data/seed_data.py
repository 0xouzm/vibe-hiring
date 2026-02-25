"""Seed data for demo — 3 companies, 6 candidates, roles, and profiles.

All scores sourced from discuss/demo-dataset.md.
"""

from src.models.dna_score import DimensionScores

# ── Seed companies ──────────────────────────────────────────────────

SEED_COMPANIES: list[dict] = [
    {
        "id": "velocity-labs",
        "name": "Velocity Labs",
        "industry": "Technology",
        "size": "50-200",
        "description": (
            "Fast-growing B2B SaaS startup, just closed Series B. "
            "Rapid product iteration, free engineering culture, remote-first."
        ),
        "scores": DimensionScores(
            pace=82, collab=40, decision=55, expression=78,
            unc=75, growth=35, motiv=70, execution=30,
        ),
        "cas": 81,
        "cas_tier": "Silver",
    },
    {
        "id": "meridian-financial",
        "name": "Meridian Financial Systems",
        "industry": "Fintech",
        "size": "2000+",
        "description": (
            "Public financial technology company serving banks and insurers. "
            "High compliance requirements, stable engineering, hybrid work."
        ),
        "scores": DimensionScores(
            pace=32, collab=68, decision=80, expression=45,
            unc=25, growth=55, motiv=40, execution=82,
        ),
        "cas": 88,
        "cas_tier": "Gold",
    },
    {
        "id": "bloom-education",
        "name": "Bloom Education",
        "industry": "EdTech",
        "size": "50-200",
        "description": (
            "Mission-driven edtech company helping K-12 schools personalize "
            "teaching. Young, passionate engineering team, office-first."
        ),
        "scores": DimensionScores(
            pace=60, collab=75, decision=48, expression=72,
            unc=58, growth=70, motiv=88, execution=55,
        ),
        "cas": 74,
        "cas_tier": "Silver",
    },
]

# ── Seed roles (open positions) ────────────────────────────────────

SEED_ROLES: list[dict] = [
    {
        "id": "role-vl-frontend",
        "company_id": "velocity-labs",
        "title": "高级前端工程师",
        "level": "senior",
        "skills": ["React", "TypeScript", "Next.js"],
        "nice_to_have": ["WebGL", "D3.js"],
        "salary_range": {"min": 250000, "max": 350000, "currency": "CNY"},
        "location": "远程",
        "remote_policy": "remote",
        "description": "负责核心产品前端架构设计与性能优化，打造极致用户体验。",
    },
    {
        "id": "role-vl-fullstack",
        "company_id": "velocity-labs",
        "title": "全栈工程师",
        "level": "mid",
        "skills": ["Python", "React", "PostgreSQL"],
        "nice_to_have": ["Go", "Kubernetes"],
        "salary_range": {"min": 200000, "max": 300000, "currency": "CNY"},
        "location": "远程",
        "remote_policy": "remote",
        "description": "参与从后端 API 到前端交互的全链路开发，快速迭代产品功能。",
    },
    {
        "id": "role-mf-backend",
        "company_id": "meridian-financial",
        "title": "后端工程师",
        "level": "senior",
        "skills": ["Java", "Spring Boot", "Oracle"],
        "nice_to_have": ["Kafka", "Redis"],
        "salary_range": {"min": 300000, "max": 450000, "currency": "CNY"},
        "location": "上海",
        "remote_policy": "hybrid",
        "description": "参与核心交易系统的后端开发，确保金融级别的稳定性和安全性。",
    },
    {
        "id": "role-mf-devops",
        "company_id": "meridian-financial",
        "title": "DevOps 工程师",
        "level": "mid",
        "skills": ["Docker", "Kubernetes", "CI/CD"],
        "nice_to_have": ["Terraform", "AWS"],
        "salary_range": {"min": 250000, "max": 400000, "currency": "CNY"},
        "location": "上海",
        "remote_policy": "hybrid",
        "description": "负责基础设施自动化、持续交付流水线和生产环境运维。",
    },
    {
        "id": "role-be-product",
        "company_id": "bloom-education",
        "title": "产品工程师",
        "level": "mid",
        "skills": ["React", "Node.js", "MongoDB"],
        "nice_to_have": ["AI/ML", "教育行业经验"],
        "salary_range": {"min": 180000, "max": 280000, "currency": "CNY"},
        "location": "北京",
        "remote_policy": "onsite",
        "description": "深度参与产品设计与全栈开发，用技术改变教育。",
    },
]

# ── Seed candidate profiles ────────────────────────────────────────

SEED_PROFILES: list[dict] = [
    {
        "user_id": "alex-chen",
        "title": "高级前端工程师",
        "years_experience": 6,
        "skills": ["React", "TypeScript", "Next.js", "WebGL", "Tailwind CSS"],
        "education": [{"degree": "本科", "school": "浙江大学", "major": "计算机科学"}],
        "bio": "6 年前端经验，专注于性能优化和交互动效。喜欢独立思考、快速出活。",
        "location": "杭州",
        "remote_preference": "remote",
    },
    {
        "user_id": "maria-santos",
        "title": "全栈工程师",
        "years_experience": 4,
        "skills": ["React", "Python", "Node.js", "PostgreSQL", "GraphQL"],
        "education": [{"degree": "硕士", "school": "清华大学", "major": "软件工程"}],
        "bio": "热爱用技术解决有意义的问题。偏好协作环境，关注产品影响力。",
        "location": "北京",
        "remote_preference": "hybrid",
    },
    {
        "user_id": "james-wright",
        "title": "后端工程师",
        "years_experience": 8,
        "skills": ["Java", "Spring Boot", "Oracle", "Kafka", "Redis"],
        "education": [{"degree": "本科", "school": "上海交通大学", "major": "计算机科学"}],
        "bio": "8 年后端开发经验，专注于高可用分布式系统。追求代码质量和架构稳定。",
        "location": "上海",
        "remote_preference": "hybrid",
    },
    {
        "user_id": "priya-sharma",
        "title": "产品工程师",
        "years_experience": 3,
        "skills": ["React", "Node.js", "MongoDB", "Figma", "产品设计"],
        "education": [{"degree": "本科", "school": "北京大学", "major": "信息管理"}],
        "bio": "跨界产品与工程的 T 型人才，对教育科技充满热情。",
        "location": "北京",
        "remote_preference": "onsite",
    },
    {
        "user_id": "david-kim",
        "title": "DevOps 工程师",
        "years_experience": 5,
        "skills": ["Docker", "Kubernetes", "Terraform", "AWS", "CI/CD"],
        "education": [{"degree": "本科", "school": "华中科技大学", "major": "通信工程"}],
        "bio": "5 年 DevOps 经验，擅长基础设施自动化。喜欢数据驱动的决策方式。",
        "location": "上海",
        "remote_preference": "hybrid",
    },
    {
        "user_id": "sophie-zhang",
        "title": "初级工程师",
        "years_experience": 1,
        "skills": ["Python", "React", "JavaScript", "Git"],
        "education": [{"degree": "本科", "school": "南京大学", "major": "计算机科学"}],
        "bio": "应届生，学习能力强，广泛探索各技术方向。希望加入使命驱动的团队。",
        "location": "南京",
        "remote_preference": "onsite",
    },
]

# ── Seed candidates ─────────────────────────────────────────────────

SEED_CANDIDATES: list[dict] = [
    {
        "id": "alex-chen",
        "name": "Alex Chen",
        "title": "Senior Frontend Engineer",
        "email": "alex@example.com",
        "scores": DimensionScores(
            pace=78, collab=45, decision=60, expression=75,
            unc=70, growth=30, motiv=55, execution=35,
        ),
        "consistency": 0.91,
    },
    {
        "id": "maria-santos",
        "name": "Maria Santos",
        "title": "Full-Stack Engineer",
        "email": "maria@example.com",
        "scores": DimensionScores(
            pace=55, collab=72, decision=50, expression=65,
            unc=50, growth=75, motiv=82, execution=60,
        ),
        "consistency": 0.87,
    },
    {
        "id": "james-wright",
        "name": "James Wright",
        "title": "Backend Engineer",
        "email": "james@example.com",
        "scores": DimensionScores(
            pace=28, collab=60, decision=85, expression=55,
            unc=20, growth=25, motiv=35, execution=85,
        ),
        "consistency": 0.94,
    },
    {
        "id": "priya-sharma",
        "name": "Priya Sharma",
        "title": "Product Engineer",
        "email": "priya@example.com",
        "scores": DimensionScores(
            pace=68, collab=80, decision=42, expression=70,
            unc=62, growth=80, motiv=90, execution=50,
        ),
        "consistency": 0.89,
    },
    {
        "id": "david-kim",
        "name": "David Kim",
        "title": "DevOps Engineer",
        "email": "david@example.com",
        "scores": DimensionScores(
            pace=50, collab=35, decision=75, expression=40,
            unc=30, growth=40, motiv=45, execution=78,
        ),
        "consistency": 0.92,
    },
    {
        "id": "sophie-zhang",
        "name": "Sophie Zhang",
        "title": "Junior Engineer",
        "email": "sophie@example.com",
        "scores": DimensionScores(
            pace=72, collab=70, decision=45, expression=50,
            unc=65, growth=85, motiv=75, execution=45,
        ),
        "consistency": 0.78,
    },
]

# ── Expected match matrix (for validation) ──────────────────────────
# Format: (candidate_id, company_id, expected_match_percentage)

EXPECTED_MATCHES: list[tuple[str, str, int]] = [
    # Velocity Labs
    ("alex-chen", "velocity-labs", 91),
    ("maria-santos", "velocity-labs", 72),
    ("james-wright", "velocity-labs", 48),
    ("priya-sharma", "velocity-labs", 74),
    ("david-kim", "velocity-labs", 56),
    ("sophie-zhang", "velocity-labs", 76),
    # Meridian Financial
    ("alex-chen", "meridian-financial", 52),
    ("maria-santos", "meridian-financial", 65),
    ("james-wright", "meridian-financial", 92),
    ("priya-sharma", "meridian-financial", 58),
    ("david-kim", "meridian-financial", 83),
    ("sophie-zhang", "meridian-financial", 54),
    # Bloom Education
    ("alex-chen", "bloom-education", 72),
    ("maria-santos", "bloom-education", 89),
    ("james-wright", "bloom-education", 55),
    ("priya-sharma", "bloom-education", 93),
    ("david-kim", "bloom-education", 60),
    ("sophie-zhang", "bloom-education", 81),
]
