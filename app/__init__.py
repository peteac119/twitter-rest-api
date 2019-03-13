from flask import Flask
from app.exceptions import *


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('FLASK_CONFIG')
    from .api import api_bp as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
