#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa.
'''
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to mySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    # Execute SQL query to retrieve all states, sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print each row
    for state in cursor.fetchall():
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
