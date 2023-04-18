#!/usr/bin/python3
"""
contains the class definition of a City
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()

class State(Base):
    """ the City class will be mapped to the mysql table cities
        __tablename__: 'cities'
        id: id of object instance
        name: string of max 128 chars not null
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
