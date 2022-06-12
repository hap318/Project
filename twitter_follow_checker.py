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

users = tweepy.Cursor(api.friends, user_get, count=200).items()

while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    print("@" + user.screen_name)