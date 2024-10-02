from unittest.mock import patch, mock_open
import unittest
import pandas as pd

from finance_operations import reading_transaction_csv, reading_transaction_xlsx


def test_reading_transaction_csv():
    # Подмена open для тестирования данных CSV
    mock_data = 'date,amount,category,note\n' \
                '2023-01-01,1000,Salary,January Salary\n' \
                '2023-01-15,-200,Groceries,Food expenses\n' \
                '2023-02-01,-150,Utilities,January Utilities\n'

    with patch('builtins.open', new_callable=mock_open, read_data=mock_data), \
         patch('os.path.exists', return_value=True):
        csv_file_path = '../data/transactions.csv'
        result = reading_transaction_csv(csv_file_path)

        expected_result = [
            {'date': '2023-01-01', 'amount': '1000', 'category': 'Salary', 'note': 'January Salary'},
            {'date': '2023-01-15', 'amount': '-200', 'category': 'Groceries', 'note': 'Food expenses'},
            {'date': '2023-02-01', 'amount': '-150', 'category': 'Utilities', 'note': 'January Utilities'},
        ]

        assert result == expected_result
        # mock_file.assert_called_once_with(csv_file_path, mode='r', encoding='utf-8')


def test_reading_transaction_xlsx():
    # Подмена pandas.read_excel для тестирования данных Excel
    mock_df = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-15', '2023-02-01'],
        'amount': [1000, -200, -150],
        'category': ['Salary', 'Groceries', 'Utilities'],
        'note': ['January Salary', 'Food expenses', 'January Utilities'],
    })

    with patch('pandas.read_excel', return_value=mock_df), \
         patch('os.path.exists', return_value=True):
        excel_file_path = '../data/transactions_excel.xlsx'
        result = reading_transaction_xlsx(excel_file_path)

        expected_result = [
            {'date': '2023-01-01', 'amount': 1000, 'category': 'Salary', 'note': 'January Salary'},
            {'date': '2023-01-15', 'amount': -200, 'category': 'Groceries', 'note': 'Food expenses'},
            {'date': '2023-02-01', 'amount': -150, 'category': 'Utilities', 'note': 'January Utilities'},
        ]

        assert result == expected_result
