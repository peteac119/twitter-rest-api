from envparse import env

HTTP_RETRY_STATUS_CODE = env.list('HTTP_RETRY_STATUS_CODE', default=[429, 502, 503, 504], subcast=int)

# Twitter API Configuration
TWITTER_CONSUMER_K = env.str('TWITTER_CONSUMER_K', default='')
TWITTER_CONSUMER_S = env.str('TWITTER_CONSUMER_S', default='')
TWITTER_ROOT_URL = env.str('TWITTER_ROOT_URL', default='')
