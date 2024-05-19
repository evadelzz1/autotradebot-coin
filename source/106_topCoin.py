import pyupbit
import pandas as pd
import time

def get_tickers(fiat='KRW'):
    return pyupbit.get_tickers(fiat=fiat)

def get_ohlcv(ticker, interval='day', count=2):
    return pyupbit.get_ohlcv(ticker, interval=interval, count=count)

def calculate_price_change(c):
    close_prices = c['close']
    prev_close = close_prices.iloc[-2]
    current_close = close_prices.iloc[-1]
    price_change = current_close - prev_close
    change_rate = (price_change / prev_close) * 100
    return change_rate

def main():
    tickers = get_tickers(fiat='KRW')
    change_rates = pd.Series(dtype=float)  # 변동률을 저장할 시리즈 변수

    print('Calculating... (최근 가격변동율 높은 Top 코인)')
    for ticker in tickers:
        try:
            data = get_ohlcv(ticker, interval='day', count=2)
            if data is not None and len(data) >= 2:
                change_rate = calculate_price_change(data)
                change_rates[ticker] = round(change_rate, 2)
                
            time.sleep(0.04)  # 초당 요청 빈도를 줄이기 위해 지연 시간을 줌 (너무 많이 보내면, 어뷰징 요청으로 막힐 수 있음)
            
        except Exception as e:
            print(f"Error processing ticker {ticker}: {e}")
            continue

    sorted_change_rates = change_rates.sort_values(ascending=False)
    print(sorted_change_rates[:5])  # 상위 5개를 보여준다

if __name__ == "__main__":
    main()




# #########################################################
# pyupbit.get_ohlcv() : 분봉 데이터 조회
# #########################################################
# 
# 1, 3, 5, 10, 15, 30, 60, 240분봉에 대해서 최대 200개 조회 가능
#
# ticker = 가격 내역을 조회할 코인의 ticker
# interval = 가격 조회 간격을 의미합니다. interval에 지정 가능한 값은 다음과 같습니다.
#     minute1 = 1분봉
#     minute3 = 3분봉
#     minute5 = 5분봉
#     minute10 = 10분봉
#     minute15 = 15분봉
#     minute30 = 30분봉
#     minute60 = 60분봉
#     minute240 = 240분봉
#     day = 일봉
#     week = 주봉
#     month = 월봉
# count = 최근 몇일지의 데이터를 조회할지를 의미 (default값은 200입니다.)
# to = 출력할 max date time을 지정
# period = 데이터 요청 주기 (초) (default 값은 0.1 입니다.)

# #########################################################
#
# Output
# 
# - DataFrame index = 기준 날짜/시간
# - 시가 : open = 기준 시간과 시가(시작 가격)
# - 고가 : high
# - 저가 : low
# - 종가 : close
# - 거래량 : volume = 거래량 (거래된 코인의 개수)
# - 거래액 : value = 거래 금액 (거래된 코인의 개수에 대한 가격)
# #########################################################

# 분봉=https://docs.upbit.com/reference/분minute-캔들-1
# 일봉=https://docs.upbit.com/reference/일day-캔들-1
# 주봉=https://docs.upbit.com/reference/주week-캔들-1
# 월봉=https://docs.upbit.com/reference/월month-캔들-1