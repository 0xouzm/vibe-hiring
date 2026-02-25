"""Company DNA 题库 — CQ11 至 CQ20。

由 company_questions.py 导入以组成完整的 20 题题库。
"""

from src.models.questionnaire import Question, QuestionOption, QuestionType

COMPANY_QUESTIONS_EXT: list[Question] = [
    Question(
        id="CQ11",
        title="成长",
        scenario=(
            "公司提供每年一周的带薪职业发展时间，没有附加条件。"
            "你团队里大部分人会选择："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="深耕——参加核心领域的高级研讨或认证"),
            QuestionOption(key="B", text="拓宽——有意探索日常工作以外的领域"),
            QuestionOption(key="C", text="看全局——跟领导层，旁听战略会议，理解更大的图景"),
            QuestionOption(key="D", text="做实事——跳过课程，花一周为一个未解决的内部问题搭原型"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="CQ12",
        title="驱动力",
        scenario=(
            "经历数月的高强度工作后发布了一个大版本，"
            "你的团队通常怎么庆祝或认可付出？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="公开表扬——all-hands 上喊出来，领导层认可，显眼的赞扬"),
            QuestionOption(key="B", text="实际奖励——奖金、额外假期、公司出资的团队晚餐"),
            QuestionOption(key="C", text="自主权——团队可以选择下一步做什么，一段自主导向的工作时间"),
            QuestionOption(key="D", text="低调认可——站会上简短说句『干得好』，然后继续下一件事"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="CQ13",
        title="执行风格 + 工作节奏",
        scenario=(
            "一位新团队成员接手了一个有 20 多个 bug 和长长功能积压的项目。"
            "没有硬性截止日期——管理层说『让它变好。』"
            "在你的团队文化里，期望的做法是："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="立刻开始 ship 快速修复——可见的进展能建立动力和信任"),
            QuestionOption(key="B", text="第一周先理解全貌，然后制定优先级路线图"),
            QuestionOption(key="C", text="找到导致大部分 bug 的根源架构问题，先修地基——即使几周内看不到可见进展"),
            QuestionOption(key="D", text="按投入/产出分类，第一周清掉所有快速修复，然后重新评估"),
        ],
        dimensions=["execution", "pace"],
    ),
    Question(
        id="CQ14",
        title="执行风格",
        scenario=(
            "对于一个跨团队、持续 6 周以上、有多个依赖的项目，"
            "你的团队通常怎么跟踪进度？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="详细的项目跟踪器，包含里程碑、依赖关系图和定期同步——结构化且可见"),
            QuestionOption(key="B", text="轻量级共享文档，列出关键里程碑和目标日期——里程碑临近时核对"),
            QuestionOption(key="C", text="非正式——大家知道自己在做什么，通过 Slack 和站会浮现进度"),
            QuestionOption(key="D", text="自适应——明确终态和第一个里程碑，每个里程碑后根据学到的东西重新规划"),
        ],
        dimensions=["execution"],
    ),
    Question(
        id="CQ15",
        title="成长",
        scenario=(
            "如果现在要补一个 HC，两个同样合格的候选人申请——"
            "一位在你的精确领域有 8 年深度经验，另一位在三个不同领域有 5 年经验——"
            "你的团队最可能倾向于："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="深度专家——深度难得，我们需要能端到端负责复杂问题的人"),
            QuestionOption(key="B", text="跨领域通才——多面性更重要；他们会带来新视角并更快适应"),
            QuestionOption(key="C", text="专家，但希望逐步拓宽——T 型是理想状态"),
            QuestionOption(key="D", text="通才，但前提是必要时能深入——按需深度"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="CQ16",
        title="表达风格 + 协作模式",
        scenario=(
            "另一个部门向客户承诺你的团队将在 6 周内交付一个功能。"
            "你的诚实估计是 10 周。承诺之前没人跟你的团队商量过。"
            "你的团队会怎么处理？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="和对方部门开私下会议，摆出现实，在告知客户前先内部协商"),
            QuestionOption(key="B", text="接受时间线但大幅砍范围——按时交付一个『第一期』，完整版本后续跟进"),
            QuestionOption(key="C", text="上报给共同的领导层——透明呈现取舍，让高管来决定"),
            QuestionOption(key="D", text="和对方部门一起直接去找客户，说明真实时间线，并提供过渡方案"),
        ],
        dimensions=["expression", "collab"],
    ),
    Question(
        id="CQ17",
        title="工作节奏 + 协作 + 执行（预算分配）",
        scenario=(
            "分配 100% 来反映你的团队在一个典型 sprint 中"
            "实际的集体精力分配："
        ),
        type=QuestionType.budget,
        options=[
            QuestionOption(key="A", text="埋头执行（编码/设计/构建）"),
            QuestionOption(key="B", text="团队内部讨论、评审和结对"),
            QuestionOption(key="C", text="跨职能沟通（PM、利益相关方、其他团队）"),
            QuestionOption(key="D", text="学习、调研和探索"),
            QuestionOption(key="E", text="文档、流程改进和知识管理"),
        ],
        dimensions=["pace", "collab", "execution"],
    ),
    Question(
        id="CQ18",
        title="决策风格（预算分配）",
        scenario=(
            "分配 100 分来反映你的团队做重大决策时实际的权重分配——"
            "不是你觉得应该怎样，而是实际怎样："
        ),
        type=QuestionType.budget,
        options=[
            QuestionOption(key="A", text="量化证据——指标、基准、A/B 测试结果"),
            QuestionOption(key="B", text="经验和模式识别——『我们之前见过类似的』"),
            QuestionOption(key="C", text="利益相关者对齐——获得受影响人群的认同"),
            QuestionOption(key="D", text="第一性原理推导——从基本面和约束条件出发"),
        ],
        dimensions=["decision"],
    ),
    Question(
        id="CQ19",
        title="驱动力 + 成长（强制排序）",
        scenario=(
            "按从最准确到最不准确排列以下对你团队文化的描述"
            "（1=最准确，5=最不准确）："
        ),
        type=QuestionType.ranking,
        options=[
            QuestionOption(key="A", text="使命驱动——大家在这里是因为相信我们正在创造的影响"),
            QuestionOption(key="B", text="成长引擎——大家在这里是因为比其他任何地方成长都快"),
            QuestionOption(key="C", text="匠心文化——大家在这里是因为能做出职业生涯中最好的作品"),
            QuestionOption(key="D", text="薪酬优渥——大家在这里是因为整体薪酬真的有竞争力"),
            QuestionOption(key="E", text="生活友好——大家在这里是因为工作生活的融合真的被尊重"),
        ],
        dimensions=["motiv", "growth"],
    ),
    Question(
        id="CQ20",
        title="全维度交叉（强制排序）",
        scenario=(
            "想想最近几个成功的招聘——上手最快、融入最好的人。"
            "按对在你团队蓬勃发展的重要性从高到低排列："
        ),
        type=QuestionType.ranking,
        options=[
            QuestionOption(key="A", text="速度到产出——做事快；ship 然后迭代，而不是追求完美"),
            QuestionOption(key="B", text="结构化思维——规划仔细，跟踪承诺，为模糊性带来秩序"),
            QuestionOption(key="C", text="坦诚沟通者——有想法直说，即使不舒服"),
            QuestionOption(key="D", text="独立操作者——不需要太多指导就能自主负责；自己搞定"),
            QuestionOption(key="E", text="好奇学习者——快速上手新领域；不怕做回初学者"),
        ],
        dimensions=["pace", "execution", "expression", "collab", "growth", "unc"],
    ),
]
