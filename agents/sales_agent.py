"""
Sales Support Agent

Author : Vansh Anand
"""

from rag.rag_pipeline import retrieve_context


def sales_agent(state):

    query = state["user_query"]

    context = retrieve_context(query)

    state["retrieved_context"] = context

    response = f"""
Sales Support

Relevant Information

{context}
"""

    state["department_response"] = response

    return state
