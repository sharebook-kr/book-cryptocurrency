import pyupbit

access_key = "t88RbbxB8NHNyqBUegeVqowGQOGEefeee3W2dGNU"
secret_key = "VCLoAhrxbvyrukYChbxfxD6O1ESegeckIgbqeiQf"

upbit = pyupbit.Upbit(access_key, secret_key)
ret = upbit.sell_limit_order("KRW-XRP", 1000, 20)
print(ret)

