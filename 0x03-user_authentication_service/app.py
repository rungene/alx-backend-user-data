#!/usr/bin/env python3
"""
app module
"""
from flask import Flask, jsonify, request, abort
from auth import Auth
import uuid

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    returns a json payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Register user with email and password"""
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            return jsonify('message: email and password required')
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """respond to the POST /sessions route."""
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
