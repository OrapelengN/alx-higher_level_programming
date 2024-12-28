#!/usr/bin/python3
import MySQLdb
import sys


def list_states():
    """Fetches and lists all states from the database."""
    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to select all states, ordered by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results
    rows = cursor.fetchall()

    # Print the results as tuples
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_states()

