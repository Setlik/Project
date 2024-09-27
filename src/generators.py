from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[str, None, None]:
    """Функция принимает список словарей с транзакциями и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        yield transaction["description"]



def card_number_generator(start_range: int, end_range: int) -> Generator[str, None, None]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X - цифра номера карты.
    Генерирует номера в диапазоне от start_range до end_range включительно."""

    while start_range <= end_range:
        if start_range < 1 or end_range > 9999999999999999:
            raise ValueError("Неверный диапазон значений.")
        card_number = f"{start_range:016d}"
        card_number = " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
        yield card_number
        start_range += 1


