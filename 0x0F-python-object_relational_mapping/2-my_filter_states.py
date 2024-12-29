#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
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
    query = (
            "SELECT * FROM states WHERE name = '{}' "
            "ORDER BY id ASC".format(state_name)
            )

    # Execute the query
    cursor.execute(query)

    # Fetch and print results
    for state in cursor.fetchall():
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
