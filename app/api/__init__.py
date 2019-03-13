from flask import Blueprint
from flask_restful import Api
from .resources import add_resources

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

add_resources(api)
