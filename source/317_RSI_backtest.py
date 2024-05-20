import pyupbit
from ConfigUpbit import upbit
import pandas as pd
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt

ticker = 'KRW-ETH'

data = pyupbit.get_ohlcv(ticker=ticker, interval='day')

if data is None:
    print("[Error] Data not loading....")
    exit(1)

print(data)

#04) 데이터프레임 열 이름 붙여주기
df = pd.DataFrame(data, columns=['open','high','low','close','volume'])

# 인덱스의 날짜 시간을 'time_open' 열로 변환
df['time_open'] = df.index

# #05) 데이터프레임 열 type을 실수형으로 변환
df = df.astype({'open' : 'float', 'high' : 'float', 'low' : 'float', 'close' : 'float', 'volume' : 'float'})

# # #06) Date 열의 형태를 epoch에서 Pandas.Timestamp로 변경 
# df['time_open'] = df['time_open'].apply(lambda date: pd.Timestamp(time.ctime(date/1000.)))

# ====== 판다스로 RSI 매매 전략 구현 ====== 
# RSI의 AU(Average of UP), AD(Average of Down)를 구하기 위한 구간(t_interval) 개수
n_rsi = 9  

# 07-1) 변동폭 계산 : 현재 종가 - 지난 종가
df['close_bef'] = df['close'].shift(1) 
df['updown'] = df['close'] - df['close_bef'] 

# 07-2) 상승, 하락 구분
df['up'] = np.where(df['updown'] > 0.0, df['updown'], 0)
df['down'] = np.where(df['updown'] > 0.0, 0, df['updown'])
print(df)

# 07-3) 상승분 평균 AU, 하락분 평균 AD
#       simple moving average
def get_average(updown, n):
    average = updown.rolling(n).mean()
    return average

df['au'] = get_average(df['up'], n_rsi)
df['ad'] = get_average(df['down'], n_rsi)

# 07-4) RS : 상대강도
df['rs'] = df['au']/df['ad'].abs()

# 07-5) RSI : 상대강도 지수
df['rsi'] = df['rs']/(1.0 + df['rs'])*100

# 07-6) RSI 교차점
df['crs70'] = np.where(df['rsi'] > 70, 1, 0)
df['crs30'] = np.where(df['rsi'] < 30, 1, 0)
df['time_crs70'] = df['crs70'].diff() 
df['time_crs30'] = df['crs30'].diff() 

#07-7) 매수, 매도지점 표시
df['cross_buy'] = np.where(df['time_crs30']==-1, df['close'], np.NaN)
df['cross_sell'] = np.where(df['time_crs70']==-1, df['close'], np.NaN)

print('\n', '#07-7)')
print(df)

#08) 시계열 데이터 가시화, 차트에 매수지점(^), 매도지점(v) 표시
fig, axs = plt.subplots(2,1,figsize=(10,9))

axs[0].plot(df['time_open'],df['close'], label='close')
axs[0].scatter(df['time_open'], df['cross_buy'], marker='^', color='red', label='buy')
axs[0].scatter(df['time_open'], df['cross_sell'], marker='v', color='blue', label='sell')
 
axs[0].set_title('BTC trading based on RSI(Relative Strength Index)')

axs[0].set_xlim(np.datetime64('2023-11-01'), np.datetime64('2024-07-01'))

axs[0].set_ylabel('Price (USDT)')   
axs[0].legend(loc='best')
axs[0].tick_params(axis='x', rotation=15)
axs[0].grid(True)

axs[1].plot(df['time_open'],df['rsi'], 'm', label='RSI')
axs[1].set_xlim(np.datetime64('2023-11-01'), np.datetime64('2024-07-01'))
major_yticks = [30, 70]
axs[1].set_yticks(major_yticks)
axs[1].legend(loc='best')
axs[1].tick_params(axis='x', rotation=15)
axs[1].grid(True)

# #10) 이익 계산, 계산결과 출력
no_buy  = df['cross_buy'].count()
no_sell = df['cross_sell'].count()

print('\n','#10) ---')
print(f'* Number of buying  : {no_buy}', '\n',
      f' Number of selling : {no_sell}')

#11-1) 매수일/매수가(df_buy), 매도일/매도가(df_sell) 저장
df_buy = df[['time_open', 'cross_buy']].dropna()
df_sell= df[['time_open', 'cross_sell']].dropna()

print('\n','# Buying Info.')
print(df_buy)
print('\n','# Selling Info.')
print(df_sell)


#09) 차트를 그림파일로 저장
file_path = './zbacktesting/'
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f'RSI_{timestamp}.png'
plt.savefig(file_path + file_name, dpi=200)
plt.show()



# reference:
#   https://coffee4m.com/파이썬-바이낸스-api-비트코인-투자-백테스팅-rsi-매매/

