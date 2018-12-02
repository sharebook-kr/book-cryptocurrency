import pybithumb

orderbook = pybithumb.get_orderbook("BTC")
bids = orderbook['bids']
asks = orderbook['asks']

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print("매수호가: ", price, "매수잔량: ", quant)

for ask in asks:
    price = ask['price']
    quant = ask['quantity']
    print("매도호가: ", price, "매도잔량: ", quant)


