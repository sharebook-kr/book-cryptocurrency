import ccxt

binance = ccxt.binance()
ohlcvs = binance.fetch_ohlcv('ETH/BTC')
print(ohlcvs)
