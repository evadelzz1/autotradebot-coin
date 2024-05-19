import pyupbit as ub

access_key = 'access_key'
secret_key = 'secret_key'

upbit = ub.Upbit(access=access_key, secret=secret_key)

my_balance = upbit.get_balances()

for i in my_balance:
    print(i)
