import pybithumb


def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    price = pybithumb.get_current_price(ticker)
    last_ma5 = ma5[-2]

    if price > last_ma5:
        return True
    else:
        return False


tickers = pybithumb.get_tickers()
for ticker in tickers:
    bull = bull_market(ticker)
    if bull:
        print("{} 상승장".format(ticker))
    else:
        print("{} 하락장".format(ticker))
