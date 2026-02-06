import os
import json
import database
from typing import List, TypedDict, Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

load_dotenv()

llm = ChatOpenAI(
    model="Qwen/Qwen3-30B-A3B",
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("BASE_URL"),
    temperature=0.7,
)

class QuestionsJson(TypedDict):
    num: int
    q: str
    state: Literal["not_asked", "completed"]
    score: float


class AgentState(TypedDict):
    user_name: str
    user_level: str
    DB_info: str
    questions: List[QuestionsJson]
    current_qn: str
    current_qn_num: int | None
    ans_status: str
    exit_status: Literal["Yes", "No"]
    remarks: str

# 节点定义

def collect_userinfo(state: AgentState) -> AgentState:
    print("=== 收集用户信息 ===")
    state["user_name"] = input("请输入您的姓名: ")
    state["user_level"] = input("请输入您的级别: ")
    print()
    return state


def db_search(state: AgentState) -> AgentState:
    print("=== 数据库检索 ===")
    state["DB_info"] = database.main(state["user_level"])
    return state


def generate_qns(state: AgentState) -> AgentState:
    print("=== 生成问题 ===")

    prompt = f"""
你是一个系统，只能输出 JSON。

【任务】
基于下列参考信息，生成 3 个考核问题。

【参考信息】
{state["DB_info"]}

【JSON Schema】
[
  {{
    "num": 1,
    "q": "问题内容"
  }}
]

【规则】
1. 只能输出 JSON
2. 不要解释
3. 不要 Markdown
4. 数组长度必须是 3
5. 即使信息不足，也必须生成问题

现在只输出 JSON。
"""

    try:
        response = llm.invoke(prompt)
        content = response.content.strip()

        if content.startswith("```"):
            content = content.strip("`")

        raw_questions = json.loads(content)

    except Exception as e:
        print(f"LLM 生成问题失败，使用默认问题: {e}")
        raw_questions = []

    # ===== 系统级清洗（关键）=====
    clean_questions: List[QuestionsJson] = []

    for i, q in enumerate(raw_questions[:3], start=1):
        clean_questions.append({
            "num": int(q.get("num", i)),
            "q": str(q.get("q", "")).strip(),
            "state": "not_asked",
            "score": 0.0
        })

    # 补足 3 个问题
    while len(clean_questions) < 3:
        clean_questions.append({
            "num": len(clean_questions) + 1,
            "q": "（补充问题）请结合参考信息进行说明",
            "state": "not_asked",
            "score": 0.0
        })

    state["questions"] = clean_questions
    print(f"成功生成 {len(clean_questions)} 个问题\n")
    return state


def output_qns(state: AgentState) -> AgentState:
    print("=== 输出问题 ===")

    for q in state["questions"]:
        if q["state"] == "not_asked":
            print(f"问题 {q['num']}: {q['q']}\n")
            state["current_qn"] = q["q"]
            state["current_qn_num"] = q["num"]
            return state

    state["exit_status"] = "Yes"
    return state


def answer_qns(state: AgentState) -> AgentState:
    if state["current_qn"]:
        print("=== 回答问题 ===")
        print(f"当前问题: {state['current_qn']}")
        state["ans_status"] = input("请输入您的答案: ")
        print()
    return state


def check_answer(state: AgentState) -> AgentState:
    if not state["ans_status"]:
        return state

    print("=== 批改答案 ===")

    prompt = f"""
你是一个自动评分系统，只能输出 JSON。

【问题】
{state["current_qn"]}

【用户答案】
{state["ans_status"]}

【参考信息】
{state["DB_info"]}

【JSON Schema】
{{
  "evaluation": "一句简短评价",
  "score": 0.0,
  "reference_points": ["要点1", "要点2", "要点3"]
}}

【规则】
1. 只能输出 JSON
2. 不要解释
3. 不要 Markdown
4. 如果无法判断，请给 5.0 分

现在只输出 JSON。
"""

    try:
        response = llm.invoke(prompt)
        result = json.loads(response.content.strip())
    except Exception as e:
        print(f"批改失败，使用兜底评分: {e}")
        result = {
            "evaluation": "答案已提交，但模型解析失败",
            "score": 5.0,
            "reference_points": []
        }

    print(f"评价: {result['evaluation']}")
    print(f"得分: {result['score']}/10\n")

    for q in state["questions"]:
        if q["num"] == state["current_qn_num"]:
            q["score"] = float(result["score"])
            break

    state["remarks"] = result["evaluation"]
    return state


def update_qn_list(state: AgentState) -> AgentState:
    print("=== 更新问题列表 ===")

    for q in state["questions"]:
        if q["num"] == state["current_qn_num"]:
            q["state"] = "completed"
            print(f"问题 {q['num']} 已完成")
            break

    # 清空临时状态
    state["current_qn"] = ""
    state["current_qn_num"] = None
    state["ans_status"] = ""

    state["exit_status"] = (
        "Yes" if all(q["state"] == "completed" for q in state["questions"]) else "No"
    )

    print()
    return state


def exit_decision(state: AgentState) -> str:
    return "生成概览" if state["exit_status"] == "Yes" else "输出问题"


def generate_summary(state: AgentState) -> AgentState:
    print("=== 生成训练概览 ===")

    total = sum(q["score"] for q in state["questions"])
    avg = total / len(state["questions"])

    print(f"学员: {state['user_name']}")
    print(f"级别: {state['user_level']}")
    print(f"平均得分: {avg:.1f}/10\n")

    for q in state["questions"]:
        print(f"问题 {q['num']}: {q['q']}")
        print(f"  得分: {q['score']}/10\n")

    if avg >= 8:
        print("表现优秀，建议挑战更高级内容。")
    elif avg >= 6:
        print("表现良好，建议针对弱项复习。")
    else:
        print("需要加强学习，建议系统复盘相关知识点。")

    return state

# LangGraph 构建
graph = StateGraph(AgentState)

graph.add_node("收集用户信息", collect_userinfo)
graph.add_node("数据库检索", db_search)
graph.add_node("生成问题", generate_qns)
graph.add_node("输出问题", output_qns)
graph.add_node("回答问题", answer_qns)
graph.add_node("批改答案", check_answer)
graph.add_node("更新问题列表", update_qn_list)
graph.add_node("生成概览", generate_summary)

graph.set_entry_point("收集用户信息")

graph.add_edge("收集用户信息", "数据库检索")
graph.add_edge("数据库检索", "生成问题")
graph.add_edge("生成问题", "输出问题")
graph.add_edge("输出问题", "回答问题")
graph.add_edge("回答问题", "批改答案")
graph.add_edge("批改答案", "更新问题列表")

graph.add_conditional_edges(
    "更新问题列表",
    exit_decision,
    {
        "输出问题": "输出问题",
        "生成概览": "生成概览"
    }
)

graph.add_edge("生成概览", END)

QA_training_agent = graph.compile()

# 运行入口
if __name__ == "__main__":
    initial_state: AgentState = {
        "user_name": "",
        "user_level": "",
        "DB_info": "",
        "questions": [],
        "current_qn": "",
        "current_qn_num": None,
        "ans_status": "",
        "exit_status": "No",
        "remarks": ""
    }

    print("=== 开始问答训练 ===")
    QA_training_agent.invoke(initial_state)
    print("=== 训练结束 ===")
