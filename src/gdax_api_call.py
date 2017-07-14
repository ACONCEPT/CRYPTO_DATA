#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:27:57 2017

@author: joe
"""

import gdax
import pandas as pd 

pc = gdax.PublicClient() 

def get_products():
    products = pd.DataFrame(pc.getProducts())
    return list(products.id)
    
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
    return stats 


#historicrates = pd.getProductHistoricRates()

def gdax_orderbooks(products):
    obks = []
    obk = {} 
    for product in products:        
        pc.productID = product
        obk = pc.getProductOrderBook()
        obk['product'] = product
        obks.append(obk)
    return obks   
