import pyupbit

df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="minute1", count=60)

df['open'] = df['open'].resample('2T').first()
df['high'] = df['high'].resample('2T').max()
df['low'] = df['low'].resample('2T').min()
df['close'] = df['close'].resample('2T').last()
df['volume'] = df['volume'].resample('2T').sum()
df = df.dropna()

print(df)

# 리샘플링 (resample) : https://wikidocs.net/158101

# resample에 'nT'의 값을 주면 n개의 값을 자동으로 선택한다. 
# 각 선택된 값에서 시가 중 첫 값, 고가 중 높은 값, 저가 중 낮은 값, 종가 중 마지막 값, 거래량의 합을 각 열에 값으로 주고, 
# NaN 값을 제거하는 dropna() 메소드로 2분당 시세를 구했다.
