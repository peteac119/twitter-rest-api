from app.twitter.client import TwitterClient


def get_tweets_by_user(user, limit):
    return TwitterClient(limit).get_tweets_by_user(user)
