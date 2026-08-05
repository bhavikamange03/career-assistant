import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from database.lakebase import get_connection


def initialize_database():

    with open("database/schema.sql", "r") as file:
        sql = file.read()

    statements = [
        statement.strip()
        for statement in sql.split(";")
        if statement.strip()
        and not statement.strip().startswith("--")
    ]

    with get_connection() as conn:

        cursor = conn.cursor()

        for statement in statements:
            print("Executing:")
            print(statement[:80])

            cursor.execute(statement)

        conn.commit()

        cursor.close()


if __name__ == "__main__":

    initialize_database()

    print("Database initialized successfully!")