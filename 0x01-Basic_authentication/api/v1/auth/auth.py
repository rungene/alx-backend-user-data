#!/usr/bin/env python3
"""
auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """if path is not in excluded paths returns true,
        hence authentication is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Return None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return None
        """
        return None
