#!/usr/bin/python3
"""
This module defines a new engine for the storage system of the HBNB project.
The DBStorage engine interacts with a MySQL database to manage data persistence
using SQLAlchemy ORM.

Classes:
    DBStorage: Manages long-term storage of all class instances in a MySQL database.

The DBStorage class:
    - Establishes a connection to the MySQL database using SQLAlchemy.
    - Provides methods for interacting with the database such as all(), new(), save(), delete(), and reload().
    - Handles storage and retrieval of data models including User, State, City, Place, Review, and Amenity.
    - Supports querying and filtering of stored data based on class type.
    - Ensures data integrity and relationships through SQLAlchemy's ORM capabilities.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of hbnb models in a SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStorage"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}', pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(User).all()
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        return {obj.__class__.__name__ + '.' + obj.id: obj for obj in objs}

    def new(self, obj):
        """Adds a new object to the database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
