import pyupbit
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (12, 6)

# 데이터 가져오기
df = pyupbit.get_ohlcv("KRW-ETH", interval='day', count=100)

# 그래프 그리기
plt.plot(df.index, df["close"], label="Close Price")
plt.plot(df.index, df["open"], label="Open Price")
plt.plot(df.index, df["high"], label="High Price")
plt.plot(df.index, df["low"], label="Low Price")

# 그래프 타이틀, 라벨, 범례 추가
plt.title("ETH Price")
plt.xlabel("Date")
plt.ylabel("Price/Volume")
plt.legend()

# 그래프 출력
plt.show()


# reference:
#   https://wikidocs.net/113767