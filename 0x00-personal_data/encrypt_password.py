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
