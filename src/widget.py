from typing import Union


def mask_account_card(card: Union[str]) -> Union[str]:
    """Функция маскировки банковских карт и счетов"""
    if "Счет" in card:
        return f"{card[:5]}**{card[-4:]}"
    else:
        return f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"


def get_date(date: Union[str]) -> Union[str]:
    """Функция переводит записанную дату в короткий читаемый вариант"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

