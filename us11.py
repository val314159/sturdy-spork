import web3
from web3 import Web3
from uniswap import Uniswap
from decimal import Decimal
from kista import *

w3 = Web3()

#print(Decimal)

#print(dir(web3))
#e = Web3.fromWei(3841357360894980500000001, 'ether')
#print(e)

w = Web3.toWei(3.1, 'ether')
print(w, 'wei')

e = Web3.fromWei(w, 'ether')
print(e, 'eth')

#exit()

#address = "YOUR ADDRESS"          # or None if you're not going to make transactions
#private_key = "YOUR PRIVATE KEY"  # or None if you're not going to make transactions
address = None
private_key = None
version = 1
#version = 2                       # specify which version of Uniswap to use
#version = 3                       # specify which version of Uniswap to use
#provider = "WEB3 PROVIDER URL"    # can also be set through the environment variable `PROVIDER`
#provider = "https://ropsten.infura.io/206f5160ae22470faee089b2ed352c49"
provider = "https://mainnet.infura.io/v3/206f5160ae22470faee089b2ed352c49"
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

erc20 = dict()
for k, v in dict(
        weth='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
).items():
    print(k, v)
    print(Web3.toChecksumAddress(v))
    erc20[k] = Web3.toChecksumAddress(v)
    pass

print(erc20)

a = erc20['weth']
print("A", a)

a2 = WrapAccount(a)

print("A", a2)

print("A", a2.balance)

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

#Liquidity Methods (v1 only)¶

# Add liquidity to the pool.
#uniswap.add_liquidity(bat, 1*10**18)

# Remove liquidity from the pool.
#uniswap.remove_liquidity(bat, 1*10**18)

