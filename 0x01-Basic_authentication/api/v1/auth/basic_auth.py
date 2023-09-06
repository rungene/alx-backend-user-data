#!/usr/bin/env python3
"""
basic_auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) \
            -> str:
        """
        Returns the Base64 part of the Authorization header for
        a Basic Authentication"""
        if not authorization_header or not \
                isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        auth_type, encoded_credentials = authorization_header.split(' ')

        return encoded_credentials
