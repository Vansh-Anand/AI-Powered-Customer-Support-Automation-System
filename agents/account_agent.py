"""
Account Support Agent

Handles password reset and account management.

Author : Vansh Anand
"""

def account_agent(state):

    query = state["user_query"]

    response = f"""
Account Support

Customer Query:
{query}

Your account-related request has been received.

Password reset and profile management will be processed securely.
"""

    state["department_response"] = response

    return state
