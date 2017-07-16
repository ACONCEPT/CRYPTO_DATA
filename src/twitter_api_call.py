# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:38:13 2017

@author: joesa
"""
import os
import sys
import tweepy
inpath = os.path.dirname(os.path.dirname(__file__))  + '/input_data/'
sys.path.append(inpath)
#import timeit

from localconfig import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET , TWITTER_ACCESS_TOKEN , TWITTER_ACCESS_SECRET 


auth = tweepy.auth.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET )
auth.set_access_token(TWITTER_ACCESS_TOKEN , TWITTER_ACCESS_SECRET)

twitter_api = tweepy.API(auth)

twitter_api.__dir__()

twitter_api.search_users()

twitter_api.me()

results = twitter_api.search(q = "ETH")
print(type(results))

for result in results:
    print (result.text)
    
for friend in tweepy.Cursor(twitter_api.friends).items():
    # Process the friend here
    print(friend.screen_name,friend.id)


for tweet in tweepy.
tweepy.models.User.lists()