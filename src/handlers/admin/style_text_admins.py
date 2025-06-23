#===========ШРИФТЫ И ТЕКСТЫ С ФОРМАТИРОВАНИЕМ================
async def admins_menu_text():
    text_admin = '''
<pre>░█▀█░█▀▄░█▄█░▀█▀░█▀█░█▀▀
░█▀█░█░█░█░█░░█░░█░█░▀▀█
░▀░▀░▀▀░░▀░▀░▀▀▀░▀░▀░▀▀▀</pre>
<b>СПИСОК КОМАНД АДМИНА:</b>
/dashboard - Меню админа
/user_data_id - Поиск по ID
/mailing - Рассылка
/stats_view - Статистика
/backup_db - Файл базы данных'''
    return text_admin


async def admin_back_text():
    text = f'''
<b>Приветствую админ!</b>
Заходи в чат 

/search - поиск собеседника
'''
    return text
