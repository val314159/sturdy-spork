import os, sys, json, time, web3
from web3 import Web3, HTTPProvider
from pprint import pprint

url = "https://mainnet.infura.io/v3/206f5160ae22470faee089b2ed352c49"
w3 = Web3(Web3.HTTPProvider(url))
#w3 = Web3()

from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

if w3.isConnected():
    print(">> connected!")
else:
    raise Exception('not connected')





