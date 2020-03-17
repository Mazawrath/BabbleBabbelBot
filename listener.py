from utility import get_api, get_follower_list
import os
import tweepy
import re
import time
import translate

api = get_api()
follower_list = get_follower_list(api)


def record_tweet(status):
    final_dir = os.path.dirname(os.path.realpath(__file__)) + '/tweets/pending/'
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    r = open(final_dir + status.id_str + '.txt', 'w+')
    r.write(status.user.screen_name + '\n')
    r.write(str(status.user.created_at) + '\n')
    if status.truncated:
        r.write(status.extended_tweet["full_text"])
    else:
        r.write(status.text)
    r.close()
    pending_tweet = open(final_dir + status.id_str + '.txt', 'r+')
    # Store info about the tweet and grab the text
    screen_name = pending_tweet.readline().rstrip()
    tweet_time = pending_tweet.readline().rstrip()
    tweet = ''
    for line in pending_tweet:
        tweet = tweet + line
    tweet.rstrip()
    # Remove URL's
    tweet = re.sub(r'(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+', "", tweet)
    pending_tweet.close()
    total_attempts = 0
    # Translate the tweet
    while True:
        total_attempts += 1
        translated_tweet = translate.get_translated_tweet(tweet)
        print(f"Translated to: {translated_tweet}")
        language = translate.get_language_of_tweet(translated_tweet)
        # Check if tweet is too long
        tweet_over = 250 - 7 - len(translated_tweet)
        # Make sure the tweet is English, the tweet isn't over in characters, and have a maximum attempts
        if language == 'en' and 0 < tweet_over < 100 or total_attempts > 5:
            break
    translated_tweet = '\"' + translated_tweet + '\"\n' + 'https://twitter.com/' + screen_name + '/status/' + status.id_str
    if total_attempts <= 5:
        # Tweet has been translated, write it to approved
        completed_tweet = open(os.path.dirname(os.path.realpath(__file__)) + '/tweets/' + 'approved/' + status.id_str + '.txt', 'w+')
        completed_tweet.write(translated_tweet)
        completed_tweet.close()
    # os.remove(final_dir + status.id_str + '.txt')


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


def start_listener():
    try:
        my_stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(), stall_warnings=True)
        my_stream.filter(follow=follower_list)
    except:
        time.sleep(5)
        start_listener()


start_listener()
