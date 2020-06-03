from flask_restful import Api, Resource
from flask import Blueprint, jsonify


user_api = Blueprint('user', __name__, url_prefix='/api')
api = Api(user_api)


class User(Resource):

    @staticmethod
    def get():
        return jsonify(status=200, msg='user_ok')

    @staticmethod
    def post():
        pass


class ListUser(Resource):

    @staticmethod
    def get():
        return jsonify(status=200, msg='list_user_ok')

    @staticmethod
    def post():
        pass


api.add_resource(User, '/user/')
api.add_resource(ListUser, '/list_user/')
