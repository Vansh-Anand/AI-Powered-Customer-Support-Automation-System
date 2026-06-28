"""
sqlite_memory.py

Handles conversation memory using SQLite.

Author : Vansh Anand
"""

import sqlite3


DATABASE = "database/customer_support.db"


def initialize_database():
    """
    Creates the conversation table if it does not exist.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            customer_name TEXT,

            user_query TEXT,

            intent TEXT,

            department_response TEXT,

            final_response TEXT,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()


def save_conversation(state):
    """
    Saves one conversation into the database.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""

        INSERT INTO conversation_history(

            customer_name,

            user_query,

            intent,

            department_response,

            final_response

        )

        VALUES (?,?,?,?,?)

    """,

    (

        state["customer_name"],

        state["user_query"],

        state["intent"],

        state["department_response"],

        state["final_response"]

    ))

    connection.commit()

    connection.close()


def get_last_conversation(customer_name):
    """
    Retrieves the latest conversation of a customer.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""

        SELECT

            user_query,

            intent,

            department_response,

            final_response,

            timestamp

        FROM conversation_history

        WHERE customer_name = ?

        ORDER BY id DESC

        LIMIT 1

    """,

    (customer_name,))

    data = cursor.fetchone()

    connection.close()

    return data
