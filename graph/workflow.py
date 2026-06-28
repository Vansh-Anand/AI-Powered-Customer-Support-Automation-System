from langgraph.graph import StateGraph, START, END

from graph.state import CustomerState
from graph.router import route_query

from agents.classifier import classify_intent
from agents.sales_agent import sales_agent
from agents.technical_agent import technical_agent
from agents.billing_agent import billing_agent
from agents.account_agent import account_agent

from agents.approval_agent import approval_agent, human_approval
from agents.supervisor import supervisor_agent


def route_approval(state):
    if state.get("approval_required"):
        return "human"
    return "supervisor"


workflow = StateGraph(CustomerState)

# Nodes
workflow.add_node("classifier", classify_intent)
workflow.add_node("sales", sales_agent)
workflow.add_node("technical", technical_agent)
workflow.add_node("billing", billing_agent)
workflow.add_node("account", account_agent)

workflow.add_node("approval", approval_agent)
workflow.add_node("human", human_approval)
workflow.add_node("supervisor", supervisor_agent)

# Start
workflow.add_edge(START, "classifier")

# Conditional Routing
workflow.add_conditional_edges(
    "classifier",
    route_query,
    {
        "sales": "sales",
        "technical": "technical",
        "billing": "billing",
        "account": "account",
    },
)

workflow.add_edge("sales", "approval")
workflow.add_edge("technical", "approval")
workflow.add_edge("billing", "approval")
workflow.add_edge("account", "approval")

workflow.add_conditional_edges(
    "approval",
    route_approval,
    {
        "human": "human",
        "supervisor": "supervisor"
    }
)

workflow.add_edge("human", "supervisor")
workflow.add_edge("supervisor", END)

customer_support_graph = workflow.compile()
