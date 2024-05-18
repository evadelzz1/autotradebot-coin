import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time

# -- Functions --------------------------------------------------

def get_month_price(market, year, month):
    url = "https://api.upbit.com/v1/candles/months"

    queryparams = {
        "market": market,
        "to" : f"{year}-{month:02d}-01T00:00:00+09:00", # TC 기준 시간이며 +09:00 를 붙여 KST 시간으로 요청 가능
        "count": 1
    }

    headers = {"accept": "application/json"}
    
    res = requests.get(url, headers=headers, params=queryparams)
    
    # 요청 성공 했을 경우 : code 200
    if res.status_code == 200:
        try:
            data = res.json()[0]
            # print(data)

            high_price = data["high_price"] # 고가
            low_price = data["low_price"]   # 저가
            candle_acc_trade_price = data["candle_acc_trade_price"]     # 누적거래 금액
            candle_acc_trade_volume = data["candle_acc_trade_volume"]   # 누적 거래량

            return(high_price, low_price, candle_acc_trade_price, candle_acc_trade_volume)

        except Exception as e:
            raise Exception(e)
    else:
        res.status_code == 400

def drawing_chart(filename):
    matplotlib.rcParams['font.family'] = 'AppleGothic'   # 'Malgun Gothic' # Windows
    matplotlib.rcParams['font.size'] = 9 
    matplotlib.rcParams['axes.unicode_minus'] = False

    # CSV 파일에서 데이터 읽기
    df = pd.read_csv(filename, index_col=0)

    # '원' 문자 제거
    df['high_price'] = df['high_price'].str.replace(' 원', '')
    df['low_price'] = df['low_price'].str.replace(' 원', '')

    # ',' 제거 및 숫자로 변환
    df['high_price'] = pd.to_numeric(df['high_price'].str.replace(',', ''))
    df['low_price'] = pd.to_numeric(df['low_price'].str.replace(',', ''))

    # 막대 그래프 생성
    ax = df.plot(kind='bar', y=['high_price', 'low_price'], figsize=(16, 8), alpha=0.8)

    # 그래프 제목과 축 라벨 설정
    plt.title('Monthly Report (KRW-ETH)')
    plt.xlabel('Month')
    plt.ylabel('high_price')

    # x축 label 회전
    plt.xticks(rotation=45)

    # 범례 추가
    plt.legend(['High Price', 'Low Price'])

    # 그래프 츌력
    plt.show()


# -- Start --------------------------------------------------

# 종목 = 비트코인(KRW)
market = "KRW-ETH"

# []에 KRW-BTC 월간 데이터 저장
month_data = []

# 2020년 01월 ~ 2022년 12월 까지의 데이터를 []에 저장
for year in range(2024,2025):
    for month in range(1, 13):
        if year == 2024 and month >= 4:
            break

        data = get_month_price(market, year, month)
        print(year, month, data)
        month_data.append(data) 

# df = pd.DataFrame(month_data, columns=['고가','저가','누적 거래대금','누적 거래량'])
df = pd.DataFrame(month_data, columns=['high_price','low_price','acc_trade_price','acc_trade_volume'])
print(df)

df['high_price'] = df['high_price'].apply(lambda x: '{:,.0f} 원'.format(x))
df['low_price'] = df['low_price'].apply(lambda x: '{:,.0f} 원'.format(x))
df['acc_trade_price'] = df['acc_trade_price'].apply(lambda x: '{:,.0f} 원'.format(x))
df['acc_trade_volume'] = df['acc_trade_volume'].apply(lambda x: '{:,.0f} 개'.format(x))

index = [(f"{year}년 {month}월") for year in range(2024,2025) for month in range(1, 13) if not (year == 2024 and month >= 4)]

if len(index) == len(month_data):
    df.index = pd.Index(index, name="월")
    print(df.head(10))

    filename = 'monthly_ETH.csv'
    df.to_csv(filename, encoding='utf-8-sig')

    with open(filename, "r") as f:
        for itr in f.readlines():
            print(itr)

    time.sleep(3)
    
    print('drawing...')
    drawing_chart(filename)

else:
    print("[Error] different list count")

# reference:print(index.length)
#   https://velog.io/@chlalsgur96/upbit-API를-이용한-웹-스크래핑-및-데이터-시각화-Toy-Project
