#!/usr/bin/python3 
import MySQLdb  # or 'import pymysql' if you use pymysql instead
import sys


def main():
    # Ensure there are 4 arguments
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql username> "
              "<mysql password> <database name> <state name>")
        return

    # Collect arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL database using MySQLdb (or pymysql)
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name)
        cursor = db.cursor()

        # Debug: Print state_name and query
        print(f"State name: {state_name}")
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        print(f"Executing query: {query} with {state_name}")
        
        # Use parameterized query to prevent SQL injection
        cursor.execute(query, (state_name,))  # This ensures state_name is treated as a parameter

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:  # Catch database errors
        print(f"Error: {e}")
    finally:
        # Ensure resources are closed
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    main()
