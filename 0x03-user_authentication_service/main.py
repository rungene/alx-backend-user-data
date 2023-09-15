#!/usr/bin/env python3
"""
Main file
"""
import unittest
import requests
from app import app

BASE_URL = 'http://localhost:5000'


class TestEndPoints(unittest.TestCase):
    """End to end integrations Test"""
    def test_register_user(self):
        response = request.post(f'{BASE_URL}/users',
                                data={'email': 'rungene@me.com',
                                      'password': 'pass'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('user created', response.text)


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
