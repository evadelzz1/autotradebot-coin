import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 차트 정보를 받아오는 url을 다른 코인 또는 다른 기간으로 호출하기 편하게 format스트링 구조로 만듭니다.
def getTokenPrice(_term, _interval, _coin, _count):
    url = "https://crix-api.upbit.com/v1/crix/candles/{term}/{interval}?code=CRIX.UPBIT.{coin}&count={count}".format(
        term = _term, interval = _interval, coin = _coin, count = _count)

    res = requests.get(url).json()
    return res

def main():
    priceLists = getTokenPrice('minutes', 240, 'KRW-ETH', 20)
    # print(priceLists)
    
    chartData = []
    for item in priceLists:
        code = item['code']
        code2 = code.replace("CRIX.UPBIT.", "")
        open = item['openingPrice']
        high = item['highPrice']
        low = item['lowPrice']    
        close = item['tradePrice']
        kst = item['candleDateTimeKst']
        
        if 'KRW' in code:  
            print (code2, open, high, low, close, kst)
            chartData.append([code2, open, high, low, close, kst])

    # pandas의 Dataframe 자료형에 다운로드하여 정리한 데이터를 입력합니다.
    columns = ['coin','open','high','low','close','kst']
    df = pd.DataFrame.from_records(chartData, columns = columns)
    df.index = pd.DatetimeIndex(df.kst)

    # 데이터프레임 출력
    # print(df)
    
    
    ####################### 그래프 그리기 #######################
    fig, ax1 = plt.subplots(figsize=(12, 6))

    width = 0.02  # 막대 너비

    # DatetimeIndex를 matplotlib의 float dates로 변환
    x = mdates.date2num(df.index.to_pydatetime())

    # 각 데이터에 대해 막대 그래프 그리기
    ax1.bar(x - width * 1.5, df['open'], width, label='Open', color='blue')
    ax1.bar(x - width * 0.5, df['high'], width, label='High', color='green')
    ax1.bar(x + width * 0.5, df['low'], width, label='Low', color='red')
    ax1.bar(x + width * 1.5, df['close'], width, label='Close', color='orange')

    # 그래프 타이틀과 라벨 설정
    ax1.set_title('KRW-ETH Price Data')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price')
    ax1.legend()

    # x축 레이블 회전 및 포맷 설정
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)

    # 그래프 출력
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

# reference:
#   https://steemit.com/kr/@minari/4otktz-kr-dev-python

