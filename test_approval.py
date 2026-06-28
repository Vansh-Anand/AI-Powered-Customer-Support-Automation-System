from agents.approval_agent import approval_agent, human_approval


state = {

    "customer_name": "Vansh",

    "user_query": "What are your pricing plans?",

    "intent": "Billing",

    "retrieved_context": "",

    "department_response": "",

    "final_response": "",

    "approval_required": False,

    "approval_status": False

}

state = approval_agent(state)

print("Approval Required:")

print(state["approval_required"])

state = human_approval(state)

print("\nApproval Status:")

print(state["approval_status"])

print("\nFinal Response:")

print(state["final_response"])
