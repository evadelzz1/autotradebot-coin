from dotenv import load_dotenv
import os
import pandas as pd
import datetime
import time
import pyupbit

if not load_dotenv():    # load .env
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit_access_key = os.getenv("UPBIT_ACCESS_KEY")
upbit_secret_key = os.getenv("UPBIT_SECRET_KEY")

print(f'### [Config Upbit] ACCESS_KEY: {upbit_access_key[0:10]}...')
print(f'### [Config Upbit] SECRET_KEY: {upbit_secret_key[0:10]}...')
print('=' * 50)

upbit = pyupbit.Upbit(upbit_access_key, upbit_secret_key)

ticker = 'KRW-ETH'

data = pyupbit.get_ohlcv(ticker=ticker, interval='day')

if data is None:
    print("[Error] Data not loading....")
    exit(1)

print(data)

# RSI 지표 공식 (https://rebro.kr/139)
#
# 주어진 기간의 모든 날의 주가에 대해서
# 1. 가격이 전일 가격보다 상승한 날의 상승분을 U(up) 값이라고 하고, 하락한 날의 하락분은 D(down) 값이라고 한다. 
# 2. U와 D의 평균값을 각각 AU(average ups), AD(average downs)이라고 한다. 
# 3. AU를 AD로 나눈 값을 RS(relative strength) 값이라고 한다. RS가 크다는 것은 일정 기간 동안 하락한 폭보다 상승한 폭이 더 크다는 것을 의미한다.
# 4. RSI = RS / (1+ RS)을 통해서 RSI를 구한다. 보통 RSI는 백분율로 나타내므로 최종적으로 식에 100을 곱해준다. 

closedata = data["close"]   # 종가 데이터만 가져옴
print(closedata)

delta = closedata.diff()    # 당일 종가와 전일 종가를 비교하여 차이를 delta 에 저장함
print(delta)

ups, downs = delta.copy(), delta.copy()
ups[ups < 0] = 0
downs[downs > 0] = 0

print(ups)
print(downs)

period = 14
au = ups.ewm(com = period-1, min_periods=period).mean()
ad = downs.abs().ewm(com = period-1, min_periods=period).mean()

print(au)
print(ad)

RS = au/ad
RSI = pd.Series(100 - (100/(1+RS)))
print(RSI)


# reference:
#   https://rebro.kr/139
#   https://rebro.kr/140
#   https://rebro.kr/144
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

