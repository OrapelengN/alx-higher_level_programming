#!/usr/bin/python3
"""
Lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # SQL query (case-sensitive matching)
    cursor.execute(
                   "SELECT * FROM states "
                   "WHERE name LIKE BINARY 'N%' "
                   "ORDER BY id ASC"
            )

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))

    # Close cursor and database connection
    cursor.close()
    db.close()
