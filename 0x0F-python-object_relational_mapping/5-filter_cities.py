#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`,
ordered by the cities' `id`.
The cities are filtered by the state name, which is provided as an argument.

It connects to the MySQL database using the provided username, password, and
database name,
and performs a safe query using parameterized SQL to prevent SQL injection.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name>
    <state_name>

Arguments:
    mysql_username: MySQL username for the database connection.
    mysql_password: MySQL password for the database connection.
    database_name: The name of the database to connect to.
    state_name: The name of the state whose cities we want to list.

The script outputs the cities (if any) in the specified state,
sorted by the city's id.
"""
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

    # Print the results in the desired format
    if cities:
        print(", ".join([city[0] for city in cities]))
    else:
        print()

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
