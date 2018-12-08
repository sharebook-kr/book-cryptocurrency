import pybithumb

def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(5).mean()
    last_ma5 = ma5[-2]
    cur_price = pybithumb.get_current_price(ticker)

    if cur_price > last_ma5:
        return True
    else:
        return False

tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker, " 상승장")
    else:
        print(ticker, " 하락장")


