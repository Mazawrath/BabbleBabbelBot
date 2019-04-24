from credentials import dsn, consumer_key, consumer_secret, access_token, access_token_secret
import tweepy
import sentry_sdk


def get_api():
    sentry_sdk.init(dsn)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_follower_list(api):
    output = []
    for friend in tweepy.Cursor(api.friends).items():
        output.append(friend.id_str)
    return output
