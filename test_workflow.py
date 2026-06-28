from graph.workflow import customer_support_graph

queries = [
    "What are your pricing plans?",
    "My application crashes while uploading files.",
    "I need a refund.",
    "I forgot my account password."
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
    print(f"Detected Intent:\n{result['intent']}")
    print(f"\nDepartment Response:\n{result['department_response'].strip()}")
print("-" * 40)
