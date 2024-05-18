import pyupbit as pu
import pandas as pd
import time

def get_tickers(fiat='KRW'):
    return pu.get_tickers(fiat=fiat)

def get_ohlcv(ticker, interval='day', count=2):
    return pu.get_ohlcv(ticker, interval=interval, count=count)

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
            ohlcv = get_ohlcv(ticker, interval='day', count=2)
            if ohlcv is not None and len(ohlcv) >= 2:
                change_rate = calculate_price_change(ohlcv)
                change_rates[ticker] = round(change_rate, 2)
                
            time.sleep(0.04)  # 초당 요청 빈도를 줄이기 위해 지연 시간을 줌 (너무 많이 보내면, 어뷰징 요청으로 막힐 수 있음)
            
        except Exception as e:
            print(f"Error processing ticker {ticker}: {e}")
            continue

    sorted_change_rates = change_rates.sort_values(ascending=False)
    print(sorted_change_rates[:5])  # 상위 5개를 보여준다

if __name__ == "__main__":
    main()
