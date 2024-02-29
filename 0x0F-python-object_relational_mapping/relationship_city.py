#!/usr/bin/python3
"""creates City class using SQLALchemy"""


from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    creates a city table
    __tablename__: cities
    Attributes:
    id, name, state_id
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
