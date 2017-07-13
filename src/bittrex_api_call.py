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
import timeit
from localconfig import BITTREX_ID , BITTREX_SECRET 

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
    # orderbook columns are "quantity, rate,otype" otype is added in this function, it can be buy or sell
    orderbook = btrx.get_orderbook(market,'both',20).get('result')
    buys = pd.DataFrame(orderbook.get('buy'))
    sells = pd.DataFrame(orderbook.get('sell'))
    buys['otype'] = 'buy'
    sells['otype'] = 'sell'
    obk = buys.append(sells)
    return obk

def all_orderbooks(markets): 
    orderbooks = []
    for market in markets:
        orderbooks.append(current_orderbook(market))
    return orderbooks

def main(): 
    pass


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == '__main__':
#    main ()
#    openorders = btrx.get_open_orders()
#    orderhist = btrx.get_order_history()

    get_markets_time = (timeit.timeit(get_markets,number = 1000)/ 1000)
    markets = get_markets()
    
    wrapped_tickers = wrapper(get_tickers, markets)    
    get_tickers_time = (timeit.timeit(wrapped_tickers ,number = 1000) / 1000)    
    tickers = get_tickers(markets)   
    
    market_summaries_time = (timeit.timeit(market_summaries_now,number = 1000) / 1000)    
    market_summaries = market_summaries_now() 
    
    wrapped_obks = wrapper(all_orderbooks,markets)
    obks_time = (timeit.timeit(wrapped_obks, number = 1000))
    orderbooks = all_orderbooks(markets)