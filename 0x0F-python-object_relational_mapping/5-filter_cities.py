#!/usr/bin/python3
import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    """Lists all cities of a given state, ordered by city ID, with protection
    against SQL injection."""
    # Connect to the MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()

    # Perform the SQL query with a JOIN and filtering by state name
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query, (state_name,))

    # Fetch and print all results
    cities = cur.fetchall()
    city_names = [city[0] for city in cities]  # Extract city names from result

    # Print cities as a comma-separated string
    print(", ".join(city_names))

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    # Ensure that exactly 4 arguments are passed (including the script name)
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        # Call the function to filter cities by state
        filter_cities_by_state(username, password, database, state_name)
