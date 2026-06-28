"""
Technical Support Agent

Author : Vansh Anand
"""

from rag.rag_pipeline import retrieve_context


def technical_agent(state):

    query = state["user_query"]

    # Retrieve relevant information from Technical Manual
    context = retrieve_context(query)

    # Store context in shared state
    state["retrieved_context"] = context

    # Department-specific response
    response = """
Technical Support

We have analyzed your issue.

Please follow the troubleshooting steps provided above.

If the issue persists, contact our technical support team.
"""

    state["department_response"] = response

    return state
