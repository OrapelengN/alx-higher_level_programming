#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
and displays them in the format <state name>: (<city id>) <city name>.
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Take arguments: mysql username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities, ordered by city.id and related to their states
    results = (
        session.query(City, State)
        .join(State)
        .order_by(City.id)
        .all()
    )

    # Display the results as required
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
