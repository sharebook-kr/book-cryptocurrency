import pyupbit

access_key = "t88RbbxB8NHNyqBUegeVqowGQOGEefeee3W2dGNU"
secret_key = "VCLoAhrxbvyrukYChbxfxD6O1ESegeckIgbqeiQf"

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())