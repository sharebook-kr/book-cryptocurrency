import pyupbit

orderbook = pyupbit.get_orderbook("KRW-BTC")
print(orderbook)