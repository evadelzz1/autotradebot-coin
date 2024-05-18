from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt
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

_ticker = 'USDT-BTC'

data = pyupbit.get_ohlcv(ticker=_ticker, interval='day', count=200)
# data = pyupbit.get_ohlcv(ticker=_ticker, interval='day', count=100)
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

plt.figure(figsize=(12, 5))  # 그래프 윈도우 크기 조정

dataSet["Price"] = dataSet["close"].plot(label="Price", linestyle='-', color='black')                           # 가격 (실선, 검정색)
dataSet["Day5"] = dataSet["close"].rolling(window=5).mean().plot(label="MA5", linestyle='--', color='blue')     # 5일 이동 평균 (점선, 파란색)
dataSet["Day20"] = dataSet["close"].rolling(window=20).mean().plot(label="MA20", linestyle='-.', color='green') # 20일 이동 평균 (파선, 녹색)
dataSet["Day60"] = dataSet["close"].rolling(window=60).mean().plot(label="MA60", linestyle=':', color='red')    # 60일 이동 평균 (점선, 붉은색)

plt.legend(fontsize = 13) # 범례 표시
plt.tight_layout()
plt.show()


# reference:
#   https://anpigon.tistory.com/220
#   https://anpigon.tistory.com/225?category=1070983 : 볼린저 밴드(Bollinger Bands)
#   https://anpigon.tistory.com/221?category=1070983 : 이동평균선 돌파 전략 백테스팅
#   https://anpigon.tistory.com/217?category=1070983 : [비트코인 자동매매] 상승장 알리미 스케쥴러 적용하기
#   https://anpigon.tistory.com/216?category=1070983 : [비트코인 자동매매] 상승장 알리미 슬랙으로 발송하기


