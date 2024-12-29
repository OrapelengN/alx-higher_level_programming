#!/usr/bin/python3
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
