from agents.classifier import classify_intent


sample_state = {
    "customer_name": "",
    "user_query": "I forgot my account password.",
    "intent": "",
    "retrieved_context": "",
    "department_response": "",
    "final_response": "",
    "approval_required": False,
    "approval_status": False
}


result = classify_intent(sample_state)

print("Detected Intent:")
print(result["intent"])
