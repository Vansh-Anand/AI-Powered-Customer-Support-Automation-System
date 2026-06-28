"""
approval_agent.py

Author : Vansh Anand
"""


HIGH_RISK_KEYWORDS = [
    "refund",
    "cancel",
    "cancellation",
    "account closure",
    "close account",
    "compensation",
    "management"
]


def approval_agent(state):

    query = state["user_query"].lower().strip()

    print("Customer Query:", query)

    state["approval_required"] = any(
        keyword in query
        for keyword in HIGH_RISK_KEYWORDS
    )

    return state


def human_approval(state):

    if not state["approval_required"]:

        state["approval_status"] = True

        return state

    print("\n" + "="*60)

    print("HUMAN APPROVAL REQUIRED")

    print("="*60)

    print("\nCustomer Query:")

    print(state["user_query"])

    choice = input("\nApprove Request? (yes/no): ").strip().lower()

    if choice == "yes":

        state["approval_status"] = True

        state["final_response"] = (

            "Request approved by supervisor."

        )

    else:

        state["approval_status"] = False

        state["final_response"] = (

            "Request rejected by supervisor."

        )

    return state
