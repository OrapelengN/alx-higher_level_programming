#!/usr/bin/python3
"""
Lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
"""
import MySQLdb


def get_states_by_name_like(username, password, database, name_like):
    """
    This function retrieves all states from the database hbtn_0e_0_usa that have a name starting with the provided like pattern.

    Args:
        username: The username for the MySQL database.
        password: The password for the MySQL database.
        database: The name of the MySQL database.
        name_like: The pattern to match against the state names (e.g., 'N%').

    Returns:
        A list of tuples, where each tuple represents a state with its id and name.
    """

    # Connect to the MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=database)
    cur = conn.cursor()

    # Execute the query to get states with names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(query, (name_like,))

    # Fetch all results
    query_rows = cur.fetchall()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return query_rows


if __name__ == "__main__":
    # Get user input for username, password, and database name
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter database name: ")

    # Get states starting with 'N' from the database
    states = get_states_by_name_like(username, password, database, "N%")

    # Print the results
    for state in states:
        print(state)
