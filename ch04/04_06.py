import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text
 
soup = BeautifulSoup(html, "html5lib")
tags = soup.select(".lwidth tbody .strong td em")

for tag in tags:
    print(tag.text)
