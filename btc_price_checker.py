import requests
import pandas as pd

def get_crypto_price(symbol):
    api_key = 'Tpk_82ce535768454d589bac207bb9b057de'
    api_url = f'https://sandbox.iexapis.com/stable/crypto/{symbol}/price?token={api_key}'
    raw = requests.get(api_url).json() #.json gives dictionary format
    price = raw['price']
    return float(price)

while True:
    btc = get_crypto_price('btcusd')
    print('Price of 1 Bitcoin: {} USD'.format(btc))