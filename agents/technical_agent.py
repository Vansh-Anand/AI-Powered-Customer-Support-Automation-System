"""
Technical Support Agent

Handles application and software issues.

Author : Vansh Anand
"""

def technical_agent(state):

    query = state["user_query"]

    response = f"""
Technical Support

Customer Query:
{query}

Suggested troubleshooting:

• Restart the application.
• Check for software updates.
• Verify your internet connection.

The Technical Manual will provide detailed troubleshooting in the next stage.
"""

    state["department_response"] = response

    return state
