import pybithumb

tickers = pybithumb.get_tickers()
print(tickers)
print(len(tickers))
print(type(tickers))
