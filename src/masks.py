from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    ''' Функция которая маскирует номер банковской карты'''
    private_number = card_number[:6] + "******" + card_number[-4:]
    formatted_card_number = " ".join(private_number[i : i + 4] for i in range(0, len(private_number), 4))
    return formatted_card_number




def get_mask_account(account_number: Union[str]) -> Union[str]:
    ''' Функция которая маскирует номер банковского счета'''
    mask_account = '**' + account_number[-4:]
    return mask_account




