from envparse import env

HTTP_RETRY_STATUS_CODE = env.list('HTTP_RETRY_STATUS_CODE', default=[429, 502, 503, 504], subcast=int)

# Twitter API Configuration
TWITTER_CONSUMER_KEY = env.str('TWITTER_CONSUMER_KEY', default='')
TWITTER_CONSUMER_SECRET = env.str('TWITTER_CONSUMER_SECRET', default='')
TWITTER_ROOT_URL = env.str('TWITTER_ROOT_URL', default='')
