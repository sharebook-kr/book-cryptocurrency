import ccxt

binance = ccxt.binance()
orderbook = binance.fetch_order_book('ETH/BTC')
print(orderbook['bids'])
print(orderbook['asks'])
