#!/usr/bin/python3
"""
Script to print the first State object from the database 'hbtn_0e_6_usa'
using SQLAlchemy.

The script connects to the database, queries for the first state based on the
lowest id,
and prints the state id and name. If the states table is empty,
it prints 'Nothing' followed
by a new line.
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    # Take the arguments: username, password, database name
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

    # Query for the first State object
    state = session.query(State).order_by(State.id).first()

    # If a state is found, display it; otherwise print "Nothing"
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
