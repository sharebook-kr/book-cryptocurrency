import ccxt

binance = ccxt.binance()
orderbook = binance.fetch_order_book('ETH/BTC')
for ask in orderbook['asks']:
    print(ask[0], ask[1])
