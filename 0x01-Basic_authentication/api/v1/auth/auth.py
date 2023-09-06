#!/usr/bin/env python3
"""
auth
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """
    Manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """if path is not in excluded paths returns true,
        hence authentication is required
        """
        if not path or not excluded_paths:
            return True
        path = path + '/' if not path.endswith('/') else path

        for path_excludes in excluded_paths:
            match = re.match(path_excludes + '([*]?|(/)?)', path)
            if match:
                return False
        return True

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
