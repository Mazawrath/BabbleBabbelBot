import os
import re
import translate

file_path = os.path.dirname(os.path.realpath(__file__)) + '/tweets/'
file_list = os.listdir(file_path + '/pending')

for single_tweet in file_list:
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
    keyboard = input('y: Translate tweet\n'
                     'n: Delete tweet\n'
                     'q: quit\n')
    if keyboard == 'y':
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
            keyboard = input('y: Accept tweet\n'
                             'n: Translate again\n'
                             'q: delete tweet\n')
            if keyboard == 'y':
                completed_tweet = open(file_path + 'approved/' + single_tweet, 'w+')
                completed_tweet.write(translated_tweet)
                completed_tweet.close()
                break
            elif keyboard == 'n':
                continue
            elif keyboard == 'q':
                break
    elif keyboard == 'q':
        break
    os.remove(file_path + '/pending/' + single_tweet)
print('All done')
