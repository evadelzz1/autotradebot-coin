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

tickers = get_transaction_amount("day", 5)	# 거래대금 상위 5개 코인 선정
print(tickers)

balances = upbit.get_balances()
money = get_myBalance(balances)
print(f'1회 투자금액(원금의 0.012%): {money}')

money = money / len(tickers)		# 각각의 코인에 공평하게 자본 분배
print(f'코인당 1회 투자금액: {money}')

for ticker in tickers:
    data = pyupbit.get_ohlcv(ticker=ticker, interval="day")    # 코인의 일봉 정보

    before_rsi14 = get_rsi(data, 14).iloc[-2]                   # 작일 RSI14
    rsi14 = get_rsi(data, 14).iloc[-1]                          # 당일 RSI14

    # 이미 매수한 코인은 추가로 매수할 수 없으니 미리 비트코인의 보유 유무를 확인
    if has_coin(ticker, balances):
        # 매도 조건 수정
        if before_rsi14 > 70 and rsi14 < 70:
            amount = upbit.get_balance(ticker)                  # 현재 비트코인 보유 수량	  
            result = upbit.sell_market_order(ticker, amount)    # 시장가에 매도 
            balances = upbit.get_balances()                     # 매도를 했으니 잔고를 최신화!
            print(f'[Sell] {result["uuid"]}')

    else:
        # 매수 조건 수정
        if before_rsi14 < 30 and rsi14 > 30:
            result = upbit.buy_market_order(ticker, money)      # 시장가에 비트코인을 가진 원화만큼 매수
            balances = upbit.get_balances()                     # 매수를 했으니 잔고를 최신화!
            print(f'[Buy] {result["uuid"]}')


# reference:
#   https://me-in-journey.com/entry/업비트자동매매-RSI-지표를-이용한-자동매매-프로그램-만들기-1
#   https://me-in-journey.com/entry/업비트자동매매-RSI-지표를-이용한-자동매매-프로그램-만들기-2
#   https://rebro.kr/139
#   https://rebro.kr/140


# RSI 지표 (상대강도지수, Relative Strength Index)
# : 현재 상태가 과매도인지 과매수인지 보여주는 지표
#   - 30이하에서는 매수 신호 (과하게 팔고있으니 곧 상승 예상) -> 선물 거래 : 오를거니 롱포지션
#   - 70이상에서는 매도 신호 (과하게 사고있으니 곧 하락 예상) -> 선물 거래 : 내릴거니 숏포지션
#
# : 천장과 바닥이 보이는 횡보장에서는 잘 맞아떨어지는 지표
#   BUT 대세 하락장이나 상승장에서 이 지표를 맹신했다가는 손해로 이어질 수 있음 
#   - 30이하라면 앞으로 올라야 되지만 계속 하락(하락장)
#   - 70이상이라면 떨어져야 되는데 계속 오르는 경우(상승장)

