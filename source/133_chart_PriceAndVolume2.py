import pyupbit
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (12, 6)

# 데이터 가져오기
data = pyupbit.get_ohlcv("KRW-ETH", interval='day', count=100)

# 그래프 그리기
plt.rcParams["axes.grid"] = False
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.formatter.limits"] = -10000, 10000

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Close', color=color)
ax1.plot(data.index, data['close'], color=color, label='Close Price')
ax1.tick_params(axis='y', labelcolor=color)

# 오른쪽 Y 축을 위한 별도의 축 생성
ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Volume', color=color)
ax2.plot(data.index, data['volume'], color=color, label='Volume', linestyle=':')
ax2.tick_params(axis='y', labelcolor=color)

# 그래프에 범례 추가
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# 그래프 타이틀 추가
plt.title('ETH Price and Volume')
fig.tight_layout()  

# 그래프 출력
plt.show()
