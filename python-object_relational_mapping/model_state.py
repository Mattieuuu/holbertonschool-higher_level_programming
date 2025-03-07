#!/usr/bin/python3
"""
Module defining the State class and its mapping to the MySQL table 'states'.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for declarative models
Base = declarative_base()


class State(Base):
    """
    State class that maps to the 'states' table in the database.

    Attributes:
        id (int): Auto-incremented, primary key, cannot be null.
        name (str): String with maximum length of 128 characters
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)