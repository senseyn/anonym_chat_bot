import sqlite3


class Database:
    # ===========ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ=========
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    #===========ДОБАВЛЕНИЕ В ОЧЕРЕДЬ=========
    def add_queue(self, chat_id):
        with self.connection:
def add_queue(self, chat_id):
    with self.connection:
        self.cursor.execute("INSERT INTO queue (chat_id) VALUES (?)", (chat_id,))
        print("✅ added to queue")
