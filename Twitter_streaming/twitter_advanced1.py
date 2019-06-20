"""
 Some sort of simple information retrieval from a stream of tweets stored in a file using tweeter API
 More info about the Twitter API at: https://dev.twitter.com/overview/api
"""

import json
import matplotlib.pyplot as plt
from twitter_basics import *

def most_followed_user_tweet(output_file):
    """
    This function should print on console and return the tweet in output_file tweeted by the user with most followers,
     the name of the user, and the user's number of followers
     (if the most followed user has tweeted more than once, the oldest tweet should be selected)
    :param output_file:
    :return:
    """
    file = open(output_file, "r")

    for line in file.readlines():
        t = json.loads(line)
        if "user" in t.keys():
            print(t['user']['name'],t['user']['followers_count'])
           # time.sleep(0.1)
           # if (t[x] is not None):
            #    for y in t[x]:
            #        print(y)

        #time.sleep(10)



# extract tweet that hs been retweeted the most

def most_status_changes_user_tweet(output_file):
    """
    This function should print on console and return the tweet in output_file tweeted by the user that has tweeted
    the most since joining twitter.
     (if the most f the name of the user, and the user's number of followers
ollowed user has tweeted more than once, the oldest tweet should be selected)

    :param output_file:
    :return:
    """
    file = open(output_file, "r")

    for line in file.readlines():
        t = json.loads(line)
        if "user" in t.keys():
            print(t['user']['name'], t['user']['statuses_count'])
        time.sleep(0.1)
        # if (t[x] is not None):
        #    for y in t[x]:
        #        print(y)

        # time.sleep(10)


# evaluate the lexical complexity of your twitter "corpus" using the metrics defined before
# tag and analyse tweets

def find_tweets_by_keyword(output_file, keyword_list):
    """
   This functions returns the tweets in outout_file that match one or more of the keywords in keyword_list
   It's up to you to define an appropriate data structure returned by this function

    :param output_file: a file containing tracked tweet(s)
    :param keyword_list: a list of keywords to search tweets
    """
    file = open(output_file, "r")

    for line in file.readlines():
        t = json.loads(line)
        for x in t:
            print(x, t[x])


def plot_tweets_by_attribute(output_file, attribute):
    """
    This functions plots a histogram of number of tweets per "attribute" in output_file.
    For instance, if attribute = "language", then it plots a histogram showing the number of tweets per language found;
    if attribute "location" it plots the number of tweets per different user location

    :param output_file:
    :param attribute: a categorical attribute meaningful for a tweet
    :return:
    """
    if attribute == 'language':
        lan = {}
        file = open(output_file, "r")
        for line in file.readlines():
            t = json.loads(line)
            if t['lang'] not in lan.keys():
                lan[t['lang']] = 0
            lan[t['lang']] += 1
        p = []
        for x in lan:
            p.append(lan[x])
        plt.bar(lan.keys(),p)
        plt.title("Language")
        plt.show()


if __name__ == '__main__':

    """ UNCOMMENT AS REQUIRED"""

    most_followed_user_tweet("test_tweet.json")               # Note the path to the file: .. is used to go up one level in the directory structure
    plot_tweets_by_attribute("test_tweet.json", "language")
    time.sleep(1)
    print("\nStatus Changed\n")
    time.sleep(1)
    most_status_changes_user_tweet("test_tweet.json")

    #print(lexical_complexity_tweet_stream("../part01/test_tweet.json", 1, [3]))