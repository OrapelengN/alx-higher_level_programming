#!/usr/bin/python3
"""
Script to query and display the State object with the name passed as
an argument from the database 'hbtn_0e_6_usa'.
The script uses SQLAlchemy to connect to the MySQL database and query the
'states' table.
If a state with the given name is found, its 'id' is displayed; otherwise,
'Not found' is printed.
The query is secure against SQL injection by using parameterized queries.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    # Take the arguments: mysql username, password, database name,
    # and state name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine that will interact with the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with the given name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
