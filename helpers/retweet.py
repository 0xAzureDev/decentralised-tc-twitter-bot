import tweepy


def submit_retweet(tweet_id: int, twitter: object) -> None:
    """
    Submit Retweet
    --------------

    Submits the proposals tweet for retweeting.

    :param tweet_id: The id for the tweet to be retweeted.
    """

    # Credentials
    api_key = twitter["api_key"]
    api_secret = twitter["api_secret"]
    bearer_token = twitter["bearer_token"]
    access_token = twitter["access_token"]
    access_token_secret = twitter["access_token_secret"]

    # Connecting to the Twitter API using the Credentials
    client = tweepy.Client(bearer_token, api_key, api_secret,
                           access_token, access_token_secret)

    # Retweet
    client.retweet(tweet_id)
