#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            # create a Session
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds user to the database
        Args:
            email: The email address of the user
            hashed_password: The password of the user
        Return:
            new user object"""
        user = User(email=email, hashed_password=hashed_password)

        # Add he user to the db session
        self._session.add(user)

        # commit to the session, persist the user to the db
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Gets the first user from the users table

        Args:
            kwargs: Arbitrary key word args

        Return:
            First row found inusers table
            or Not found if no results found
            or InvalidRequestError are raised
            when wrong query args are passed
        """
        query = self._session.query(User)
        try:
            first_user = query.filter_by(**kwargs).first()
            if not first_user:
                raise NoResultFound
            return first_user
        except TypeError:
            raise InvalidRequestError
