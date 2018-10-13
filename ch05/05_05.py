import pybithumb

detail = pybithumb.get_market_detail("BTC")
print(detail)
print(type(detail))
