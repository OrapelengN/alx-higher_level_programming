#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_base import Base  # Assuming this is in model_base.py

class State(Base):
    """ State class that represents the states table """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

    # This establishes the relationship with the City class.
    cities = relationship(
        "City", back_populates="state", cascade="all, delete-orphan"
    )
