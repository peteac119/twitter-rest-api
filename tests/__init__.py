import os
import httpretty

from unittest import TestCase
from app import create_app


class BaseTestCase(TestCase):
    def setUp(self):
        # Set test environment
        os.environ['FLASK_CONFIG'] = '../tests/test_config.py'
        self.app = create_app()
        self.client = self.app.test_client()

        self.invalid_token_response = {
            "errors": [
                {
                    "code": 99,
                    "label": "authenticity_token_error",
                    "message": "Unable to verify your credentials"
                }
            ]
        }

        self.unauthorized_response = {
            "errors": [
                {
                    "message": "Invalid or expired token",
                    "code": 89
                }
            ]
        }

        self.mock_token = {
            "token_type": "test_token_type",
            "access_token": "test_access_token"
        }

        self.mock_tweet_response = {
            "id": 1238475588942304,
            "id_str": "1238475588942304",
            "text": "test_text_here",
            "truncated": False,
            "entities": {
                "hashtags": [
                    {
                        "text": "hashtag1",
                        "indices": [
                            65,
                            79
                        ],
                    },
                    {
                        "text": "hashtag2",
                        "indices": [
                            80,
                            94
                        ],
                    }
                ],
                "symbols": [],
                "user_mentions": [
                    {
                        "screen_name": "test_name",
                        "name": "test_name",
                        "id":
                            123412423905823
                        ,
                        "id_str": "123412423905823",
                        "indices": [
                            3,
                            14
                        ],
                    }
                ],
                "urls": [],
            }
        }
