import pyupbit
from ConfigUpbit import upbit

ticker = 'KRW-LOOM'

try:
    order_list = upbit.get_order(ticker_or_uuid=ticker, state='wait', limit=100)

    for index, order in enumerate(order_list):

        list = order_list[index]
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
        
        print(f"Index: {index}, Order: {order}")

except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('[Error]', e)