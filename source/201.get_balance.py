from dotenv import load_dotenv
import os
import pyupbit

if not load_dotenv():    # load .env
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit_access_key = os.getenv("UPBIT_ACCESS_KEY")
upbit_secret_key = os.getenv("UPBIT_SECRET_KEY")

print(f'### [Config Upbit] ACCESS_KEY: {upbit_access_key[0:10]}...')
print(f'### [Config Upbit] SECRET_KEY: {upbit_secret_key[0:10]}...')
        
try:
    upbit = pyupbit.Upbit(upbit_access_key, upbit_secret_key)

    ticker = "KRW-ETH"
    
    balance = upbit.get_balance()
    print(f'KRW : {balance:15.5f}')

    balance = upbit.get_balance(ticker=ticker)
    print(f'ETH : {balance:15.5f}')
    
    avgBuyPrice = upbit.get_avg_buy_price(ticker)   # 평균 매수가 조회
    print(f'ETH 평균매수가 : {format(avgBuyPrice, ",")}')
    
except Exception as e:                              # 예외가 발생했을 때 실행됨
    print('[Error]', e)