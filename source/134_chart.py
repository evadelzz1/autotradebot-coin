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

# Close 가격을 막대 그래프로 표시
ax1.set_xlabel('Date')
ax1.set_ylabel('Close', color='tab:red')
ax1.bar(data.index, data['close'], color='tab:red', label='Close Price')

# Volume에 음수를 곱하여 막대 그래프로 표시
ax2 = ax1.twinx()  
ax2.set_ylabel('-Volume', color='tab:blue')
ax2.bar(data.index, -data['volume'], color='tab:blue', alpha=0.5, label='Volume')

# 그래프에 범례 추가
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# 그래프 타이틀 추가
plt.title('ETH Price and Volume')
fig.tight_layout()  

plt.show()
