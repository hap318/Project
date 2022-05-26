import tweepy

all_keys = open("C:/Users/Henry/Desktop/Files/twitter2.txt", 'r').read().split()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator)
def find_tweet(keyword):
    tweets = tweepy.Cursor(api.search, q=keyword, lang='en').items(1)
    for tweet in tweets:
        print(tweet.text)
        print('https://twitter.com/twitter/statuses/{id}'.format(id = tweet.id))
        print("\n")
    return tweet.text

while True:
    find_tweet(input("enter key word: "))
