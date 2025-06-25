#=========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram import Router, F  # - магический фильтр
from aiogram.fsm.context import FSMContext
# from aiogram.enums import ChatAction
from aiogram.types import Message

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from create_bot import bot
from src.db.database import Database
from src.keyboards.user_kb import stop_search_button, start_search_button, button_user_search_dialog
from src.middlewares.command_setter import set_commands_state
from src.states.menu_states import MenuStates, MenuSearch

#======================================
match_router = Router()

db = Database(r'src/db/db_handler.db')  # база данных


#======================КОМАНДЫ БОТА==============================
@match_router.message(F.text.in_(["➡️ Следующий", "/search"]), MenuSearch.Search)
async def search_next_user(message: Message):
    # ПРОВЕРКА НАЛИЧИЯ В ПОИСКЕ ИЛИ ПЕРЕКЛЮЧЕНИЕ НА СЛЕДУЮЩЕГО
    chat_id = message.chat.id
    if db.add_queue(chat_id) is True:
        await message.answer(f"ВЫ УЖЕ В ОЧЕРЕДИ! \n/stop - остановить поиск", parse_mode="HTML")
    else:
        # button = await button_user_search_dialog() # для другой функции
        button = await stop_search_button()
        try:
            db.add_queue(chat_id)  # ДОБАВЛЕНИЕ В БАЗУ
            await message.answer(f"Поиск собеседника.. \n/stop - остановить поиск", parse_mode="HTML",
                                 reply_markup=button)
        except Exception as e:
            await message.answer(
                "Произошла ошибка при добавлении вас в очередь. Пожалуйста, попробуйте еще раз.")
            print(f"Ошибка добавления в очередь: {e}")


@match_router.message(F.text.in_(["❤️ Начать поиск", "/search"]), MenuStates.Main)
async def search_new_user(message: Message, state: FSMContext):
    chat_id = message.chat.id
    if message.chat.type == "private":
        await state.set_state(MenuSearch.Search)
        await set_commands_state(state, message.chat.id)
        button = await stop_search_button()
        button_false = await start_search_button()
        button_new_chat = await button_user_search_dialog()
        chat_two = db.get_chat()  # получание айди второго собеседника который первый в очереди

        if db.create_chat(chat_id, chat_two) is False:
            try:
                db.add_queue(chat_id)  # ДОБАВЛЕНИЕ В БАЗУ
                await message.answer(f"Поиск собеседника.. \n/stop - остановить поиск", parse_mode="HTML",
                                     reply_markup=button)
            except Exception as e:
                await state.set_state(MenuStates.Main)
                await set_commands_state(state, message.chat.id)
                await message.answer(
                    '''Произошла ошибка при добавлении вас в очередь. Пожалуйста, попробуйте еще раз.
                    Нажмите /search - поиска собеседника
                    ''', parse_mode="HTML", reply_markup=button_false
                )
                print(f"Ошибка добавления в очередь: {e}")
        else:
            text_create_chat = '''
Собеседник найден!\n
Следующий собеседник - /search
Остановить диалог - /stop
'''
            await message.answer(text_create_chat, parse_mode="HTML", reply_markup=button_new_chat)
            await bot.send_message(chat_id=chat_two, text=text_create_chat, parse_mode="HTML",
                                   reply_markup=button_new_chat)
    else:
        await message.answer("Эта команда доступна только в личных сообщениях.")


@match_router.message(F.text.in_(["❌ Остановить поиск", "/stop", "🚫 Закончить диалог"]), MenuSearch.Search)
async def search_stop_user(message: Message, state: FSMContext):
    global stop_user, no_stop_user
    chat_id = message.chat.id
    chat_info = db.get_active_chat_delete(chat_id)  # получаем айди
    button = await start_search_button() # главное меню кнопок

    if chat_info:
        print(chat_info, chat_id)
        # Определяем собеседников
        stop_user_one = chat_info.get('user_one')
        stop_user_two = chat_info.get('user_two')

        if str(chat_id) == stop_user_one:
            stop_user = stop_user_one
            no_stop_user = stop_user_two
        elif str(chat_id) == stop_user_two:
            stop_user = stop_user_two
            no_stop_user = stop_user_one
        else:
            await message.answer("Вы не находитесь в активном чате.")

        try:
            # Отправляем сообщение о завершении
            await bot.send_message(chat_id=stop_user, text="Вы закончили диалог", parse_mode="HTML",
                                   reply_markup=button)
            await bot.send_photo(chat_id=no_stop_user, text="Собеседник закончил диалог", parse_mode="HTML",
                                 reply_markup=button)
            # состояние 1 юзера
            await state.set_state(MenuStates.Main)
            await set_commands_state(state, message.chat.id)
            # состояние 2 юзера.
            user_state_info = state.storage
            await user_state_info.set_state(no_stop_user, MenuStates.Main)
            await set_commands_state(state, no_stop_user)

            print(f"Завершение диалога отпрвленно пользователю {no_stop_user}.")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
            await message.answer("Произошла ошибка при завершении чата")
    else:
        # удаляем пользователя из очереди
        try:
            db.delete_queue(chat_id)  # УДАЛЕНИЕ ИЗ ОЧЕРЕДИ
            await state.set_state(MenuStates.Main)
            await set_commands_state(state, message.chat.id)
            await message.answer(f"Поиск остановлен. \n/search - начать поиск", parse_mode="HTML", reply_markup=button)
        except Exception as e:
            await state.set_state(MenuStates.Main)
            await set_commands_state(state, message.chat.id)
            await message.answer("Произошла ошибка при остановке поиска. Вы в главном меню", parse_mode="HTML",
                                 reply_markup=button)
            print(f"Ошибка удаления из очереди: {chat_id}, {e}")


# Обработчик сообщений
@match_router.message(F.text)
async def handle_photo_message(message: Message):
    # Логика для обработки фото сообщений
    await forward_message(message)


@match_router.message(F.photo)
async def handle_photo_message(message: Message):
    # Логика для обработки фото сообщений
    await forward_message(message)


@match_router.message(F.sticker)
async def handle_photo_message(message: Message):
    # Логика для обработки фото сообщений
    await forward_message(message)


@match_router.message(F.video)
async def handle_photo_message(message: Message):
    # Логика для обработки фото сообщений
    await forward_message(message)


@match_router.message(F.animation)
async def handle_photo_message(message: Message):
    # Логика для обработки фото сообщений
    await forward_message(message)


@match_router.message(F.audio)
async def handle_photo_message(message: Message):
    # Логика для обработки фото сообщений
    await forward_message(message)


@match_router.message(F.voice)
async def handle_photo_message(message: Message):
    # Логика для обработки фото сообщений
    await forward_message(message)


@match_router.message(F.video_note)
async def handle_photo_message(message: Message):
    # Логика для обработки фото сообщений
    await forward_message(message)


async def forward_message(message: Message):
    # перенаправления сообщения между пользователями.
    chat_id = message.chat.id
    chat_info = db.get_active_chat(chat_id) # проверка наличия чата в базе
    if chat_info:
        # Определяем собеседников
        user_one = chat_info.get('user_one')
        user_two = chat_info.get('user_two')

        if str(chat_id) == user_one:
            recipient = user_two
        elif str(chat_id) == user_two:
            recipient = user_one
        else:
            await message.answer("Вы не находитесь в активном чате.")
            return

        try:
            # Перенаправляем сообщения
            if message.text:
                await bot.send_message(recipient, message.text)
            elif message.photo:
                await bot.send_photo(recipient, message.photo[-1].file_id)
            elif message.sticker:
                await bot.send_sticker(recipient, message.sticker.file_id)
            elif message.video:
                await bot.send_video(recipient, message.video.file_id)
            elif message.animation:
                await bot.send_animation(recipient, message.animation.file_id)
            elif message.audio:
                await bot.send_animation(recipient, message.audio.file_id)
            elif message.voice:
                await bot.send_voice(recipient, message.voice.file_id)
            elif message.video_note:
                await bot.send_video_note(recipient, message.video_note.file_id)

            print(f"Сообщение отправлено пользователю {recipient}.")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
            await message.answer("Произошла ошибка при отправке сообщения собеседнику.")
    else:
        await message.answer("Вы не в чате. Пожалуйста, начните новый поиск.")
