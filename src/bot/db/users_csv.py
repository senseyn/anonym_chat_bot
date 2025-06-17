import csv
import os
from datetime import datetime
from aiogram.types import User

# Абсолютный путь к файлу CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), "users_data.csv")

# Заголовки CSV
FIELDNAMES = ["USER_ID", "FIRST_NAME", "LAST_NAME", "USERNAME", "PREMIUM", "LANGUAGE", "IS_BOT", "DATE_JOIN"]


def create_csv_file_if_not_exists() -> None:
    # Создаёт CSV если его ещё нет.
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="w", newline='', encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def normalize_dict_row(row: dict) -> dict:
    # Удаляет BOM и пробелы из ключей строки.
    return {k.strip("\ufeff").strip(): v for k, v in row.items()}


def user_already_exists(user_id: str) -> bool:
    # Проверяет, существует ли пользователь в CSV-файле.
    if not os.path.exists(CSV_PATH):
        return False

    with open(CSV_PATH, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        # Удаление BOM из заголовков
        if reader.fieldnames:
            reader.fieldnames = [field.strip("\ufeff").strip() for field in reader.fieldnames]

        for row in reader:  # type: dict
            cleaned = normalize_dict_row(row)
            if cleaned.get("USER_ID") == user_id:
                return True
    return False


def add_user_check(user: User) -> None:
    # Добавляет пользователя в CSV.
    create_csv_file_if_not_exists()

    user_id = str(user.id)

    if user_already_exists(user_id):
        return

    with open(CSV_PATH, mode="a", newline='', encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            "USER_ID": user_id,
            "FIRST_NAME": user.first_name or "",
            "LAST_NAME": user.last_name or "",
            "USERNAME": "@" + user.username if user.username != "" else "":,
            "PREMIUM": user.is_premium or "",
            "LANGUAGE": user.language_code,
            "IS_BOT": user.is_bot,
            "DATE_JOIN": datetime.now().isoformat(sep=' ', timespec='seconds')
        })


#===========ПРОВЕРКА ДАТЫ И ЕЕ СБОР==========================
# даем функции значение str, если нету вернем тоже либо ничего
def user_registration_date(user_id: str) -> str | None:
    if not os.path.exists(CSV_PATH):
        return None

    with open(CSV_PATH, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames:
            reader.fieldnames = [field.strip("\ufeff").strip() for field in reader.fieldnames]

        for row in reader:  # type: dict
            cleaned = normalize_dict_row(row)
            if cleaned.get("USER_ID") == user_id:
                return cleaned.get("DATE_JOIN")

    return None
