#!/usr/bin/env python3
"""
session_exp_auth
"""
from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """add an expiration date to a Session ID."""
    def __init__(self):
        """Initialisation instance"""
        try:
            self.session_duration = int(os.environ.get('SESSION_DURATION', 0))
        except (ValueError, TypeError):
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create session Id by calling super()"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[sesion_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns user id for session id"""
        if not session_id:
            return None
        if not self.user_id_by_session_id.get(session_id):
            return None
        session_dict = self.user_id_for_session_id.get(session_id)
        user_id = session_dict.get('user_id')
        if self.session_duration <= 0:
            return user_id
        if not self.session_dict.get('created_at'):
            return None
        created_at = session_dict.get('created_at')
        session_duration = timedelta(seconds=self.session_duration)
        expire_datetime = created_at + session_duration
        current_datetime = datetime.now()

        if expire_datetime < current_datetime:
            return None
        return user_id
