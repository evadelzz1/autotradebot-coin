import pyupbit
from ConfigUpbit import upbit
import pandas as pd
import matplotlib.pyplot as plt

def get_SMA_MACD(_ticker) :
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
    axes[1].set_ylim(-7000, 7000)   # Y 축 범위 설정
    dataSet[["macd", "signal"]].plot(ax=axes[1])
    axes[1].axhline(0, color='gray', linestyle='--')
    axes[1].set_title('MACD')

    # Plot Oscillator
    axes[2].set_ylim(-3000, 3000)   # Y 축 범위 설정
    axes[2].bar(dataSet.index, dataSet['oscillator'])
    axes[2].axhline(0, color='gray', linestyle='--')
    axes[2].set_title('Oscillator')

    plt.tight_layout()
    plt.show()

def main():
    coin = 'USDT-BTC'
    get_SMA_MACD(coin)

if __name__ == "__main__":
    main()


# reference:
#   https://anpigon.tistory.com/232
#   https://superhky.tistory.com/235
#   https://superhky.tistory.com/244
#   https://superhky.tistory.com/447
#   https://blog.naver.com/jun652006/222316267357
