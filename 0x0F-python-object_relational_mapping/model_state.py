#!/usr/bin/python3
"""
This script defines a State class for use with SQLAlchemy ORM.

The class represents a state, which is mapped to the `states`
table in the database.
It inherits from SQLAlchemy's `Base` class, which is used to manage
the database connection and ORM mapping.

Usage:
    - Create a new state by creating an instance of the State class and
    adding it to the session.
    - Query states using SQLAlchemy's query API.

Attributes:
    id (int): The state ID (Primary Key).
    name (str): The name of the state.

Example:
    new_state = State(name="California")
    session.add(new_state)
    session.commit()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define Base in this file if it is not imported from elsewhere
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with City (a state can have multiple cities)
    cities = relationship(
         "City", back_populates="state", cascade="all, delete-orphan"
    )
