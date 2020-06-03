from flask import Flask
from api.user import user_api
from api.admin import admin_api
from settings import config


app = Flask('Spider')


def init():
    app.config.from_object(config['development'])


def create_app():
    init()
    print(app.config['TEST'])
    app.register_blueprint(user_api)
    app.register_blueprint(admin_api)
    return app
