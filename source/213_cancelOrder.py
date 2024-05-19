from ConfigUpbit import upbit
import CustomModule as cm
from datetime import datetime
import time

uuidLists = []

uuidLists.append('9d5591b7-673e-402f-b680-ba2150af741d')
uuidLists.append('b778439e-0d17-448b-8ec8-1daa41593f39')


print(uuidLists)


cancelResultlists = []

print("\n\n=======  cancel order  ====================")
for i in uuidLists:
    res = upbit.cancel_order(i)
    cancelResultlists.append(res)
    print(i, " : ", res, "\n")

print("\n\n=======  cancel detail  ===================")
for i in cancelResultlists:
    print(i)

print("\n\n=======  cancel uuid  =====================")
for i in cancelResultlists:
    # print("[", i['uuid'], "] ", i)
    print(f'uuid: {i["uuid"]}')

