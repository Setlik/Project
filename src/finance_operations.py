import csv
import logging
import os

import pandas as pd

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/reading_trans.log",
    filemode="w",
)
logger = logging.getLogger()


def reading_transaction_csv(file_path: str) -> list:
    """Функция для считывания финансовых операций из CSV."""
    logger.info(f"Попытка загрузки финансовых операций из CSV файла: {file_path}")

    if not os.path.exists(file_path):
        logger.warning(f"Файл не существует: {file_path}")
        return []

    transactions = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(row)
        logger.info(f"Финансовые операции успешно загружены из CSV файла. Количество записей: {len(transactions)}")
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении CSV файла: {e}")

    return transactions


def reading_transaction_xlsx(file_path: str) -> list:
    """Функция для считывания финансовых операций из Excel."""
    logger.info(f"Попытка загрузки финансовых операций из Excel файла: {file_path}")

    if not os.path.exists(file_path):
        logger.warning(f"Файл не существует: {file_path}")
        return []

    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"Финансовые операции успешно загружены из Excel файла. Количество записей: {len(transactions)}")
        return transactions
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении Excel файла: {e}")
        return []


# def test_load_functions():
#     print("Загрузка финансовых операций из CSV:")
#     csv_operations = reading_transaction_csv('../data/transactions.csv')
#     print(csv_operations)
#
#     print("\nЗагрузка финансовых операций из Excel:")
#
#     excel_operations = reading_transaction_xlsx('../data/transactions_excel.xlsx')
#     print(excel_operations)
#
#
# # Запуск тестирования
# if __name__ == "__main__":
#     test_load_functions()
