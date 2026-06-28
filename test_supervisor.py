from agents.supervisor import supervisor_agent

state = {

    "customer_name": "Vansh",

    "user_query": "Tell me about pricing plans.",

    "intent": "Sales",

    "retrieved_context":
    """Starter Plan
Professional Plan
Enterprise Plan""",

    "department_response":
    """Sales Support
We provide three subscription plans.""",

    "final_response": "",

    "approval_required": False,

    "approval_status": True

}

state = supervisor_agent(state)

print("=" * 60)

print(state["final_response"])
