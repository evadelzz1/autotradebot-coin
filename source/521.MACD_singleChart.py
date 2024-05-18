import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define the API endpoint URL
url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=100"

# Send a GET request to the API endpoint and retrieve the data
response = requests.get(url)
data = response.json()

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data, dtype="float", columns=["open time", "open", "high", "low", "close", "volume", "close time", "quote asset volume", "number of trades", "taker buy base asset volume", "taker buy quote asset volume", "ignore"])
df['date'] = pd.to_datetime(df['open time'], unit='ms')
df.set_index('date', inplace=True)

# Print the data
print(df.tail())


dataSet = df.loc['2023':'2024', ['close']]
print(dataSet)

dataSet["ema_short"] = dataSet["close"].ewm(12).mean()          # 12일간의 지수 이동평균
dataSet["ema_long"] = dataSet["close"].ewm(26).mean()           # 26일간의 지수 이동평균
dataSet["macd"] = dataSet["ema_short"] - dataSet["ema_long"]    # MACD = ShortEMA-LongEMA
dataSet["signal"] = dataSet["macd"].ewm(9).mean()               # Signal = MACD 9일 지수 이동평균선
dataSet["oscillator"] = dataSet["macd"] - dataSet["signal"]     # Oscillator = MACD - Signal

# Plot Close, EMA Short, and EMA Long
plt.figure(figsize=(12, 8))

plt.plot(dataSet.index, dataSet["close"], label='Close')
plt.plot(dataSet.index, dataSet["ema_short"], label='EMA Short')
plt.plot(dataSet.index, dataSet["ema_long"], label='EMA Long')

plt.legend()
plt.title('Close Price and Exponential Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()


# Plot MACD
plt.figure(figsize=(12, 8))
dataSet["macd"].plot()
plt.axhline(0, linestyle='--')
plt.legend()
plt.show()

# Plot Oscillator
plt.figure(figsize=(12, 8))
plt.bar(dataSet.index, dataSet['oscillator'])
plt.show()

exit(1)




# 12일, 26일에 대한 지수이동평균과 종가 차트
dataSet[["close", "ema_short", "ema_long"]].plot(figsize=(12, 8))
plt.show()
exit(1)

# MACD 차트
dataSet["macd"].plot(figsize=(12, 8))
plt.axhline(0, linestyle='--')
plt.show()
exit(1)

# Oscillator 차트 : MACD - Signal  (여기서, Signal은 MACD 9일 지수 이동평균선)
plt.figure(figsize=(15, 5))
plt.bar(dataSet.index, dataSet['oscillator'])
plt.show()

# reference:
#   https://anpigon.tistory.com/232
#   https://blog.naver.com/kimwh253967/223105802259?isInf=true&trackingCode=external

