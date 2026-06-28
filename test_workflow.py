from graph.workflow import customer_support_graph

state = {
    "customer_name": "Vansh",
    "user_query": "I forgot my account password.",
    "intent": "",
    "retrieved_context": "",
    "department_response": "",
    "final_response": "",
    "approval_required": False,
    "approval_status": False
}

result = customer_support_graph.invoke(state)

print("\nDetected Intent:")
print(result["intent"])

print("\nDepartment Response:")
print(result["department_response"])
