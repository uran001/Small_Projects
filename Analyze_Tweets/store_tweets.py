
from time import sleep
import datetime
from tweepy import OAuthHandler
from tweepy import Stream
import json
from tweepy.streaming import StreamListener


class TweetToFileListener(StreamListener):

    def set_output_file(self, file_name):
        # to clear the content of a file, just open and close it
        open(file_name, 'w').close()

        self.output_file = file_name

    def on_data(self, data):
        print(data)
        with open(self.output_file,'a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)

def get_tweet_stream(output_file, twitter_credentials):
    """
        This function is given and returns a "stream" to listen to tweets and store them in output_file
        To understand how this function works, check it against the code of twitter_streaming in preclass

        :param output_file: the file where the returned stream will store tweets
        :param twitter_credentials: a dicionary containing the credentials to aceess twitter (you should have created your own!_
        :return: a "stream" variable to track live tweets
    """

    access_token = twitter_credentials['access_token']
    access_token_secret = twitter_credentials['access_token_secret']
    consumer_key = twitter_credentials['consumer_key']
    consumer_secret = twitter_credentials['consumer_secret']

    l = TweetToFileListener()
    l.set_output_file(output_file)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    return stream

def listen_and_store_tweets(keywords, duration, output_file, twitter_credentials):
    """
    This function tracks live tweets on a given topic for a certain duration and stores them in a file

    :param keywords: a list of keywords to track
    :param duration: the time the tracking will stay alive, e.g., 10 seconds
    :param output_file: the file where tweets will be stored
    :param twitter_credentials: a dictionary with credentials to access twitter
    """
    stream = get_tweet_stream(output_file, twitter_credentials)

    stream.filter(track=keywords, sync=True) # track all the tweets in which the keywords 'brexit' and 'Brexit' appear, the async option makes sure that tracking does not block teh execution of the program
    sleep(duration)# this keeps the tracking alive for 10 seconds
    stream.disconnect()

if __name__ == '__main__':

    access_token = "1056802651440992257-ezrj9wJS8mAs37BfXXYxwPooYrpGrt"
    access_token_secret = "iZyyk4BRNiOjvqO2dGONJ8os7Vq63OK808xvIJaUYHtN7"
    consumer_key = "hdBSuF28Xyd1XfPkPq59fuHFn"
    consumer_secret = "sNElohsvd0nSwhCDN5htK2V8QivDsWR3p12iRovUumNnI0Vfz6"

    tweet_cred = {'access_token': access_token, 'access_token_secret': access_token_secret,
                  'consumer_key': consumer_key, 'consumer_secret': consumer_secret}
    l = ["c++", "java", "python", "golang", "php"]

    listen_and_store_tweets(l, 60 * 60, "stored_tweets.json", tweet_cred)


