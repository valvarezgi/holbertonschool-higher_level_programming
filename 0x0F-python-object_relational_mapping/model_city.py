#!/usr/bin/python3
'''Define the city and Base classes
'''
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship


class City(Base):
    '''REpresents a city'''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement='auto', nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State')
