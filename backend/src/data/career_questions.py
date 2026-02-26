"""Career DNA 题库 — 30 道标准化行为场景题。

Q01-Q15 定义在此文件；Q16-Q30 在 career_questions_ext.py 中。
合并导出：CAREER_QUESTIONS（全部 30 道 Question 对象列表）。
"""

from src.models.questionnaire import Question, QuestionOption, QuestionType

from src.data.career_questions_ext import CAREER_QUESTIONS_EXT

# -- Q01-Q15 ---------------------------------------------------------

_CAREER_Q01_Q15: list[Question] = [
    Question(
        id="Q01",
        title="工作节奏 + 决策风格",
        scenario=(
            "你接手了一个新项目。负责人说『越快交付越好——先看看客户怎么说。』"
            "评估后你发现：快速方案有明显瑕疵，但一周内能交付；"
            "完善方案需要三周，但质量更扎实。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="先交付快速版本，收集反馈，再决定是否优化"),
            QuestionOption(key="B", text="和负责人协商折中：两周内交付一个可用版本"),
            QuestionOption(key="C", text="主张采用完善方案，用数据说明返工的长期成本"),
            QuestionOption(key="D", text="快速交付，同时启动优化计划，确保问题不会累积"),
        ],
        dimensions=["pace", "decision"],
    ),
    Question(
        id="Q02",
        title="协作模式 + 沟通",
        scenario=(
            "周五下午——你发现了工作中一个潜在风险。不是紧急问题，但放着不管"
            "下周可能出状况。大部分同事已经下班了。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="自己花几个小时处理好，周一早会时分享"),
            QuestionOption(key="B", text="在团队群里发消息说明问题，看有没有人想一起处理"),
            QuestionOption(key="C", text="创建一个高优先级待办，周一第一件事处理"),
            QuestionOption(key="D", text="直接联系最熟悉那块业务的同事，快速一起解决"),
        ],
        dimensions=["collab", "expression"],
    ),
    Question(
        id="Q03",
        title="不确定性容忍",
        scenario=(
            "你被分配到一个全新项目。经理说『大方向在这——"
            "怎么做你自己想办法。』没有需求文档，没有参考实现。"
            "你的第一反应是："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="兴奋——终于有机会从零定义一些东西了"),
            QuestionOption(key="B", text="先花几天调研类似产品和方案，再做决定"),
            QuestionOption(key="C", text="找经理把需求和边界确认清楚"),
            QuestionOption(key="D", text="快速搭一个最小原型，用它来推动更具体的讨论"),
        ],
        dimensions=["unc"],
    ),
    Question(
        id="Q04",
        title="表达风格（主测）",
        scenario=(
            "你提交了一份工作方案，一位资深同事审阅后给了大量修改意见。"
            "仔细看后，你觉得大部分是风格偏好而非真正的问题。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="逐条回复你的理由，引用规范或最佳实践支持你的立场"),
            QuestionOption(key="B", text="开一个 15 分钟的通话，聊聊主要分歧"),
            QuestionOption(key="C", text="接受大部分建议——对方更资深，团队和谐更重要"),
            QuestionOption(key="D", text="有道理的建议接受；纯风格问题就说『个人偏好——保持原样』"),
        ],
        dimensions=["expression"],
    ),
    Question(
        id="Q05",
        title="驱动力来源",
        scenario=(
            "四个 offer 薪资、地点、职级完全一样，公司不同。你会倾向哪个？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="一家应对气候变化的公司——工作有挑战但商业模式尚未验证"),
            QuestionOption(key="B", text="一家高速增长公司，今年收入翻了三倍——股权可能非常值钱"),
            QuestionOption(key="C", text="一家专业文化卓越的公司——团队有多位业界大牛"),
            QuestionOption(key="D", text="一家盈利稳定的公司，工作生活平衡好，每年有可预期的涨薪"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="Q06",
        title="工作节奏 + 不确定性容忍",
        scenario=(
            "你在调研解决方案时发现两条路径：方案 A 久经验证但效果一般；"
            "方案 B 来自最新研究，理论效果很好但零实战验证。"
            "项目截止日期在三个月后。"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="选 A——已验证、低风险，轻松赶上截止日期"),
            QuestionOption(key="B", text="花一周小范围验证 B；如果不行就切回 A"),
            QuestionOption(key="C", text="选 B——三个月够用，如果成功就是突破性成果"),
            QuestionOption(key="D", text="以 A 为主线推进，同时把 B 作为未来优化方向探索"),
        ],
        dimensions=["pace", "unc"],
    ),
    Question(
        id="Q07",
        title="协作模式 + 成长路径",
        scenario=(
            "一位初级同事总来问你同一领域的类似问题，你已经解释过两三次了。"
            "你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="写文档或录视频，方便对方之后自助查阅"),
            QuestionOption(key="B", text="继续耐心回答——帮助别人也加深了自己的理解"),
            QuestionOption(key="C", text="推荐更系统的学习资源（课程、书籍），帮对方根本性提升"),
            QuestionOption(key="D", text="安排一次结对工作，带对方完整走一遍解决问题的过程"),
        ],
        dimensions=["collab", "growth"],
    ),
    Question(
        id="Q08",
        title="表达风格（主测）",
        scenario=(
            "方案讨论会上，你认为一个方案有严重缺陷——但方案是项目负责人提的。"
            "会议室里有八个人。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="当场提出你的顾虑，用清晰的推理支撑"),
            QuestionOption(key="B", text="会后找负责人私下沟通"),
            QuestionOption(key="C", text="会上用温和的探询式提问，看负责人能否自己发现问题"),
            QuestionOption(key="D", text="会上不说，之后给负责人发一份详细的书面分析"),
        ],
        dimensions=["expression"],
    ),
    Question(
        id="Q09",
        title="驱动力 + 成长路径（强制排序）",
        scenario="按对你的重要性从高到低排列：",
        type=QuestionType.ranking,
        options=[
            QuestionOption(key="A", text="成为某个前沿领域公认的专家"),
            QuestionOption(key="B", text="带领越来越大的团队"),
            QuestionOption(key="C", text="参与改变世界的产品"),
            QuestionOption(key="D", text="获得出色的经济回报"),
            QuestionOption(key="E", text="拥有对自己时间和精力的自由掌控"),
        ],
        dimensions=["motiv", "growth"],
    ),
    Question(
        id="Q10",
        title="工作节奏 + 协作（预算分配）",
        scenario="分配你理想的工作精力比例（总计 100%）：",
        type=QuestionType.budget,
        options=[
            QuestionOption(key="A", text="独立执行（核心专业工作）"),
            QuestionOption(key="B", text="团队讨论、方案评审、协作"),
            QuestionOption(key="C", text="跨职能沟通（产品、业务方）"),
            QuestionOption(key="D", text="学习新知识或探索新方向"),
            QuestionOption(key="E", text="文档、知识管理"),
        ],
        dimensions=["pace", "collab", "execution"],
    ),
    Question(
        id="Q11",
        title="决策风格",
        scenario=(
            "你的团队在评估三家供应商做一个关键业务迁移。你有两周的试用数据、"
            "行业基准，以及来自其他公司可信同行的强力推荐。定量数据略微偏向"
            "供应商 A，但你信任的同行一致推荐供应商 B，说『数据反映不了"
            "实际使用体验。』你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="做加权评分卡，基于数据和基准呈现量化排名，将口碑反馈标注为次要参考"),
            QuestionOption(key="B", text="充分重视同行的实战经验——他们在实际业务中用过这些工具。推荐 B 并记录理由"),
            QuestionOption(key="C", text="设计一周结构化试点，让团队在真实任务中同时使用两家，产出兼顾指标和体验的一手数据"),
            QuestionOption(key="D", text="把数据和推荐都带到团队，引导讨论，让集体判断驱动决策"),
        ],
        dimensions=["decision"],
    ),
    Question(
        id="Q12",
        title="工作节奏 + 执行风格",
        scenario=(
            "你刚接手一个约 40 人每天使用的内部系统，积压了 23 个改进需求和 8 个已知问题。"
            "经理说你全权负责——没有硬性截止日期，只需『让它变得更好。』"
            "你的前两周计划是："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="挑三个呼声最高的快速改进，几天内上线，用这个势头了解真正重要的东西，再做更大的规划"),
            QuestionOption(key="B", text="访谈重度用户、梳理工作流一周，然后制定一份优先级路线图，按序推进"),
            QuestionOption(key="C", text="找到一个能让后续所有变更都更容易的基础性改进，把整整两周投入在这个地基上"),
            QuestionOption(key="D", text="按投入/产出分类所有需求，第一周清掉所有快速改进，然后在更清晰的认知下重新评估"),
        ],
        dimensions=["pace", "execution"],
    ),
    Question(
        id="Q13",
        title="不确定性容忍（交叉验证）",
        scenario=(
            "公司要进入新市场。你在做 demo，但没人能确定潜在客户最关心哪些功能。"
            "两份分析报告意见不一，三次客户对话各自强调不同痛点。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="选择至少两次对话中出现的痛点，围绕它做一个聚焦的 demo，根据真实反馈迭代"),
            QuestionOption(key="B", text="做一个模块化 demo，包含三条独立路径，让销售可以根据受众实时调整"),
            QuestionOption(key="C", text="推回去——在动手之前再安排五次客户发现访谈。做错了的 demo 成本更高"),
            QuestionOption(key="D", text="围绕分析师共识的问题框架来设计 demo，相信分析师能看到个体买家看不到的市场模式"),
        ],
        dimensions=["unc"],
    ),
    Question(
        id="Q14",
        title="决策风格 + 不确定性容忍",
        scenario=(
            "你是项目负责人，项目进行到第六周。昨天竞争对手发布了一个与你们约 60% 重叠的方案。"
            "领导要求当天给出评估：转向、加码还是其他？你有直觉、团队意见，"
            "也可以做严谨分析——但那需要三天。领导需要你今天下班前给出判断。"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="现在就分享你真实的直觉——在这个问题领域浸泡了六周，即使没有表格，你的判断也是有根据的。速度最重要"),
            QuestionOption(key="B", text="花一天做快速结构化分析——方案对比、差异化地图、粗略切换成本估算——带着明确的置信度呈现结论"),
            QuestionOption(key="C", text="告诉领导这么重要的决定不应该当天做。提议 48 小时评估，先给一个明确标注为『不可靠』的初步判断"),
            QuestionOption(key="D", text="召集 90 分钟团队会议，收集集体视角和盲点，然后呈现团队立场而非个人判断"),
        ],
        dimensions=["decision", "unc"],
    ),
    Question(
        id="Q15",
        title="工作节奏 + 执行风格（交叉验证）",
        scenario=(
            "团队周五刚完成一个重大项目。周一，经理提到公司两周后的 all-hands "
            "上可以做一次项目复盘分享（非强制）。你会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="自告奋勇这周整理一个轻量级 10 分钟复盘——趁记忆新鲜，够用就好"),
            QuestionOption(key="B", text="提议团队花一个下午做深入内部复盘，然后下周精炼成一个 all-hands 演示"),
            QuestionOption(key="C", text="建议跳过 all-hands 分享，跑一个快速异步复盘——大家周三前在共享文档里写下收获"),
            QuestionOption(key="D", text="主张第二周做一次正式复盘——收集周期时间数据、问题统计，产出对其他团队也有价值的内容"),
        ],
        dimensions=["pace", "execution"],
    ),
]

# -- 合并导出 ----------------------------------------------------------

CAREER_QUESTIONS: list[Question] = _CAREER_Q01_Q15 + CAREER_QUESTIONS_EXT
"""全部 30 道 Career DNA 题目（Q01-Q30）。"""
