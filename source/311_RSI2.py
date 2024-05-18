from ConfigUpbit import upbit
import pandas as pd
import datetime
import time
import math
import pyupbit


# -- Functions --------------------------------------------------

# RSI 지표를 구하는 함수
def get_rsi(df, period=14):

    # 전일 대비 변동 평균
    df['change'] = df['close'].diff()

    # 상승한 가격과 하락한 가격
    df['up'] = df['change'].apply(lambda x: x if x > 0 else 0)
    df['down'] = df['change'].apply(lambda x: -x if x < 0 else 0)

    # 상승 평균과 하락 평균
    df['avg_up'] = df['up'].ewm(alpha=1/period).mean()
    df['avg_down'] = df['down'].ewm(alpha=1/period).mean()

    # 상대강도지수(RSI) 계산
    df['rs'] = df['avg_up'] / df['avg_down']
    df['rsi'] = 100 - (100 / (1 + df['rs']))
    RSI = df['rsi']

    return RSI

# 현재 보유한 원화 자산 확인
def get_myBalance(balances, money_rate = 0.012):    # 투자 비중 (money_rate)
    myMoney = float(balances[0]['balance'])         # 현재 보유한 원화 자산
    money = myMoney * money_rate                    # 매수에 할당할 비용
    money = math.floor(money)		                # 소수점 버림

    return money

# 이미 매수한 코인인지 확인
def has_coin(ticker, balances):
    result = False
    
    for coin in balances:
        coin_ticker = coin['unit_currency'] + "-" + coin['currency']
        
        if ticker == coin_ticker:
            result = True
            
    return result


# -- Start --------------------------------------------------

ticker = 'KRW-BTC'

balances = upbit.get_balances()

data = pyupbit.get_ohlcv(ticker=ticker, interval="day")    # 코인의 일봉 정보

money = get_myBalance(balances)
print(f'1회 투자금액(원금의 0.012%): {money}')

money = get_myBalance(balances, money_rate=0.3)
print(f'1회 투자금액(원금의 0.3%): {money}\n')

yesterday_rsi = get_rsi(data, 14).iloc[-2]      # 하루 전의 RSI14 값을 이용
print(f'어제 기준 RSI: {yesterday_rsi:.5f}')

today_rsi = get_rsi(data, 14).iloc[-1] 	        # 당일의 RSI14 값을 이용
print(f'당일 기준 RSI: {today_rsi:.5f}\n')

# 이미 매수한 코인은 추가로 매수할 수 없으니 미리 비트코인의 보유 유무를 확인   
if has_coin(ticker, balances):
    # 매도 조건 충족
    if yesterday_rsi > 70:
        amount = upbit.get_balance(ticker)                  # 현재 비트코인 보유 수량	  
        result = upbit.sell_market_order(ticker, amount)    # 시장가에 매도 
        balances = upbit.get_balances()                     # 매도를 했으니 잔고를 최신화!
        print(f'[Sell] {result["uuid"]}')

else:
    # 매수 조건 충족
    if yesterday_rsi < 30:
        result = upbit.buy_market_order(ticker, money)      # 시장가에 비트코인을 가진 원화만큼 매수
        balances = upbit.get_balances()                     # 매수를 했으니 잔고를 최신화!
        print(f'[Buy] {result["uuid"]}')




# reference:
#   https://rebro.kr/139
#   https://rebro.kr/140
#   https://me-in-journey.com/entry/업비트자동매매-RSI-지표를-이용한-자동매매-프로그램-만들기-1


# RSI 지표 (상대강도지수, Relative Strength Index)
# : 현재 상태가 과매도인지 과매수인지 보여주는 지표
#   - 30이하에서는 매수 신호 (과하게 팔고있으니 곧 상승 예상) -> 선물 거래 : 오를거니 롱포지션
#   - 70이상에서는 매도 신호 (과하게 사고있으니 곧 하락 예상) -> 선물 거래 : 내릴거니 숏포지션
#
# : 천장과 바닥이 보이는 횡보장에서는 잘 맞아떨어지는 지표
#   BUT 대세 하락장이나 상승장에서 이 지표를 맹신했다가는 손해로 이어질 수 있음 
#   - 30이하라면 앞으로 올라야 되지만 계속 하락(하락장)
#   - 70이상이라면 떨어져야 되는데 계속 오르는 경우(상승장)

