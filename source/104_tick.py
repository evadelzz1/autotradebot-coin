import requests

url = "https://api.upbit.com/v1/trades/ticks?market=KRW-ETH&count=300"
resp = requests.get(url)
ticks = resp.json()

for tick in ticks:
    print(tick)


# reference:
#   https://wikidocs.net/112460

