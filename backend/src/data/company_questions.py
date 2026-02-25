"""Company DNA 题库 — 20 道行为场景题。

CQ01-CQ10 定义在此文件；CQ11-CQ20 在 company_questions_ext.py 中。
合并导出：COMPANY_QUESTIONS（全部 20 道 Question 对象列表）。
由 HR + 5 名以上同团队员工（匿名）填写，构建公司文化画像。
"""

from src.models.questionnaire import Question, QuestionOption, QuestionType

from src.data.company_questions_ext import COMPANY_QUESTIONS_EXT

# -- CQ01-CQ10 -------------------------------------------------------

_COMPANY_Q01_Q10: list[Question] = [
    Question(
        id="CQ01",
        title="工作节奏 + 决策风格",
        scenario=(
            "一个功能技术上已经就绪，但还有些粗糙的地方。产品负责人说"
            "『尽快拿到用户反馈。』在你的团队里，最可能的结果是："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="立刻发布，收集数据，根据真实反馈打磨——速度是我们学习的方式"),
            QuestionOption(key="B", text="再花一周磨平最明显的粗糙之处，然后发布——平衡很重要"),
            QuestionOption(key="C", text="等到体验打磨到位再发——我们宁愿晚一些也不愿发半成品"),
            QuestionOption(key="D", text="先发给小范围内测用户，验证后再全面铺开——可控的速度"),
        ],
        dimensions=["pace", "decision"],
    ),
    Question(
        id="CQ02",
        title="协作模式 + 表达风格",
        scenario=(
            "周五下午，一位工程师发现了一个非紧急的生产环境风险。"
            "大部分团队成员已经收工了。在你的团队里，通常会怎么做？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="自己修好，周一站会时提一下——个人主动性被重视"),
            QuestionOption(key="B", text="在团队频道描述问题，有空的人会跳进来一起搞"),
            QuestionOption(key="C", text="创建一个高优先级工单——流程确保不会遗漏"),
            QuestionOption(key="D", text="ping 最熟悉那块代码的人，快速结对修复——定向协作"),
        ],
        dimensions=["collab", "expression"],
    ),
    Question(
        id="CQ03",
        title="不确定性容忍",
        scenario=(
            "一个新项目来了，只有大致方向，没有需求文档、没有线框图、"
            "没有参考实现。你的团队通常怎么启动？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="直接上手——大家开始搭原型，边做边想"),
            QuestionOption(key="B", text="花几天调研类似方案，然后对齐一个计划"),
            QuestionOption(key="C", text="推动先出一个更清晰的 brief 再投入资源——模糊性浪费精力"),
            QuestionOption(key="D", text="快速跑一个 spike 来暴露未知，然后重新聚集、正式规划"),
        ],
        dimensions=["unc"],
    ),
    Question(
        id="CQ04",
        title="表达风格",
        scenario=(
            "设计评审中，一位相对初级的团队成员不同意资深同事的方案。"
            "在你的团队文化里，通常会怎么样？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="直接在会上提出——不论资历，每个人的意见同等重要"),
            QuestionOption(key="B", text="委婉地提出，通常以提问的方式而非直接挑战"),
            QuestionOption(key="C", text="通常会在会上忍住，会后私下提"),
            QuestionOption(key="D", text="会后用书面形式（评论、文档或消息）分享自己的看法"),
        ],
        dimensions=["expression"],
    ),
    Question(
        id="CQ05",
        title="驱动力",
        scenario=(
            "想想你团队里表现最好的人为什么留下来（薪酬以外），"
            "主要原因通常是："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="使命——他们相信公司正在尝试改变世界的事"),
            QuestionOption(key="B", text="成长轨迹——他们能看到通往更大范围、更高职级和更大影响力的清晰路径"),
            QuestionOption(key="C", text="技术——他们能和优秀的同行一起解决技术上有挑战性的问题"),
            QuestionOption(key="D", text="平衡——可预期的工作时间、可控的压力，以及对个人生活的尊重"),
        ],
        dimensions=["motiv"],
    ),
    Question(
        id="CQ06",
        title="工作节奏 + 不确定性容忍",
        scenario=(
            "你的团队在评估两个技术方案：方案 A 久经验证，结果可预测；"
            "方案 B 来自最新研究，理论性能更好但零生产使用记录。"
            "截止日期在 3 个月后，你的团队最可能会："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="选 A——已验证且可靠胜过理论上的承诺"),
            QuestionOption(key="B", text="花一周压力测试 B；如果扛得住就切换，否则 A 是后备"),
            QuestionOption(key="C", text="选 B——三个月足够，突破性成果值得冒险"),
            QuestionOption(key="D", text="以 A 为主线推进，同时并行探索 B 作为未来选项"),
        ],
        dimensions=["pace", "unc"],
    ),
    Question(
        id="CQ07",
        title="协作模式 + 成长",
        scenario=(
            "当团队中有人在某个特定领域积累了深厚专业知识时，"
            "团队通常怎么分享和利用这些知识？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="写内部文档或录教程——可扩展的自助知识库"),
            QuestionOption(key="B", text="成为团队的 go-to person，有需要就直接问——自然而私人的方式"),
            QuestionOption(key="C", text="偶尔组织知识分享会或 workshop 给更广泛的团队"),
            QuestionOption(key="D", text="在实际任务中和其他人结对，通过实践传递知识"),
        ],
        dimensions=["collab", "growth"],
    ),
    Question(
        id="CQ08",
        title="表达风格 + 执行风格",
        scenario=(
            "一位团队成员错过了承诺的截止日期好几天，没有外部因素——"
            "纯粹是低估了复杂度。在你的团队里，典型的反应是："
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="提前主动标记延迟，分享修订计划，团队相应调整——透明是期望"),
            QuestionOption(key="B", text="做一个回顾来理解发生了什么，改进未来的估算——流程改进"),
            QuestionOption(key="C", text="悄悄处理——deadline 顺延，只要质量好就没什么大不了的"),
            QuestionOption(key="D", text="有明显的不满——承诺被认真对待，错过会有社交层面的后果"),
        ],
        dimensions=["expression", "execution"],
    ),
    Question(
        id="CQ09",
        title="决策风格 + 不确定性容忍",
        scenario=(
            "一个高风险决策需要本周做出。数据不全，团队意见冲突，"
            "没时间做彻底分析。你的团队通常怎么处理？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="最资深的人基于经验拍板——速度重要，而且他们见过类似情况"),
            QuestionOption(key="B", text="团队做一个快速的结构化分析——即使压缩了，数据也比直觉强"),
            QuestionOption(key="C", text="快速召集小组讨论，收集各方视角，顺应浮现的共识"),
            QuestionOption(key="D", text="选最可逆的方案——最小承诺，快速学习，快速调整"),
        ],
        dimensions=["decision", "unc"],
    ),
    Question(
        id="CQ10",
        title="协作模式",
        scenario=(
            "三位团队成员在做需要互相集成的独立模块。接口还没定义，"
            "截止日期很紧。在你的团队里，通常会怎么做？"
        ),
        type=QuestionType.choice,
        options=[
            QuestionOption(key="A", text="各自基于假设先开始做，有具体产出后再对齐"),
            QuestionOption(key="B", text="团队留出半天一起设计接口，然后再各自写代码"),
            QuestionOption(key="C", text="一个人先拟好接口契约，发出去征求异步反馈——主动驱动"),
            QuestionOption(key="D", text="耦合度最高的两个模块先结对，第三个人等核心契约确定后加入"),
        ],
        dimensions=["collab"],
    ),
]

# -- 合并导出 ----------------------------------------------------------

COMPANY_QUESTIONS: list[Question] = _COMPANY_Q01_Q10 + COMPANY_QUESTIONS_EXT
"""全部 20 道 Company DNA 题目（CQ01-CQ20）。"""
