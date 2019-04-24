from utility import get_api
import tweepy
import re

api = get_api()


def get_follower_list():
    output = []
    for friend in tweepy.Cursor(api.friends).items():
        output.append(friend.id_str)
    return output


follower_list = get_follower_list()


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.user.id_str in follower_list:
            # Retweet
            if re.match(r'^RT', status.text, flags=0):
                print('Retweet from ' + status.user.screen_name)
            else:
                print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, stall_warnings=True, tweet_mode='extended')

myStream.filter(follow=follower_list)
