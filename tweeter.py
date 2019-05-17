from utility import authenticate_twitter
import os
import schedule
import random
import tweepy
import time

api = authenticate_twitter()


def tweet_random():
    file_path = os.path.dirname(os.path.realpath(__file__)) + '/tweets/approved/'
    file_list = os.listdir(file_path)
    if len(file_list) == 0:
        return
    file = file_path + file_list[random.randint(0, len(file_list) - 1)]
    tweet = open(file, 'r+')
    tweet_text = ''
    for line in tweet:
        tweet_text = tweet_text + line
    tweet.close()
    try:
        api.update_status(tweet_text)
    except tweepy.RateLimitError:
        time.sleep(15)
        tweet_random()
    except Exception:
        os.remove(file)
        tweet_random()
    os.remove(file)
    return


schedule.every().day.at("08:00").do(tweet_random)
schedule.every().day.at("10:00").do(tweet_random)
schedule.every().day.at("12:00").do(tweet_random)
schedule.every().day.at("14:00").do(tweet_random)
schedule.every().day.at("16:00").do(tweet_random)
schedule.every().day.at("18:00").do(tweet_random)

while True:
    schedule.run_pending()
    time.sleep(1)
