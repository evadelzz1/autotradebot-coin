from ConfigUpbit import upbit

orderlists = []
resultlists = []
uuidLists = []

ticker = 'KRW-LOOM'

buyResult = upbit.buy_market_order(ticker=ticker, price=6000)
sellResult = upbit.sell_market_order(ticker=ticker, volume=44)

print("\n\n=======  buy order  =======================")
print(f"## Buy Result: ", buyResult['uuid'], "\n")
print(f"{buyResult}\n\n")

print("\n\n=======  sell order  ======================")
print(f"## Sell Result: ", sellResult['uuid'], "\n")
print(f"{sellResult}\n\n")



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