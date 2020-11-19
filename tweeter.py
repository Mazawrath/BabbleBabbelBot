from utility import get_api
import os
import schedule
import random
import tweepy
import time

api = get_api()


def tweet_random():
    # Choose a random account to tweet from
    file_path = os.path.dirname(os.path.realpath(__file__)) + '/tweets/approved/'
    file_list = os.listdir(file_path)
    if len(file_list) == 0:
        # There is no content to tweet, return
        return
    account_dir = file_path + file_list[random.randint(0, len(file_list) - 1)] + '/'

    file_path = account_dir
    file_list = os.listdir(file_path)
    if len(file_list) == 0:
        # Delete the folder since there are no tweets in the account
        os.rmdir(account_dir)
    tweet_file = file_path + file_list[random.randint(0, len(file_list) - 1)]
    tweet = open(tweet_file, 'r+')
    tweet_text = ''
    for line in tweet:
        tweet_text = tweet_text + line
    tweet.close()
    try:
        api.update_status(tweet_text)
    except tweepy.RateLimitError:
        time.sleep(15)
        return
    except Exception:
        os.remove(tweet_file)
    # Delete the tweet file since the contents were published
    os.remove(tweet_file)
    # Check if there are any remaining tweets in the account directory
    if len(os.listdir(account_dir)) == 0:
        # Delete the folder since there are no tweets in the account
        os.rmdir(account_dir)
    return


schedule.every().day.at("00:00").do(tweet_random)
schedule.every().day.at("02:00").do(tweet_random)
schedule.every().day.at("04:00").do(tweet_random)
schedule.every().day.at("06:00").do(tweet_random)
schedule.every().day.at("08:00").do(tweet_random)
schedule.every().day.at("10:00").do(tweet_random)
schedule.every().day.at("12:00").do(tweet_random)
schedule.every().day.at("14:00").do(tweet_random)
schedule.every().day.at("16:00").do(tweet_random)
schedule.every().day.at("18:00").do(tweet_random)
schedule.every().day.at("20:00").do(tweet_random)
schedule.every().day.at("22:00").do(tweet_random)

schedule.every().day.at("01:00").do(tweet_random)
schedule.every().day.at("03:00").do(tweet_random)
schedule.every().day.at("05:00").do(tweet_random)
schedule.every().day.at("07:00").do(tweet_random)
schedule.every().day.at("09:00").do(tweet_random)
schedule.every().day.at("11:00").do(tweet_random)
schedule.every().day.at("13:00").do(tweet_random)
schedule.every().day.at("15:00").do(tweet_random)
schedule.every().day.at("17:00").do(tweet_random)
schedule.every().day.at("19:00").do(tweet_random)
schedule.every().day.at("21:00").do(tweet_random)
schedule.every().day.at("23:00").do(tweet_random)

while True:
    schedule.run_pending()
    time.sleep(1)
