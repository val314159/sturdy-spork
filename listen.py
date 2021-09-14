#!/usr/bin/env python3

import os, sys, json, time, web3
from web3.exceptions import *
from web3 import Web3, HTTPProvider
from pprint import pprint

#url = "https://mainnet.infura.io/v3/206f5160ae22470faee089b2ed352c49"
#w3 = Web3(Web3.HTTPProvider(url))
w3 = Web3()

# need for this infura
# doesn't seem to break anything on ganache-cli
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

if w3.isConnected():
    print(">> connected!")
else:
    raise Exception('not connected')

from uniswap import Uniswap
from decimal import Decimal
#from kista import *
import kista

def LoadContract(name, address):
    return kista.WrapContract(
        w3.eth.contract(address=address, abi=kista.load_abi(name))) 

address = None
private_key = None

uniswap1 = Uniswap("","",version=1,web3=w3)
uniswap2 = Uniswap("","",version=2,web3=w3)
uniswap3 = Uniswap("","",version=3,web3=w3)

erc20 = dict()
e00='0x0000000000000000000000000000000000000000'
for k, v in dict(
        e00 ='0x0000000000000000000000000000000000000000',
        weth='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        dai ='0x6b175474e89094c44da98b954eedeac495271d0f',
        wbtc='0x2260fac5e5542a773aa44fbcfedf7c193bc2c599',
        usdc='0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
        uni ='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984',
        bat ="0x0D8775F648430679A709E98d2b0Cb6250d2887EF",
).items():
    #print(k, v)
    #print(Web3.toChecksumAddress(v))
    erc20[k] = Web3.toChecksumAddress(v)
    pass

factory2 = LoadContract("UniswapV2Factory", "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f")
factory3 = LoadContract("UniswapV3Factory", "0x1F98431c8aD98523631AE4a59f267346ea31F984")

def get_pool(token0=None, token1=None, fee=3000, symbol0=None, symbol1=None):
    if token0 is None: token0 = erc20[symbol0]
    if token1 is None: token1 = erc20[symbol1]
    return factory3.getPool(token0, token1, fee)

def v3_pool_info(symbol0, symbol1, fee=3000):
    pool_address = get_pool(symbol0=symbol0,
                            symbol1=symbol1, fee=fee)
    print()
    print("PL", pool_address, "fee", fee)
    pool = LoadContract("UniswapV3Pool", pool_address)
    tok0 = LoadContract("IERC20", pool.token0())
    tok1 = LoadContract("IERC20", pool.token1())

    #print("  factory", pool.factory())

    print("  token0", repr(tok0.name()), "balance", tok0.balanceOf(pool_address) / (10**tok0.decimals()), tok0.symbol())
    print("  token1", repr(tok1.name()), "balance", tok1.balanceOf(pool_address) / (10**tok1.decimals()), tok1.symbol())
    
    #print("  fee", pool.fee())
    return pool, tok0, tok1


factory3 = LoadContract("UniswapV3Factory", "0x1F98431c8aD98523631AE4a59f267346ea31F984")
myContract = factory3.contract
event_filter = myContract.events.PoolCreated.createFilter(fromBlock=11220070,
                                                          toBlock="latest",
                                                          argument_filters={})
for e in event_filter.get_all_entries():
    pprint(e['blockNumber'])
    pprint(e['args'])
exit()

pool, tok0, tok1 = v3_pool_info('wbtc', 'weth', 3000)

e = pool.contract.events
myContract = pool.contract
#print(e)
#event_filter = myContract.events.Mint.createFilter(fromBlock="latest", argument_filters={'arg1':10})
#event_filter = myContract.events.Mint.createFilter(fromBlock="latest", argument_filters={})
#print(event_filter.get_new_entries())

event_filter = myContract.events.Burn.createFilter(fromBlock=11220070,
                                                   toBlock="latest",
                                                   argument_filters={})
for e in event_filter.get_all_entries():
    pprint(e['blockNumber'])
    pprint(e['args'])
exit()

event_filter = myContract.events.Swap.createFilter(fromBlock=13220070,
                                                   toBlock="latest",
                                                   argument_filters={})
for e in event_filter.get_all_entries():
    pprint(e['blockNumber'])
    pprint(e['args'])
exit()

event_filter = myContract.events.Mint.createFilter(fromBlock=1,
                                                   toBlock="latest",
                                                   argument_filters={})

print(event_filter.get_all_entries())

exit()
#print(dir(event_filter))
for n, e in enumerate(event_filter.get_all_entries()):
    d = dict(e)
    d['args'] = dict(e['args'])
    d['no'] = n
    pprint(d)
    #for k,v in e.items():
    #print("D", k, v)
#    print("E", dict(e))
##print(event_filter.get_all_entries())
print("N", n)
#print(len(event_filter.get_all_entries()))
#print(json.dumps(dict(event_filter.get_all_entries())))
