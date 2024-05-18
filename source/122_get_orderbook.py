import pyupbit

# 개별 가격 조회
price_KRW = pyupbit.get_current_price(["KRW-ETH"])
print(f"\n##########  ETH : {int(price_KRW):>10,} 원 ####################\n")

# 호가 조회
orderbooks = pyupbit.get_orderbook('KRW-ETH')

# orderbook_units의 매수 가격과 수량을 bid 리스트에, 매도 가격과 수량을 ask 리스트에 저장
bid = [(unit['bid_price'], unit['bid_size'], 'bid') for unit in orderbooks['orderbook_units']]
ask = [(unit['ask_price'], unit['ask_size'], 'ask') for unit in orderbooks['orderbook_units']]

# bid와 ask 리스트를 합침
merged_list = bid + ask

# 가격을 기준으로 소팅 (역순))
sorted_list = sorted(merged_list, key=lambda x: x[0], reverse=True)
# print(sorted_list)

# 결과 출력
print(f"            bid |     price    |             ask")
print("-" * 50)
for item in sorted_list:
    # print(item)
    bid_size = f"{item[1]:15.5f}" if item[2] == 'bid' else '        0.00000'
    ask_size = f"{item[1]:15.5f}" if item[2] == 'ask' else '        0.00000'
    # print(f"{bid_size} | {int(item[0]):>10,} | {ask_size}")
    price = f"{int(item[0]):>10,} ◀" if int(price_KRW) == int(item[0]) else f"{int(item[0]):>10,}  "
    print(f"{bid_size} | {price} | {ask_size}")
print("-" * 50)

                      
####################################################
# Syntax)
# pyupbit.get_orderbook(ticker, limit_info=True/False)
#   - ticker = 호가 정보를 뽑을 코인의 ticker. 또는 ticker들을 담은 list. 
#              (1개 이상의 ticker를 동시에 전달하려면 list의 형태로 전달해도 무방합니다.)
#   - limit_info = 제한 정보를 표시한다 Ture, 표시하지 않는다 False (기본값은 False 입니다.)
#
####################################################