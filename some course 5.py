import requests
import time

url = 'https://api.binance.com/api/v3/ticker/price'

'''
response = requests.get(url, params={'symbol': 'BTCUSDT'})

"""
content = response.content

print(content)
print(type(content))
"""

price_object = response.json()
print(price_object)
print(type(price_object))

price = float(price_object["price"])
print(price)
'''

bitcoin_prices = []

for i in range(30):
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price = float(response.json()['price'])
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))
