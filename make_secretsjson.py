#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 17:31:54 2017

@author: joe
"""
import os
import json 

# client id and secret id, do this before setting up the bittrex apie
CLIENT_ID = 'ed17a2e26eaa4cd496c3614e02260d78'
CLIENT_SECRET = '1367db1119f648c48b04f4bf3206b2ac'

a = {'key':CLIENT_ID,'secret':CLIENT_SECRET}

os.path.exists(os.environ['HOME'] + '/repos/' + '/bittrexapi/' + 'python-bittrex' + '/bittrex' + '/test/secrets.json')

with open (os.environ['HOME'] + '/repos/' + '/bittrexapi/' + 'python-bittrex' + '/bittrex' + '/test/secrets.json','w') as outfile:
    json.dump(a,outfile)
    