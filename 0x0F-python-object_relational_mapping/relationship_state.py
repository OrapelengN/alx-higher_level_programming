#!/usr/bin/python3
"""
This module defines the State class, which represents the 'states' table in the
database.
It defines the State class with SQLAlchemy ORM mappings to the states table.
Additionally, it establishes a relationship to the City class, where deleting a
State will also delete related City objects.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_base import Base


class State(Base):
    """
    State class representing the 'states' table.

    Attributes:
        id (int): Primary key for the state, auto-generated.
        name (str): Name of the state (max 128 chars), cannot be null.
        cities (relationship): One-to-many relationship with City table.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

    # This establishes the relationship with the City class.
    cities = relationship(
        "City", back_populates="state", cascade="all, delete-orphan"
    )
