from graph.workflow import customer_support_graph

queries = [
    "I forgot my account password.",
    "What are your pricing plans?",
    "My app crashes",
    "I need a refund",
    "I forgot my password"
]

for query in queries:
    state = {
        "customer_name": "Vansh",
        "user_query": query,
        "intent": "",
        "retrieved_context": "",
        "department_response": "",
        "final_response": "",
        "approval_required": False,
        "approval_status": False
    }

    result = customer_support_graph.invoke(state)
    
    print("-" * 40)
    print(f"Query: {query}")
    print(f"Detected Intent: {result['intent']}")
    print(f"Department Response: {result['department_response']}")
print("-" * 40)
