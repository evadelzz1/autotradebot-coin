import pyupbit

data = pyupbit.get_ohlcv("KRW-ETH", "day", 10)
#data = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="day", count=10)

print(f'\n======================== raw data (all) ========================')
print(data)

df = data[["close", "volume"]]

print(f'\n==================== raw data (close, volume) ===================')
print(df)

print(f'\n==================== closed mean (by pandas) ====================')
print('mean     : ', df['close'].mean())
print('Min      : ', df['close'].min())     # 최저가
print('Min Date : ', df['close'].idxmin())  # 최저가 날짜
print('Max      : ', df['close'].max())     # 최고가
print('Max Date : ', df['close'].idxmax())  # 최고가 날짜

# reference:
#   https://coderyoon.tistory.com/8
