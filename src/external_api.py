import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_exchange_rate(from_currency, to_currency="RUB", amount=1):
    '''функция для обработки запроса к api(конвертера валют)'''
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("result")
    return None


def get_transaction_amount_in_rubles(transaction):
    '''функция которая принимает на вход транзакцию и возвращает сумму транзакции в рублях'''
    amount = transaction["amount"]
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)
    elif currency in ("USD", "EUR"):
        rate = get_exchange_rate(currency)
        if rate is not None:
            return float(amount) * rate
    return None


