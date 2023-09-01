#!/usr/bin/env python3
"""
encrypt_password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    uses the bcrypt library to generate a salted
    and hashed password

    Args:
        password: str, password to hash

    Return:
        salted, hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if password is valid

    Args:
        hashed_password:(bytes) this is the hashed password
        password:(str) password to confirm entered by user

    Return:
        bool
    """
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
