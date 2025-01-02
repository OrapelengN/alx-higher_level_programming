#!/usr/bin/python3
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
    states = cur.fetchall()

    # print(f"Found {len(states)} matching state(s).") # Debugging

    # Fetch all results
    for state in states:
        print(state)

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
