#!/usr/bin/env python3
"""
user
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):
    """User class to map users tabel
    Defines tabels details which we will be mapping
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
