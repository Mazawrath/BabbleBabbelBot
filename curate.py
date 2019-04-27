import os
import re
import translate

file_path = os.path.dirname(os.path.realpath(__file__)) + '/tweets/'
file_list = os.listdir(file_path + '/pending')

for single_tweet in reversed(file_list):
    pending_tweet = open(file_path + 'pending/' + single_tweet, 'r+')
    screen_name = pending_tweet.readline().rstrip()
    tweet_time = pending_tweet.readline().rstrip()
    tweet = ''
    for line in pending_tweet:
        tweet = tweet + line
    tweet.rstrip()
    # Remove URL's
    tweet = re.sub(r'(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+', "", tweet)
    pending_tweet.close()
    print('tweet by: @' + screen_name)
    print('tweeted at: ' + tweet_time)
    print(tweet)
    keyboard = int(input('1: Translate tweet\n'
                         '0: Delete tweet\n'
                         '-1: Quit\n'))
    if keyboard == 1:
        while True:
            translated_tweet = translate.get_translated_tweet(tweet)
            # Remove URL's
            tweet_over = 250 - 3 - len(translated_tweet)
            if tweet_over < 0:
                print('Tweet may be cut off. It\'s ' + str(tweet_over) + ' over.')
                translated_tweet = translated_tweet[:tweet_over]
            translated_tweet = '\"' + translated_tweet + '\"\n' + 'https://twitter.com/' + screen_name + '/status/' + single_tweet[
                                                                                                                      :-4]
            print(translated_tweet)
            keyboard = int(input('1: Accept tweet\n'
                                 '2: Translate again\n'
                                 '0: Delete tweet\n'))
            if keyboard == 1:
                completed_tweet = open(file_path + 'approved/' + single_tweet, 'w+')
                completed_tweet.write(translated_tweet)
                completed_tweet.close()
                break
            elif keyboard == 2:
                continue
            elif keyboard == 0:
                break
    elif keyboard == -1:
        break
    os.remove(file_path + '/pending/' + single_tweet)
print('All done')
