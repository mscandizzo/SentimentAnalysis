import tweepy
from textblob import TextBlob

access_token = '952716301851652096-Zdn01tpFWXOcTbPuHdye0LkeL4dcyW8'
access_token_secret = 'TDnC2QSAIzJN1uZcwwG3ZFYru5D2KSEg2KoKJz48uIRPV'
consumer_key = 'aLSimwfXagEX2RfBBmRRq9Mxs'
consumer_secret = 'U99xcJ8DkwKtrIm2tzfCmnQJovmbHef7L9BLDmjJTYgkomEwfP'

class tweetfeed:
    def __init__(self):

        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

    def tweet_search(self, string, rpp = 5, page = 5):
        return self.api.search(q=string,rpp= rpp,page =page)