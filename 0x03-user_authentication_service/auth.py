#!/usr/bin/env python3
"""
auth module
"""
import bcrypt


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
