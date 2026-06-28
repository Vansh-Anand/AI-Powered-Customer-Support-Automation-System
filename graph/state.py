"""
state.py

Shared state used across every LangGraph node.

Author : Vansh Anand
"""

from typing import TypedDict


class CustomerState(TypedDict):
    """
    Stores all customer information during workflow execution.
    """

    # Customer Information
    customer_name: str

    # Customer Query
    user_query: str

    # Detected Department
    intent: str

    # Context retrieved from company documents
    retrieved_context: str

    # Department Agent Output
    department_response: str

    # Supervisor Final Response
    final_response: str

    # Human Approval
    approval_required: bool
    approval_status: bool
