from utility import get_api
import os
import schedule
import random

api = get_api()


def tweet_random():
    file_path = os.path.dirname(os.path.realpath(__file__)) + '/tweets/approved/'
    file_list = os.listdir(file_path)
    if len(file_list) == 0:
        return
    tweet = open(file_path + file_list[random.randint(0, len(file_list) - 1)], 'r+')
    tweet_text = ''
    for line in tweet:
        tweet_text = tweet_text + line
    tweet.close()
    # Check that tweet isn't empty
    if tweet:
        api.update_status(tweet_text)
    os.remove(file_path + file_list[random.randint(0, len(file_list) - 1)])
    return


schedule.every().day.at("08:00").do(tweet_random)
schedule.every().day.at("10:00").do(tweet_random)
schedule.every().day.at("12:00").do(tweet_random)
schedule.every().day.at("14:00").do(tweet_random)
schedule.every().day.at("16:00").do(tweet_random)

while True:
    schedule.run_pending()

