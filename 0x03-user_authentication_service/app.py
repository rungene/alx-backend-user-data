#!/usr/bin/env python3
"""
app module
"""
from flask import Flask, jsonify, request, abort, redirect, url_for
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


@app.route('/sessions' methods=['DELETE', strict_slashes=False])
def logout():
    """implements logout"""
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if not user:
            return 403
        AUTH.destroy_session(session_id)
        return redirect(url_for('/'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
