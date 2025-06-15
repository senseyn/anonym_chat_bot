import csv
import os
from datetime import datetime
from aiogram.types import User

# Абсолютный путь к файлу CSV, независимо от текущей рабочей директории
CSV_PATH = os.path.join(os.path.dirname(__file__), "users_data.csv")

# Заголовки CSV
FIELDNAMES = ["user_id", "first_name", "last_name", "username", "date_joined"]


def create_csv_file_if_not_exists() -> None:
    """
    Создаёт CSV-файл с заголовками, если его ещё нет.
    """
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="w", newline='', encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def normalize_dict_row(row: dict) -> dict:
    """
    Удаляет BOM и пробелы из ключей строки.
    """
    return {k.strip("\ufeff").strip(): v for k, v in row.items()}


def user_already_exists(user_id: str) -> bool:
    """
    Проверяет, существует ли пользователь в CSV-файле.
    """
    if not os.path.exists(CSV_PATH):
        return False

    with open(CSV_PATH, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        # Удалим BOM из заголовков (если есть)
        if reader.fieldnames:
            reader.fieldnames = [field.strip("\ufeff").strip() for field in reader.fieldnames]

        for row in reader:  # type: dict
            cleaned = normalize_dict_row(row)
            if cleaned.get("user_id") == user_id:
                return True
    return False


def add_user_check(user: User) -> None:
    """
    Добавляет пользователя в CSV, если он ещё не был добавлен.
    """
    create_csv_file_if_not_exists()

    user_id = str(user.id)

    if user_already_exists(user_id):
        return

    with open(CSV_PATH, mode="a", newline='', encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            "user_id": user_id,
            "first_name": user.first_name or "",
            "last_name": user.last_name or "",
            "username":  "@" + user.username or "",
            "date_joined": datetime.now().isoformat(sep=' ', timespec='seconds')
        })
