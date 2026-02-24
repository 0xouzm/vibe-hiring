"""Company DNA question bank — CQ11 through CQ20.

Imported by company_questions.py to form the full 20-question bank.
"""

from src.models.questionnaire import Question, QuestionOption, QuestionType

COMPANY_QUESTIONS_EXT: list[Question] = [
    Question(
        id="CQ11",
        title="Growth",
        scenario=(
            "Your company offers a full week of paid professional development per year "
            "with no strings attached. Most people on your team would choose to:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Go deep — advanced workshop or certification in their core domain"),
            QuestionOption(key="B", text="Go wide — explore something deliberately outside their daily work"),
            QuestionOption(key="C", text="Go strategic — shadow leadership, attend strategy sessions, understand the bigger picture"),
            QuestionOption(key="D", text="Go applied — skip courses and spend the week building a prototype for an unsolved internal problem"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="CQ12",
        title="Motivation",
        scenario=(
            "After shipping a major release following months of intense work, how does "
            "your team typically celebrate or recognize the effort?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Public recognition — shout-outs at all-hands, leadership acknowledgment, visible praise"),
            QuestionOption(key="B", text="Tangible rewards — bonuses, extra time off, team dinner funded by the company"),
            QuestionOption(key="C", text="Autonomy — the team gets to choose what they work on next, a period of self-directed work"),
            QuestionOption(key="D", text="Low-key acknowledgment — a brief \"great job\" in standup, then on to the next thing"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="CQ13",
        title="Execution + Pace",
        scenario=(
            "A new team member inherits a project with 20+ open bugs and a long feature "
            "backlog. No hard deadline — management says \"make it better.\" In your "
            "team's culture, the expected approach is:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Start shipping quick wins immediately — visible progress builds momentum and trust"),
            QuestionOption(key="B", text="Spend the first week understanding the full picture, then create a prioritized roadmap"),
            QuestionOption(key="C", text="Identify the root architectural issue causing most bugs, fix that foundation first — even if nothing visible ships for weeks"),
            QuestionOption(key="D", text="Categorize by effort/impact, clear all quick wins in week one, then reassess"),
        ],
        dimensions=["execution", "pace"],
    ),
    Question(
        id="CQ14",
        title="Execution",
        scenario=(
            "For a cross-team project spanning 6+ weeks with multiple dependencies, "
            "how does your team typically track progress?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Detailed project tracker with milestones, dependency maps, and regular syncs — structured and visible"),
            QuestionOption(key="B", text="Lightweight shared doc with key milestones and target dates — check in as milestones approach"),
            QuestionOption(key="C", text="Informal — people know what they're doing, progress surfaces through Slack and standups"),
            QuestionOption(key="D", text="Adaptive — define the end state and first milestone clearly, re-plan after each milestone based on what we learned"),
        ],
        dimensions=["execution"],
    ),
    Question(
        id="CQ15",
        title="Growth",
        scenario=(
            "If you had to fill one open headcount on your team right now, and two "
            "equally qualified candidates applied — one with 8 years of deep expertise "
            "in your exact domain, the other with 5 years across three different "
            "domains — your team would most likely prefer:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="The deep specialist — depth is hard to find, and we need someone who can own complex problems end-to-end"),
            QuestionOption(key="B", text="The cross-domain generalist — versatility matters more; they'll bring fresh perspectives and adapt faster"),
            QuestionOption(key="C", text="The specialist, but we'd want them to gradually broaden — T-shaped is the ideal"),
            QuestionOption(key="D", text="The generalist, but only if they show the ability to go deep when needed — depth on demand"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="CQ16",
        title="Expression + Collab",
        scenario=(
            "Another department promised a client that your team would deliver a feature "
            "in 6 weeks. Your honest estimate is 10 weeks. No one consulted your team "
            "before making the commitment. How would your team handle this?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Arrange a private meeting with the other department, lay out the reality, and jointly renegotiate before telling the client"),
            QuestionOption(key="B", text="Commit to the timeline but aggressively cut scope — deliver a \"Phase 1\" on time, full version later"),
            QuestionOption(key="C", text="Escalate to shared leadership — present the trade-offs transparently and let executives decide"),
            QuestionOption(key="D", text="Go directly to the client with the other department, explain the realistic timeline, and offer an interim plan"),
        ],
        dimensions=["expression", "collab"],
    ),
    Question(
        id="CQ17",
        title="Pace + Collab + Execution (Budget Allocation)",
        scenario=(
            "Distribute 100% to reflect how your team actually spends its collective "
            "energy in a typical sprint:"
        ),
        type=QuestionType.budget,
        options=[
            QuestionOption(key="A", text="Heads-down execution (coding / designing / building)"),
            QuestionOption(key="B", text="Internal team discussion, review, and pairing"),
            QuestionOption(key="C", text="Cross-functional communication (PM, stakeholders, other teams)"),
            QuestionOption(key="D", text="Learning, research, and exploration"),
            QuestionOption(key="E", text="Documentation, process improvement, and knowledge management"),
        ],
        dimensions=["pace", "collab", "execution"],
    ),
    Question(
        id="CQ18",
        title="Decision (Budget Allocation)",
        scenario=(
            "Allocate 100 points to reflect how your team actually weighs these inputs "
            "when making major decisions — not how you think you should, but how it "
            "really works:"
        ),
        type=QuestionType.budget,
        options=[
            QuestionOption(key="A", text="Quantitative evidence — metrics, benchmarks, A/B test results"),
            QuestionOption(key="B", text="Experience and pattern recognition — \"we've seen this before\""),
            QuestionOption(key="C", text="Stakeholder alignment — getting buy-in from affected people"),
            QuestionOption(key="D", text="First-principles reasoning — working from fundamentals and constraints"),
        ],
        dimensions=["decision"],
    ),
    Question(
        id="CQ19",
        title="Motiv + Growth (Forced Ranking)",
        scenario=(
            "Rank these descriptions of your team's culture from most accurate to "
            "least accurate (1 = most, 5 = least):"
        ),
        type=QuestionType.ranking,
        options=[
            QuestionOption(key="A", text="Mission-Driven — People are here because they believe in the impact we're making"),
            QuestionOption(key="B", text="Growth Engine — People are here because they're growing faster than anywhere else"),
            QuestionOption(key="C", text="Craft Culture — People are here because they get to do the best work of their careers"),
            QuestionOption(key="D", text="Well-Compensated — People are here because the total compensation is genuinely competitive"),
            QuestionOption(key="E", text="Life-Friendly — People are here because the work-life integration is genuinely respected"),
        ],
        dimensions=["motiv", "growth"],
    ),
    Question(
        id="CQ20",
        title="Full Cross-Dimension (Forced Ranking)",
        scenario=(
            "Think about the last few successful hires on your team — the people who "
            "ramped up fastest and fit in best. Rank these traits from most important "
            "to least important for thriving on your team:"
        ),
        type=QuestionType.ranking,
        options=[
            QuestionOption(key="A", text="Speed-to-Impact — Gets things done quickly; ships and iterates rather than perfecting"),
            QuestionOption(key="B", text="Structured Thinker — Plans carefully, tracks commitments, brings order to ambiguity"),
            QuestionOption(key="C", text="Candid Communicator — Says what they think directly, even when it's uncomfortable"),
            QuestionOption(key="D", text="Independent Operator — Takes ownership without much hand-holding; figures things out alone"),
            QuestionOption(key="E", text="Curious Learner — Picks up new domains fast; comfortable being a beginner"),
        ],
        dimensions=["pace", "execution", "expression", "collab", "growth", "unc"],
    ),
]
