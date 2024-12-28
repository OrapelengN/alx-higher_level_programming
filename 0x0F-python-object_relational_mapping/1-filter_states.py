#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor to execute queries
    cur = db.cursor()

    # Execute query to fetch states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all results
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
