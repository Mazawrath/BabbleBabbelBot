# -*- coding: utf-8 -*-
from credentials import client_id, client_secret, user_agent, username, password, reddit_dsn
from praw import Reddit
from sentry_sdk import init, configure_scope

signature = '\n\n*** \n' \
            '^(I\'m a bot.) [^What ^is ^this ^bot?](' \
            'https://www.reddit.com/user/TranslateThisBot/comments/bpxaxw/what_is_this_bot/) [^GitHub](' \
            'https://github.com/Mazawrath/BabbleBabbelBot) ^(Created by /u/Mazawrath)'


def authenticate_reddit():
    init(reddit_dsn)
    return Reddit(client_id=client_id,
                       client_secret=client_secret,
                       user_agent=user_agent,
                       username=username,
                       password=password)


def configure_sentry(comment):
    with configure_scope() as scope:
        scope.user = {"id": comment.author.name}
        scope.set_tag("subreddit", comment.subreddit.display_name)
        scope.set_extra("comment_id", comment.id)
        scope.set_extra("parent_id", comment.parent_id[2:])
        scope.set_extra("submission_id", comment.link_id[2:])
