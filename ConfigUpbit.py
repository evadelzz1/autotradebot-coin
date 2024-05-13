from dotenv import load_dotenv
import os
import pyupbit

if not load_dotenv():
    print("Could not load .env file or it is empty. Please check if it exists and is readable.",)
    exit(1)

upbit_access_key = os.getenv("UPBIT_ACCESS_KEY")
upbit_secret_key = os.getenv("UPBIT_SECRET_KEY")
 
print(f'### [Config Upbit] ACCESS_KEY: {upbit_access_key[0:10]}...')
print(f'### [Config Upbit] SECRET_KEY: {upbit_secret_key[0:10]}...')

try:
    upbit = pyupbit.Upbit(access=upbit_access_key, secret=upbit_secret_key)
    response = upbit.get_balances()

    if 'error' in response:
        error_message = response['error']['message']
        print("[Error] Reason: ", error_message)
        exit(1)
    
    print(f'### [Config Upbit] "upbit" object Loading Ok"')

except Exception as e:
    print("[Error] Reason: ", e)
    