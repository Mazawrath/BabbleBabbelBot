import time
from reddit.utility import authenticate_reddit, signature
import translate
from credentials import username

reddit = authenticate_reddit()

# for submission in reddit.subreddit('all').stream.submissions():
#     print(submission)
start_time = time.time()

for comment in reddit.subreddit('test').stream.comments():
    if comment.created_utc < start_time:
        continue
    if 'u/' + username in comment.body:
        print(comment.body)
        parent = comment.parent()
        # This may be cheating, but I have no idea how to tell whether the object is a submission or comment other
        # than doing this ¯\_(ツ)_/¯
        if parent.__class__.__name__ == 'Submission':
            # Post
            if len(parent.selftext) > 0:
                comment.reply(translate.get_translated_tweet(parent.selftext) + signature)
        elif parent.__class__.__name__ == 'Comment':
            # Comment
            comment.reply(translate.get_translated_tweet(parent.body) + signature)
