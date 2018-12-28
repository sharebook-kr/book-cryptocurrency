import ccxt
from datetime import datetime

binance = ccxt.binance()
ohlcvs = binance.fetch_ohlcv('ETH/BTC')

for ohlc in ohlcvs:
    print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'))
