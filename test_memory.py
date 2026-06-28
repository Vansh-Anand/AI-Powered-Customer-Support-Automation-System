from memory.sqlite_memory import *

initialize_database()

sample_state = {

    "customer_name": "Vansh",

    "user_query": "I need a refund.",

    "intent": "Billing",

    "retrieved_context": "",

    "department_response": "Refund request received.",

    "final_response": "Supervisor approval required.",

    "approval_required": True,

    "approval_status": False

}

save_conversation(sample_state)

conversation = get_last_conversation("Vansh")

print("="*60)

print("Last Conversation\n")

print(conversation)
