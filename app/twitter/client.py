import base64

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

from flask import current_app
from requests import Session, HTTPError
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from app.exceptions import *
from urllib.parse import quote_plus

# Exception type mapped to HTTP status code
EXCEPTION_MAPPING = {
    401: TwitterInvalidTokenException,
    403: TwitterUnauthorizedException
}


class TwitterClient:
    def __init__(self, limit):
        self.limit = limit
        self.root_url = current_app.config['TWITTER_ROOT_URL']

    def _call_api_with_retry(self,
                             method,
                             url,
                             headers=None,
                             params=None,
                             json=None,
                             backoff_factor=0.5,
                             retries=3,
                             **kwargs):
        try:
            # HTTP Status that triggers retry mechanism.
            status_force_list = current_app.config.get("HTTP_RETRY_STATUS_CODE")
            # 'with' statement will ensure that the request session is closed.
            with Session() as session:
                retry = Retry(
                    total=retries,
                    read=retries,
                    connect=retries,
                    backoff_factor=backoff_factor,
                    status_forcelist=status_force_list,
                    raise_on_status=False,
                )
                adapter = HTTPAdapter(max_retries=retry)
                session.mount('http://', adapter)
                session.mount('https://', adapter)
                response = session.request(method=method,
                                           url=url,
                                           headers=headers,
                                           params=params,
                                           json=json,
                                           **kwargs)
        except HTTPError as ex:
            current_app.logger.exception("Unexpected HTTPError.")
            raise ex
        else:
            status_code = response.status_code
            try:
                json_body = response.json()
            except JSONDecodeError:
                response.raise_for_status()
            else:
                if status_code not in [200, 201]:
                    exception = EXCEPTION_MAPPING.get(status_code, TwitterAPIException)

                    if 'errors' in json_body:
                        raise exception(errors=json_body['errors'], status_code=status_code)
                    else:
                        raise exception(errors=json_body, status_code=status_code)

                return json_body

    def _headers(self):
        """
        OAuth authentication is required for Twitter API.
        I follow OAuth of Application-only token.

        How to generate bearer token:
        'https://developer.twitter.com/en/docs/basics/authentication/overview/application-only'

        Response sample:
        'https://developer.twitter.com/en/docs/basics/authentication/api-reference/token'

        :return: Bearer token
        """

        consumer_key = quote_plus(current_app.config['TWITTER_CONSUMER_K'])
        consumer_secret = quote_plus(current_app.config['TWITTER_CONSUMER_S'])
        bearer_token = base64.b64encode('{}:{}'.format(consumer_key, consumer_secret).encode('utf8'))

        headers = {
            "Authorization": 'Basic {0}'.format(bearer_token.decode('utf8')),
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }

        data = {
            "grant_type": "client_credentials"
        }

        url = self.root_url + '/oauth2/token'

        token = self._call_api_with_retry(method='post',
                                          url=url,
                                          headers=headers,
                                          data=data)

        return {
            "Authorization": "Bearer %s" % token['access_token']
        }

    def get_tweets_by_hash_tag(self, hash_tag):
        """
        Retrieve all tweets based on provided hashtag.
        The number of results is based on provided limit. Default is 30.
        Standard Search API is used.

        API DOC:
        'https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets'


        :param hash_tag: String
        :return: JSON or dictionary -> Response from API
        """
        headers = self._headers()
        url = self.root_url + '/1.1/search/tweets.json'
        params = {
            'q': "%23" + hash_tag,
            'count': self.limit,
            'include_entities': True
        }

        return self._call_api_with_retry('get', url=url, headers=headers, params=params)

    def get_tweets_by_user(self, user):
        """
        Retrieve all tweets based on provided user.
        The number of results is based on provided limit. Default is 30.

        API DOC:
        'https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html'

        :param user: String
        :return: JSON or dictionary -> Response from API
        """
        headers = self._headers()
        url = self.root_url + '/1.1/statuses/user_timeline.json'
        params = {
            'screen_name': user,
            'count': self.limit
        }

        return self._call_api_with_retry('get', url=url, headers=headers, params=params)
