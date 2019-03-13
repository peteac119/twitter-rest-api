from app.twitter.client import TwitterClient


def get_tweets_by_hash_tag(hash_tag, limit):
    return TwitterClient(limit).get_tweets_by_hash_tag(hash_tag)
