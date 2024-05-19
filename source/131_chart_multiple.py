import pyupbit
import matplotlib.pyplot as plt

# 데이터 가져오기
data = pyupbit.get_ohlcv("KRW-ETH", interval='day', count=100)

# 그래프 그리기
plt.rcParams["axes.grid"] = True
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.formatter.limits"] = -10000, 10000

plt.plot(data.index, data["close"], label="Close Price", linestyle='-', color="black")
plt.plot(data.index, data["open"], label="Open Price", linestyle='--', color="blue")
plt.plot(data.index, data["high"], label="High Price", linestyle='-.', color="green")
plt.plot(data.index, data["low"], label="Low Price", linestyle=':', color="red")

# 그래프 타이틀, 라벨, 범례 추가
plt.title("ETH Price")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Price/Volume")

# 그래프 출력
plt.show()


# reference:
#   https://wikidocs.net/113767
