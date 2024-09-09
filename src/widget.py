def mask_account_card(card: str) -> str:
    """Функция маскировки банковских карт и счетов"""
    if card == "":
        return ""
    elif "Счет" in card:
        return f"{card[:5]}**{card[-4:]}"
    else:
        return f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"


def get_date(date: str) -> str:
    """Функция переводит записанную дату в короткий читаемый вариант"""
    if date == "":
        return ""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
