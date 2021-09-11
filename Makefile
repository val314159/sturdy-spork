call: clean all
all:
	echo ok
out:
	cd uniswap-v2-core ; solc-0.5.16 contracts/*.sol -oout --abi --bin
	cd uniswap-v3-core ; solc-0.7.6  contracts/*.sol -oout --abi --bin
	mkdir -p out ; cp uniswap-v?-core/out/*.abi out
qqqq:
	$(MAKE) uniswap
uniswap: uniswap-v2-core/out uniswap-v3-core/out
	mkdir -p out ; cp uniswap-v?-core/out/*.abi out
uniswap-v2-core/out:
	cd uniswap-v2-core ; solc-0.5.16 contracts/*.sol -oout --abi --bin
uniswap-v3-core/out:
	cd uniswap-v3-core ; solc-0.7.6  contracts/*.sol -oout --abi --bin
clean:
	find . -name '*~'| xargs rm -fr
	find . -name out | xargs rm -fr
