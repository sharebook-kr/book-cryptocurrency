import pyupbit

access_key = "t88RbbxB8NHNyqBUegeVqowGQOGEefeee3W2dGNU"
secret_key = "VCLoAhrxbvyrukYChbxfxD6O1ESegeckIgbqeiQf"

upbit = pyupbit.Upbit(access_key, secret_key)
ret = upbit.buy_limit_order("KRW-XRP", 100, 20)
print(ret)
