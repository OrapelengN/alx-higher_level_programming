#!/usr/bin/python3
"""
Lists all cities from the hbtn_0e_4_usa database,
sorted in ascending order by cities.id.

Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: MySQL username for the database connection.
    mysql_password: MySQL password for the database connection.
    database_name: The name of the database to connect to (hbtn_0e_4_usa).

The script connects to the MySQL server running on localhost at port 3306 and
retrieves and prints all cities from the cities table, sorted by their id.
Each city's id, name, and corresponding state name are displayed.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Ensure that 3 arguments are passed (including the script name)
    if len(sys.argv) != 4:
        print(
            "Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> "
            "<database_name>"
        )
        sys.exit(1)

    # Retrieve MySQL username, password, and database name
    # from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Query to select cities and their state names, sorted by cities.id
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """

    # Execute the query and fetch the results
    cursor.execute(query)

    # Fetch and print all results
    for city in cursor.fetchall():
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()
