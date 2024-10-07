import logging
import re

import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='C:/Users/kroli/Desktop/home_work/venv/home_work/logs/masks.log',
                    filemode='w')
logger = logging.getLogger()


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты."""
    if not isinstance(card_number, str) or card_number == "":
        logger.warning('Пустой или некорректный номер карты передан для маскировки.')
        return ""
    logger.info('Маскируем номер карты.')
    digits = re.findall(r'\d', card_number)
    if not digits:
        logger.warning('Нет цифр для маскировки в переданном номере карты.')
        return card_number
    if len(digits) < 16:
        logger.warning('Недостаточно цифр для создания номера карты. Возвращаем оригинал.')
        return card_number
    digits = digits[-16:]
    masked_digits = digits[:6] + ['******'] + digits[-4:]
    letters = re.findall(r'\D', card_number)
    masked_card_number = ''.join(masked_digits)
    formatted_card_number = ''.join(letters) + ' '.join(
        masked_card_number[i: i + 4] for i in range(0, len(masked_card_number), 4))
    logger.info(f'Замаскированный номер карты: {formatted_card_number}')
    return formatted_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета."""
    if account_number is None or account_number == "":
        logger.warning('Пустой номер счета передан для маскировки.')
        return ""
    if len(account_number) < 4:
        logger.warning('Недостаточно символов для маскировки, возвращаем оригинал.')
        return account_number
    mask_account = "**" + account_number[-4:]
    return mask_account
