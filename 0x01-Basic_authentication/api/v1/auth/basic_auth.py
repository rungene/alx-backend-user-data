#!/usr/bin/env python3
"""
basic_auth
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        Returns the decoded value of a Base64 string
        base64_authorization_header"""
        if not base64_authorization_header or not \
                isinstance(base64_authorization_header, str):
            return None

        try:
            return base64.b64decode(base64_authorization_header) \
                .decode('utf-8')

        except base64.binascii.Error:
            return None

    def extract_user_credentials(
                                self,
                                decoded_base64_authorization_header:
                                str) -> (str, str):
        """
        returns the user email and password
        from the Base64 decoded value."""
        if not decoded_base64_authorization_header or not \
                isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None
        username, password = decoded_base64_authorization_header.split(':', 1)
        return username, password
