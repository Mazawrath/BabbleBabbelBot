import os
import re
import time

import tweepy

import translate
from utility import get_api, get_follower_list

api = get_api()
follower_list = get_follower_list(api)


def auto_translate_tweet(dir_path, tweet_id, tweet, screen_name):
    print("\"Translating\" tweet")
    tweet.rstrip()
    # Remove URL's
    tweet = re.sub(r'(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+', "", tweet)
    # Replace any @ symbols with & so no users get tagged
    tweet = re.sub("@", "&", tweet)
    # Reject tweet if it is too short
    if len(tweet) < 75:
        os.remove(dir_path + tweet_id + '.txt')
        return

    total_attempts = 0
    # Translate the tweet
    while True:
        total_attempts += 1
        translated_tweet = translate.get_translated_tweet(tweet)
        print(f"Translated to: {translated_tweet}")
        # Check if tweet is too long
        tweet_over = 250 - 7 - len(translated_tweet)
        # Make sure the tweet is English, the tweet isn't over in characters, and have a maximum attempts
        if translate.get_language_of_tweet(translated_tweet) == 'en' and tweet_over > 0 or total_attempts > 3:
            break
    translated_tweet = '\"' + translated_tweet + '\"\n' + 'https://twitter.com/' + screen_name + '/status/' + tweet_id

    # Only try to translate the tweet correctly 3 times, if it goes over that, just give up
    if total_attempts <= 3:
        # Check if the directory for the account exists, if it doesn't create a directory for the account
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        completed_tweet = open(dir_path + tweet_id + '.txt', 'w+')
        completed_tweet.write(translated_tweet)
        completed_tweet.close()
        # os.remove(dir_path + tweet_id + '.txt')


def record_tweet(status):
    final_dir = os.path.dirname(os.path.realpath(__file__)) + '/tweets/' + 'approved/' + status.user.id_str + '/'
    if status.truncated:
        tweet = status.extended_tweet["full_text"]
    else:
        tweet = status.text
    auto_translate_tweet(final_dir, status.id_str, tweet, status.user.screen_name)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # Check that user making status is followed and check that the status is not a retweet
        if status.user.id_str in follower_list and not re.match(r'^RT', status.text, flags=0):
            print('Tweet from @' + status.user.screen_name)
            if status.truncated:
                print(status.extended_tweet["full_text"])
            else:
                print(status.text)
            record_tweet(status)


def start_listener():
    try:
        my_stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(), stall_warnings=True)
        my_stream.filter(follow=follower_list)
    except:
        time.sleep(5)
        start_listener()


start_listener()
