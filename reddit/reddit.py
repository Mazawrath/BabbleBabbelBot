import time
from reddit.utility
import translate
from credentials import username

reddit = twitter_utility.authenticate_reddit()

# for submission in reddit.subreddit('all').stream.submissions():
#     print(submission)
start_time = time.time()

for comment in reddit.subreddit('test').stream.comments():
    if comment.created_utc < start_time:
        continue
    if 'u/' + username in comment.body:
        print(comment.body)
        comment.reply(translate.get_translated_tweet(comment.parent()))
