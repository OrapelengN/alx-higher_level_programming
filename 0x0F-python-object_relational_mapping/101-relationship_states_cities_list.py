#!/usr/bin/python3
"""
This script lists all State objects and corresponding City objects from the
database.
It takes three arguments: mysql username, mysql password, and database name.
The script uses SQLAlchemy to connect to the MySQL server and perform the
query.

The results are sorted by the state ID and city ID in ascending order.
Each state is printed followed by its cities with the specified format:

<state id>: <state name>
<tabulation><city id>: <city name>

The script should only use one query to retrieve the data.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from relationship_base import Base

if __name__ == "__main__":
    # Parse command-line arguments
    if len(argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py "
              "<mysql username> <mysql password> <database name>")
        exit(1)

    mysql_user = argv[1]
    mysql_pwd = argv[2]
    db_name = argv[3]

    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{mysql_user}:{mysql_pwd}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and their cities in one go
    states = session.query(State).order_by(State.id).all()

    # Print the results with proper indentation
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()
