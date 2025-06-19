



@start_router.message(Command('help'), MenuStates.Main)
async def cmd_start(message: Message, state: FSMContext):
    #========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    #========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        delete_mess_commands(e)
    # ================================
    name = message.from_user.first_name  # Достаем имя пользователя
    text = bot_text_baner()
    await message.answer(text, parse_mode="HTML")
