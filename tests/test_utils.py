import unittest
import os
import json

from unittest.mock import mock_open, patch
from utils import load_finance_operations


class TestLoadFinanceOperations(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('os.path.exists', return_value=True)
    def test_load_empty_list(self, mock_exists, mock_open):
        result = load_finance_operations('dummy_path.json')
        self.assertEqual(result, [])


    @patch('builtins.open', new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    @patch('os.path.exists', return_value=True)
    def test_load_valid_json(self, mock_exists, mock_open):
        result = load_finance_operations('dummy_path.json')
        self.assertEqual(result, [{"amount": 100, "currency": "USD"}])


    @patch('builtins.open', new_callable=mock_open, read_data='{"amount": 100}')
    @patch('os.path.exists', return_value=True)
    def test_load_non_list_json(self, mock_exists, mock_open):
        result = load_finance_operations('dummy_path.json')
        self.assertEqual(result, [])


    @patch('os.path.exists', return_value=False)
    def test_file_does_not_exist(self, mock_exists):
        result = load_finance_operations('non_existing_file.json')
        self.assertEqual(result, [])


    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    def test_json_decode_error(self, mock_exists, mock_open):
        mock_open.side_effect = IOError("File not accessible")
