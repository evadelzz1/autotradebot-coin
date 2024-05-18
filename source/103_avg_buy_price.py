from ConfigUpbit import upbit
import pyupbit

#-- 토큰의 현재 가격 조회 (get_current_price) ------------------------------------------

# 개별 가격 조회
price_KRW = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-IOST"])

print("\n")
print("BTC  : {0:>10,} 원".format(int(price_KRW["KRW-BTC"]))) # 딕셔너리 type
print("ETH  : {0:>10,} 원".format(int(price_KRW["KRW-ETH"])))
print("XRP  : {0:>10,} 원".format(int(price_KRW["KRW-XRP"])))
print("IOST : {0:>10,} 원".format(int(price_KRW["KRW-IOST"])))

# 아래와 같이 ETH로도 가격 조회가 가능함
price_BTC = pyupbit.get_current_price("BTC-ETH")

print("\n")
print("ETH Current Price: {} BTC\n".format(price_BTC))

#-- 토큰의 평균 가격 조회 (get_avg_buy_price)------------------------------------------
price_BTC = upbit.get_avg_buy_price("BTC-ETH")

print("\n")
print("ETH Average Price: {}\n".format(price_BTC))


# 참고 표준 출력 : https://wikidocs.net/20403

# reference:
#   https://wikidocs.net/110982


# pyupbit.get_tickers()                 : 암호화폐 목록 얻기
# pyupbit.get_current_price("KRW-BTC")  : 암호화폐 현재가 얻기
# upbit.get_avg_buy_price("BTC-ETH")    : 평균 매수가 조회
