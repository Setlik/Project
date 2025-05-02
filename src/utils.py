import json
import logging
import os
from logging import getLogger, basicConfig, DEBUG

from dotenv import load_dotenv
import re
from typing import List, Dict


def filter_by_description(transactions: List[Dict], search_term: str) -> List[Dict]:
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def count_operations_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category in description:
                category_count[category] += 1
    return category_count


load_dotenv()
file_path = os.getenv("file_path")

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../logs/utils.log',
                    filemode='w')
logger = logging.getLogger()


def load_finance_operations(file_path):
    '''функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    logger.info(f'Попытка загрузки финансовых операций из файла: {file_path}')
    if not os.path.exists(file_path):
        logger.warning(f'Файл не существует: {file_path}')
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info('Финансовые операции успешно загружены')
                return data
            else:
                logger.warning(f'Данные в файле не являются списком: {file_path}')
                return []
    except json.JSONDecodeError:
        logger.error(f'Ошибка декодирования JSON в файле: {file_path}')
        return []
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')
        return []
