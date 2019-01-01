import requests 
r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitcoin = r.json() 
print(bitcoin) 
print(type(bitcoin))
