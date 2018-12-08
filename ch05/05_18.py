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

is_bull = bull_market("BTC")
if is_bull:
    print("비트코인 상승장")