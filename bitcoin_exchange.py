"""
Use the bitcoin API to convert dollars to Bitcoin
https://www.coindesk.com/coindesk-api

Attribution:
This app powered by CoinDesk, https://www.coindesk.com/price/bitcoin

"""

import requests

from pprint import pprint

def main():
    user_bitcoins = user_input_bitcoin()
    price = bitcoin_to_dollar(user_bitcoins)

    display_results(user_bitcoins, price)

def user_input_bitcoin():
    user_input = int(input('Enter the number of bitcoins:'))
    return user_input

def get_API_bitcoin():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url)
    data = response.json()
    return data 

def bitcoin_to_dollar(bitcoin):
    data = get_API_bitcoin()
    rate = extract_rate(data)
    bitcoin_value_in_dollars = convert_bitcoin_to_dollars(bitcoin, rate)
    return bitcoin_value_in_dollars

def extract_rate(data):
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    return dollars_exchange_rate

def convert_bitcoin_to_dollars(bitcoin, price):
    final_price = bitcoin * price
    return final_price 

def display_results(bitcoin, price):
    print(f'{bitcoin} Bitcoin is equivalent to $ {price:.2f}')

if __name__ == '__main__':
    main()

