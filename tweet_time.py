from datetime import datetime

import tweepy
import time

all_keys = open("C:/Users/Henry/Desktop/twitter2.txt", 'r').read().split()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator)

while True:
    curr_time = datetime.now()
    api.update_status(curr_time)
    time.sleep(10)
    print(curr_time)



