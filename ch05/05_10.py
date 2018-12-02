import pybithumb

all = pybithumb.get_current_price("ALL")
for k, v in all.items():
    print(k, v)
