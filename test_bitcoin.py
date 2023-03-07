
import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin_exchange  

class BitcoinExchangeTestCase(TestCase):

    @patch('builtins.input', side_effect=['3'])
    def test_user_input_bitcoin(self, mock_input):
        answer = bitcoin_exchange.user_input_bitcoin()
        self.assertEqual(3, answer)

    @patch('bitcoin_exchange.get_API_bitcoin')
    def test_bitcoin_to_dollar_with_mock_response(self, mock_rates):
        
        #Mock API response with a fixed exchange rate

        mock_rate = 30000
        api_response = {"time":{"updated":"Mar 6, 2023 23:41:00 UTC","updatedISO":"2023-03-06T23:41:00+00:00","updateduk":"Mar 6, 2023 at 23:41 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"22,401.6684","description":"United States Dollar","rate_float":22401.6684},"GBP":{"code":"GBP","symbol":"&pound;","rate":"18,718.6549","description":"British Pound Sterling","rate_float":18718.6549},"EUR":{"code":"EUR","symbol":"&euro;","rate":"21,822.4956","description":"Euro","rate_float":21822.4956}}}
        mock_rates.side_effect = [api_response]

        # Test that the program correctly converts 3 bitcoins to dollars using the mock response 

        converted = bitcoin_exchange.bitcoin_to_dollar(3)
        self.assertEqual(90000, converted)

        # Test that the API was called once
        mock_rates.assert_called_once()

    @patch('builtins.print')
    def test_display_results(self, mock_print):
        # test that the display function correctly formats the output

        bitcoin_exchange.display_results(3, 90000)
        mock_print.assert_called_once_with('3 Bitcoin is equivalent to $90000.00')

    def test_convert_bitcoin_to_dollars(self):
        # Test that the convert function correctly calculates the exchange rate

        price = bitcoin_exchange.convert_bitcoin_to_dollars(3, 30000)
        self.assertEqual(90000, price)

    @patch('builtins.input', side_effect=['abc'])
    @patch('builtins.print')

    def test_user_input_bitcoin_with_invalid_input(self, mock_print, mock_input):
        # Test that the program handles invalid input (non-integer value)

        with self.assertRaises(ValueError):
            bitcoin_exchange.user_input_bitcoin()

            # Test that an error message is printed to the console


