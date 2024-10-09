import re
from typing import List, Dict
from collections import Counter


def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx['description'])]

def count_transactions_by_category(transactions):
    """Подсчитывает количество транзакций по описанию."""
    description_counter = Counter()
    for tx in transactions:
        description = tx.get("description","")
        description_counter[description] += 1
    return dict(description_counter)
