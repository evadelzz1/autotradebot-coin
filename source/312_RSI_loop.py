import pyupbit
from ConfigUpbit import upbit
import pandas as pd
import datetime
import time

def rsi(ohlc: pd.DataFrame, period: int = 14):
    delta = ohlc["close"].diff()
    ups, downs = delta.copy(), delta.copy()
    ups[ups < 0] = 0
    downs[downs > 0] = 0

    AU = ups.ewm(com = period-1, min_periods = period).mean()
    AD = downs.abs().ewm(com = period-1, min_periods = period).mean()
    RS = AU/AD

    return pd.Series(100 - (100/(1 + RS)), name = "RSI")  


def rsi2(df, period=14):
    df['change'] = df['close'].diff()   # 전일 대비 변동 평균

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

while True:
    ticker = 'KRW-ETH'

    data = pyupbit.get_ohlcv(ticker=ticker, interval='minute5')
    current_rsi = rsi(data, 14).iloc[-1]
    current_rsi2 = rsi2(data, 14).iloc[-1]
    
    formatedNow = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    print(f'[{formatedNow}] RSI: {current_rsi:.5f},  RSI2: {current_rsi2:.5f}')
    time.sleep(3)



# reference:
#   https://rebro.kr/139
#   https://rebro.kr/140
#   https://rebro.kr/144