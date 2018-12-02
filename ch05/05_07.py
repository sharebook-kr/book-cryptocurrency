import pybithumb
import datetime

orderbook = pybithumb.get_orderbook("BTC")
ms = int(orderbook['timestamp'])

dt = datetime.datetime.fromtimestamp(ms/1000)
print(dt)