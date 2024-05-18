from ConfigUpbit import upbit
import time
import math
import datetime as dt
import pyupbit

ticker = 'KRW-LOOM'
amountPerBuy = 6000
loopWaitTime = 30   # seconds
actionCount = 0
initialAssets = upbit.get_balance()

while True:
    try:
        if initialAssets < amountPerBuy:
            break

        currentPrice = pyupbit.get_current_price(ticker)
        # print(f"Current Price : {currentPrice}")
        
        buyResult = upbit.buy_market_order(ticker=ticker, price=amountPerBuy)
        # print(f"{buyResult}\n\n")

        # waiting order process....
        time.sleep(3)

        # 매수된 토큰수량 확인
        balance = upbit.get_balance(ticker=ticker)
        sellCount = math.floor(balance)
        # print(f"{ticker_} : {balance:15.5f} : {sellCount}")

        # 지정가 매도 : sell_limit_order(티커 이름, 판매 희망 가격, 수량)
        sellPrice = round(currentPrice * 1.03, 1)
        sellResult = upbit.sell_limit_order(ticker, sellPrice, sellCount)
        # print(f"{sellResult}\n\n")

        actionCount += 1
        initialAssets -= amountPerBuy
        
        formatedNow = dt.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print(f'[{formatedNow}] [{actionCount:04d}] Token: {ticker}, BuyPrice : {currentPrice}, SellPrice: {sellPrice}, Count: {sellCount}')

        time.sleep(loopWaitTime)
        
    except Exception as e:
        print('[Error]', e)
        time.sleep(1)


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