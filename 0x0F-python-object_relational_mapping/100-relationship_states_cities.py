#!/usr/bin/python3
"""
This script creates a State 'California' with a City 'San Francisco' in the
database.
The script connects to MySQL server using the provided username, password,
and database name.
The State and City are linked with a relationship defined in SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from model_base import Base


if __name__ == "__main__":
    """
    Main execution:
    - Connect to the database using SQLAlchemy.
    - Create tables if they do not exist.
    - Insert California and San Francisco if not present.
    """

    # Take arguments for username, password, and database name
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the connection string
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create the tables (if not already created)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City objects
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add them to the session and commit
    session.add(california)
    session.add(san_francisco)
    session.commit()

    print(f"State: {california.name}, City: {san_francisco.name}")

    # Close the session
    session.close()
