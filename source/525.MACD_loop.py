from dotenv import load_dotenv
import os
import time
import datetime as dt
import pandas as pd
import pyupbit

if not load_dotenv():    # load .env
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit_access_key = os.getenv("UPBIT_ACCESS_KEY")
upbit_secret_key = os.getenv("UPBIT_SECRET_KEY")

print(f'### [Config Upbit] ACCESS_KEY: {upbit_access_key[0:10]}...')
print(f'### [Config Upbit] SECRET_KEY: {upbit_secret_key[0:10]}...')
print('=' * 50)


def get_SMA_MACD(_ticker) :
    # data = pyupbit.get_ohlcv(ticker=_ticker, interval='day', count=200)
    data = pyupbit.get_ohlcv(ticker=_ticker, interval='day', count=100)
    # data = pyupbit.get_ohlcv(ticker=_ticker, interval='minutes1', count=116)
    print(data)
    
    if data is None:
        print("[Error] Data not loading....")
        exit(1)
    
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data, dtype="float", columns=["open", "high", "low", "close", "volume", "value"])
    # print(df.tail())
    
    dataSet = df.loc['2023':'2024', ['close']]
    # print(dataSet)

    # dataSet["ema_short"] = dataSet["close"].ewm(12).mean()          # 12일간의 지수 이동평균
    # dataSet["ema_long"] = dataSet["close"].ewm(26).mean()           # 26일간의 지수 이동평균
    # dataSet["macd"] = dataSet["ema_short"] - dataSet["ema_long"]    # MACD = ShortEMA-LongEMA
    # dataSet["signal"] = dataSet["macd"].ewm(9).mean()               # Signal = MACD 9일 지수 이동평균선
    # dataSet["oscillator"] = dataSet["macd"] - dataSet["signal"]     # Oscillator = MACD - Signal

    ShortEMA = dataSet["close"].ewm(12).mean()      # 12일간의 지수 이동평균
    LongEMA = dataSet["close"].ewm(26).mean()       # 26일간의 지수 이동평균
    MACD = ShortEMA - LongEMA                       # MACD = ShortEMA-LongEMA
    Signal = MACD.ewm(9).mean()                     # Signal = MACD 9일 지수 이동평균선
    Oscillator = MACD - Signal                      # Oscillator = MACD - Signal
    
    SMA01 = df['close'].rolling(window=3).mean()    # 3일 이동 평균
    SMA02 = df['close'].rolling(window=10).mean()   # 10일 이동 평균
    SMA03 = df['close'].rolling(window=50).mean()   # 50일 이동 평균

    return (SMA01, SMA02, SMA03, MACD, Signal)


upbit = pyupbit.Upbit(upbit_access_key, upbit_secret_key)

coin = 'USDT-BTC'

# get_SMA_MACD(coin)
# exit(1)
    
while True:
    try:
        now = dt.datetime.now()        
        start_time = now - dt.timedelta(hours=1)
        end_time = now + dt.timedelta(hours=10)
        formatedNow = dt.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        if start_time < now < end_time:
            SMA01, SMA02, SMA03, MACD, Signal = get_SMA_MACD(coin)

            print(f'[{formatedNow}] MACD: {MACD.iloc[-1]:15.5f}, SMA01: {SMA01.iloc[-1]:15.5f}, SMA02: {SMA02.iloc[-1]:15.5f}, SMA03: {SMA03.iloc[-1]:15.5f}, Signal: {Signal.iloc[-1]:15.5f}')
        
        time.sleep(5)
        
    except Exception as e:
        print('[Error]', e)
        time.sleep(1)
        

# reference:
#   https://anpigon.tistory.com/232
#   https://superhky.tistory.com/235
#   https://superhky.tistory.com/244
#   https://superhky.tistory.com/447
#   https://blog.naver.com/jun652006/222316267357
