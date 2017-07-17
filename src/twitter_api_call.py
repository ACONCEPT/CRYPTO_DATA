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
import datetime
import pandas as pd
#import timeit

from localconfig import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET , TWITTER_ACCESS_TOKEN , TWITTER_ACCESS_SECRET 


auth = tweepy.auth.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET )
auth.set_access_token(TWITTER_ACCESS_TOKEN , TWITTER_ACCESS_SECRET)

twitter_api = tweepy.API(auth)   

def twitter_search_generator(search_term,num_results = 'ALL'):
    for result in tweepy.Cursor(twitter_api.search,q = search_term).items(num_results): 
        yield result

def twitter_search(search_term, result_count,df = False):
    results = []
    a = ''
    for x in twitter_search_generator(search_term,result_count): 
        result = {}
        result['data'] = x._json
        result['search_term'] = search_term
        result['etl_time'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S -%Z")
        result['id'] = x.id
        results.append(result)
    if df:
        a = pd.DataFrame(results)
        a.set_index('id')
    a = results
    return a

def main ():
    search_results = twitter_search('ETH',100)
    return search_results

if __name__ == '__main__':
    search_results = main() 

    
#
#example = search_results.iloc[0]
#statusobj = example['response_object']
#statusobj.text   
#dir(statusobj)
#print(statusobj.geo)
#print(statusobj.coordinates)
#print(statusobj.geo)
#print(statusobj.possibly_sensitive)
#print(statusobj.place)
#print(statusobj.favorite_count)
#print(statusobj.favorited)
##print(statusobj.favorite)
#print(statusobj.entities)
#print(statusobj.id)
#print(statusobj.id_str)
#print(statusobj.in_reply_to_screen_name)
#print(statusobj.in_reply_to_status_id)
#print(statusobj.in_reply_to_status_id_str)
#print(statusobj.in_reply_to_user_id)
#print(statusobj.in_reply_to_user_id_str)
#print(statusobj.is_quote_status)
#print(statusobj._json)
#print(type(statusobj.metadata))
#print(statusobj.metadata['iso_language_code'])
#check = statusobj._json
#check['metadata']