#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Create engine to connect to MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    # Create a configured session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states with 'a' in the name
    states_to_delete = (
            session.query(State).filter(State.name.like('%a%')).all()
    )

    # Delete all matching records
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction
    session.commit()

    # Close session
    session.close()
