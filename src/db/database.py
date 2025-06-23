import sqlite3


class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def add_queue(self, chat_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `queue` (`chat_id`)")
