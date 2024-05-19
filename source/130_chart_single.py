import pyupbit
import matplotlib.pyplot as plt

data = pyupbit.get_ohlcv("KRW-ETC", interval='day', count=100)
print(data)

# 가격 차트 그리기
plt.rcParams["axes.grid"] = True
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.formatter.limits"] = -10000, 10000

data["close"].plot()

# 그래프 타이틀, 라벨, 범례 추가
plt.title("ETH Price")
plt.legend(fontsize = 13) # 범례 표시

# 그래프 출력
plt.show()



# reference:
#   https://wikidocs.net/113767