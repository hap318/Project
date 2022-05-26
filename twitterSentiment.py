import nltk
# nltk.download('movie_reviews')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('shakespeare')
# nltk.download('twitter_samples')
nltk.download('vader_lexicon')
from nltk.corpus import shakespeare
from nltk.corpus import twitter_samples
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from utils import *
import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer

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
    return tweetsList


def get_train_test_data():

    pos_review_ids = movie_reviews.fileids('pos')
    neg_review_ids = movie_reviews.fileids('neg')

    pos_train_ids, pos_test_ids = split_data(pos_review_ids)
    neg_train_ids, neg_test_ids = split_data(neg_review_ids)

    training = [(movie_reviews.words(f), 'pos') for f in pos_train_ids] + [(movie_reviews.words(f), 'neg') for f in neg_train_ids]
    testing = [(movie_reviews.words(f), 'pos') for f in pos_test_ids] + [(movie_reviews.words(f), 'neg') for f in neg_test_ids]

    training_norm = [(FreqDist(normalise(wordlist)), label) for (wordlist, label) in training]
    testing_norm = [(FreqDist(normalise(wordlist)), label) for (wordlist, label) in testing]
    return training_norm, testing_norm


random.seed(67)
training,testing=get_train_test_data()

nltk_nb=NaiveBayesClassifier.train(training)

def classInput(input):
    return nltk_nb.classify_many([FreqDist(normalise(input.split()))])

def classList(input,num):
    replies = []
    for i in input:
        replies.append(classInput(i))
        print(classInput(i))
    posNum = 0
    negNum = 0
    for r in replies:
        if r == ['neg']:
            negNum += 1
        elif r == ['pos']:
            posNum += 1
    print("pos:", posNum/num*100, "%")
    print("neg:", negNum/num*100, "%")

classList(find_tweet(input("enter words: "), 20), 20)

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("ok this is meant to be seen as good "))


