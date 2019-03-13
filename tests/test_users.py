import json
import httpretty

from tests import BaseTestCase


class UserTestCase(BaseTestCase):
    def setUp(self):
        super(UserTestCase, self).setUp()

    @httpretty.activate
    def test_users_with_invalid_token_error(self):
        httpretty.register_uri(
            httpretty.POST,
            "http://test.com/oauth2/token",
            body=json.dumps(self.invalid_token_response),
            status=403,
            content_type='application/json'
        )
        response = self.client.get('/users/sample_user')

        self.assertEqual(403, response.status_code)

        actual_json = response.json
        expected_json = {
            "error": [
                {
                    "code": 99,
                    "label": "authenticity_token_error",
                    "message": "Unable to verify your credentials"
                }
            ]
        }

        self.assertDictEqual(actual_json, expected_json)

    @httpretty.activate
    def test_users_with_non_authorized_response(self):
        httpretty.register_uri(
            httpretty.POST,
            "http://test.com/oauth2/token",
            body=json.dumps(self.unauthorized_response),
            status=401,
            content_type='application/json'
        )
        response = self.client.get('/users/sample_user')

        self.assertEqual(401, response.status_code)

        actual_json = response.json
        expected_json = {
            "error": [
                {
                    "message": "Invalid or expired token",
                    "code": 89
                }
            ]
        }

        self.assertDictEqual(actual_json, expected_json)

    @httpretty.activate
    def test_users_with_normal_sweets(self):
        httpretty.register_uri(
            httpretty.POST,
            "http://test.com/oauth2/token",
            body=json.dumps(self.mock_token),
            status=200,
            content_type='application/json'
        )

        httpretty.register_uri(
            httpretty.GET,
            "http://test.com/1.1/statuses/user_timeline.json?screen_name=sample_user",
            body=json.dumps(self.mock_tweet_response),
            status=200,
            content_type='application/json'
        )

        response = self.client.get('/users/sample_user')

        self.assertEqual(200, response.status_code)

        actual_json = response.json
        self.assertDictEqual(self.mock_tweet_response, actual_json)
