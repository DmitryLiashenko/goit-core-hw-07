                            # ФУНКЦИЯ ДЛЯ ОПРЕДЕЛЕНИЯ ДАТЫ ПОЗДРОВЛЕНИЯ

import datetime as dt                                  # ИМПОРТИРУЕМ МОДУЛЬ
from datetime import timedelta as td                   # С МОДУЛЯ ИМПОРТИРУЕМ КЛАС timedelta
from datetime import datetime as dtdt                  # С МОДУЛЯ ИМПОРТИРУЕМ КЛАС datetime
users = [                                              # СПИСОК СЛОВАРЕЙ С ДАТАМИ РОЖДЕНИЯ (для примера)
    {"name": "John Doe", "birthday": "1985.02.25"},
    {"name": "Jane Smith", "birthday": "1990.02.28"}
]

def get_upcoming_birthdays(users = None):                                 # СОЗДАЕМ ФУНКЦИЮ                                            
    try:                                                                  # НАЧАЛО БЛОКА ОБРАБОТКИ ОШИБОК
        congratulation_data = []                                          # СОЗДАЕМ СПИСОК СЛОВАРЕЙ С ДАТАМИ ПОЗДРАВЛЕНИЙ                          
        today = dtdt.today().date()                                       # ОПРЕДЕЛЯЕМ СЕГОДНЯШНЮЮ ДАТУ                                             
        future_day = today + td(days = 7)                                 # СОЗДАЕМ ПЕРЕМЕННУЮ С ДАТОЙ + 7 ДНЕЙ ОТ СЕГОДНЯШНЕЙ
        for user in users:                                                # ПЕРЕБИРАЕМ ДАННЫЕ В СПИСКЕ     
            birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date() # ПЕРЕВОДИМ СТРОКУ ДНЯ РОЖДЕНИЯ В ОБЪЕКСТ datetime
            birthday = dt.date(today.year,birthday.month, birthday.day )  # МЕНЯЕМ ГОД ДЛЯ РОЖДЕНИЯ НА ТЕКУЩИЙ
            if (today < birthday) and (birthday <= future_day):           # ПРОВЕРЯЕМ БУДЕТ ЛИ ДР В БЛИЖАЙШИЕ 7 ДНЕЙ(ВКЛЮЧИТЕЛЬНО)
                if birthday.weekday() == 5:                               # БЕРЕМ ДЕНЬ НЕДЕЛИ ДР И ПРОВЕРЯЕМ ЕСЛИ ЭТО НЕ СУББОТА 
                    birthday = birthday + td(days = 2)                    # ЕСЛИ СУББОТА ДОБАВЛЯЕМ К ДАТЕ 2 ДНЯ      
                    congratulation_data.append({'name':user['name'], 'congratulation_date':birthday.strftime("%Y.%m.%d")})  # ДОБАВЛЯЕМ СЛОВАРЬ В СПИСОК
                elif birthday.weekday() == 6:                                                                               # БЕРЕМ ДЕНЬ НЕДЕЛИ ДР И ПРОВЕРЯЕМ ЕСЛИ ЭТО НЕ ВОСКРЕСЕНИЕ
                    birthday = birthday + td(days = 1)                                                                      # ЕСЛИ ДА, ТО ДОБАВЛЯЕМ ОДИН ДЕНЬ К ДАТЕ ПОЗДРАВЛЕНИЯ
                    congratulation_data.append({'name':user['name'], 'congratulation_date':birthday.strftime("%Y.%m.%d")})  # ДОБАВЛЯЕМ СЛОВАРЬ В СПИСОК
                else:                                                                                                       # ЕСЛИ БУДНИЙ ДЕНЬ 
                    congratulation_data.append({'name':user['name'], 'congratulation_date':birthday.strftime("%Y.%m.%d")})  # ЗАНОСИМ В СПИСОК БЕЗ ИЗМЕНЕНИЙ
        return congratulation_data
    except Exception:                                                                                                       # кОНЕЦ БЛОКА ОБРАБОТКИ ОШИБОК
        print("Something bad")                                                                                              # ВОЗВРАЩАЕМ СПИСОК СЛОВАРЕЙ В ФУНКЦИЮ
print(get_upcoming_birthdays(users))    
        