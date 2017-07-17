#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:29:28 2017

@author: joe
"""

import os
import pandas as pd 
import sys
inpath = os.path.dirname(os.path.dirname(__file__))  + '/input_data/'
sys.path.append(inpath)
#import timeit
from localconfig import BITTREX_ID , BITTREX_SECRET 
import datetime

PUBLIC_SET = ['getmarkets', 
              'getcurrencies', 
              'getticker', 
              'getmarketsummaries', 
              'getorderbook',
			 'getmarkethistory']

MARKET_SET = ['getopenorders', 
              'cancel', 
              'sellmarket', 
              'selllimit', 
              'buymarket', 
              'buylimit']

ACCOUNT_SET = ['getbalances', 
               'getbalance', 
               'getdepositaddress', 
               'withdraw', 
               'getorder', 
               'getorderhistory', 
               'getwithdrawalhistory', 
               'getdeposithistory']
    
import bittrex
btrx = bittrex.Bittrex(BITTREX_ID, BITTREX_SECRET)

def get_markets():
    markets = pd.DataFrame(btrx.get_markets()['result'])
    marketnames = markets.MarketName     
    return list(marketnames)
    
def get_tickers(markets):
    results = []        
    for x in markets:
        a = btrx.get_ticker (x)    
        a['result']['Market'] = x 
        results.append(a['result'])
    return pd.DataFrame(results)        

def market_summaries_now ():    
    market_summaries = pd.DataFrame(btrx.get_market_summaries()['result'])
    return market_summaries

def current_orderbook (market): 
    orderbook = btrx.get_orderbook(market,'both',20).get('result')
    orderbook['MarketName'] = market
    return orderbook

def all_orderbooks(markets): 
    orderbooks = []
    for market in markets:
        orderbooks.append(current_orderbook(market))
    return pd.DataFrame(orderbooks)


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def get_all_data(markets):
    starttime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S -%Z")    
    market_summaries = market_summaries_now()
    market_summaries = market_summaries.query("MarketName in {}".format(markets))
    market_summaries = market_summaries.set_index('MarketName')
    market_summaries['etl_time'] = starttime
    orderbooks = all_orderbooks(markets)
    orderbooks = orderbooks.set_index('MarketName')    
    return market_summaries.join(orderbooks)

def get_focus_data(market_focus):
    markets = get_markets()
    focus_markets = [m for m in markets if market_focus in m]
    focus_data = get_all_data(focus_markets)
    return focus_data

def main(focus = 'ETH'): 
    return get_focus_data(focus)
    

if __name__ == '__main__':    
    data = main()
    