from ConfigUpbit import upbit
import CustomModule as cm
import time
from datetime import datetime

uuidLists = []

uuidLists.append('1b84329f-b3b9-4a36-9fa1-5ab1c08c50f4')
uuidLists.append('f2e2b497-14e6-43d9-9a0e-e9fb3febeccd')

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

