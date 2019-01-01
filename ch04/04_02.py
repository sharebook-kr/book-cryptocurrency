import requests
from bs4 import BeautifulSoup
 
url = "http://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text
 
soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_per")
tag = tags[0]
print(tag.text)
