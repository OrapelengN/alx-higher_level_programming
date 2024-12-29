#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    # Take the arguments: mysql username, password, database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine that will interact with the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects where the name contains 'a' (case insensitive)
    states = (session.query(State)
              .filter(State.name.like('%a%'))
              .order_by(State.id)
              .all())

    # If there are results, print them
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()