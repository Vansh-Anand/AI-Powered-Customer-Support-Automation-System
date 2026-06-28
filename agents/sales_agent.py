"""
Sales Support Agent

Author : Vansh Anand
"""

from rag.rag_pipeline import retrieve_context


def sales_agent(state):

    query = state["user_query"]

    context = retrieve_context(query)

    state["retrieved_context"] = context

    response = """
Sales Support

We provide three subscription plans.
Please refer to the pricing guide above for complete details.
"""

    state["department_response"] = response

    return state
