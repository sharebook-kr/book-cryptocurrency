import ccxt

binance = ccxt.binance()
markets = binance.fetch_tickers()
print(markets.keys())
