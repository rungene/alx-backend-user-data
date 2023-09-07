#!/usr/bin/env python3
"""
session_auth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class that inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        Args:
            user_id(str): user identifier
        Return:
            str:generated user_id string
        """
        if not user_id or not isinstance(user_id, str):
            return None
        # Genarate session id as string
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
