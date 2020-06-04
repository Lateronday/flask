from functools import wraps
from flask_restful import Api, Resource
from flask import Blueprint, jsonify, request, g
from test import generate_token, token_expired


user_api = Blueprint('user', __name__, url_prefix='/api')
api = Api(user_api)


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        g.current_user = generate_token()
        g.b = 2
        return func(*args, **kwargs)
    return wrapper


class User(Resource):
    decorators = [decorator]

    @staticmethod
    def get():
        print(g.current_user)
        return jsonify(status=200, msg=g.current_user)

    @staticmethod
    def post():
        pass


# @user_api.before_request
# def before_request():
#     print(request.path)


class ListUser(Resource):
    decorators = [decorator]

    @staticmethod
    def get():
        print(g.current_user)
        print(g.b)
        return jsonify(status=200, msg=g.current_user)

    @staticmethod
    def post():
        pass


api.add_resource(User, '/user/')
api.add_resource(ListUser, '/list_user/')
