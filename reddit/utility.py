from credentials import client_id, client_secret, user_agent, username, password
import praw

def authenticate_reddit():
    return praw.Reddit(client_id=client_id,
                       client_secret=client_secret,
                       user_agent=user_agent,
                       username=username,
                       password=password)
