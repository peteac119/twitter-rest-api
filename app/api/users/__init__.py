from flask_restful import Resource, reqparse
from app import TwitterAPIException
from app.api.users.services import get_tweets_by_user


class UserSearch(Resource):
    def get(self, user):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', type=int, location='args')
        args = parser.parse_args()

        try:
            return get_tweets_by_user(user, args['limit']), 200
        except TwitterAPIException as ex:
            return {'error': ex.errors[0]}, ex.status_code
