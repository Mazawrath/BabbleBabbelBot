from utility import get_api, get_follower_list
import tweepy
import re

api = get_api()
follower_list = get_follower_list(api)


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
