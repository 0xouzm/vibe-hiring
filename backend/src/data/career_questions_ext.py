"""Career DNA 题库 — Q16 至 Q30。

由 career_questions.py 导入以组成完整的 30 题题库。
"""

from src.models.questionnaire import Question, QuestionOption, QuestionType

CAREER_QUESTIONS_EXT: list[Question] = [
    Question(
        id="Q16",
        title="协作模式（交叉验证）",
        scenario=(
            "你的团队刚启动一个高优先级项目，截止日期只有两周。"
            "三个独立模块可以并行开发。你负责其中一个，但整体架构还没定义清楚。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="基于自己的最佳接口假设先开始做，等有具体产出后再和其他人对齐"),
            QuestionOption(key="B", text="提议花半天让三个模块负责人一起画接口，然后再各自编码"),
            QuestionOption(key="C", text="自己先拟一份接口契约，发出去征求异步反馈——如果几小时内没有异议就开工"),
            QuestionOption(key="D", text="和耦合度最高的那个模块的开发者先结对设计，然后再拉第三个人"),
        ],
        dimensions=["collab"],
    ),
    Question(
        id="Q17",
        title="表达风格（交叉验证）+ 决策风格",
        scenario=(
            "你做一个功能已经两周了，刚意识到可能会比截止日期晚 3-4 天——"
            "原因是技术复杂度超出预期，不是规划失误。距离截止日期还有一周。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="立刻发消息给经理：『提个醒——X 遇到复杂度问题，可能晚 3-4 天。原因和调整后的计划如下。』"),
            QuestionOption(key="B", text="先把复杂度攻克了，这样汇报时能同时呈现问题和解决方案"),
            QuestionOption(key="C", text="在下一次 1:1 或站会上随口提一下——还有时间，不值得专门通知"),
            QuestionOption(key="D", text="给经理和更广泛的团队发一份详细的书面更新，记录挑战、已尝试的方案和修正后的时间线"),
        ],
        dimensions=["expression", "decision"],
    ),
    Question(
        id="Q18",
        title="表达风格（关键交叉验证）",
        scenario=(
            "你的团队围绕系统重构的两个方案争论了一周，5:5 对半分，"
            "讨论在绕圈子。你有很强的倾向。没有指定的决策者。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="写一份结构化对比文档，列出利弊和数据，分享后明确要求本周内做出最终决定"),
            QuestionOption(key="B", text="建议团队直接选一个然后全力投入——犹豫不决的代价比选『稍微不对』的方案更大"),
            QuestionOption(key="C", text="私下和对方阵营的关键人物聊，了解他们的顾虑，然后提出一个吸收了他们关切的修改版方案"),
            QuestionOption(key="D", text="提议一个限时 spike：双方各用两天做一个小 POC，然后基于实际结果决定"),
        ],
        dimensions=["expression"],
    ),
    Question(
        id="Q19",
        title="执行风格（主测）",
        scenario=(
            "你负责一个需要跨三个服务协调的功能，估计需要六周。"
            "经理问：『你打算怎么跟踪进度？』"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="搭建详细的项目跟踪器，包含周里程碑、依赖关系图和风险登记表。前两周安排每日简短同步会"),
            QuestionOption(key="B", text="创建一个轻量级共享文档，列出三个关键里程碑和目标日期。每个里程碑临近时和相关人核对"),
            QuestionOption(key="C", text="保持非正式——你了解相关的人。需要更新时在 Slack 上 ping 他们，风险在每周 1:1 中标记"),
            QuestionOption(key="D", text="明确定义终态和第一个里程碑。第一个里程碑完成后再规划后续——届时你对实际复杂度更有数"),
        ],
        dimensions=["execution"],
    ),
    Question(
        id="Q20",
        title="执行风格（交叉验证）",
        scenario=(
            "你向 team lead 承诺了周四交付一个组件。周二晚上你发现低估了工作量——"
            "要在周四交付就必须牺牲测试覆盖和错误处理的质量。"
            "如果做到位，周一才能交付。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="立刻发消息给 lead：『修正估期为周一。以下是我低估的部分和调整后的计划。』周一交付高质量版本"),
            QuestionOption(key="B", text="全力冲刺周四——加班也行。承诺就是承诺，可靠性意味着说到做到"),
            QuestionOption(key="C", text="周四先交付已完成的部分，附上一份清晰的『已知缺口』清单，然后周一补齐剩余质量工作"),
            QuestionOption(key="D", text="先确认是否真的有人需要周四拿到，还是这个 deadline 本来就是软性的。如果有弹性，悄悄改到周一"),
        ],
        dimensions=["execution"],
    ),
    Question(
        id="Q21",
        title="驱动力来源（交叉验证）",
        scenario=(
            "你在公司干了两年，表现很好。一个猎头联系你，新职位薪资、通勤、"
            "职级都一样。哪个因素最可能让你认真考虑跳槽？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="新公司在做你觉得非常有意义的事——气候、医疗或教育——你的工作直接贡献于这个使命"),
            QuestionOption(key="B", text="新岗位有清晰的加速晋升路径：12 个月内正式评审高级职称，并有薪酬提升"),
            QuestionOption(key="C", text="团队由一位公认的领域顶级导师领导——她的前下属都说她彻底改变了他们的职业生涯"),
            QuestionOption(key="D", text="公司给每位员工 20% 自主时间和每年 1 万美元预算去探索任何项目或技能，无需审批"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="Q22",
        title="成长路径（主测）",
        scenario=(
            "公司给你一周带薪职业发展时间，完全自由——不要求汇报或立即应用。"
            "你会怎么用？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="参加核心技能领域的高级进阶研讨——从『不错』变成『卓越』"),
            QuestionOption(key="B", text="有意跨出自己的领域——开发者去做 UX 冲刺，市场人去上数据科学训练营"),
            QuestionOption(key="C", text="跟三位不同的高管各待一天——旁听他们的会议，理解决策方式，看到组织全局"),
            QuestionOption(key="D", text="跳过课程。找一个公司里真正没解决的问题，花一周做出一个可用原型"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="Q23",
        title="协作模式（交叉验证，成长视角）",
        scenario=(
            "另一个部门的同事邀请你共同主导一个新的内部项目。项目有趣但模糊——"
            "没有 playbook，领导层让你们俩自己搞定。你们的专业水平大致相当。"
            "你怎么组织合作？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="根据各自优势分成两个独立部分，各自端到端负责，每周同步。清晰边界，清晰所有权"),
            QuestionOption(key="B", text="所有事情一起做——关键交付物结对，联合开会，共享文档。慢一点但产出是深度协作的"),
            QuestionOption(key="C", text="一个人主导，另一个支持。你哪边都行——重要的是有一个明确的决策者"),
            QuestionOption(key="D", text="一开始密集共创对齐愿景，然后各自独立推进主体工作，最后汇合做集成"),
        ],
        dimensions=["collab"],
    ),
    Question(
        id="Q24",
        title="驱动力 + 成长路径组合（强制排序）",
        scenario="按吸引力从高到低排列以下角色定位（1=最高，4=最低）：",
        type=QuestionType.ranking,
        options=[
            QuestionOption(key="A", text="深度影响专家——专注一个影响数千用户的高风险问题。范围窄，不可替代的专业能力。成功 = 对人们生活的切实改变"),
            QuestionOption(key="B", text="快速成长通才——两年内轮转三个职能，每次都是拉伸型任务。成功 = 在陌生领域快速产出的能力"),
            QuestionOption(key="C", text="精通赛道专家——在最好的培训、会议、导师支持下深耕。两年后成为该领域顶尖从业者。成功 = 同行认可与技艺卓越"),
            QuestionOption(key="D", text="高杠杆操盘手——跨职能、高曝光、直接接触高管。广泛而有时混乱。成功 = 业务成果和不断扩大的影响范围"),
        ],
        dimensions=["motiv", "growth"],
    ),
    Question(
        id="Q25",
        title="成长路径（交叉验证，专精 vs. 通才）",
        scenario=(
            "你已经干了五年，在主要技能上有很强的声誉。一次重组产生了两个新岗位，"
            "你是两个的首选候选人：\n\n"
            "角色 X：成为全公司你所在学科的权威。制定标准、审核关键工作、指导专家。"
            "深度继续加深，范围留在你的领域内。三年后：行业级专家。\n\n"
            "角色 Y：混合角色，将你的技能与两个你从未正式涉足的相邻领域结合。"
            "第一年你经常是房间里经验最少的人。三年后：少有人具备的独特跨职能视角。"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="毫不犹豫选 X——深度稀缺，在一件事上做到最好就是职业护城河"),
            QuestionOption(key="B", text="毫不犹豫选 Y——广度创造深度无法给予的机会，重新做回初学者值得长期的多面性"),
            QuestionOption(key="C", text="选 X，但有些犹豫——你会争取偶尔参与跨职能项目以保持全面"),
            QuestionOption(key="D", text="选 Y，但有些犹豫——你会争取在原来的领域保留一个小的顾问角色"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="Q26",
        title="不确定性容忍（交叉验证）",
        scenario=(
            "公司刚收购了一家初创公司。你被指派做产品整合，但领导层只给了高层愿景——"
            "没有路线图、没有成功指标，被收购团队内部意见也不统一。"
            "你的第一个月："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="按自己的最佳理解开始做，从实际结果中学习并修正方向"),
            QuestionOption(key="B", text="花两周访谈双方利益相关者，在编码之前整合出一份统一的方向文档"),
            QuestionOption(key="C", text="提议一个小型可逆的试点整合来验证假设，用结果去争取更明确的授权"),
            QuestionOption(key="D", text="向上反馈：项目需要先明确范围和成功标准，才能开展有意义的工作"),
        ],
        dimensions=["unc"],
    ),
    Question(
        id="Q27",
        title="决策风格（预算分配）",
        scenario=(
            "做重大决策时，给以下输入分配 100 分——"
            "反映你实际的权重，而非你觉得应该怎样："
        ),
        type=QuestionType.budget,
        options=[
            QuestionOption(key="A", text="量化证据——指标、A/B 测试、基准、市场数据"),
            QuestionOption(key="B", text="模式识别——过往经验和直觉判断"),
            QuestionOption(key="C", text="利益相关者共识——受影响人群的认同"),
            QuestionOption(key="D", text="第一性原理推导——从基本约束出发的逻辑推理"),
        ],
        dimensions=["decision"],
    ),
    Question(
        id="Q28",
        title="成长路径（交叉验证）",
        scenario=(
            "你同一天收到两个内部转岗 offer，薪酬、职级、团队质量完全相同。\n\n"
            "Offer X：在你已经精通 4 年的技术栈上做高级角色。你将成为"
            "无可争议的领域专家，指导新人，掌控技术路线图。\n\n"
            "Offer Y：在一个全新组建的团队做高级角色，探索你从未接触的领域。"
            "你将是经验最少的人，需要 6 个月以上的学习曲线，但会获得完全不同的视野。"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="选 X——深度创造不可替代的价值，即使在『已知』领域也总有更多可以精通的"),
            QuestionOption(key="B", text="选 Y——成长来自不适，重做初学者让你保持敏锐和多面"),
            QuestionOption(key="C", text="选 X，但争取 20% 时间跟 Y 团队交叉学习"),
            QuestionOption(key="D", text="选 Y，但前提是能从现有领域带一个项目过去，保持连续性"),
        ],
        dimensions=["growth"],
    ),
    Question(
        id="Q29",
        title="驱动力来源（交叉验证）",
        scenario=(
            "团队刚经历了三个月的艰苦冲刺，发布了一个重大功能。"
            "经理让每人选一个奖励，全部真诚提供，不带评判："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="VP 在 all-hands 上点名表扬你的具体贡献"),
            QuestionOption(key="B", text="5000 美元即时奖金，打入下个月工资，没有仪式"),
            QuestionOption(key="C", text="本季度额外三天带薪假，随便怎么用"),
            QuestionOption(key="D", text="下一个季度完全自主选择做什么项目的权利"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="Q30",
        title="表达风格，跨职能（交叉验证）",
        scenario=(
            "市场部已经向大客户承诺一个功能 6 周内上线。你是工程负责人，"
            "诚实估计需要 10-12 周。新闻稿已经发了，销售 VP 对延期的想法很愤怒。"
            "该客户是前三大营收客户。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="和市场负责人、销售 VP 开私下会议，摆出技术现实，在跟客户沟通之前先内部协商出新时间线"),
            QuestionOption(key="B", text="承诺 6 周期限但立即砍范围——按时交付一个最小版本，定义为『第一期』"),
            QuestionOption(key="C", text="上报给你们共同的高管（CTO/CEO），透明呈现取舍，让领导层决定如何处理对外承诺"),
            QuestionOption(key="D", text="和销售 VP 一起直接去找客户，坦诚说明修正后的时间线，并提供一个具体的过渡方案以维护信任"),
        ],
        dimensions=["expression"],
    ),
]
