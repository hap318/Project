import nltk
import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer
from utils import *

all_keys = open("C:/Users/Henry/Desktop/Files/twitter2.txt", 'r').read().split()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]
authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)
api = tweepy.API(authenticator)

def find_tweet(keyword, num):
    tweets = tweepy.Cursor(api.search, q=keyword, lang='en').items(num)
    tweetsList = []
    for tweet in tweets:
        print(tweet.text)
        print('https://twitter.com/twitter/statuses/{id}'.format(id = tweet.id))
        print("\n")
        tweetsList.append(tweet.text)
    return tweetsList,tweet

def classify():
    pos = 0
    neg = 0
    sia = SentimentIntensityAnalyzer()
    tweetList, tweet = find_tweet(input("Key Word: "), 10)
    for i in tweetList:
        print(sia.polarity_scores(i))
        print('https://twitter.com/twitter/statuses/{id}'.format(id=tweet.id))
        if sia.polarity_scores(i)["compound"] > 0:
            pos += 1
        elif sia.polarity_scores(i)["compound"] < 0:
            neg += 1
    print("\n")
    print("pos score:",(pos/(pos+neg))*100, "%")
    print("neg score:", (neg /(pos + neg))*100, "%")


classify()


