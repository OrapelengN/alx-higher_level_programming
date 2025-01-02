#!/usr/bin/python3
"""
Script to update the name of a state with id = 2 in the 'hbtn_0e_6_usa'
database.
The script connects to a MySQL database, changes the name of the state with id
= 2 to "New Mexico",
and commits the changes to the database.
This script uses SQLAlchemy to interact with the database and perform the
update.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    # Take the arguments: mysql username, password, and database name
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

    # Query the State object where id = 2 and update its name
    state = session.query(State).filter(State.id == 2).first()

    # If the state exists, update its name
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
