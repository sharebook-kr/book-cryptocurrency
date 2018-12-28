import pykorbit

email = "ceo_jo@gmail.com"
password = "mypassword"
key = "TVMtMRtcap22CRnFeegege84cNDuTJVmvv9FaGWJTRriY7b8cWKIez7eGGkzan0"
secret = "MEasLLFhahGAyUucm7refegEEgpvBfTUe3A2DiMA48o4egegEEv9pBmLUq4e3pM"

korbit = pykorbit.Korbit(email, password, key, secret)
order = korbit.buy_limit_order("XRP", 100, 10)
print(order)
