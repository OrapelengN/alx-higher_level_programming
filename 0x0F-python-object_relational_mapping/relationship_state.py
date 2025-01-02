#!/usr/bin/python3
"""
Defines the State class with SQLAlchemy ORM relationship.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from relationship_base import Base  # Assuming this is in model_base.py

Base = declarative_base()


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
