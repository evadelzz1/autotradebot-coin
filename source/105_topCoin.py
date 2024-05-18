from ConfigUpbit import upbit
import pandas as pd
import datetime
import time
import math
import pyupbit

# 종목 선정 : 거래량 상위 Top 5
def get_transaction_amount(interval, num):
    tickers = pyupbit.get_tickers("KRW")  # KRW 마켓의 티커 조회
    dic_ticker = {}
    
    for ticker in tickers:
        try:
            df = pyupbit.get_ohlcv(ticker, interval, count=20)
            volume_money = 0.0
            time.sleep(0.04)  # 요청 빈도를 줄이기 위해 지연 시간을 준다
            
        except Exception as e:
            print(f"Error processing ticker {ticker}: {e}")
            continue
        
        # 코인별 최근 7일간의 거래대금 합 : 순위가 바뀔 수 있으니 당일은 제외
        for i in range(1, 9):
            volume_money += df['close'].iloc[-i] * df['volume'].iloc[-i]  
        # volume_money = sum(df['close'].iloc[-i] * df['volume'].iloc[-i] for i in range(2, 9))

        dic_ticker[ticker] = volume_money

    # 거래대금이 많은 순으로 ticker 정렬
    sorted_ticker = sorted(dic_ticker.items(), key=lambda x: x[1], reverse=True)
    return [coin[0] for coin in sorted_ticker[:num]]


# -- Start --------------------------------------------------

print('Calculating... (최근 7일간 거래금액이 높은 Top 코인)')
tickers = get_transaction_amount("day", 5)	# 거래대금 상위 5개 코인 선정
print(tickers)
