#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
along with their associated state names.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == "__main__":
    # Check if there are enough arguments
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py "
              "<mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Retrieve arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Split the connection string into two parts to avoid line too long
    connection_string = (
            f'mysql+mysqldb://{mysql_username}:{mysql_password}@'
            f'localhost/{database_name}'
    )

    # Create the engine
    engine = create_engine(connection_string, pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities and their states, sorted by city.id
    cities = session.query(City).order_by(City.id).all()

    # Iterate over the cities and print the required information
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
