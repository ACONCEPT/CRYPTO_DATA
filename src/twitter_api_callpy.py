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

#stream = tweepy.Stream(auth, StreamWatcherListener(), timeout=None)