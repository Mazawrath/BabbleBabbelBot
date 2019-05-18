import time
from reddit.utility import *
from reddit.anti_abuse import *
import translate
import praw
import _thread
from credentials import username

reddit = authenticate_reddit()
start_time = time.time()


def post_message(comment):
    parent = comment.parent()
    if is_already_done(parent):
        print('Not happening.')
        return
    # This may be cheating, but I have no idea how to tell whether the object is a submission or comment other
    # than doing this ¯\_(ツ)_/¯
    if parent.__class__.__name__ == 'Submission':
        # Post
        if len(parent.selftext) > 0:
            message = parent.selftext
    elif parent.__class__.__name__ == 'Comment':
        # Comment
        if parent.author.name == username:
            print('replying to myself')
            message = parent.body[:-207]
        else:
            message = parent.body
    else:
        raise AttributeError
    print(message)
    message = translate.get_translated_tweet(message) + signature
    tries = 2
    for i in range(tries):
        # noinspection PyUnresolvedReferences
        try:
            comment.reply(message)
        except praw.exceptions.APIException as e:
            if i < tries - 1:  # i is zero indexed
                print(e)
                print('Waiting 900 seconds')
                time.sleep(900)
                continue
            else:
                raise
        break


def comment_listener():
    for comment in reddit.subreddit('test').stream.comments():
        if comment.created_utc < start_time:
            continue
        if 'u/' + username.lower() in comment.body.lower():
            configure_sentry(comment)
            _thread.start_new_thread(post_message, (comment,))


comment_listener()
