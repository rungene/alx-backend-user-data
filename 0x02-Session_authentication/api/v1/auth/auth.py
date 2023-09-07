#!/usr/bin/env python3
"""
auth
"""
from flask import request
from typing import List, TypeVar
import re
import os


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
        Validate all requests to secure the API
        """
        if not request:
            return None
        if not request or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return None
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request
        """
        if not request:
            return None
        cookie_name = os.environ.get('SESSION_NAME')
        if not cookie_name:
            return None
        _my_session_id = request.cookies.get(cookie_name)

        return _my_session_id
