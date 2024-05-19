import pyupbit
from ConfigUpbit import upbit
import pandas as pd

ticker = 'KRW-ETH'

data = pyupbit.get_ohlcv(ticker=ticker, interval='day', count=125)
# print(data)

if data is None:
    print("[Error] Data not loading....")
    exit(1)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data, dtype="float", columns=["open", "high", "low", "close", "volume", "value"])
# print(df.tail())

# 단순이동평균(SMA)
SMA05 = df['close'].rolling(window=5).mean().iloc[-1].round(5)       # 5일 단순이동평균
SMA20 = df['close'].rolling(window=20).mean().iloc[-1].round(5)      # 20일 단순이동평균
SMA60 = df['close'].rolling(window=60).mean().iloc[-1].round(5)      # 60일 단순이동평균

print(f'=== 단순이동평균(SMA) ===========')
print(f'SMA05: {SMA05}')
print(f'SMA20: {SMA20}')
print(f'SMA60: {SMA60}\n')

# 지수이동평균(EMA)
EMA05 = df['close'].ewm(span=5, adjust=False).mean().iloc[-1].round(5)  # 5일 지수이동평균
EMA20 = df['close'].ewm(span=20, adjust=False).mean().iloc[-1].round(5) # 20일 지수이동평균
EMA60 = df['close'].ewm(span=60, adjust=False).mean().iloc[-1].round(5) # 20일 지수이동평균

print(f'=== 지수이동평균(EMA) ===========')
print(f'EMA05: {EMA05}')
print(f'EMA20: {EMA20}')
print(f'EMA60: {EMA60}\n')

# 가중이동평균(WMA)
WMA05 = df['close'].ewm(alpha=1/5, min_periods=5).mean().iloc[-1].round(5)      # 5일 가중이동평균
WMA20 = df['close'].ewm(alpha=1/20, min_periods=20).mean().iloc[-1].round(5)    # 20일 가중이동평균
WMA60 = df['close'].ewm(alpha=1/60, min_periods=60).mean().iloc[-1].round(5)    # 60일 가중이동평균

print(f'=== 가중이동평균(WMA) ===========')
print(f'WMA05: {WMA05}')
print(f'WMA20: {WMA20}')
print(f'WMA60: {WMA60}\n')



# reference:
#   https://skydance.tistory.com/38?category=974710
#   https://skydance.tistory.com/39?category=974710
#   https://skydance.tistory.com/40?category=974710
#   https://superhky.tistory.com/282
#   https://superhky.tistory.com/253
#   https://superhky.tistory.com/245