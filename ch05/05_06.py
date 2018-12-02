import pybithumb

orderbook = pybithumb.get_orderbook("BTC")
print(orderbook)

for k in orderbook:
    print(k)