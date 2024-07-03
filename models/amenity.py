#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import Table, ForeignKey



place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
    extend_existing=True
    )

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    __table_args__ = {'extend_existing': True}

    name = Column(String(128), nullable=False)
    place_amenities= relationship('Place', secondary=place_amenity, backref='amenities')
