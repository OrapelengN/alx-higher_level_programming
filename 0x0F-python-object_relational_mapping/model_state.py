#!/usr/bin/python3
"""
Module to create a State class that maps to the 'states' table in a
MySQL database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sys

# Define the base class
Base = declarative_base()


class State(Base):
    """State class definition inheriting from Base"""
    __tablename__ = 'states'

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name={self.name})>"


if __name__ == "__main__":
    # Establish database connection
    engine = create_engine(
        'mysql+mysqldb://'
        '{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create all tables in the database
    # (this will create 'states' if not already created)
    Base.metadata.create_all(engine)
