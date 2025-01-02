#!/usr/bin/python3
"""
This script lists all states in a MySQL database whose name matches the provided state name.

It connects to the MySQL database using the provided username, password, and database name,
and performs a safe query using parameterized SQL to prevent SQL injection.

Usage:
    ./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>

Arguments:
    mysql_username: MySQL username for the database connection.
    mysql_password: MySQL password for the database connection.
    database_name: The name of the database to connect to.
    state_name: The name of the state to search for in the database.

The script outputs the state(s) with matching names and their corresponding id, sorted by the id.
"""
import MySQLdb
import sys


def safe_filter_states_by_name(username, password, database, state_name):
    """Lists all states in the given database whose name matches the argument,
    with protection against SQL injection."""
    # Connect to the MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = conn.cursor()

    # Use parameterized query to prevent SQL injection
    query = (
            "SELECT id, name FROM states WHERE BINARY name = %s "
            "ORDER BY id ASC"
    )
    cur.execute(query, (state_name,))

    # Fetch all results
    states = cur.fetchall()

    # Fetch all results
    if states:
        print(f"Found {len(states)} matching state(s).")
        for state in states:
            print(state)
    else:
        print("No matching states found.")

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    # Ensure that 4 arguments are passed (including the script name)
    if len(sys.argv) == 5:
        # Retrieve arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        # Call the function to filter states by name
        safe_filter_states_by_name(username, password, database, state_name)
