Project's idea  is to analyse some “big” data scrapped from the Internet using Pandas, Tweepy and
Matplotlib. 
My code analyse tweets about “programming” languages, with the ultimate objective of extracting some
interesting links to know more about programming. You can analyze other stored tweets as well 

1) Dataset
Stored data are for tweets with the keywords “python”, “java”, “c++”, “golang”, “php” tweeted around
the world for a period of 3~4 hours and stored as a json file 

2) Using the tweets in the json file, it creates a dataframe retaining, for each tweet, only information about the
language, the user location, and the actual tweet (i.e., the ‘text’)

3) It Creates and shows a histogram of the top 5 languages used in the tweets that you have stored (see an example in
top5.png). 
4) It Plots a histogram of the top 5 location from where the tweets that you have stored were issued.

5) It Creates a dataframe that retains only the tweets in the English language

6) From the tweets in English, it creates a dataframe to retain only the relevant ones. A tweet is relevant if it contains
at least one of the following keywords: [tutorial, programming, software, linux, windows, mac os, data,
dictionary]

7) It Plots a histogram to show the relation between “number of relevant tweets in English” and the keywords that
you have used at 1)

8) Some of the relevant tweets in English may contain links to Web pages 3 . It extracts these links and
store them in files named <language>.txt

(for instance, python.txt will store all the links found in relevant tweets in English about “python”).
Note that a Web link is a string of variable length that always starts with “http://” or “https://”.
