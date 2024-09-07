def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item["state"] == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция фильтрует список словарей по значению ключа 'date'
    по умолчанию список фильтруется по убыванию.
    """

    return sorted(data, key=lambda x: x["date"], reverse=reverse)
