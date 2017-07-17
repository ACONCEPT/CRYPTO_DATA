#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:27:57 2017

@author: joe
"""

import gdax
import pandas as pd 
import datetime

pc = gdax.PublicClient() 

def get_products():
    products = pd.DataFrame(pc.get_products())
    return list(products.id), products.set_index('id')
    
def get_currencies():
    return pc.getCurrencies() 

def all_24hr_stats(products):
    stats = []
    stat = {} 
    for product in products:        
        pc.productID = product
        stat = pc.getProduct24HrStats()        
        stat['product'] = product
        stats.append(stat)
    stats = pd.DataFrame(stats)
    stats = stats.set_index('product')
    return stats 

def gdax_orderbooks(products,ilevel = 1):
    obks = []
    obk = {} 
    for product in products:        
        obk = pc.get_product_order_book(product,level = ilevel)
        obk['product'] = product
        obks.append(obk)
    obks = pd.DataFrame(obks)
    obks = obks.set_index('product')
    return obks
    
def gdax_tickers(products): 
    tickers = []
    for product in products:
        tick= pc.get_product_ticker(product)
        tick['product']= product
        tickers.append(tick)
    tickers = pd.DataFrame(tickers)
    tickers = tickers.set_index('product')
    return tickers

def gdax_trades(products): # 100 most recent trades
    trades = []
    for product in products:
        trade = {} 
        trade['last_100_trades'] = list(pc.get_product_trades(product))
        trade['product'] = product
        trades.append(trade)
    trades = pd.DataFrame(trades)
    trades = trades.set_index('product')    
    return trades

        
def gdax_product_history(products,start=None, end=None, granularity=None):
    hists = []    
    for product in products:
        hist = {}
        hist['hist'] = pc.get_product_historic_rates(product,start,end,granularity)
        hist['product'] = product
        hists.append(hist)
    hists = pd.DataFrame(hists)
    hists = trades.set_index('product')
    return hists

def gdax_24hr_stats(products):
    stats = []
    stat = {}
    for product in products: 
        stat = pc.get_product_24hr_stats(product)
        stat['product'] = product
        stats.append(stat)
    stats = pd.DataFrame(stats)
    stats = stats.set_index('product')
    stats = stats.rename(columns = {'volume' :'volume_day'})
    return stats

def all_gdax_data(products, df = True):
    start_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S -%Z")
    last_day = gdax_24hr_stats(products)
    orderbooks = gdax_orderbooks(products,ilevel = 1)
    tickers = gdax_tickers(products)
    trades = gdax_trades(products)
#    hist = gdax_product_history(products()) #TODO determine date for start and end here
#    return last_day, orderbooks, tickers, trades
    all_data = last_day.join(orderbooks,lsuffix ='_day',rsuffix='_obk') 
    all_data = all_data.join(tickers,rsuffix='_ticker')
    all_data = all_data.join(trades)    
    all_data['etl_time'] = start_time
    if not df:
        all_data = all_data.to_dict('dict')
    return all_data

def gdax_focus(focus): 
    ax , b = get_products()
    return [a for a in ax if focus in a]


def gdax_time ():
    return pc.get_time()

def gdax_currencies():
    return pc.get_currencies()

def main(focus = 'ETH'):    
    if focus == 'ALL':
        products , t = get_products()
    else:
        products = gdax_focus(focus)        
    data  = all_gdax_data(products)
    return data 

if __name__ == '__main__':
    data = main()    
#    last_day, orderbooks, tickers, trades = all_gdax_data(products)
#    last_day.join(tickers)
    
