from langgraph.graph import StateGraph, START, END

from graph.state import CustomerState
from graph.router import route_query

from agents.classifier import classify_intent
from agents.sales_agent import sales_agent
from agents.technical_agent import technical_agent
from agents.billing_agent import billing_agent
from agents.account_agent import account_agent


workflow = StateGraph(CustomerState)

# Nodes
workflow.add_node("classifier", classify_intent)
workflow.add_node("sales", sales_agent)
workflow.add_node("technical", technical_agent)
workflow.add_node("billing", billing_agent)
workflow.add_node("account", account_agent)

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

# End
workflow.add_edge("sales", END)
workflow.add_edge("technical", END)
workflow.add_edge("billing", END)
workflow.add_edge("account", END)

customer_support_graph = workflow.compile()
