import os
import translate

file_path = os.path.dirname(os.path.realpath(__file__)) + '/Tweets/'
file_list = os.listdir(file_path + '/Pending')

for single_tweet in file_list:
    pending_tweet = open(file_path + 'Pending/' + single_tweet, 'r+')
    screen_name = pending_tweet.readline()
    tweet_time = pending_tweet.readline()
    tweet = ''
    for line in pending_tweet:
        tweet = tweet + line
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
            print(translated_tweet)
            keyboard = input('y: Accept tweet\n'
                             'n: Translate again\n'
                             'q: delete tweet\n')
            if keyboard == 'y':
                completed_tweet = open(file_path + 'Approved/' + single_tweet, 'w+')
                completed_tweet.write(translated_tweet)
                completed_tweet.close()
                break
            elif keyboard == 'n':
                continue
            elif keyboard == 'q':
                break
    elif keyboard == 'q':
        break
    os.remove(file_path + '/Pending/' + single_tweet)
print('All done')
