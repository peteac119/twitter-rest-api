from flask_restful import Resource, reqparse
from app import *
from app.api.hashtag.services import get_tweets_by_hash_tag


class HashTagSearch(Resource):
    def get(self, hash_tag):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', type=int, location='args', default=30)
        args = parser.parse_args()

        try:
            return get_tweets_by_hash_tag(hash_tag, args['limit']), 200
        except TwitterAPIException as ex:
            return {'error': ex.errors[0]}, ex.status_code
