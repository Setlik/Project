import unittest
from unittest.mock import MagicMock, patch

from external_api import get_exchange_rate, get_transaction_amount_in_rubles


class TestCurrencyFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_get_exchange_rate_success(self, mock_get):
        # Настройка mock-объекта
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 75.0}
        mock_get.return_value = mock_response

        rate = get_exchange_rate("USD")
        self.assertEqual(rate, 75.0)

    @patch('requests.get')
    def test_get_exchange_rate_failure(self, mock_get):
        # Настройка mock-объекта для ошибки
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        rate = get_exchange_rate("USD")
        self.assertIsNone(rate)

    @patch('requests.get')
    def test_get_transaction_amount_in_rubles_with_usd(self, mock_get):
        # Настройка mock-объекта
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 75.0}
        mock_get.return_value = mock_response

        transaction = {"amount": 100, "currency": "USD"}
        amount_in_rubles = get_transaction_amount_in_rubles(transaction)
        self.assertEqual(amount_in_rubles, 7500.0)

    @patch('requests.get')
    def test_get_transaction_amount_in_rubles_with_rub(self, mock_get):
        transaction = {"amount": 100, "currency": "RUB"}
        amount_in_rubles = get_transaction_amount_in_rubles(transaction)
        self.assertEqual(amount_in_rubles, 100.0)

    @patch('requests.get')
    def test_get_transaction_amount_in_rubles_invalid_currency(self, mock_get):
        transaction = {"amount": 100, "currency": "GBP"}  # некорректная валюта
        amount_in_rubles = get_transaction_amount_in_rubles(transaction)
        self.assertIsNone(amount_in_rubles)