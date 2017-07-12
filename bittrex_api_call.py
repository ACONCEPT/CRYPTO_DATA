#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:29:28 2017

@author: joe
"""

import os
import pandas as pd 
import sys
sys.path.append(__file__)

from localconfig import BITTREX_ID , BITTREX_SECRET

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



if __name__ == '__main__':
    main ()
    btrx.get_open_orders
    btrx.get_order_history
    markets = get_markets()
    tickers = get_tickers(markets)
    market_summaries = market_summaries_now() 
    orderbooks = all_orderbooks(markets)


