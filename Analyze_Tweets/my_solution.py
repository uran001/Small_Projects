
import json
import time
import pandas as pd
import matplotlib.pyplot as plt
import re

"""OPEN TWEETS FILE AND PRINT NUMBER OF TWEETS"""

def open_count(file):

    file = open(file, "r")
    tweets = 0
    ans = []
    for line in file.readlines():
        try:
            tweet = json.loads(line)
            ans.append([tweet['user']['lang'], tweet['user']['location'],tweet['text']])

            tweets += 1
        except:
            continue
    print(tweets, "tweets stored in the file")
    return ans


"""CREATIGN DATAFRAME WITH LAN, LOCATION, TEXT"""

def histogram_lan(lang):


    # lang = reversed(lang)
    # print(lang)
    l = len(lang)

    li = []
    li.append(lang[l - 1])
    li.append(lang[l - 2])
    li.append(lang[l - 3])
    li.append(lang[l - 4])
    li.append(lang[l - 5])

    lan = [x[0] for x in li]
    lan_count = [x[1] for x in li]
    num = [1, 2, 3, 4, 5]
    plt.bar(num, lan_count)
    plt.xticks(num, lan)
    plt.show()


def histogram_loc(loc):


    # lang = relocversed(lang)
    # print(lang)
    l = len(loc)

    # hahahahaha
    d = {}

    li = []
    li.append(loc[l - 2])
    li.append(loc[l - 3])
    li.append(loc[l - 4])
    li.append(loc[l - 5])
    li.append(loc[l - 6])

    #print(li)

    loc = [x[0] for x in li]
    loc_count = [x[1] for x in li]
    num = [1, 2, 3, 4, 5]
    plt.bar(num, loc_count)
    plt.xticks(num, loc)
    plt.show()

def count_lan(lan, file):
        file = open(file, "r")

        ans = []


        for line in file.readlines():
            try:
                d = json.loads(line)
                if d['user']['lang'] == lan:
                    ans.append(d['text'])
            except:
                continue
        return ans

def count_by_keyword(data, keywords):
    ans = 0
    for x in data:
        for y in keywords:
            if y in x:
                ans += 1
                break
    print(ans)
def find_urls(text):

    lang = ["python", "c++", "golang", "php", "java"]
    text1 = re.findall(r"[\w]+",text)
    text = text.split(' ')
    #print(text1)
    urls = []
    # print(text)
    id = ""
    for x in text:
        if "http" in x:
            urls.append(x)
        x = x.lower()
        if x in lang:
            id = x

        #   print(x)
    for x in text1:
        x = x.lower()
        if x in lang:
            id = x
        #  pri
    return [urls,id]



if __name__ == '__main__':

    """OPEN TWEETS FILE AND PRINT NUMBER OF TWEETS CREATIGN DATAFRAME WITH LAN, LOCATION, TEXT"""
    ans = open_count("tweets.json")
    """HITOGRAM BY LANGUAGE"""
    lang = {}
    for x in ans:
        if x[0] not in lang.keys():
            lang[x[0]] = 1
        else:
            lang[x[0]] += 1
    lang = sorted(lang.items(), key=lambda kv: kv[1])
    histogram_lan(lang)

    """HISTOGRAM BY LOCATION"""
    loc = {}
    for x in ans:
        if x[1] not in loc.keys():
            loc[x[1]] = 1
        else:
            loc[x[1]] += 1
    loc = sorted(loc.items(), key=lambda kv: kv[1])
    print ("Number of languages {0}".format(lang))
    histogram_loc(loc)

    """COUNT ONLY ENG"""
    data_lan = count_lan('en', 'tweets.json')

    """COUNT BY KEYWORDS"""
    #count_by_keyword(data_lan, ['tutorial', 'programming', 'software', 'linux', 'windows', 'mac os', 'data','dictionary'])

    """COUNT RELEVANT TWEETS"""
    lang = {}
    for x in ans:
        if x[0] not in lang.keys():
            lang[x[0]] = 1
        else:
            lang[x[0]] += 1
    for x in lang.keys():
        if x == 'en':
            print("Number of tweets in English {0}".format(lang[x]))
            break

    lang_dict = {"python":[], "c++":[], "golang":[], "php":[], "java":[]}

    urls = []
    for x in data_lan:
        urls = find_urls(x)
        #print(urls[0])
        if urls[1] in lang_dict.keys():
            lang_dict[urls[1]].append(urls[0])

    for x in lang_dict:
        #print("For {0} urls are {1} ".format(x, lang_dict[x]))
        temp = lang_dict[x]
        data = []
        #print(x)
        file = open(x + ".txt", "w+")
        for c in temp:
            if len(c) > 0:
                try:
                    file.write(c[0])
                except: UnicodeEncodeError
        file.close()



