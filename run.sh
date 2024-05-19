#!/bin/bash

echo '
---------------------------------------------------------------------------------------------------------------------------
100_.py                         110_price_history.py            120_get_orderbook.py        130_chart_single.py
101_ticker.py                   111_candle_data.py              121_display_orderbook.py    131_chart_multiple.py
102_price.py                    112_candle_2Minutes.py                                      132_chart_PriceAndVolume.py
103_avg_buy_price.py            113_candle_dataframe.py                                     133_chart_PriceAndVolume2.py
104_tick.py                     114_candle_variation.py                                     134_chart.py
105_topCoin.py                                                                              138_chart_save_result.py
106_topCoin.py                                                                              139_chart.py

201_get_balance.py              211_buyOrder.py                 221_buyNsellMarketOrder.py
202_get_balance.py              212_getOrderList.py             222_buyNsellMarketOrder.py
                                213_cancelOrder.py              223_buyNsellMarketOrder_loop.py
                                214_buyNcancelOrder.py          224_buyNsellOrder_loop.py
                                215_sellOrder.py                231_getOrder.py

300_Stock_Indicator.py          311_RSI.py                      321_MACD_singleChart.py     331.py
301_MovingWindows.py            312_RSI_loop.py                 322_MACD_multipleChart.py   332.py
                                313_RSI2.py                     323_MACD_graph.py           333_buyNsell.py
                                314_RSI2_highTradeTickers.py    324_MACD_graph.py           341.py
                                315_RSI2_divide_buy_amount.py   325_MACD_loop.py
                                316_RSI2.py                     
---------------------------------------------------------------------------------------------------------------------------
'
echo "Select : "
read fileNo

python ./source/${fileNo}*.py
