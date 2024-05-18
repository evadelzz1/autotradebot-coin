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
print('=' * 50)

try:
    upbit = pyupbit.Upbit(upbit_access_key, upbit_secret_key)

    order_list = upbit.get_order(
        ticker_or_uuid='KRW-IOST',
        state='wait',
        limit=100
    )

    print(order_list)
    
    list = order_list[0]
    pUuid = list["uuid"]
    pOrder = list["side"]
    pOrderType = list["ord_type"]
    pPrice = list["price"]
    pVolume = list["volume"]
    pRemainVolume = list["remaining_volume"]
    pMarket = list["market"]
    pOrderDate = list["created_at"]
    
    print(f'''
uuid: {pUuid}  =======================
- market    : {pMarket}
- order     : {pOrder}  ({pOrderType})
- price     : {pPrice}
- volume    : {pVolume}    [remain_volume: {pRemainVolume}]
- orderDate : {pOrderDate}
''')

except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('[Error]', e)