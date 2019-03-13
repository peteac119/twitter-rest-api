from app.api.hashtag import HashTagSearch
from app.api.users import UserSearch


def add_resources(api):

    # Hashtag
    api.add_resource(HashTagSearch, '/hashtags/<string:hash_tag>')

    # User
    api.add_resource(UserSearch, '/users/<string:user>')
