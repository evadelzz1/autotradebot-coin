from ConfigUpbit import upbit
import CustomModule as cm
import time
from datetime import datetime

####################################################
# buy_limit_order  : 지정가 매수
# sell_limit_order : 지정가 매도
####################################################

lists = []
lists.append('KRW-IOST, 11.92, 450')    # 최소 주문 금액 : 5,000 WON
lists.append('KRW-IOST, 11.70, 450')
print(lists)

orderlists = []
resultlists = []
uuidLists = []

print("\n\n=======  buy order  =======================")
for i in lists:
    orderlists = i.split(',')

    orderTicker = i.split(',')[0]
    orderPrice = float(i.split(',')[1])
    orderCount = int(i.split(',')[2])
    
    # 지정가 매수 : buy_limit_order(티커 이름, 주문할 가격, 수량)
    res = upbit.buy_limit_order(orderTicker, orderPrice, orderCount)
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

print("\n\n========= command =========")
for i in resultlists:
    print(f"uuidLists.append('{i['uuid']}')")


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


# reference:
#   https://coderyoon.tistory.com/13

