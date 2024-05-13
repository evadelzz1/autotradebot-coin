import pyupbit
import pandas as pd

df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="day", count=10)

print(f'\n========================== closed mean ==========================')
print(df['close'].mean())

print(f'\n==================== raw data (close, volume) ===================')
print(df[["close", "volume"]])

print(f'\n======================== raw data (all) ========================')
print(df)