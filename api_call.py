#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:29:28 2017

@author: joe
"""

#import argparse
#import json
#import pprint
#import requests
#import sys
#import urllib
#import hashlib
#import time 
import os
import pandas as pd 

print ( os.environ['HOME']) 

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

CLIENT_ID = 'ed17a2e26eaa4cd496c3614e02260d78'.encode ('utf-8')
CLIENT_SECRET = '1367db1119f648c48b04f4bf3206b2ac'.encode('utf-8')

btrx = bittrex.Bittrex(CLIENT_ID, CLIENT_SECRET)

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

btrx.get_open_orders
btrx.get_order_history
markets = get_markets()
tickers = get_tickers(markets)
market_summaries = market_summaries_now() 
orderbooks = all_orderbooks(markets)
