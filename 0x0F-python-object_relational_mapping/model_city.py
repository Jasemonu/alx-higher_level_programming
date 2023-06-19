#!/usr/bin/python3
"""
This script defines a City class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """A class that inherit from Base = declarative_base()"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
