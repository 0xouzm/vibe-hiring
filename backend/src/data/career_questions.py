"""Career DNA question bank — 30 standardized behavioral scenario questions.

Questions Q01-Q15 are defined here; Q16-Q30 are in career_questions_ext.py.
Combined export: CAREER_QUESTIONS (list of all 30 Question objects).
"""

from src.models.questionnaire import Question, QuestionOption, QuestionType

from src.data.career_questions_ext import CAREER_QUESTIONS_EXT

# ── Q01–Q15 ─────────────────────────────────────────────────────────

_CAREER_Q01_Q15: list[Question] = [
    Question(
        id="Q01",
        title="Work Pace + Decision Style",
        scenario=(
            "You've picked up a new feature. The PM says \"the sooner it ships, "
            "the better — let's see what users think.\" After assessing the work, "
            "you find the quick approach has obvious technical shortcomings but can "
            "ship in one week; the thorough approach takes three weeks but produces "
            "a cleaner architecture. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Ship the quick version, collect data, then decide whether to refactor"),
            QuestionOption(key="B", text="Negotiate a middle ground with the PM: a workable version in two weeks"),
            QuestionOption(key="C", text="Advocate for the thorough approach, using data to explain the long-term cost of tech debt"),
            QuestionOption(key="D", text="Ship quick but simultaneously start a refactor plan so debt doesn't accumulate"),
        ],
        dimensions=["pace", "decision"],
    ),
    Question(
        id="Q02",
        title="Collaboration Mode + Communication",
        scenario=(
            "Friday afternoon — you spot a production risk. It's not a critical bug, "
            "but if left alone it could cause issues next week. Most of the team has "
            "wrapped up for the day. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Fix it yourself in a couple of hours, then share what you did at Monday standup"),
            QuestionOption(key="B", text="Post in the team channel explaining the issue, see if anyone wants to jump in"),
            QuestionOption(key="C", text="Create a detailed ticket marked high-priority, tackle it first thing Monday"),
            QuestionOption(key="D", text="Reach out directly to the colleague closest to that code, fix it together quickly"),
        ],
        dimensions=["collab", "expression"],
    ),
    Question(
        id="Q03",
        title="Uncertainty Tolerance",
        scenario=(
            "You've been assigned to a brand-new project. Your manager says \"here's "
            "the rough direction — figure out how to get there.\" No spec, no reference "
            "implementation. Your first instinct is:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Excitement — finally a chance to define something from zero"),
            QuestionOption(key="B", text="Spend a few days researching comparable products and approaches before committing"),
            QuestionOption(key="C", text="Go back to your manager and try to pin down requirements and boundaries"),
            QuestionOption(key="D", text="Build a minimal prototype fast, then use it to drive a more concrete discussion"),
        ],
        dimensions=["unc"],
    ),
    Question(
        id="Q04",
        title="Expression Style",
        scenario=(
            "During code review a senior colleague leaves extensive change requests on "
            "your PR. After careful reading, you believe most are stylistic preferences "
            "rather than genuine issues. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Reply point by point with your reasoning, linking docs or best practices to support your position"),
            QuestionOption(key="B", text="Hop on a 15-minute call to talk through the key disagreements"),
            QuestionOption(key="C", text="Accept most suggestions — they're more senior, and team harmony matters"),
            QuestionOption(key="D", text="Accept the suggestions that have merit, and on pure style issues say \"personal preference — keeping as-is\""),
        ],
        dimensions=["expression"],
    ),
    Question(
        id="Q05",
        title="Motivation Source",
        scenario=(
            "Four offers are identical in pay, location, and title. The companies differ. "
            "Which do you lean toward?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="A company tackling climate change — technically challenging but the business model is still unproven"),
            QuestionOption(key="B", text="A high-growth company that tripled revenue this year — equity could be very valuable"),
            QuestionOption(key="C", text="A company with an exceptional engineering culture — several domain luminaries on the team"),
            QuestionOption(key="D", text="A profitable, stable company with great work-life balance and predictable annual raises"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="Q06",
        title="Work Pace + Uncertainty Tolerance",
        scenario=(
            "You're researching a technical approach and find two paths: Path A is "
            "battle-tested but mediocre performance; Path B comes from a recent paper "
            "with great theoretical results but zero production validation. The project "
            "deadline is three months away."
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Go with A — proven and low-risk, you'll hit the deadline comfortably"),
            QuestionOption(key="B", text="Spend one week pressure-testing B; if it doesn't hold up, switch to A"),
            QuestionOption(key="C", text="Go with B — three months is enough, and if it works it's a breakthrough"),
            QuestionOption(key="D", text="Build on A as the main track, explore B on the side as a future optimization"),
        ],
        dimensions=["pace", "unc"],
    ),
    Question(
        id="Q07",
        title="Collaboration Mode + Growth Path",
        scenario=(
            "A junior colleague keeps coming to you with similar questions in your area "
            "of expertise. You've already explained the same concept two or three times. "
            "You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Write documentation or record a video so they can self-serve going forward"),
            QuestionOption(key="B", text="Keep patiently answering — helping others deepens your own understanding too"),
            QuestionOption(key="C", text="Point them toward a more systematic learning resource (course, book) to level up fundamentally"),
            QuestionOption(key="D", text="Schedule a pair-programming session to walk through the problem-solving process end to end"),
        ],
        dimensions=["collab", "growth"],
    ),
    Question(
        id="Q08",
        title="Expression Style",
        scenario=(
            "During sprint planning, you believe a proposed technical approach has a "
            "serious flaw — but the proposal comes from the team lead. Eight people "
            "are in the room. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Raise your concern on the spot, backing it with clear reasoning"),
            QuestionOption(key="B", text="Wait until after the meeting and bring it up privately with the lead"),
            QuestionOption(key="C", text="Ask a gentle probing question in the meeting, seeing if the lead catches the issue themselves"),
            QuestionOption(key="D", text="Stay quiet in the meeting, then send the lead a detailed written analysis afterward"),
        ],
        dimensions=["expression"],
    ),
    Question(
        id="Q09",
        title="Motivation + Growth Path (Forced Ranking)",
        scenario="Rank these from most to least important to you:",
        type=QuestionType.ranking,
        options=[
            QuestionOption(key="A", text="Becoming a recognized expert in a cutting-edge technical domain"),
            QuestionOption(key="B", text="Leading an increasingly large team"),
            QuestionOption(key="C", text="Working on a product that changes the world"),
            QuestionOption(key="D", text="Earning exceptional financial compensation"),
            QuestionOption(key="E", text="Having freedom and control over your time and energy"),
        ],
        dimensions=["motiv", "growth"],
    ),
    Question(
        id="Q10",
        title="Work Pace + Collaboration (Budget Allocation)",
        scenario="Distribute 100% of your ideal work energy:",
        type=QuestionType.budget,
        options=[
            QuestionOption(key="A", text="Solo execution (coding / design / analysis)"),
            QuestionOption(key="B", text="Team discussion, design review, pairing"),
            QuestionOption(key="C", text="Cross-functional communication (PM, business)"),
            QuestionOption(key="D", text="Learning new tech or exploring new directions"),
            QuestionOption(key="E", text="Documentation, knowledge management"),
        ],
        dimensions=["pace", "collab", "execution"],
    ),
    Question(
        id="Q11",
        title="Decision Style",
        scenario=(
            "Your team is evaluating three vendors for a critical infrastructure "
            "migration. You have two weeks of trial data, industry benchmarks, and "
            "strong personal recommendations from trusted engineers at other companies. "
            "The quantitative data slightly favors Vendor A, but the engineers you "
            "respect are unanimously recommending Vendor B, saying \"the numbers don't "
            "capture the developer experience.\" You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Build a weighted scorecard from the data and benchmarks, present the quantitative ranking, flag anecdotal feedback as secondary"),
            QuestionOption(key="B", text="Give significant weight to the engineers' lived experience — they've used these tools in production. Recommend Vendor B with their reasoning documented"),
            QuestionOption(key="C", text="Design a one-week structured pilot where your own team uses both on a real task, generating first-party data that captures both metrics and experience"),
            QuestionOption(key="D", text="Bring both data and recommendations to the team, facilitate discussion, let collective judgment drive the decision"),
        ],
        dimensions=["decision"],
    ),
    Question(
        id="Q12",
        title="Work Pace + Execution Style",
        scenario=(
            "You've just taken ownership of an internal tool used daily by ~40 people. "
            "There are 23 feature requests and 8 bug reports in the backlog. Your "
            "manager says you have full autonomy — no hard deadline, just \"make it "
            "better.\" Your first two weeks look like:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Pick the three most-requested quick fixes, ship them within days, use the momentum to learn what actually matters before planning bigger"),
            QuestionOption(key="B", text="Interview power users and map workflows for a week, then create a prioritized roadmap that sequences changes toward a coherent improved experience"),
            QuestionOption(key="C", text="Identify the single highest-impact architectural improvement that would make all future changes easier, and invest the full two weeks on that foundation"),
            QuestionOption(key="D", text="Categorize everything by effort/impact, knock out all quick wins in week one, then reassess with a clearer picture of the codebase"),
        ],
        dimensions=["pace", "execution"],
    ),
    Question(
        id="Q13",
        title="Uncertainty Tolerance (cross-validation)",
        scenario=(
            "Your company is entering a new market. You're building a demo but nobody "
            "can specify which features prospects care about most. Two analyst reports "
            "disagree, and three prospect conversations each emphasized different pain "
            "points. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Pick the pain point that appeared in at least two conversations, build a focused demo around it, iterate based on real reactions"),
            QuestionOption(key="B", text="Build a modular demo with three separate tracks so sales can adapt in real time depending on the audience"),
            QuestionOption(key="C", text="Push back — schedule five more discovery calls before building anything. Building the wrong demo costs more than a two-week delay"),
            QuestionOption(key="D", text="Design the demo around the problem framing the analysts agree on, trusting that analysts see market patterns individual buyers miss"),
        ],
        dimensions=["unc"],
    ),
    Question(
        id="Q14",
        title="Decision Style + Uncertainty Tolerance",
        scenario=(
            "You're tech lead, six weeks into a project. Yesterday a competitor launched "
            "a product overlapping ~60% with yours. The CEO wants a same-day assessment: "
            "pivot, double down, or something else? You have gut instinct, team opinions, "
            "and could do rigorous analysis — but that would take three days. CEO needs "
            "your input by EOD."
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Share your honest instinct now — six weeks in this problem space makes your gut read informed, even without a spreadsheet. Speed matters"),
            QuestionOption(key="B", text="Spend the day on rapid structured analysis — feature comparison, differentiation map, rough switching-cost estimates — present findings with explicit confidence levels"),
            QuestionOption(key="C", text="Tell the CEO a same-day call on something this consequential will likely be wrong. Propose a 48-hour evaluation with a preliminary read clearly labeled as unreliable"),
            QuestionOption(key="D", text="Convene a 90-minute team session to surface collective perspectives and blind spots, then present a team position rather than an individual one"),
        ],
        dimensions=["decision", "unc"],
    ),
    Question(
        id="Q15",
        title="Work Pace + Execution Style (cross-validation)",
        scenario=(
            "Your team just finished a major release Friday. On Monday, your manager "
            "mentions optional interest in a technical retrospective at the company "
            "all-hands in two weeks. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Volunteer to put together a lightweight 10-minute retro yourself this week while details are fresh — good enough now beats polished later"),
            QuestionOption(key="B", text="Propose the team spend one focused afternoon on a thorough internal retro, then distill it into a polished all-hands presentation the following week"),
            QuestionOption(key="C", text="Suggest skipping the all-hands talk but running a quick async retro — everyone drops takeaways in a shared doc by Wednesday"),
            QuestionOption(key="D", text="Advocate for a proper retrospective in the second week — gather cycle-time data, incident counts, and produce something genuinely reusable for other teams"),
        ],
        dimensions=["pace", "execution"],
    ),
]

# ── Combined export ──────────────────────────────────────────────────

CAREER_QUESTIONS: list[Question] = _CAREER_Q01_Q15 + CAREER_QUESTIONS_EXT
"""All 30 Career DNA questions (Q01–Q30)."""
