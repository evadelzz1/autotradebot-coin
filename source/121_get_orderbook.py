import pyupbit
import pprint

# 주문 정보 가져오기
orderbooks = pyupbit.get_orderbook('KRW-ETH')

total_ask_size = orderbooks['total_ask_size']
total_bid_size = orderbooks['total_bid_size']

print('#' * 50)
pprint.pprint(orderbooks)   # https://wikidocs.net/105471

print('#' * 50)
print('매도호가 총합:', total_ask_size)
print('매수호가 총합:', total_bid_size)

print('#' * 50)
def print_orderbook(orderbooks):
    print(f"{'Ask Price':<10}{'Ask Size':<15}{'Bid Price':<10}{'Bid Size':<15}")
    print("-" * 50)
    for unit in orderbooks['orderbook_units']:
        print(f"{unit['ask_price']:<10}{unit['ask_size']:<15}{unit['bid_price']:<10}{unit['bid_size']:<15}")

print_orderbook(orderbooks)

# reference:print(index.length)
#   https://coderyoon.tistory.com/10


####################################################
# Syntax)
# pyupbit.get_orderbook(ticker, limit_info=True/False)
#   - ticker = 호가 정보를 뽑을 코인의 ticker. 또는 ticker들을 담은 list. 
#              (1개 이상의 ticker를 동시에 전달하려면 list의 형태로 전달해도 무방합니다.)
#   - limit_info = 제한 정보를 표시한다 Ture, 표시하지 않는다 False (기본값은 False 입니다.)
#
####################################################