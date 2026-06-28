"""
classifier.py

Intent Classification Node

Author : Vansh Anand
"""

from langchain_ollama import ChatOllama


# Load Local Llama 3 Model
llm = ChatOllama(
    model="llama3.1",
    temperature=0
)


def classify_intent(state):
    """
    Classifies the customer's query into one department.
    """

    query = state["user_query"]

    prompt = f"""
You are an intent classification assistant.

Classify the customer query into ONLY ONE of these categories:

Sales
Technical
Billing
Account

Return ONLY the category name.

Customer Query:
{query}
"""

    response = llm.invoke(prompt)

    intent = response.content.strip()

    print(f"\nIntent Detected:\n{intent}")

    state["intent"] = intent

    return state
