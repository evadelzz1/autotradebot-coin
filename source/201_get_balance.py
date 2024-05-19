import pyupbit
from ConfigUpbit import upbit
        
try:
    ticker = "KRW-ETH"
    
    print("============ 현재 가격 (upbit.get_balance) ============")
    balance = upbit.get_balance()
    print(f'KRW : {balance:15.5f}')

    balance = upbit.get_balance(ticker=ticker)
    print(f'ETH : {balance:15.5f}\n')
    
    print("============ 평균매수가격 (upbit.get_avg_buy_price) ============")
    avgBuyPrice = upbit.get_avg_buy_price(ticker)   # 평균 매수가 조회
    print(f'ETH 평균매수가 : {format(avgBuyPrice, ",")}\n')
    
except Exception as e:                              # 예외가 발생했을 때 실행됨
    print('[Error]', e)