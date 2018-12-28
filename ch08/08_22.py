import ccxt

binance = ccxt.binance()
ticker = binance.fetch_ticker('ETH/BTC')
print(ticker['open'], ticker['high'], ticker['low'], ticker['close'])
