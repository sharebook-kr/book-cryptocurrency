import pykorbit

orderbook = pykorbit.get_orderbook("BTC")
asks = orderbook['asks']
for ask in asks:
    print(ask[0], ask[1])
