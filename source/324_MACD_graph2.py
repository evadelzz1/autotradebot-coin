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

    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    # Plot Close, EMA Short, and EMA Long
    dataSet[["close", "ema_short", "ema_long"]].plot(ax=axes[0])
    axes[0].set_title('Close, EMA Short, and EMA Long')

    # Plot MACD
    dataSet[["macd", "signal"]].plot(ax=axes[1])
    axes[1].axhline(0, color='gray', linestyle='--')
    axes[1].bar(dataSet.index, dataSet['oscillator'])
    
    axes[1].set_title('MACD, Signal, Oscillator')
    axes[1].set_xlabel('Date')    

    # Y 축의 0점을 가운데로 설정하기 : Set y-axis limits
    y_min, y_max = axes[1].get_ylim()
    if abs(y_min) > abs(y_max):
        y_max = abs(y_min)
    else:
        y_min = -abs(y_max)
    axes[1].set_ylim(y_min, y_max)
    

    # 그래프 타이틀 추가
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
