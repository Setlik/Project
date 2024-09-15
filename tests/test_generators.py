import pytest

from generators import card_number_generator, transaction_descriptions, filter_by_currency
from tests.conftest import transaction


def test_filter_by_currency_usd(transaction):
    filtered_transactions = list(filter_by_currency(transaction, "USD"))
    assert len(filtered_transactions) == 3
    for transaction in filtered_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_rub(transaction):
    filtered_transactions = list(filter_by_currency(transaction, "RUB"))
    assert len(filtered_transactions) == 2
    for transaction in filtered_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "RUB"


def test_filter_by_currency_empty(transaction):
    filtered_transactions = list(filter_by_currency(transaction, "EUR"))
    assert len(filtered_transactions) == 0


def test_filter_by_currency_empty_list():
    filtered_transactions = list(filter_by_currency([], "USD"))
    assert len(filtered_transactions) == 0


def test_transaction_descriptions(transaction):
    descriptions = list(transaction_descriptions(transaction))
    assert len(descriptions) == len(transaction)
    for i, description in enumerate(descriptions):
        assert description == transaction[i]["description"]


def test_transaction_descriptions_empty_list():
    descriptions = list(transaction_descriptions([]))
    assert len(descriptions) == 0


def test_card_number_generator_invalid_range():
    with pytest.raises(ValueError):
        list(card_number_generator(0, 10000000000000000))


def test_card_number_generator_empty_range():
    card_numbers = list(card_number_generator(1, 0))
    assert len(card_numbers) == 0


def test_card_number_generator():
    # Проверяем диапазон от 1234567890123456 до 1234567890123459
    start_range = 1
    end_range = 5

    # Получаем все номера карт из генератора
    card_numbers = list(card_number_generator(start_range, end_range))

    # Проверяем, что количество номеров соответствует диапазону
    assert len(card_numbers) == end_range - start_range + 1

    # Проверяем, что все номера имеют правильный формат
    for card_number in card_numbers:
        # Проверяем, что номер состоит из 16 цифр, разделенных пробелами
        assert len(card_number.replace(" ", "")) == 16
