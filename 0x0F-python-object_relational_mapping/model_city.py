#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base  # assuming model_state.py exists


class City(Base):
    __tablename__ = 'cities'

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship with State (a city belongs to one state)
    state = relationship("State", back_populates="cities")
