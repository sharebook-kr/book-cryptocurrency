import pybithumb
import time

tickers = pybithumb.get_tickers()
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker, price)
    time.sleep(0.1)