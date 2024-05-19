import pyupbit
from ConfigUpbit import upbit

import CustomModule as cm
from datetime import datetime

def get_total_balance():
    balance_f = 0.0

    for balance in upbit.get_balances():
        if balance['currency'] == 'KRW':
            balance_f += float(balance['balance'])
        else:
            balance_f += ((float(balance['balance'])
                          * float(balance['avg_buy_price'])))

    return balance_f

def get_detail_balance():
    responses = upbit.get_balances()
    for res in responses:
        print(
            f"Currency: {res['currency']:>10} | "
            f"Balance: {float(res['balance']):>20.10f} | "
            f"Locked: {res['locked']:>5} | "
            f"avg_buy_price: {float(res['avg_buy_price']):>20.10f} | "
            f"avg_buy_price_modified: {res['avg_buy_price_modified']:>5} | "
            f"unit_currency: {res['unit_currency']:>5}"
        )

def get_token_price(_tickers):
    nowDate = cm.nowDate()

    currentTokenPrice = pyupbit.get_current_price(_tickers)
    print(f'[current toekn price] {currentTokenPrice}')
    
    for ticker in _tickers:
        print(f'[{ticker}] {currentTokenPrice[ticker]}')
        
        res = pyupbit.get_ohlcv(
            ticker=ticker,
            interval='minute1',
            count=5,
            period=0.1
        )
        
        print(res)


def main():
    nowDate = cm.nowDate()
    try:
        print(f'\n========================== My Balance ==========================')
        myBalance = get_total_balance()
        print(f'Current Total Balance: {myBalance}  ({nowDate})')

        print(f'\n==========================  Details  ==========================')
        get_detail_balance()
        
        print(f'\n========================== My Assets ==========================')
        tickers = ['KRW-BTC', 'KRW-ETH']
        get_token_price(tickers)
        
        print(f'\n========================== Orderbook ==========================')
        orderbook = pyupbit.get_orderbook(tickers)
        print(orderbook)

    except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
        print('예외가 발생했습니다.', e)

if __name__ == "__main__":
    main()
