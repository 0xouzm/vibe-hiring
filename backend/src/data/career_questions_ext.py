"""Career DNA question bank — Q16 through Q30.

Imported by career_questions.py to form the full 30-question bank.
"""

from src.models.questionnaire import Question, QuestionOption, QuestionType

CAREER_QUESTIONS_EXT: list[Question] = [
    Question(
        id="Q16",
        title="Collaboration Mode (cross-validation)",
        scenario=(
            "Your team just kicked off a high-priority project with a tight two-week "
            "deadline. Three separate modules can technically be developed in parallel. "
            "You're assigned one, but the overall architecture hasn't been clearly "
            "defined. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Start building your module based on your best interface assumptions, then align with others once you have something concrete"),
            QuestionOption(key="B", text="Propose a half-day architecture session where all three module owners sketch interfaces together before anyone codes"),
            QuestionOption(key="C", text="Draft the interface contracts yourself and share for async feedback — if no objections within a few hours, start building"),
            QuestionOption(key="D", text="Pair up with the developer on the most tightly coupled module and design your two pieces together first, then loop in the third person"),
        ],
        dimensions=["collab"],
    ),
    Question(
        id="Q17",
        title="Expression Style (cross-validation) + Decision Style",
        scenario=(
            "You've been working on a feature for two weeks and just realized you'll "
            "likely miss the deadline by 3-4 days due to unforeseen technical complexity, "
            "not poor planning. There's still a week until the deadline. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Message your manager immediately: \"Heads up — hitting complexity on X, likely 3-4 days late. Here's why and my adjusted plan.\""),
            QuestionOption(key="B", text="Finish working through the complexity first so you can present the problem alongside a concrete solution"),
            QuestionOption(key="C", text="Bring it up casually at your next 1:1 or standup — not urgent enough for a special notification since there's still time"),
            QuestionOption(key="D", text="Send a detailed written update to your manager and the broader team documenting the challenge, what you've tried, and the revised timeline"),
        ],
        dimensions=["expression", "decision"],
    ),
    Question(
        id="Q18",
        title="Expression Style (key cross-validation)",
        scenario=(
            "Your team has been debating two competing approaches for a system redesign "
            "for a week. The group is split 50/50 and the discussion is going in circles. "
            "You have a strong opinion. There's no designated decision-maker. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Write a structured comparison document with pros/cons and data, share it, and explicitly call for a final decision by end of week"),
            QuestionOption(key="B", text="Suggest the team just pick one and commit — indecision costs more than picking the \"slightly wrong\" approach"),
            QuestionOption(key="C", text="Talk privately with key people on the other side to understand their concerns, then propose a modified version of your approach that addresses them"),
            QuestionOption(key="D", text="Propose a time-boxed spike: each side builds a small proof-of-concept in two days, then decide based on concrete results"),
        ],
        dimensions=["expression"],
    ),
    Question(
        id="Q19",
        title="Execution Style",
        scenario=(
            "You're leading a feature that involves coordinating work across three "
            "services. You've estimated it at six weeks. Your manager asks: \"How will "
            "you track progress?\""
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Set up a detailed project tracker with weekly milestones, dependency maps, and a risk register. Schedule brief daily syncs with contributors for the first two weeks"),
            QuestionOption(key="B", text="Create a lightweight shared doc listing the three key milestones and their target dates. Check in with contributors as each milestone approaches"),
            QuestionOption(key="C", text="Keep it informal — you know the people involved. Ping them in Slack when you need updates, and flag risks in your weekly 1:1 with your manager"),
            QuestionOption(key="D", text="Define the end state and first milestone clearly. Re-plan the rest after milestone one lands, when you'll know more about actual complexity"),
        ],
        dimensions=["execution"],
    ),
    Question(
        id="Q20",
        title="Execution Style (cross-validation)",
        scenario=(
            "You promised your team lead you'd deliver a component by Thursday. "
            "Tuesday evening you realize you underestimated the work — hitting Thursday "
            "means cutting corners on test coverage and error handling. Doing it "
            "properly means delivering Monday instead. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Message your lead immediately: \"Revising estimate to Monday. Here's what I underestimated and my adjusted plan.\" Deliver a high-quality version on Monday"),
            QuestionOption(key="B", text="Push hard for Thursday — work late if needed. A commitment is a commitment; reliability means delivering on your word"),
            QuestionOption(key="C", text="Deliver what's done by Thursday with a clear \"known gaps\" list, then complete the remaining quality work by Monday"),
            QuestionOption(key="D", text="Check whether anyone actually needs it Thursday or if the deadline is soft. If there's flexibility, quietly shift to Monday"),
        ],
        dimensions=["execution"],
    ),
    Question(
        id="Q21",
        title="Motivation Source (cross-validation)",
        scenario=(
            "You've been at your company for two years, performing well. A recruiter "
            "contacts you about a new role — same salary, same commute, equivalent "
            "title. Which single factor would most likely make you seriously consider "
            "leaving?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="The new company is working on a problem you find deeply meaningful — climate, healthcare, or education — and your work directly contributes to that mission"),
            QuestionOption(key="B", text="The new role offers a clear, accelerated promotion path: formal senior-title review within 12 months with a compensation bump"),
            QuestionOption(key="C", text="The team is led by someone widely regarded as one of the best mentors in your field — former reports credit her with transforming their careers"),
            QuestionOption(key="D", text="The company gives every employee 20% discretionary time and a $10K annual budget to explore any project or skill, no questions asked"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="Q22",
        title="Growth Path",
        scenario=(
            "Your company gives you a full week of paid professional development. "
            "No strings — no expectation to report back or apply it immediately. "
            "How do you spend it?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Intensive advanced workshop in your core skill area — move from \"good\" to \"exceptional\" in what you already do"),
            QuestionOption(key="B", text="Something deliberately outside your domain — a UX sprint if you're a developer, a data science bootcamp if you're in marketing"),
            QuestionOption(key="C", text="Shadow three different senior leaders — sit in their meetings, understand how they make decisions, see the organizational big picture"),
            QuestionOption(key="D", text="Skip courses entirely. Identify a real unsolved problem at your company and spend the week building a working prototype"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="Q23",
        title="Collaboration Mode (cross-validation, growth lens)",
        scenario=(
            "A colleague from another department invites you to co-lead a new internal "
            "initiative. The project is interesting but ambiguous — no playbook, and "
            "leadership will leave you two to figure it out. You both have roughly equal "
            "expertise. How do you structure the partnership?"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Divide into two distinct halves based on strengths. Each owns their section end-to-end, sync weekly. Clear boundaries, clear ownership"),
            QuestionOption(key="B", text="Work on everything together — pair on key deliverables, joint meetings, shared documents. Slower but deeply collaborative output"),
            QuestionOption(key="C", text="One of you takes the lead, the other supports. You're fine being either — what matters is a clear decision-maker"),
            QuestionOption(key="D", text="Intensive co-working session at the start to align on vision, then split off independently for the bulk, reconvene for final integration"),
        ],
        dimensions=["collab"],
    ),
    Question(
        id="Q24",
        title="Motivation + Growth Path combined (Forced Ranking)",
        scenario=(
            "Rank these role configurations from most to least appealing "
            "(1 = most, 4 = least):"
        ),
        type=QuestionType.ranking,
        options=[
            QuestionOption(key="A", text="Deep Impact Specialist — Single high-stakes problem affecting thousands of users. Narrow scope, irreplaceable expertise. Success = tangible difference in people's lives"),
            QuestionOption(key="B", text="Rapid-Growth Generalist — Rotate across three functions in two years. Each rotation is a stretch assignment. Success = speed of effectiveness in unfamiliar territory"),
            QuestionOption(key="C", text="Mastery-Track Expert — Go deep with the best training, conferences, mentors. In two years, among the top practitioners in your specialty. Success = peer recognition and craft excellence"),
            QuestionOption(key="D", text="High-Leverage Operator — Cross-functional, high-visibility, direct access to senior leadership. Broad, sometimes chaotic. Success = business outcomes and expanding scope"),
        ],
        dimensions=["motiv", "growth"],
    ),
    Question(
        id="Q25",
        title="Growth Path (cross-validation, specialist vs. generalist)",
        scenario=(
            "You're five years in and have a strong reputation in your primary skill. "
            "A restructuring creates two new positions; you're the top candidate for either:\n\n"
            "Role X: Go-to authority for your discipline company-wide. Set standards, "
            "review critical work, mentor specialists. Depth deepens, scope stays within "
            "your domain. In three years: industry-level expert.\n\n"
            "Role Y: Hybrid role combining your skill with two adjacent areas you've "
            "never formally worked in. First year you'll often be the least experienced "
            "person in the room. In three years: a unique cross-functional perspective "
            "few possess."
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Role X, without hesitation — depth is rare, being the best at one thing is career-proof"),
            QuestionOption(key="B", text="Role Y, without hesitation — breadth creates opportunities depth can't, being a beginner again is worth the long-term versatility"),
            QuestionOption(key="C", text="Role X, but with some reluctance — you'd negotiate for occasional cross-functional projects to stay rounded"),
            QuestionOption(key="D", text="Role Y, but with some reluctance — you'd negotiate to keep a small advisory role in your original domain"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="Q26",
        title="Uncertainty Tolerance (cross-validation)",
        scenario=(
            "Your company just acquired a startup. You're assigned to integrate their "
            "product, but leadership provides only a high-level vision — no roadmap, "
            "no success metrics, and the acquired team has conflicting ideas. Your "
            "first month:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Start building based on your best interpretation, course-correct as you learn from real results"),
            QuestionOption(key="B", text="Spend two weeks interviewing stakeholders on both sides, synthesize a unified direction document before coding"),
            QuestionOption(key="C", text="Propose a small reversible pilot integration to test assumptions, use outcomes to negotiate a clearer mandate"),
            QuestionOption(key="D", text="Escalate that the project needs defined scope and success criteria before meaningful work can begin"),
        ],
        dimensions=["unc"],
    ),
    Question(
        id="Q27",
        title="Decision Style (Budget Allocation)",
        scenario=(
            "Allocate 100 points across these inputs when making a major decision — "
            "reflect how you actually weigh each, not how you think you should:"
        ),
        type=QuestionType.budget,
        options=[
            QuestionOption(key="A", text="Quantitative evidence — metrics, A/B tests, benchmarks, market data"),
            QuestionOption(key="B", text="Pattern recognition — past experience and gut sense of what works"),
            QuestionOption(key="C", text="Stakeholder consensus — alignment among affected people"),
            QuestionOption(key="D", text="First-principles reasoning — logical deduction from fundamental constraints"),
        ],
        dimensions=["decision"],
    ),
    Question(
        id="Q28",
        title="Growth Path (cross-validation)",
        scenario=(
            "You receive two internal transfer offers on the same day. Identical "
            "compensation, title, and team quality.\n\n"
            "Offer X: Senior role on a team working in the exact tech stack you've spent "
            "4 years mastering. You'd become the undisputed domain expert, mentor juniors, "
            "own the technical roadmap.\n\n"
            "Offer Y: Senior role on a newly formed team exploring a domain you've never "
            "touched. You'd be the least experienced person, spend 6+ months ramping up, "
            "but gain entirely different exposure."
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Take X — depth creates irreplaceable value, there's always more to master even in a \"known\" domain"),
            QuestionOption(key="B", text="Take Y — growth comes from discomfort, being a beginner again keeps you sharp and versatile"),
            QuestionOption(key="C", text="Take X but negotiate 20% time to cross-train with the Y team on the side"),
            QuestionOption(key="D", text="Take Y but only if you can bring one project from your current domain to maintain continuity"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="Q29",
        title="Motivation Source (cross-validation)",
        scenario=(
            "Your team just shipped a major feature after a grueling 3-month push. "
            "Your manager asks each person to pick one reward. All genuinely offered, "
            "no judgment:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="A public shout-out from the VP at the all-hands, recognizing you by name for your specific contribution"),
            QuestionOption(key="B", text="A $5,000 spot bonus deposited in your next paycheck, no ceremony"),
            QuestionOption(key="C", text="Three extra PTO days to use however you want this quarter"),
            QuestionOption(key="D", text="The right to choose what you work on next — full autonomy over your next project for one quarter"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="Q30",
        title="Expression Style, cross-functional (cross-validation)",
        scenario=(
            "Marketing has promised a major client that a feature will be ready in 6 "
            "weeks. You're the engineering lead; your honest estimate is 10-12 weeks. "
            "A press release has already gone out. The sales VP is furious at the idea "
            "of walking it back. The client is a top-3 revenue account. You would:"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="Meet privately with the marketing lead and sales VP together, lay out the technical reality, collaboratively renegotiate the timeline before anyone talks to the client"),
            QuestionOption(key="B", text="Commit to the 6-week deadline but immediately cut scope — ship a minimal version on time, frame it as \"Phase 1\""),
            QuestionOption(key="C", text="Escalate to your shared executive (CTO/CEO), present the tradeoffs transparently, let leadership decide how to handle the external commitment"),
            QuestionOption(key="D", text="Go directly to the client with the sales VP, honestly explain the revised timeline, and offer a concrete interim solution to maintain trust"),
        ],
        dimensions=["expression"],
    ),
]
