from datetime import datetime

def nowDate():
    return datetime.now().strftime('%Y/%m/%d %H:%M:%S')

# print(nowDate())