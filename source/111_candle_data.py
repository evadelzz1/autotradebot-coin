import pyupbit

df = pyupbit.get_ohlcv(
    ticker="KRW-ETH",
    interval="minute1",
    count=20,
    # to="20240501 00:00:00",
    period=0.1)

print(len(df), type(df), df.shape)
print(df.columns)
print(df)

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

# reference:
#   https://coderyoon.tistory.com/8
#   https://github.com/sharebook-kr/pyupbit