import tweepy
import time
all_keys = open("C:/Users/Henry/Desktop/Files/twitter2.txt", 'r').read().split()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator)

user_get = input("Enter user: ")

def getRecent():
    tweets = api.user_timeline(screen_name=user_get,count=200,
                               include_rts = False,tweet_mode = 'extended')
    for tweet in tweets[:1]:
        print("ID: {}".format(tweet.id))
        print('https://twitter.com/twitter/statuses/{id}'.format(id=tweet.id))
        print(tweet.created_at)
        print(tweet.full_text)
        print("\n")

def getReplies(tweet):
    pass

getRecent()