import json
import httpretty

from tests import BaseTestCase


class HashTagTestCase(BaseTestCase):
    def setUp(self):
        super(HashTagTestCase, self).setUp()

    @httpretty.activate
    def test_invalid_token_error(self):
        httpretty.register_uri(
            httpretty.POST,
            "http://test.com/oauth2/token",
            body=json.dumps(self.invalid_token_response),
            status=403,
            content_type='application/json'
        )
        # response = self.client.post('/api/users', data=json.dumps({
        #     'email': 'myass@gmail.com',
        #     'username': 'myass',
        #     'password': 'fuckyall'
        # }), content_type='application/json')