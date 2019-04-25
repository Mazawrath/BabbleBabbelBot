from utility import get_api, get_follower_list
import os
import tweepy
import re

api = get_api()
follower_list = get_follower_list(api)


def record_tweet(status):
    final_dir = os.path.dirname(os.path.realpath(__file__)) + '/Tweets/Pending/'
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    f = open(final_dir + status.id_str + '.txt', 'w+')
    f.write(status.user.screen_name + '\n')
    f.write(str(status.user.created_at) + '\n')
    if status.truncated:
        f.write(status.extended_tweet["full_text"])
    else:
        f.write(status.text)
    f.close()


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # Check that user making status is followed
        if status.user.id_str in follower_list:
            # Check that the status is not a retweet
            if not re.match(r'^RT', status.text, flags=0):
                print('Tweet from @' + status.user.screen_name)
                if status.truncated:
                    print(status.extended_tweet["full_text"])
                else:
                    print(status.text)
                record_tweet(status)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, stall_warnings=True)

myStream.filter(follow=follower_list)
