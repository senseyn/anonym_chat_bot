#===========ШРИФТЫ И ТЕКСТЫ С ФОРМАТИРОВАНИЕМ================
def bot_text_baner(FIRST_NAME, DATE_REG):  #ТЕКСТ ПРИЕТСТВИЯ В САМОМ БОТЕ
    text_baner = f'''
<pre>░█▀█░█▀█░█▀█░█▀█░▀█▀░█▄█░░░█▀▄░█▀█░▀█▀
░█▀█░█░█░█░█░█░█░░█░░█░█░░░█▀▄░█░█░░█░
░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░░▀▀░░▀▀▀░░▀░</pre>
<pre>  ,d88b.d88b,    © 2025 Anonymous Chat
  88888888888    ПРИВЕТСТВУЮ ТЕБЯ!
  `Y8888888Y'    {FIRST_NAME}   
    `Y888Y'      ДАТА РЕГИСТРАЦИИ:              
      `Y'        {DATE_REG}  
</pre>
Привет, <b>{FIRST_NAME}</b>\nЭто телеграмм бот для анонимного общения. Пиши о своих мыслях и идеях\n
<i>* все абсолютно анонимно 🥷</i>\n<i>* только лицам, достигшим 18 лет 🔞</i>\n\n<b>ВЫБЕРИ КНОПКУ НИЖЕ ↓</b>'''
    return text_baner


#================ВЫВОД В КОНСОЛЬ=============================
def start_text_bot():  #ТЕКСТ ЗАПУСКА БОТА
    print("\033[1;42mБОТ ЗАПУЩЕН\033[0m")


def stop_text_bot():  #ТЕКСТ ОСТАНОВКИ БОТА
    print("\033[1;42mБОТ ОСТАНОВЛЕН\033[0m")
