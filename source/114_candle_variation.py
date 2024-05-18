import pyupbit

df = pyupbit.get_ohlcv(ticker="KRW-ETH", interval="minute60", count=14)
price = pyupbit.get_current_price("KRW-ETH")
print(f"\n### Now price is: {price}")
print(df)

########## 종가 변동량(var) 구한 후, df 에 추가 ##########
var = [0]           # var
varPercent = [0]    # var %

for i, v in enumerate(df["close"][1:]):
    # print(f">> i: {i}, v: {v}")
    var.append(v - df["close"].iloc[i])
    varPercent.append(f'{round((v / df["close"].iloc[i] - 1) * 100, 4)}%')

df["var"] = var
df["var %"] = varPercent

print(df[["close", "volume", "var", "var %"]])
print(f"Now price is: {price}")


# source : https://coderyoon.tistory.com/10

# 종가의 변동량을 따로 구해서 데이터프레임에 추가하고 같이 보겠습니다. 
# 여러분들도 한번 직접 해보시고 그 다음에 다음 내용을 보시면 좋을 것 같습니다.
# 코인 가격의 변동량을 나타내는 var과 변동량을 백분율로 나타낸 varPercent리스트를 넣고 데이터프레임에 집어넣었습니다. 
# 이렇게 보니까 실제로 코인이 어느정도로 변화했는지 잘 보이네요. 시간 당 많으면 1% 정도 움직였는데 요새 장치곤 매우 안정적인 변화죠.

