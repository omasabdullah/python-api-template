from flask import request, jsonify

from src.ErrorHandler import Error, ErrorType
from src.database.database import users


def show():
    return jsonify(users), 200

def index(id):
    user = get_user(id)

    if user:
        return jsonify(user), 200
    else:
        raise Error(ErrorType.not_found, 'User not found')

def create():
    new_user = request.json

    if new_user:
        users.append(new_user)
        return jsonify(new_user), 201
    else:
        raise Error(ErrorType.generic, 'Error creating user')

def update(id):
    json = request.json
    user = get_user(id)

    if user:
        user.update(json)
        return jsonify(user), 200
    else:
        raise Error(ErrorType.generic, 'Error updating user')


def get_user(id):
    return next(
        filter(
            lambda x: x.get('id') == id,
            users
        ),
    None)
