#!/usr/bin/python3
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
