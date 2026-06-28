"""
supervisor.py

Final validation before sending the response
to the customer.

Author : Vansh Anand
"""


def supervisor_agent(state):
    """
    Validates and prepares the final response.
    """

    # If approval was required but rejected
    if state["approval_required"] and not state["approval_status"]:

        state["final_response"] = (
            "Your request cannot be processed because it was not approved by the supervisor."
        )

        return state

    response = ""

    # Add retrieved knowledge if available
    if state["retrieved_context"]:

        response += "Relevant Information\n"
        response += "-" * 40 + "\n"
        response += state["retrieved_context"]
        response += "\n\n"

    # Add department response
    response += "Support Response\n"
    response += "-" * 40 + "\n"
    response += state["department_response"]

    # Final closing
    response += (
        "\n\nThank you for contacting ABC Technologies."
    )

    state["final_response"] = response

    return state
