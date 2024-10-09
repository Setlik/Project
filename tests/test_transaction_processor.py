import unittest
from typing import List, Dict
import re

# Определение функций для тестирования
def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx['description'])]

def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    category_count = {category: 0 for category in categories}
    for tx in transactions:
        for category in categories:
            if category in tx['description']:
                category_count[category] += 1
    return category_count


class TestTransactionFunctions(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {'description': 'Grocery store purchase', 'amount': 100},
            {'description': 'Gas station refill', 'amount': 50},
            {'description': 'Grocery store refund', 'amount': -20},
            {'description': 'Dinner at restaurant', 'amount': 75},
            {'description': 'Gas station snacks', 'amount': 10},
        ]

    def test_filter_transactions_by_description(self):
        result = filter_transactions_by_description(self.transactions, 'grocery')
        expected = [
            {'description': 'Grocery store purchase', 'amount': 100},
            {'description': 'Grocery store refund', 'amount': -20},
        ]
        self.assertEqual(result, expected)

        result = filter_transactions_by_description(self.transactions, 'station')
        expected = [
            {'description': 'Gas station refill', 'amount': 50},
            {'description': 'Gas station snacks', 'amount': 10},
        ]
        self.assertEqual(result, expected)

        result = filter_transactions_by_description(self.transactions, 'dinner')
        expected = [
            {'description': 'Dinner at restaurant', 'amount': 75},
        ]
        self.assertEqual(result, expected)

        result = filter_transactions_by_description(self.transactions, 'nonexistent')
        expected = []
        self.assertEqual(result, expected)

    def test_count_transactions_by_category(self):
        categories = ['Grocery', 'Gas', 'Dinner']
        result = count_transactions_by_category(self.transactions, categories)
        expected = {'Grocery': 2, 'Gas': 2, 'Dinner': 1}
        self.assertEqual(result, expected)

        categories = ['Snacks', 'Refund']
        result = count_transactions_by_category(self.transactions, categories)
        expected = {'Snacks': 0, 'Refund': 0}
        self.assertEqual(result, expected)


