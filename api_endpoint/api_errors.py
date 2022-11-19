class ApiErrors:
    """
    Class for collecting the error messages for the API.
    """
    ERR_USR_NOT_FOUND = \
        {
            "error": {
                "code": 406,
                "message": "User not found in the RSS feed list"
            }
        }

    ERR_RSS_FEED_NOT_FOUND = \
        {
            "error": {
                "code": 406,
                "message": "RSS feed not found for the specific user"
            }
        }
