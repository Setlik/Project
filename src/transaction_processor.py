import re
from typing import List, Dict

def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx['description'])]

def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    category_count = {category: 0 for category in categories}
    for tx in transactions:
        words = tx['description'].lower().split()  # разбиваем описание на слова
        for category in categories:
            if category.lower() in words:  # Проверяем наличие слова
                category_count[category] += 1
    return category_count