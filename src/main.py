#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 01:42:08 2017

@author: joe
"""
import sys
import os
import gc
srcpath = os.path.dirname(os.path.dirname(__file__))  + '/input_data/'
sys.path.append(srcpath)

import bittrex_api_call as btrx
import gdax_api_call as gdax

from twitter_api_call import twitter_search

dict_type = "dict" 
gdax_data = gdax.main('ALL', False,dict_type)
bittrex_data = btrx.main("ETH",False, dict_type )

def split_index(label):
    try:
        ab = label.split('-')
        if len(ab) != 2: 
            raise ValueError
        else:
            return ab[0], ab[1]
    except ValueError as e:        
        print('split_index returned more than two halves on index {}'.format(label))
        
        
def index_search_twitter(df):
    a = '' 
    b = ''
    for x in df.index:
        a, b =  split_index(x)
        dfa = twitter_search(a)
        dfb = twitter_search(b)
        
gc.collect()