import pybithumb

all = pybithumb.get_current_price("ALL")
tickers = pybithumb.get_tickers()

for ticker in tickers:
    prices = all[ticker]
    rate24 = prices['24H_fluctate_rate']
    print(ticker, rate24)
