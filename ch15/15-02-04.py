import pykorbit
import pykorbit.history

# BTC: 비트코인
# ETH: 이더리움
# BCH: 비트코인 캐시
# ETC: 이더리움 클래식
currency_list = ["BTC", "ETH", "BCH", "ETC"]

def check_bear_market(currency):
    df = pykorbit.history.get_daily_ohlc(currency, start="2018-01-01")
    ma5 = df['close'].rolling(window=5).mean()
    df.insert(4, "ma5", ma5)

    cur_price = pykorbit.get_current_price(currency.lower() + "_krw")
    ma5_price = df.iloc[-1]['ma5']

    if cur_price > ma5_price:
        print("상승장")
    else:
        print("하락장")

for currency in currency_list:
    print(currency, end=": ")
    check_bear_market(currency)
