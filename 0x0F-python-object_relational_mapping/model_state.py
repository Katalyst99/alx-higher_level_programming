#!/usr/bin/python3
"""Contains the class definition of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """The class State defined"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                 unique=True, nullable=False)
    name =  Column(String(128), nullable=False)
