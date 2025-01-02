#!/usr/bin/python3
"""
Defines the City class with SQLAlchemy ORM relationship.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from relationship_state import Base  # Assuming this is in model_base.py

Base = declarative_base()


class City(Base):
    """
    City class representing the 'cities' table.

    Attributes:
        id (int): Primary key for the city, auto-generated.
        name (str): Name of the city (max 128 chars), cannot be null.
        state_id (int): Foreign key referencing State.id, cannot be null.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # This establishes the relationship with the State class.
    state = relationship("State", back_populates="cities")
