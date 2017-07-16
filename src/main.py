#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 01:42:08 2017

@author: joe
"""
import sys
import os
srcpath = os.path.dirname(os.path.dirname(__file__))  + '/input_data/'
sys.path.append(srcpath)

import bittrex_api_call as btrx
import gdax_api_call as gdax

gdax_data = gdax.main('ALL')
bittrex_data = btrx.main()

bittrex_data.index

