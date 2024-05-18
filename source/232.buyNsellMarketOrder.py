from ConfigUpbit import upbit
import time
import math
import datetime as dt
import pyupbit

ticker_ = 'KRW-LOOM'

amountPerBuy = 10000

currentPrice = pyupbit.get_current_price(ticker_)
# print(f"Current Price : {currentPrice}")

buyResult = upbit.buy_market_order(ticker=ticker_, price=amountPerBuy)

# print("\n\n=======  buy order  =======================")
# print(f"## Buy Result: ", buyResult['uuid'], "\n")
# print(f"{buyResult}\n\n")


time.sleep(3)   # waiting order process....


balance = upbit.get_balance(ticker=ticker_)
sellCount = math.floor(balance)
# print(f"{ticker_} : {balance:15.5f} : {sellCount}")

# 지정가 매도 : sell_limit_order(티커 이름, 판매 희망 가격, 수량)
sellPrice = round(currentPrice * 1.03, 1)
sellResult = upbit.sell_limit_order(ticker_, sellPrice, sellCount)
# print(sellPrice)
# print("\n\n=======  sell order  =======================")
# print(f"{sellResult}\n\n")
# print(f"## Sell Result: ", sellResult['uuid'], "\n")
formatedNow = dt.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
print(f'[{formatedNow}] Token: {ticker_}, BuyPrice : {currentPrice}, SellPrice: {sellPrice}, Count: {sellCount}')




# print("\n\n=======  sell order  ======================")
# print(f"## Sell Result: ", sellResult['uuid'], "\n")
# print(f"{sellResult}\n\n")



####################################################
# buy_market_order  : 시장가 매수
# sell_market_order : 시장가 매도
####################################################
# Syntax)
# buy_market_order(ticker='KRW-ETH', price=100000)
#   - ticker = 시장가에 매수할 ticker
#   - price  = 매수할 양(얼마치를 매수할지)
#
# sell_market_order(ticker='KRW-ETH', volume=1.5)
#   - ticker = 시장가에 매도할 ticker
#   - volume = 시장가에 매도할 개수
####################################################

####################################################
# buy_limit_order  : 지정가 매수
# sell_limit_order : 지정가 매도
####################################################
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