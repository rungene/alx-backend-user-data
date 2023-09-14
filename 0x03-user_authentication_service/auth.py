#!/usr/bin/env python3
"""
auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Password hashed with bcrypt.hashpw
    Args:
        password(str): password in string format
    Returns:
        bytes is a salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid() -> str:
    """
    Generates uuid and returns string representation of a new UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers user, save to db
        Args:
            email(str): user email
            password(str):user password

        Returns:
            user if he dose not exist
            or raise ValueError if user exists
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if login is valid
        Args:
            email(str): user email
            password(str): user password
        Return
            Return true is login is valid or
            false otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return True
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """find the user corresponding to the email, generate a new
        UUID and store it in the database as the user’s session_id
        Args:
            email(str): user email
        Return:
            session_id
        """
        try:
            user = self._db.find_user_by(email=email)
            new_uuid = _generate_uuid()
            
