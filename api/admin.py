from flask import Blueprint, jsonify
from flask_restful import Api, Resource


admin_api = Blueprint('admin', __name__, url_prefix='/api')
api = Api(admin_api)


class Admin(Resource):

    @staticmethod
    def get():
        return jsonify(status=200, msg='admin_ok')

    @staticmethod
    def post():
        pass


class ListAdmin(Resource):

    @staticmethod
    def get():
        return jsonify(status=200, msg='list_admin_ok')

    @staticmethod
    def post():
        pass


api.add_resource(Admin, '/admin/')
api.add_resource(ListAdmin, '/list_admin/')
