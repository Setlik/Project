import logging
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='C:/Users/kroli/Desktop/home_work/venv/home_work/logs/masks.log',
                    filemode='w')
logger = logging.getLogger()



def get_mask_card_number(card_number: str) -> str:
    """Функция которая маскирует номер банковской карты"""
    logger.info('Маскируем номер карты.')
    private_number = card_number[:6] + "******" + card_number[-4:]
    formatted_card_number = " ".join(private_number[i: i + 4] for i in range(0, len(private_number), 4))
    if card_number == "":
        logger.warning('Пустой номер карты передан для маскировки.')
        return ""
    logger.info(f'Замаскированный номер карты: {formatted_card_number}')
    return formatted_card_number


def get_mask_account(account_number: str) -> str:
    """Функция которая маскирует номер банковского счета"""
    logger.info('Маскируем номер счета.')
    mask_account = "**" + account_number[-4:]
    if account_number == "":
        logger.warning('Пустой номер счета передан для маскировки.')
        return ""
    logger.info(f'Замаскированный номер счета: {mask_account}')
    return mask_account