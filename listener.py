from utility import get_api
import tweepy

api = get_api()


def get_follower_list():
    output = []
    for friend in tweepy.Cursor(api.friends).items():
        output.append(str(friend.id))
    return output


follower_list = get_follower_list()


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(follow=follower_list)
