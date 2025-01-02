#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table
where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve MySQL username, password, database name, and state name
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use format to safely create SQL query
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"

    # Execute the query
    cursor.execute(query, (state_name,))

    # Fetch and print results
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
