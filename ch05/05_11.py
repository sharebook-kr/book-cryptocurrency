import pybithumb

tickers = pybithumb.get_tickers()
all = pybithumb.get_current_price("ALL")

for ticker in tickers:
    print(ticker, all[ticker]['closing_price'])