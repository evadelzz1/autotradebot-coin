import pyupbit
import matplotlib.pyplot as plt

# plt.rcParams["axes.grid"] = True
plt.rcParams["figure.figsize"] = (12,6)
plt.rcParams["axes.formatter.limits"] = -10000, 10000

df = pyupbit.get_ohlcv("KRW-ETC", interval='day', count=100)
print(df)

# 가격 차트 그리기
df["close"].plot()
plt.show()


# reference:
#   https://wikidocs.net/113767