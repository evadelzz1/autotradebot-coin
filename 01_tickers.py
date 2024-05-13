import pyupbit

# 업비트의 모든 티커목록 출력
print(f'\n========================== All Market Tickers ==========================')
tickers = pyupbit.get_tickers()
print(tickers)
print(len(tickers))

# 원화 시장의 티커목록 출력
print(f'\n========================== KRW Market Tickers ==========================')
krw_tickers = pyupbit.get_tickers("KRW")
print(krw_tickers)
print(len(krw_tickers))

# BTC 시장의 티커목록 출력
print(f'\n========================== BTC Market Tickers ==========================')
btc_tickers = pyupbit.get_tickers("BTC")
print(btc_tickers)
print(len(btc_tickers))

# USDT 시장의 티커목록 출력
print(f'\n========================== USDT Market Tickers ==========================')
usdt_tickers = pyupbit.get_tickers("USDT")
print(usdt_tickers)
print(len(usdt_tickers))
