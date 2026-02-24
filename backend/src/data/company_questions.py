"""Company DNA question bank — 20 behavioral scenario questions.

Questions CQ01-CQ10 are defined here; CQ11-CQ20 are in company_questions_ext.py.
Combined export: COMPANY_QUESTIONS (list of all 20 Question objects).
Filled by HR + 5+ anonymous team members to build a company culture profile.
"""

from src.models.questionnaire import Question, QuestionOption, QuestionType

from src.data.company_questions_ext import COMPANY_QUESTIONS_EXT

# ── CQ01–CQ10 ───────────────────────────────────────────────────────

_COMPANY_Q01_Q10: list[Question] = [
    Question(
        id="CQ01",
        title="Pace + Decision",
        scenario=(
            "A feature is technically ready but has a few rough edges. The product "
            "lead says \"let's get user feedback ASAP.\" In your team, the most likely "
            "outcome is:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Ship it now, gather data, polish based on real feedback — speed is how we learn"),
            QuestionOption(key="B", text="Take one more week to smooth the most visible rough edges, then ship — balance matters"),
            QuestionOption(key="C", text="Hold until the experience is polished — we'd rather be late than ship something half-baked"),
            QuestionOption(key="D", text="Ship to a small beta group first, validate, then roll out broadly — controlled velocity"),
        ],
        dimensions=["pace", "decision"],
    ),
    Question(
        id="CQ02",
        title="Collab + Expression",
        scenario=(
            "An engineer notices a non-urgent production risk on Friday afternoon. "
            "Most of the team has wrapped up for the week. In your team, what "
            "typically happens?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="They fix it themselves and mention it at Monday standup — individual initiative is valued"),
            QuestionOption(key="B", text="They post in the team channel describing the issue, and whoever's around jumps in"),
            QuestionOption(key="C", text="They create a detailed ticket marked high-priority — process ensures nothing is missed"),
            QuestionOption(key="D", text="They ping the person closest to that code and pair-fix it quickly — targeted collaboration"),
        ],
        dimensions=["collab", "expression"],
    ),
    Question(
        id="CQ03",
        title="Uncertainty Tolerance",
        scenario=(
            "A new project lands with a rough direction but no spec, no wireframes, "
            "and no reference implementation. How does your team typically kick it off?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Dive in — people start building prototypes and figure it out as they go"),
            QuestionOption(key="B", text="Spend a few days researching comparable approaches, then align on a plan"),
            QuestionOption(key="C", text="Push for a clearer brief before committing resources — ambiguity wastes effort"),
            QuestionOption(key="D", text="Run a quick spike to surface unknowns, then regroup and plan properly"),
        ],
        dimensions=["unc"],
    ),
    Question(
        id="CQ04",
        title="Expression",
        scenario=(
            "During a design review, a relatively junior team member disagrees with "
            "a senior colleague's approach. In your team's culture, what usually happens?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="They voice it directly in the meeting — everyone's opinion carries equal weight regardless of seniority"),
            QuestionOption(key="B", text="They raise it diplomatically, often framing it as a question rather than a challenge"),
            QuestionOption(key="C", text="They typically hold back in the meeting and mention it privately afterward"),
            QuestionOption(key="D", text="They share their perspective in writing (comment, doc, or message) after reflecting"),
        ],
        dimensions=["expression"],
    ),
    Question(
        id="CQ05",
        title="Motivation",
        scenario=(
            "When you think about why your best-performing team members stay (beyond "
            "compensation), the primary reason is usually:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="The mission — they believe in what the company is trying to achieve in the world"),
            QuestionOption(key="B", text="Growth trajectory — they see a clear path to bigger scope, title, and influence"),
            QuestionOption(key="C", text="The craft — they get to work on technically challenging problems with talented peers"),
            QuestionOption(key="D", text="The balance — predictable hours, manageable stress, and respect for personal life"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="CQ06",
        title="Pace + Uncertainty Tolerance",
        scenario=(
            "Your team is evaluating two technical approaches: Path A is battle-tested "
            "with predictable results; Path B comes from recent research with better "
            "theoretical performance but zero production use. With a 3-month deadline, "
            "your team would most likely:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Go with A — proven and reliable beats theoretical promise"),
            QuestionOption(key="B", text="Spend a week stress-testing B; if it holds up, switch; if not, A is the fallback"),
            QuestionOption(key="C", text="Go with B — three months is enough runway, and breakthrough results justify the risk"),
            QuestionOption(key="D", text="Build on A as the main track while exploring B in parallel as a future option"),
        ],
        dimensions=["pace", "unc"],
    ),
    Question(
        id="CQ07",
        title="Collab + Growth",
        scenario=(
            "When a team member develops deep expertise in a specific area, how does "
            "the team typically share and leverage that knowledge?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="They write internal docs or record walkthroughs — scalable self-serve knowledge"),
            QuestionOption(key="B", text="They become the go-to person; others simply ask them when needed — organic and personal"),
            QuestionOption(key="C", text="They run occasional knowledge-sharing sessions or workshops for the broader team"),
            QuestionOption(key="D", text="They pair with others on real tasks so knowledge transfers through practice"),
        ],
        dimensions=["collab", "growth"],
    ),
    Question(
        id="CQ08",
        title="Expression + Execution",
        scenario=(
            "A team member misses a committed deadline by several days. No external "
            "factors — they simply underestimated the complexity. In your team, the "
            "typical response is:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="They proactively flag the delay early, share a revised plan, and the team adjusts — transparency is expected"),
            QuestionOption(key="B", text="There's a retrospective to understand what happened and improve estimation going forward — process improvement"),
            QuestionOption(key="C", text="It's handled quietly — deadlines shift, no big deal as long as quality is good"),
            QuestionOption(key="D", text="There's visible frustration — commitments are taken seriously, and missing them has social consequences"),
        ],
        dimensions=["expression", "execution"],
    ),
    Question(
        id="CQ09",
        title="Decision + Uncertainty Tolerance",
        scenario=(
            "A high-stakes decision needs to be made this week. You have partial data, "
            "conflicting team opinions, and no time for thorough analysis. How does your "
            "team typically handle this?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="The most senior person makes the call based on experience — speed matters, and they've seen this before"),
            QuestionOption(key="B", text="The team runs a rapid structured analysis — even compressed, data beats gut feel"),
            QuestionOption(key="C", text="They convene a quick group discussion, surface perspectives, and go with the emerging consensus"),
            QuestionOption(key="D", text="They choose the most reversible option — commit minimally, learn fast, adjust"),
        ],
        dimensions=["decision", "unc"],
    ),
    Question(
        id="CQ10",
        title="Collaboration Mode",
        scenario=(
            "Three team members are building separate modules that need to integrate. "
            "No one has defined the interfaces yet. The deadline is tight. In your "
            "team, what usually happens?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Each person starts building based on assumptions, then aligns when something concrete exists"),
            QuestionOption(key="B", text="The team blocks out a half-day to design interfaces together before anyone writes code"),
            QuestionOption(key="C", text="One person drafts the interface contracts and shares for async feedback — initiative-driven"),
            QuestionOption(key="D", text="The two most tightly coupled modules pair up first; the third person joins once the core contract exists"),
        ],
        dimensions=["collab"],
    ),
]

# ── Combined export ──────────────────────────────────────────────────

COMPANY_QUESTIONS: list[Question] = _COMPANY_Q01_Q10 + COMPANY_QUESTIONS_EXT
"""All 20 Company DNA questions (CQ01–CQ20)."""
