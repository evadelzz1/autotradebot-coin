import pyupbit
from ConfigUpbit import upbit
import pandas as pd
import datetime as dt
import time

def get_SMA_MACD(_ticker) :
    # data = pyupbit.get_ohlcv(ticker=_ticker, interval='day', count=200)
    # data = pyupbit.get_ohlcv(ticker=_ticker, interval='day', count=100)
    data = pyupbit.get_ohlcv(ticker=_ticker, interval='minutes1', count=116)
    # print(data)
    
    if data is None:
        print("[Error] Data not loading....")
        return (False, 0, 0, 0, 0, 0)
    
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data, dtype="float", columns=["open", "high", "low", "close", "volume", "value"])
    # print(df.tail())
    
    dataSet = df.loc['2023':'2024', ['close']]
    # print(dataSet)

    ShortEMA = dataSet["close"].ewm(12).mean().round(5)      # 12일간의 지수 이동평균
    LongEMA = dataSet["close"].ewm(26).mean().round(5)       # 26일간의 지수 이동평균
    MACD = (ShortEMA - LongEMA).round(5)                     # MACD = ShortEMA-LongEMA
    Signal = MACD.ewm(9).mean().round(5)                     # Signal = MACD 9일 지수 이동평균선
    Oscillator = (MACD - Signal).round(5)                    # Oscillator = MACD - Signal

    SMA01 = df['close'].rolling(window=3).mean().round(5)    # 3일 이동 평균
    SMA02 = df['close'].rolling(window=10).mean().round(5)   # 10일 이동 평균
    SMA03 = df['close'].rolling(window=50).mean().round(5)   # 50일 이동 평균

    return (True, SMA01, SMA02, SMA03, MACD, Signal)

def get_balance(_ticker):
    balances = upbit.get_balances()
    print(ticker)
    print(balances)
    for b in balances:
        if b['currency'] == _ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0
    
def get_current_price(_ticker):
    currentPrice = pyupbit.get_orderbook(ticker=_ticker)["orderbook_units"][0]["ask_price"]
    # print(f'ticker: {_ticker}, current price: {currentPrice}')
    return currentPrice

def main():
    print("autotrade start")

    # ticker = input("화폐 및 코인 코드 입력(ex.KRW-IOST) :")
    ticker = 'KRW-BTC'

    start_balance = upbit.get_balance() # "KRW"    
    print(start_balance)
    while True:
        try:
            now = dt.datetime.now()        
            start_time = now - dt.timedelta(hours=1)
            end_time = now + dt.timedelta(hours=10)
            formatedNow = dt.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

            buy_price = 0
            sell_price = 0
            
            if start_time < now < end_time:
                current_price = get_current_price(ticker)

                isValid, SMA01, SMA02, SMA03, MACD, Signal = get_SMA_MACD(ticker)
                if not isValid:
                    continue
                
                SMA01_ = SMA01.iloc[-1]
                SMA02_ = SMA02.iloc[-1]
                SMA03_ = SMA03.iloc[-1]
                MACD_ = MACD.iloc[-1]
                Signal_ = Signal.iloc[-1]
                            
                ######### 첫 번째 if 문은 매수를 위한 조건 #########
                #
                # 매수는,
                # 3일 기준 SMA와 10일 기준 SMA가 50일 기준의 SMA보다 커야 하고  = SMA01 > SMA03 && SMA02 > SMA03
                # 3일 기준 SMA가 10일 기준 SMA를 넘는 순간이며 또한 이때에       = SMA01 > SMA02
                # MACD는 Signal보다 커야 하는 조건이다.
                # 이 조건이 모두 만족할 때에 매수를 하며 매수는 0.005%의 수수료를 제외하고 통장에 있는 전액을 매수에 사용한다.
                # 이를 위해 원화 기준의 통장 잔액을 조회하고 매수 명령을 보낸다.
                # 매수가 이루어지면 매수 당시의 현재가를 “buy_price” 변수에 저장하고 print 문으로 한번 찍어준다.
                # 사실 여기의 프로그램에서는 현재 매수 가격을 별도로 알고 있을 필요가 없으나 이전 버전의 매매 프로그램에서는 매수 가격을 기준으로 매도 조건을 결정했었으므로 매수했을 때의 가격이 필요했었다.
                # 매도의 조건을 매수가격을 기준으로 판단하려면 필요한 코드이다.

                actionUuid = '0'    # 3a8d7d67-1910-4beb-acb6-ffb358f3609
                if (SMA01_ > SMA02_) and (SMA02_ > SMA03_) and (MACD_ > Signal_) :
                    krw = upbit.get_balances() # "KRW"
                    
                    # buy_result = upbit.buy_market_order(coin, krw*0.9995)
                    # buy_result = upbit.buy_market_order(ticker=ticker, price=7000)
                    # actionUuid = buy_result['uuid']
                    buy_price = current_price
        
                ######### 두 번째 if 문은 매도를 위한 조건 #########
                #
                # 매도 조건은,
                # 3일 기준 SMA가 10일 기준 SMA 보다 밑으로 가는 순간이 될 때이다.

                if (SMA01_ < SMA02_) :
                    bal = upbit.get_balance(ticker=ticker)
                    # sell_result = upbit.sell_market_order(ticker=ticker, bal*0.9995)
                    # actionUuid = sell_result['uuid']
                    sell_price = current_price
        
                # print(f'[{formatedNow}] Price: {current_price:12.3f}, MACD: {MACD.iloc[-1]:15.5f}, SMA01: {SMA01.iloc[-1]:15.5f}, SMA02: {SMA02.iloc[-1]:15.5f}, SMA03: {SMA03.iloc[-1]:15.5f}, Signal: {Signal.iloc[-1]:15.5f}')
                print(f'[{formatedNow}] Price: {current_price:12.3f}, MACD: {MACD_:15.5f}, SMA01: {SMA01_:15.5f}, SMA02: {SMA02_:15.5f}, SMA03: {SMA03_:15.5f}, Signal: {Signal_:15.5f}, buy_price: {buy_price:12.3f}, sell_price: {sell_price:12.3f}, uuid: {actionUuid}')

            # 잔고 조회를 해서 자동매매를 시작했을 때의 가격보다 7% 이득을 봤다면 프로그램 종료
            last_balance = upbit.get_balance("KRW")
            if last_balance >= (start_balance * 1.07):
                print(f'[{formatedNow}] last_balance: {last_balance}, start_balance: {start_balance}')
                break
            
            time.sleep(3)
            
        except Exception as e:
            print('[Error]', e)
            time.sleep(1)

if __name__ == "__main__":
    main()
    
    
# reference:
#   https://superhky.tistory.com/235
#   https://superhky.tistory.com/244
#   https://superhky.tistory.com/447
#   https://blog.naver.com/jun652006/222316267357
#   
#   