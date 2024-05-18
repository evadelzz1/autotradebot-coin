import requests

# url = "https://api.upbit.com/v1/trades/ticks?market=KRW-BTC&count=20"
url = "https://api.upbit.com/v1/candles/days?market=KRW-ETH&count=20"

resp = requests.get(url)
priceHistory = resp.json()

for price in priceHistory:
    print(price)


# reference:
#   https://wikidocs.net/112460


