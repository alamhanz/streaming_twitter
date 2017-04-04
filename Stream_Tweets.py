# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 13:44:26 2015

@author: Aska
"""

#IT IS FOR @jobsdotid stream tweet


#Import the necessary methods from tweepy library
import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
 
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        with open(fistr,'a') as tf:
            tf.write(data)
            tf.write("\n")
        return True

    def on_error(self, status):
        print status

fistr=raw_input('Input Raw_Data_Tweets Name :')
fistr=fistr+'.txt'
fil = open(fistr, 'w')
#Variables that contains the user credentials to access Twitter API 
access_token = raw_input('access token : ')
access_token_secret = raw_input('access token secret :')
consumer_key = raw_input('consumer key :') 
consumer_secret = raw_input('consumer secret :')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
key=raw_input('Input your keyword (split by comma):')
key=key.split(',')

#dtreaming
l = StdOutListener()
stream = Stream(auth, l)
keyword=key
stream.filter(track=keyword)
