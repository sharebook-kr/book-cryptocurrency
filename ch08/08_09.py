import pyupbit

access_key = "t88RbbxB8NHNyqBUegeVqowGQOGEefeee3W2dGNU"
secret_key = "VCLoAhrxbvyrukYChbxfxD6O1ESegeckIgbqeiQf"

upbit = pyupbit.Upbit(access_key, secret_key)
ret = upbit.cancel_order('cc52be46-1000-4126-aee7-9bfafb867682')
print(ret)
