"""
Router Module

Routes the query to the correct support agent.
"""

def route_query(state):

    intent = state["intent"].strip().lower()

    if intent == "sales":
        return "sales"

    elif intent == "technical":
        return "technical"

    elif intent == "billing":
        return "billing"

    elif intent == "account":
        return "account"

    return "sales"
