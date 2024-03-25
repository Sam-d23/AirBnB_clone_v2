#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Class defining the DBStorage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """The DBStorage engine is initialized"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(user, password, host, database), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """The current database session is querried"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        results = {}

        if cls:
            objects = self.__session.query(classes[cls]).all
        else:
            objects = []
            for key, value in classes.items():
                objects.extend(self.__session.query(value).all())

        for obj in objects:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            results[key] = obj

        return results

    def new(self, obj):
        """A new object is added to the current database session"""
        self.__session.add(obj)

    def save(self):
        """All changes of the current database session are saved"""
        self.__session.commit()

    def delete(self, obj=None):
        """An object from the current database session is deleted"""
        if not obj:
            self.__session.delete(obj)

    def reload(self):
        """All objects of the current database session are reloaded"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
