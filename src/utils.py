import json
import os

from dotenv import load_dotenv

load_dotenv()
file_path = os.getenv("file_path")


def load_finance_operations(file_path):
    '''функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        return []
