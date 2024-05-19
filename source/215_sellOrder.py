from ConfigUpbit import upbit
import CustomModule as cm
from datetime import datetime
import time

####################################################
# buy_limit_order  : 지정가 매수
# sell_limit_order : 지정가 매도
####################################################

lists = []
lists.append('KRW-IOST, 13.00, 450')
print(lists)

orderlists = []
resultlists = []
uuidLists = []

print("\n\n=======  sell order  =======================")
for i in lists:
    orderlists = i.split(',')

    orderTicker = i.split(',')[0]
    orderPrice = float(i.split(',')[1])
    orderCount = int(i.split(',')[2])
    
    # 지정가 매도 : sell_limit_order(티커 이름, 판매 희망 가격, 수량)
    res = upbit.sell_limit_order(orderTicker, orderPrice, orderCount)
    print(orderlists, " : ", res, "\n")

    resultlists.append(res)
    uuidLists.append(res['uuid'])

    time.sleep(1)

print("\n\n=======  order detail  ====================")
for i in resultlists:
    print(i)

print("\n\n=======  order uuid (for cancel)  =========")
for i in uuidLists:
    print(f"uuid: {i}")



####################################################
# buy_limit_order  : 지정가 매수
# sell_limit_order : 지정가 매도
#
# Syntax)
# buy_limit_order(ticker='KRW-ETH', price=3000000, volume=0.003)
#   - ticker = 구매를 원하는 코인의 ticker
#   - price  = 구매하고 싶은 가격
#   - volume = 구매할 개수
#
# sell_limit_order(ticker='KRW-ETH', price=3000000, volume=0.003)
#   - ticker = 판매를 원하는 코인의 ticker
#   - price = 판매하고 싶은 가격
#   - volume = 판매할 개수
####################################################
