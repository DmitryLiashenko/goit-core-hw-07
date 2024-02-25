import datetime as dt    
from dataclasses import dataclass          
from datetime import timedelta as td                   
from datetime import datetime as dtdt
from dataclasses import dataclass

def input_error(func):                              # ФУНКЦИЯ-ДЕКОРАТОР ДЛЯ ВВЕДЕННЫХ КОМАНД
    def inner(*args, **kwargs):                     # ФУНКЦИЯ ОБРАБОТКИ ОШИБОК
        try:                                        # НАЧАЛО БЛОКА ОШИБОК
            return func(*args, **kwargs)            # ПРОБУЕМ
        except ValueError:                          # ЕСЛИ ОДНА ИЗ ОШИБОК ВОЗНИКАЕТ 
            return "Give me name and phone please." # 
        except IndexError:                          #
            return "No found"                       #
        except KeyError:                            #
            return "No soch name found" 
        except Exception as e:
            return f'somthing wrong {e}'            # ВОЗВРАЩАЕМ В ФУНКЦИЮ СООБЩЕНИЕ ОБ ОПРЕДЕЛЕННОЙ ОШИБКЕ
    return inner                                    # ВОЗВРАЩАЕМ В ДЕКОРАТОР ФУНКЦИЮ ОБРАБОТКИ ОШИБОК

@input_error                                        # ПРИМЕНЯЕМ ДЕКОРАТОР
def parse_input(user_input):                        # ФУНКЦИЯ ПАРСЕРА КОМАНД           
    cmd, *args = user_input.split()                 # РАЗДЕЛЯЕМ ВВОД НА КОМАНДУ И АРГУМЕНТЫ
    cmd = cmd.strip().lower()                       # ПРИВОДИМ В НИЖНИЙ РЕГИСТР И УДАЛЯЕМ ЛИШНИИ ПРОБЕЛЫ КОМАНДЫ
    return cmd, *args                               # ВОЗВРАЩАЕМ КОМАНДУ И СПИСОК АРГУМЕНТОВ

class BaseClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(BaseClass): 
    pass

class Birthday(BaseClass):
    def __init__(self, birthday):
        try:
            birthday = dtdt.strptime("%Y.%m.%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Phone(BaseClass):
    def __str__(self):
        return self.value if len(self.value) == 10 else f'{self.value} format must be 0970000000'

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if phone not in map(str, self.phones):
            self.phones.append(Phone(phone))
            print("Contact added")
        else:
            return 'Phone already exist in Addressbook'

    def find_phone(self):
        return '; '.join(map(str, self.phones))

    def edit_phones(self, phone):
        self.phones = [Phone(phone)]
        return self.phones
    
    def add_birthday(self,birthday):
        if birthday not in map(str, self.birthday):
            self.birthday.append(Birthday(birthday))
            print("Birthday added")
        else:
            return 'Birthday already exist in Addressbook'

    def __str__(self):
        return f"Contact name: {self.name}, phones: {', '.join(map(str, self.phones))}"

class AddressBook(dict):
    def add_record(self, name, phone):
        if name not in self:
            self[name] = Record(name, phone)
            return f'{name} added'
        else:
            return f'{name} is already in the Addressbook'

    def find_record(self, name):
        return str(self.get(name, f'{name} not found in Addressbook'))

    def delete_record(self, name):
        return f'{name} deleted from Addressbook' if self.pop(name, None) else f'{name} not found in Addressbook'
    
    def get_upcoming_birthdays(book):
        pass



    
    
                               # ФУНКЦИИ ДЛЯ РАБОТЫ ОСНОВНОГО КОДА

book = AddressBook                      # СОЗДАЕМ КНИГУ КОНТАКТОВ КАК ЭКЗЕМПЛЯР КЛАССВ AddressBook
@input_error                            # ПРИМЕНЯЕМ ДЕКОРАТОР
def parse_input(user_input):            # ФУНКЦИЯ ПАРСЕРА КОМАНД           
    cmd, *args = user_input.split()     # РАЗДЕЛЯЕМ ВВОД НА КОМАНДУ И АРГУМЕНТЫ
    cmd = cmd.strip().lower()           # ПРИВОДИМ В НИЖНИЙ РЕГИСТР И УДАЛЯЕМ ЛИШНИИ ПРОБЕЛЫ КОМАНДЫ
    return cmd, *args                   # ВОЗВРАЩАЕМ КОМАНДУ И СПИСОК АРГУМЕНТОВ

@input_error                            # ПРИМЕНЯЕМ ДЕКОРАТОР
def add_contact(args):                  # ФУНКЦИЯ ДОБАВЛЕНИЯ КОНТАКТОВ
    name, phone = args                  # ПРИСВАИВАЕМ АРГУМЕНТЫ ИМЕНИ И ТЕЛЕФОНУ
    record = Record(name)               # СОЗДАЕМ ЗАПИСЬ КЛАССА Record С ИМЕНЕМ
    record.add_phone(phone)             # ИСПОЛЬЗУЯ МЕТОД ДОБАВЛЯЕМ ТЕЛЕФОН
    book.add_record(record)               # МЕТОДОМ ЗАПИСЫВАЕМ В КНИГУ КОНТАКТОВ
    return "Contact added."             # ВОЗВРАШАЕМ В ФУНКЦИЮ СООБЩЕНИЕ ОБ УСПЕШНОЙ ЗАПИСИ
            
@input_error                            
def change_contact(args):           
    name, phone = args
    for key, phone in book.items():     
        if key == name:               
            record = Record(name)
            record.add_phone(phone)
            book.add_record()                  
    return "Contact change"

@input_error                                      
def show_phone(args):
    name = args
    record = Record(name)
    return record.find_phone(name)
                
def show_all(book):
    s = ''                                                  # ОБЪЯВЛЯЕМ ПУСТУЮ СТРОКУ s
    for key, in book.items():                               # ИТЕРИРУЕМ СЛОВАРЬ
        s+=(f"{key:10} : {book[key]:10}\n")                 # ФУНКЦИЯ ВЫВОДИТ ВСЕ КОНТАКТЫ В СЛОВАРЕ(ДОБАВИТЬ \n)
    return print(book)                                      # ВОЗВРАЩАЕМ СЛОВАРЬ В ФУНКЦИЮ

@input_error
def add_birthday(args, book):
    # реалізація
    pass

@input_error
def show_birthday(args, book):
    
@input_error
def birthdays(args, book):
    congratulation_data = []                        # СОЗДАЕМ СПИСОК СЛОВАРЕЙ С ДАТАМИ ПОЗДРАВЛЕНИЙ                          
    today = dtdt.today().date()                     # ОПРЕДЕЛЯЕМ СЕГОДНЯШНЮЮ ДАТУ                                             
    future_day = today + td(days = 7)               # СОЗДАЕМ ПЕРЕМЕННУЮ С ДАТОЙ + 7 ДНЕЙ ОТ СЕГОДНЯШНЕЙ
    pass
    return congratulation_data

                                                   # ОСНОВНАЯ ФУНКЦИЯ 
def main():                                     
    print("Welcome to the assistant bot!")         # ПРИВЕТСТВИЕ
    while True:                                    # ЗАПУСКАЕМ ЦИКЛ
        user_input = input("Enter a command: ")    # ПОЛУЧАЕМ КОМАНДУ
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:           # БЛОК ВЫХОДА ИЗ БОТА
            print("Good bye!")
            break 
        elif command == "hello":                   # БЛОК ЗАПРОСА КОМАНДЫ
            print("How can I help you?")
        elif command == "add":                     # ДОБАВЛЕНИЕ КОНТАКТА
            print(add_contact(args))               # ПЕРЕДАЕМ ФУНКЦИИ АРГУМЕНТЫ И СЛОВАРЬ
        elif command == "change":                  # СМЕНА КОНТАКТА
             print(change_contact(args))           # ПЕРЕДАЕМ ФУНКЦИИ АРГУМЕНТЫ И СЛОВАРЬ
        elif command == "phone":                   # ПОКАЗЫВАЕТ КОНТАКТ ПО ИМЕНИ
            print(show_phone(args[0], book))       # ПЕРЕДАЕМ ФУНКЦИИ АРГУМЕНТЫ И СЛОВАРЬ
        elif command == "all":                     # ПОКАЗЫВВАЕМ ВЕСЬ СЛОВАРЬ
            print(show_all(book))                  # ПЕРЕДАЕМ ФУНКЦИИ СЛОВАРЬ
        elif command == "add-birthday":
            print(add_birthday(args,book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args,book))
        else:                                      
            print("Invalid command.")              # СООБЩАЕМ О НЕ ПРАВИЛЬНОЙ КОМАНДЕ

if __name__ == "__main__":                         # ПРОВЕРКА ЗАПУЩЕННА ЛИ ГЛАВНЫЙ КОД, А НЕ МОДУЛЬ
    main()

    
    