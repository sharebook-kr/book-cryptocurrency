import requests

def check_bear_market(coin, cur_price):
    url = "https://min-api.cryptocompare.com/data/histoday?aggregate=1&e=Korbit&extraParams=CryptoCompare&fsym=%s&limit=5&tryConversion=false&tsym=KRW" % coin
    r = requests.get(url)
    content = r.json()

    past_data = content['Data'][:-1]
    close_data = [day_data['close'] for day_data in past_data]
    ma5 = sum(close_data) / len(close_data)

    if cur_price < ma5:
        return True
    else:
        return False

is_btc_bear_market = check_bear_market("BTC", 10000000)
if is_btc_bear_market:
    print("하락장")
else:
    print("상승장")