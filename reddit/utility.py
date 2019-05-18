from credentials import client_id, client_secret, user_agent, username, password
import praw

signature = '\n\n*** \n' \
            '^(I\'m a bot.) [^What ^is ^this ^bot?](' \
            'https://www.reddit.com/user/TranslateThisBot/comments/bpxaxw/what_is_this_bot/) [^GitHub](' \
            'https://github.com/Mazawrath/BabbleBabbelBot) ^(Created by Mazawrath)'


def authenticate_reddit():
    return praw.Reddit(client_id=client_id,
                       client_secret=client_secret,
                       user_agent=user_agent,
                       username=username,
                       password=password)
