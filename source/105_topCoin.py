import pyupbit
from ConfigUpbit import upbit
import time

# 종목 선정 : 거래량 상위 Top 5
def get_transaction_amount(interval, num):
    tickers = pyupbit.get_tickers("KRW")  # KRW 마켓의 티커 조회
    dic_ticker = {}
    
    for ticker in tickers:
        try:
            print(ticker)
            data = pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=20)
            if data is None:
                print("[Error] Data not loading....")
                continue
                # exit(1)
            
        except Exception as e:
            print(f"Error processing ticker {ticker}: {e}")
            continue
        
        time.sleep(0.04)  # 요청 빈도를 줄이기 위해 지연 시간을 준다
                    
        # 코인별 최근 7일간의 거래대금 합 : 순위가 바뀔 수 있으니 당일은 제외
        volume_money = 0.0
        for i in range(1, 9):
            volume_money += data['close'].iloc[-i] * data['volume'].iloc[-i]  
        # volume_money = sum(df['close'].iloc[-i] * df['volume'].iloc[-i] for i in range(2, 9))

        dic_ticker[ticker] = volume_money

    # 거래대금이 많은 순으로 ticker 정렬
    sorted_ticker = sorted(dic_ticker.items(), key=lambda x: x[1], reverse=True)
    return [coin[0] for coin in sorted_ticker[:num]]


# -- Start --------------------------------------------------

print('Calculating... (최근 7일간 거래금액이 높은 Top 코인)')
topTickers = get_transaction_amount("minute5", 5)	# 거래대금 상위 5개 코인 선정

print('====== 최근 7일간 거래금액이 높은 Top 코인 ======')
for ticker in topTickers:
    print(ticker)



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