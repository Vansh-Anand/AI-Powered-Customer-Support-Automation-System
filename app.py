"""
AI-Powered Customer Support Automation System
Author: Vansh Anand
"""

from graph.workflow import customer_support_graph
from memory.sqlite_memory import initialize_database, save_conversation, get_last_conversation

def main():
    initialize_database()

    print("=" * 50)
    print("ABC Technologies Customer Support System")
    print("=" * 50)

    customer_name = input("\nCustomer Name:\n").strip()
    query = input("\nEnter your query:\n").strip()

    if "previous support issue" in query.lower():
        last_conv = get_last_conversation(customer_name)
        if last_conv:
            print("=" * 50)
            print("Previous Support Issue")
            print("=" * 50)

            print(f"\nCustomer: {customer_name}")
            print(f"\nPrevious Query:\n{last_conv[0]}")
            print(f"\nDepartment: {last_conv[1]}")
            print(f"\nDate: {last_conv[4]}")

            print("\nSummary:")
            print(f"Your previous support request was related to a {last_conv[1].lower()} issue.")

            print("\nThank you for contacting ABC Technologies.")
        else:
            print("\nNo previous support issues found.")
        return

    initial_state = {
        "customer_name": customer_name,
        "user_query": query,
        "intent": "",
        "retrieved_context": "",
        "department_response": "",
        "final_response": "",
        "approval_required": False,
        "approval_status": False
    }
    
    result = customer_support_graph.invoke(initial_state)

    save_conversation(result)

    print("\n-----------------------------------------")
    print("Final Response")
    print("-----------------------------------------")
    print(result["final_response"])


if __name__ == "__main__":
    main()
