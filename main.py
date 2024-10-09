import os

from file_reader import load_csv, load_json, load_xlsx
from masks import get_mask_account, get_mask_card_number
from transaction_processor import filter_transactions_by_description, count_transactions_by_category

json_path = os.path.join('data', 'operations.json')
csv_path = os.path.join('data', 'transactions.csv')
XLSX_path = os.path.join('data', 'transactions_excel.xlsx')


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    if choice == "1":
        transactions = load_json(json_path)
    elif choice == "2":
        transactions = load_csv(csv_path)
    elif choice == "3":
        transactions = load_xlsx(XLSX_path)
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # Проверка загрузки
    print(f"Загруженные транзакции: {transactions}")

    if not transactions:
        print("Ошибка при загрузке транзакций.")
        return

    while True:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию. "
                "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: "
            )
            .strip()
            .upper()
        )

        if status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Статус операции "{status}" недоступен.')
        else:
            print(f'Операции отфильтрованы по статусу "{status}"')
            filtered_transactions = [tx for tx in transactions if tx.get("state", "").upper() == status]
            break
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        order_choice = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        filtered_transactions.sort(key=lambda x: x["date"], reverse=(order_choice == "по убыванию"))

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == "да":
        filtered_transactions = [
            tx for tx in filtered_transactions if tx["operationAmount"]["currency"]["code"] == "RUB"
        ]

    description_filter = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    )
    if description_filter == "да":
        search_string = input("Введите слово для поиска: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    description_counts = count_transactions_by_category(filtered_transactions)
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        print(f"Подсчет транзакций по описанию: {description_counts}")
        for tx in filtered_transactions:
            masked_from = get_mask_account(tx.get("from", ""))
            masked_to = get_mask_account(tx.get("to", ""))
            masked_card_from = get_mask_card_number(tx.get("from", ""))
            masked_card_to = get_mask_card_number(tx.get("to", ""))

            amount = tx["operationAmount"]["amount"]
            currency = tx["operationAmount"]["currency"]["name"]

            if "Счет" in (tx.get("from", "") or "") and "Счет" in (tx.get("to", "") or ""):
                print(f"{tx['date']} {tx['description']}")
                print(f"Счет: {masked_from} -> Счет: {masked_to}")
                print(f"Сумма: {amount} {currency}\n")
            elif "Счет" in (tx.get("to", "") or ""):
                print(f"{tx['date']} {tx['description']}")
                print(f"Счет: {masked_to}")
                print(f"Сумма: {amount} {currency}\n")
            else:
                formatted_card_from = get_mask_card_number(masked_card_from)
                formatted_card_to = get_mask_card_number(masked_card_to)
                print(f"{tx['date']} {tx['description']}")
                print(f"Транзакция: {formatted_card_from} -> {formatted_card_to}")
                print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
