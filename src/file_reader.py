import json
import csv

import openpyxl
from typing import List, Dict


def load_json(file_path: str) -> List[Dict]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_csv(file_path: str) -> List[Dict]:
    transactions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if row["id"] == '' or row["state"] == '' or row["date"] == '':
                    continue

                transactions.append({
                    "id": int(row["id"]),
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {
                            "name": row["currency_name"],
                            "code": row["currency_code"]
                        }
                    },
                    "from": row.get("from", ''),
                    "to": row.get("to", ''),
                    "description": row["description"]
                })
        return transactions
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []


def load_xlsx(file_path: str) -> List[Dict]:
    transactions = []
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_data = dict(zip(headers, row))
            if row_data["id"] is None or row_data["state"] is None or row_data["date"] is None:
                continue

            transactions.append({
                "id": int(row_data["id"]),
                "state": row_data["state"],
                "date": row_data["date"],
                "operationAmount": {
                    "amount": row_data["amount"],
                    "currency": {
                        "name": row_data["currency_name"],
                        "code": row_data["currency_code"]
                    }
                },
                "from": row_data.get("from", ""),
                "to": row_data.get("to", ""),
                "description": row_data["description"]
            })
        return transactions
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
