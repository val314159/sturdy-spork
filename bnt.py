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

a0="0xee98420CfE9A94Fc6532E5fE89d92DD60718871F"
a1="0xf7A4ca3d1Dc5817336CB9580822701F31Cc5A9eC"

p0="0xb75425430db0b9db1b371a118fb626bbf8aeb0d713601aac3fdd5c05d28ed637"
p1="0x4708782b211d897c53c532513b8b27711c10d83f344ece1b18400daa0af9fc3b"

if w3.isConnected():
    print(">> connected!")
else:
    raise Exception('not connected')

#print(w3.eth.get_balance(a0))
#print(w3.eth.get_balance(a1))

#import web3
#from web3 import Web3
from uniswap import Uniswap
from decimal import Decimal
#from kista import *
import kista

#w3 = Web3()

#print(dir(web3))
#e = Web3.fromWei(3841357360894980500000001, 'ether')
#print(e)

if 0:
    w = Web3.toWei(3.1, 'ether')
    print(w, 'wei')

    e = Web3.fromWei(w, 'ether')
    print(e, 'eth')
    pass

#address_key = "YOUR ADDRESS"          # or None if you're not going to make transactions
#private_key = "YOUR PRIVATE KEY"  # or None if you're not going to make transactions
address = None
private_key = None
#version = 1
#version = 2                       # specify which version of Uniswap to use
#version = 3                       # specify which version of Uniswap to use
#provider = "WEB3 PROVIDER URL"    # can also be set through the environment variable `PROVIDER`
#provider = "https://ropsten.infura.io/206f5160ae22470faee089b2ed352c49"
#provider = "https://mainnet.infura.io/v3/206f5160ae22470faee089b2ed352c49"
#uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

#provider = "https://mainnet.infura.io/v3/206f5160ae22470faee089b2ed352c49"
#uniswap = Uniswap(address=address, private_key=private_key, version=version)

factory_address = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
router_address  = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

uniswap1 = Uniswap("","",version=1,web3=w3)
uniswap2 = Uniswap("","",version=2,web3=w3)
uniswap3 = Uniswap("","",version=3,web3=w3)

#uniswap1 = Uniswap(address=address, private_key=private_key, version=1)
#uniswap2 = Uniswap(address=address, private_key=private_key, version=2)
#uniswap3 = Uniswap(address=address, private_key=private_key, version=3)

erc20 = dict()
e00='0x0000000000000000000000000000000000000000'
for k, v in dict(
        e00='0x0000000000000000000000000000000000000000',
        eth='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        dai='0x6b175474e89094c44da98b954eedeac495271d0f',
        btc='0x2260fac5e5542a773aa44fbcfedf7c193bc2c599',
        usd='0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
        uni='0x1f9840a85d5af5bf1d1762f925bdaddc4201f984',
        bat="0x0D8775F648430679A709E98d2b0Cb6250d2887EF",
).items():
    #print(k, v)
    #print(Web3.toChecksumAddress(v))
    erc20[k] = Web3.toChecksumAddress(v)
    pass

#print(erc20)
#a = erc20['weth']
#print("A", a)
#print("A", type(a))
#print(kista.load_abi('IERC20'))

def LoadContract(address, name):
    return kista.WrapContract(
        w3.eth.contract(address=address, abi=kista.load_abi(name)))

factory_address = "0x1F98431c8aD98523631AE4a59f267346ea31F984"
factory = LoadContract(factory_address, "UniswapV3Factory")

a1 = factory_address
a2 = factory_address

print("F", factory.owner())
print("F", factory.feeAmountTickSpacing(11))
print("F", factory.getPool(a1,a2,1))

exit()

for k, v in erc20.items():
    print("================")
    c1 = LoadContract(v, 'IERC20')
    try:
        info = (c1.name(), c1.symbol(), c1.decimals(), c1.totalSupply())
        print(info)
    except BadFunctionCallOutput:
        print("SKIP", k)
        continue
    try:
        #w = uniswap2.get_price_input(v, erc20['dai'], 10**18)#, route=erc20['uni'])
        #print(2, w, 'weii')
        #w = uniswap2.get_price_input(v, e00, 10**18)
        #print(2, w, 'weii')
        w = uniswap3.get_price_input(v, erc20['eth'], 10**18)
        print(3, w, 'weii', 'weth')
    except ContractLogicError:
        print("ERR")
    try:
        w = uniswap3.get_price_input(v, erc20['dai'], 10**18)
        print(3, w, 'weii', 'dai')
    except ContractLogicError:
        print("ERR")
        pass
    try:
        w = uniswap3.get_price_input(v, erc20['usd'], 10**18)
        print(3, w, 'weii', 'usd')
    except ContractLogicError:
        print("ERR")
        pass

    pass

#print(type(erc20['eth']))

if 0:
    w = uniswap2.get_price_input(erc20['eth'], erc20['dai'], 10**18)
    d = Web3.fromWei(w, 'ether')
    print(2, d, 'dai')

    w = uniswap3.get_price_input(erc20['eth'], erc20['dai'], 10**18)
    d = Web3.fromWei(w, 'ether')
    print(3, d, 'dai')

    w = uniswap2.get_price_output(erc20['eth'], erc20['dai'], 10**18)
    d = Web3.fromWei(w, 'ether')
    print(2, d, 'dai')

    w = uniswap3.get_price_output(erc20['eth'], erc20['dai'], 10**18)
    d = Web3.fromWei(w, 'ether')
    print(3, d, 'dai')

exit()

#rint(c0.functions())
#a2 = WrapAccount(a)

#print("A", a2)

#print("A", a2.balance)

print("-----")

x1 = uniswap.get_ex_eth_balance(erc20['weth'])

print(x1)

exit()

for k,v in erc20:
    print(k, v)

#Web3.toChecksumAddress(lower_case_address).', '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2')


x1 = uniswap.get_ex_eth_balance(erc20['weth'])




exit()

# Some token addresses we'll be using later in this guide
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
xai = "0x2a1530C4C41db0B0b2bB646CB5Eb1A67b7158667"
bat = xai

w = uniswap.get_price_input(eth, xai, 10**18)
#d = Web3.fromWei(w, 'ether')
print(w, 'xai')

# Get the balance of ETH in an exchange contract.
x1 = uniswap.get_ex_eth_balance(bat)

# Get the balance of a token in an exchange contract.
x2 = uniswap.get_ex_token_balance(bat)

# Get the exchange rate of token/ETH
x3 = uniswap.get_exchange_rate(bat)

print(x1,x2,x3)

#Liquidity Methods (v1 only)??

# Add liquidity to the pool.
#uniswap.add_liquidity(bat, 1*10**18)

# Remove liquidity from the pool.
#uniswap.remove_liquidity(bat, 1*10**18)

