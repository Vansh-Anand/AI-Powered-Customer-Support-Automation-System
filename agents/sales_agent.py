"""
Sales Support Agent

Handles product, pricing and subscription queries.

Author : Vansh Anand
"""

def sales_agent(state):

    query = state["user_query"]

    response = f"""
Sales Support

Customer Query:
{query}

We provide three subscription plans:

1. Starter Plan
2. Professional Plan
3. Enterprise Plan

Detailed pricing will be retrieved from the Pricing Guide in the next stage.
"""

    state["department_response"] = response

    return state
