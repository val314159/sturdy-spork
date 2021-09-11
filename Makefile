call: clean all
all: uniswap_contracts
out/IERC20.abi: interfaces/IERC20.sol
	solc interfaces/*.sol -oout --abi
uniswap_contracts: uniswap-v2-core/out uniswap-v3-core/out out/IERC20.abi
	cp uniswap-v?-core/out/*.abi out
uniswap-v2-core/out:
	cd uniswap-v2-core ; solc-0.5.16 contracts/*.sol -oout --abi --bin
uniswap-v3-core/out:
	cd uniswap-v3-core ; solc-0.7.6  contracts/*.sol -oout --abi --bin
clean:
	find . -name '*~'| xargs rm -fr
	find . -name out | xargs rm -fr
