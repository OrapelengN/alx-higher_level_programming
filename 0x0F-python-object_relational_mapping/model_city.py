#!/usr/bin/python3
"""
Defines a City class that maps to the cities table in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base  # Import Base from model_state


class City(Base):
    """
    City class that represents a record in the cities table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
