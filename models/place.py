#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    __table_args__ = {'extend_existing': True}
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    user = relationship('User', back_populates='places')
    city = relationship('City', back_populates='places')
    reviews = relationship('Review', back_populates='place', cascade='all, delete')

    @property
    def reviews(self):
        """Returns the list of Review instances with place_id equals to the current Place.id"""
        return [review for review in models.storage.all(Review).values() if review.place_id == self.id]

