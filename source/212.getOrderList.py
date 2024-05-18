from ConfigUpbit import upbit
import CustomModule as cm
import time
from datetime import datetime

order_list = upbit.get_order(
    ticker_or_uuid='KRW-IOST',
    state='wait',
    limit=100
)

print(order_list)



# reference:print(index.length)
#   https://cosmosproject.tistory.com/501


