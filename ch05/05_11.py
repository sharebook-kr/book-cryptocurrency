import requests

url = "https://min-api.cryptocompare.com/data/histoday?aggregate=1&e=Korbit&extraParams=CryptoCompare&fsym=ETH&limit=5&tryConversion=false&tsym=KRW"
r = requests.get(url)
content = r.json()

for day_data in content['Data']:
    print(day_data)