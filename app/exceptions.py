class TwitterAPIException(Exception):
    def __init__(self, errors, status_code, *args, **kwargs):
        super(TwitterAPIException, self).__init__(*args, **kwargs)
        self.errors = errors,
        self.status_code = status_code


class TwitterUnauthorizedException(TwitterAPIException):
    def __init__(self, errors, status_code, *args, **kwargs):
        super(TwitterUnauthorizedException, self).__init__(errors, status_code, *args, **kwargs)


class TwitterInvalidTokenException(TwitterAPIException):
    def __init__(self, errors, status_code, *args, **kwargs):
        super(TwitterInvalidTokenException, self).__init__(errors, status_code, *args, **kwargs)
