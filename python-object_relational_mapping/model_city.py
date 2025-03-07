#!/usr/bin/python3
"""
Defines the City class and links it to the MySQL table 'cities'.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that represents the 'cities' table in MySQL.

    Attributes:
        id (int): Auto-incremented primary key.
        name (str): Name of the city (max 128 characters).
        state_id (int): Foreign key referencing the 'states' table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Optional relationship to link City with State
    state = relationship("State")