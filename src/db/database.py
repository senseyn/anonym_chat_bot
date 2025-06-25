import sqlite3


class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    #===========ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ=========
    def add_queue(self, chat_id):
        with self.connection:
            # проверяем наличие юзера в таблице очереди
            self.cursor.execute("SELECT * FROM queue WHERE chat_id = ?", (chat_id,))
            presence_user = self.cursor.fetchone()

            if presence_user is None:
                # Если пользователя нету добавляем его
                self.cursor.execute("INSERT INTO queue (chat_id) VALUES (?)", (chat_id,))
                print(f"Пользователь: {chat_id} добавлен в очередь")
                return False
            else:
                print(f"Пользователь: {chat_id} уже в очереди")
                return True

    def delete_queue(self, chat_id):
        with self.connection:
            self.cursor.execute("DELETE FROM queue WHERE chat_id = ?", (chat_id,))
            print(f"Пользователь: {chat_id} вышел из очереди")

    #===========СОЗДАНИЕ ДИАЛОГА=========
    def get_chat(self):
        with self.connection:
            chat = self.cursor.execute("SELECT * FROM queue", ()).fetchmany(1)
            if bool(len(chat)):
                for row in chat:
                    return row[1]
            else:
                return False

    def create_chat(self, chat_one, chat_two):
        with self.connection:
            if chat_two != 0:
                # СОЗДАНИЕ ЧАТА
                self.cursor.execute("DELETE FROM queue WHERE chat_id = ?", (chat_two,))
                self.cursor.execute("INSERT INTO chats (chat_one, chat_two) VALUES (?, ?)", (chat_one, chat_two,))
                print(f"Чат был создан {chat_one, chat_two}")
                return True
            else:
                # СТАНОВИМСЯ В ОЧЕРЕДЬ
                return False

    def get_active_chat_delete(self, chat_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM chats WHERE chat_one = ? OR chat_two = ?", (chat_id, chat_id))

            chat = self.cursor.fetchone()

            # Если чат есть вернем информацию
            if chat:
                chat_info = {"id": chat[0], "user_one": chat[1], "user_two": chat[2]}
                chat_id_to_delete = chat[0]
                # Запрос на удаление чата из базы
                self.cursor.execute("DELETE FROM chats WHERE id = ?", (chat_id_to_delete,))
                print(f"Чат с id {chat_id_to_delete} был удален.")
                return chat_info
            else:
                return False


    def get_active_chat(self, chat_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM chats WHERE chat_one = ? OR chat_two = ?", (chat_id, chat_id))

            chat = self.cursor.fetchone()

            # Если чат есть вернем информацию
            if chat:
                chat_info = {"id": chat[0], "user_one": chat[1], "user_two": chat[2]}
                return chat_info
            else:
                print(f'Чат не найден для {chat_id}')
                return False