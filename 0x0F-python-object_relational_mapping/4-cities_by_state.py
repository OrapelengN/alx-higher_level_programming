#!/usr/bin/python3
import MySQLdb
import sys


def list_cities_by_state(username, password, database):
    """Lists all cities in the given database along with
    their associated states."""
    # Connect to the MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()

    # Perform the SQL query with a JOIN between cities and states
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query)

    # Fetch and print all results
    cities = cur.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    # Ensure that exactly 3 arguments are passed (excluding the script name)
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Call the function to list cities by state
        list_cities_by_state(username, password, database)
