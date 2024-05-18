from ConfigUpbit import upbit
import CustomModule as cm
import time
from datetime import datetime

lists = []
lists.append('KRW-IOST, 11.85, 450')    # 최소 주문 금액 : 5,000 WON
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


print("\n\n\n...")
print("Waiting 5 sec for Cancel.....")
print("...\n\n\n")
time.sleep(5)

cancelResultlists = []

print("\n\n=======  cancel order  ====================")
for i in uuidLists:
    res = upbit.cancel_order(i)
    cancelResultlists.append(res)
    print(i, " : ", res, "\n")

print("\n\n=======  cancel detail  ===================")
for i in cancelResultlists:
    print(i)

print("\n\n=======  cancel uuid  =====================")
for i in cancelResultlists:
    # print("[", i['uuid'], "] ", i)
    print(f'uuid: {i["uuid"]}')
