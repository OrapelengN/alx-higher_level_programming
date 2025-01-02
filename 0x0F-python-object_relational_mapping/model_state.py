#!/usr/bin/python3
"""
This module defines the `State` class that maps to the `states` table in the
`hbtn_0e_6_usa` database.

The `State` class is used to represent individual states,
and it uses SQLAlchemy ORM to interact with the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define Base in this file if it is not imported from elsewhere
Base = declarative_base()


class State(Base):
    """
    State class representing a state in the `states` table.

    Attributes:
        id (int): The state ID (Primary Key).
        name (str): The name of the state.

    Methods:
        __repr__: Returns a string representation of the state object,
        including its ID and name.
    """

    __tablename__ = 'states'

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with City (a state can have multiple cities)
    cities = relationship(
         "City", back_populates="state", cascade="all, delete-orphan"
    )
