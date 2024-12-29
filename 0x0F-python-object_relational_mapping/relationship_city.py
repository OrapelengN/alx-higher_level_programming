#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_base import Base  # Assuming this is in model_base.py

class City(Base):
    """ City class that represents the cities table """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # This establishes the relationship with the State class.
    state = relationship("State", back_populates="cities")
