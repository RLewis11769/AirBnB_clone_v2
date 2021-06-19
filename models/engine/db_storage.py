#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base


classes = {
          'User': User, 'Place': Place,
          'State': State, 'City': City, 'Amenity': Amenity,
          'Review': Review
          }


class DBStorage:
    """A method of storage???"""
    __engine = None
    __session = None
    user = getenv('HBNB_MYSQL_USER')
    password = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST')
    database = getenv('HBNB_MYSQL_DB')

    def __init__(self):
        """Instantiation of self"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                          self.user,
                                          self.password,
                                          self.host,
                                          self.database),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query current db sesh: all objects of class.name"""
        """if cls=None, query all: User, State, City, etc."""
        dict = {}
        if not cls:
            for womp in classes.values():
                for y in self.__session.query(womp):
                    dict[y.__class__.__name__ + '.' + y.id] = y
            return dict
        else:
            for instance in self.__session.query(cls):
                dict[instance.__class__.__name__ +
                     '.' + instance.id] = instance
            return dict

    def new(self, obj):
        """add object to current db sesh: self.__session"""
        from models import FileStorage
        self.__session.add(obj)

    def save(self):
        """commit all chgs of cur db sesh: self.__session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from curr db sesh obj: !=None"""
        if obj:
            del obj

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        engine = sessionmaker(bind=self.__engine,
                              expire_on_commit=False)
        Session = scoped_session(engine)
        self.__session = Session()

    def close(self):
        self.__session.close()
