import pybithumb

all = pybithumb.get_current_price("ALL")
tickers = pybithumb.get_tickers()

for ticker in tickers:
    prices = all[ticker]
    rate24 = prices['fluctate_rate_24H']
    print(ticker, rate24)
