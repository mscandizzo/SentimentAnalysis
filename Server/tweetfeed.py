# Required libraries 

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler as OAH
from tweepy import Stream
import time

import json
from mongoconn import get_mongo_db

# Required user, passwords, key and secret
access_token = '952716301851652096-Zdn01tpFWXOcTbPuHdye0LkeL4dcyW8'
access_token_secret = 'TDnC2QSAIzJN1uZcwwG3ZFYru5D2KSEg2KoKJz48uIRPV'
consumer_key = 'aLSimwfXagEX2RfBBmRRq9Mxs'
consumer_secret = 'U99xcJ8DkwKtrIm2tzfCmnQJovmbHef7L9BLDmjJTYgkomEwfP'

# Authentication process to connect to Tweeter API

auth = OAH(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class tweetfeed(StreamListener):
    '''
    Streams tweets and saves to a MongoDB database
    The time_limit parameter offers the functionality of 
    keeping the feed running only for a discrete amount of time
    (otherwise i will just keep going)
    '''
    def __init__(self,api,time_limit=60,**kwargs):

        super(tweepy.StreamListener,self).__init__()
        self.api = api
        self.star_time = time.time()
        self.time_limit = time_limit
        self.collection = get_mongo_db('tweets',**kwargs)['tweets']

    def tweet_search(self, string, rpp = 5, page = 5):
        '''
        Search for specific keyword or list of keywords
        rpp = number of tweets to retrieve
        page = number of pages to search 
        '''
        return self.api.search(q=string,rpp= rpp,page =page)

    def on_data(self,tweet):
        '''
        While running it will collect tweets and store the 
        tweets into the MongoDB Database
        '''
        if (time.time() - self.star_time) < self.time_limit:
            self.collection.insert(json.loads(tweet))
            return True
        else:
            return False

    def on_error(self,status):
        return True # keep stream open


    
def run_stream(keyword='python',**kwargs):
    '''
    It connects to Tweeter API and collects all tweets 
    for a given keyworkd or list of keywords
    '''
    stream = tweepy.Stream(auth = auth,listener = tweetfeed(api))
    stream.filter(track=keyword)
    print('finalized')




