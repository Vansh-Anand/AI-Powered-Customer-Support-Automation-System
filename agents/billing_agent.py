"""
Billing Support Agent

Handles invoices, payments and refund requests.

Author : Vansh Anand
"""

def billing_agent(state):

    query = state["user_query"]

    response = f"""
Billing Support

Customer Query:
{query}

Your billing request has been received.

If this request involves a refund, supervisor approval may be required.
"""

    state["department_response"] = response

    return state
