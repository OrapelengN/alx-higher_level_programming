#!/usr/bin/python3
"""
Script to add a new state "Louisiana" to the 'hbtn_0e_6_usa' database using
SQLAlchemy.
The script connects to a MySQL database and inserts the state "Louisiana"
into the 'states' table.
After insertion, the script prints the 'id' of the newly created state.
The query uses parameterized queries to ensure protection against
SQL injection.
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

    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to persist the new state
    session.commit()

    # Print the id of the newly added state
    print(f"{new_state.id}")

    # Close the session
    session.close()
