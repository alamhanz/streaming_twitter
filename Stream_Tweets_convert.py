# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 19:57:19 2015

@author: Aska
"""
import json
import numpy as np
import pandas as pd
import sys
#import matplotlib.pyplot as plt

fistr = raw_input('Input Raw_Data_Tweets Name :')
tweets_data_path = fistr+'.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets_data2=[]
print 'Number of tweets : ',len(tweets_data)
i=0
while i <= len(tweets_data)-1:
    try:
        tweets_data[i]['id']=str(tweets_data[i]['id'])
        tweets_data[i]['user']['id']=str(tweets_data[i]['user']['id'])
        tweets_data[i]['entities']['user_mentions']=str(tweets_data[i]['entities']['user_mentions'])
        tweets_data[i]['entities']['hashtags']=str(tweets_data[i]['entities']['hashtags'])
        
        if tweets_data[i]['lang']=='in':
            tweets_data2.append(tweets_data[i])
    except :
        print "Nope"
    i=i+1
tweets_data=list(np.copy(tweets_data2))
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['id_text'] = map(lambda tweet: tweet['id'], tweets_data)
tweets['created_at'] = map(lambda tweet: tweet['created_at'], tweets_data)
tweets['language'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
tweets['user_id'] = map(lambda tweet: tweet['user']['id'], tweets_data)
tweets['user_screen_name'] = map(lambda tweet: tweet['user']['screen_name'], tweets_data)
tweets['user_name'] = map(lambda tweet: tweet['user']['name'], tweets_data)
tweets['Location'] = map(lambda tweet: tweet['user']['location'], tweets_data)
tweets['friend_count'] = map(lambda tweet: tweet['user']['friends_count'], tweets_data)
tweets['followers_count'] = map(lambda tweet: tweet['user']['followers_count'], tweets_data)
tweets['Statuses_count'] = map(lambda tweet: tweet['user']['statuses_count'], tweets_data)
tweets['retweet_count']= map(lambda tweet: tweet['retweet_count'], tweets_data)
tweets['user_mention']= map(lambda tweet: tweet['entities']['user_mentions'], tweets_data)
tweets['hashtags']= map(lambda tweet: tweet['entities']['hashtags'], tweets_data)


#tweets_by_lang = tweets['lang'].value_counts()

#save it to excel
writer = pd.ExcelWriter(fistr+'_result.xlsx')
tweets.to_excel(writer,'MyTweet')
writer.save()

print "---------------------------------------------------------"