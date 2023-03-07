"""
Use the bitcoin API to convert dollars to Bitcoin
https://www.coindesk.com/coindesk-api

Attribution:
This app powered by CoinDesk, https://www.coindesk.com/price/bitcoin

"""

import requests

from pprint import pprint

# the main function is called first, which then calls user_input_bitcoin() to prompt the user 
# to enter the number of bitcoins they want con convert.

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

# 2; bitcoin to dollar is called , which calls get_Api_bitcoin to retrieve the latest bitcoin exchange rate 
# from the CoinDesk API.

def bitcoin_to_dollar(bitcoin):
    data = get_API_bitcoin()
    rate = extract_rate(data)
    bitcoin_value_in_dollars = convert_bitcoin_to_dollars(bitcoin, rate)
    return bitcoin_value_in_dollars

# 3: extract_rate is then used to extract the USD exchange rate from the JSON response .
def extract_rate(data):
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    return dollars_exchange_rate

# 4: bitcoins_to_dollars then calculates the equivalent value of the user's input in US dollars
# by multiplying the bitcoin amount by the current USD exchange rate.

def convert_bitcoin_to_dollars(bitcoin, price):
    final_price = bitcoin * price
    return final_price 

# The final converted value is returned by bitcoin to dollar and passed tp display_results to print 
# the result to the user.

def display_results(bitcoin, price):
    print(f'{bitcoin} Bitcoin is equivalent to $ {price:.2f}')

if __name__ == '__main__':
    main()

# This program could benefit from additional error handling and edge case testing to make it more robust.
#  See test_bitcoin.py 