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


fig, axes = plt.subplots(3, 1, figsize=(12, 8))

# Plot Close, EMA Short, and EMA Long
dataSet[["close", "ema_short", "ema_long"]].plot(ax=axes[0])
axes[0].set_title('Close, EMA Short, and EMA Long')

# Plot MACD
axes[1].set_ylim(-5000, 5000)    # Y 축 범위 설정
dataSet["macd"].plot(ax=axes[1])
axes[1].axhline(0, color='gray', linestyle='--')
axes[1].set_title('MACD')


# Plot Oscillator
axes[2].set_ylim(-2000, 2000)   # Y 축 범위 설정
axes[2].bar(dataSet.index, dataSet['oscillator'])
axes[2].axhline(0, color='gray', linestyle='--')
axes[2].set_title('Oscillator')

plt.tight_layout()
plt.show()


# reference:
#   https://anpigon.tistory.com/232


