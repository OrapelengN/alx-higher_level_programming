#!/usr/bin/python3
"""
This script inserts a new state into the `states` table and displays all states
from the database.
"""

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert_and_display_records():
    """Inserts a new state and displays all states."""
    # Database connection parameters
    username = "root"
    password = "root"
    database = "hbtn_0e_6_usa"

    # Create engine and session
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert a new state record
    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    # Display all records from the states table
    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    insert_and_display_records()
