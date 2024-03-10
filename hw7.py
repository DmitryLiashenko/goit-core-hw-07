import pickle
import datetime as dt
from dataclasses import dataclass
from datetime import timedelta as td
from datetime import datetime as dtdt



def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "No found"
        except KeyError:
            return "No such name found"
        except Exception as e:
            return f'Something wrong {e}'
    return inner

@input_error
def get_upcoming_birthdays(book):
    congratulation_data = []
    today = dtdt.today().date()
    future_day = today + td(days=7)
    for record in book.values():
        if record.birthday:
            birthday = record.birthday.value
            birthday_date = dt.date(today.year, birthday.month, birthday.day)
            if (today < birthday_date) and (birthday_date <= future_day):
                if birthday_date.weekday() == 5:
                    birthday_date = birthday_date + td(days=2)
                    congratulation_data.append({'name': record.name.value, 'congratulation_date': birthday_date.strftime("%Y-%m-%d")})
                elif birthday_date.weekday() == 6:
                    birthday_date = birthday_date + td(days=1)
                    congratulation_data.append({'name': record.name.value, 'congratulation_date': birthday_date.strftime("%Y-%m-%d")})
                else:
                    congratulation_data.append({'name': record.name.value, 'congratulation_date': birthday_date.strftime("%Y-%m-%d")})
    return congratulation_data

@dataclass
class BaseClass:
    value: str

    def __str__(self):
        return str(self.value)


@dataclass
class Name(BaseClass):
    pass


@dataclass
class Birthday(BaseClass):
    def __init__(self, birthday):
        try:
            self.value = dtdt.strptime(birthday, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")


@dataclass
class Phone(BaseClass):
    def __str__(self):
        return self.value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if phone not in map(str, self.phones):
            self.phones.append(Phone(phone))
        else:
            return 'Phone already exists in Addressbook'

    def find_phone(self):
        return '; '.join(map(str, self.phones))

    def edit_phones(self, phone):
        self.phones = [Phone(phone)]
        return self.phones

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return "Birthday added or changed"
        

    def __str__(self):
        birthday_str = f"birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name}, phones: {', '.join(map(str, self.phones))}, {birthday_str}"

    def __str__(self):
        return f"Contact name: {self.name}, phones: {', '.join(map(str, self.phones))}, birthday: {self.birthday}"


class AddressBook(dict):
    def add_record(self, record):
        if record.name.value not in self:
            self[record.name.value] = record
            return record.name.value
        else:
            return f'{record.name.value} is already in the Addressbook'

    def find_record(self, name):
        return str(self.get(name, f'{name} not found in Addressbook'))

    def delete_contact(self, name):
        return f'{name} deleted from Addressbook' if self.pop(name, None) else f'{name} not found in Addressbook'
     
    def save_data(book, filename="addressbook.pkl"):
            with open(filename, "wb") as f:
                pickle.dump(book, f)

    def load_data(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
                book = AddressBook()
                return book

    def add_birthday(self, name, birthday):
        record = self.get(name)
        if record:
            return record.add_birthday(birthday)
        else:
            return f"{name} not found in Addressbook"

    def show_birthday(self, name):
        record = self.get(name)
        return record.birthday.value if record and record.birthday else f"{name} has no birthday in Addressbook"


    def get_upcoming_birthdays(self):
        users = [{'name': record.name.value, 'birthday': record.birthday.value.strftime("%Y-%m-%d")} for record in self.values() if record.birthday]
        congratulation_data = get_upcoming_birthdays(users)
        return congratulation_data


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book):
    name, phone = args
    if len(phone) == 10:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added"
    else:
        return "format must be 0970000000"

        


@input_error
def change_contact(args, book):
    name, phone = args
    for key, record in book.items():
        if key == name:
            record.edit_phones(phone)
            return "Contact changed"
    return "Contact not found"


@input_error
def show_phone(args, book):
    name = args[0]
    record = book.get(name)
    return record.find_phone() if record else f"{name} not found in Addressbook"

@input_error
def delete_contact(args, book):
    name = args[0]
    result = book.delete_contact(name)
    return result


def show_all(book):
    for key, record in book.items():
        print(record)


@input_error
def add_birthday(args, book):
    name, birthday = args
    result = book.add_birthday(name, birthday)
    return result


@input_error
def show_birthday(args, book):
    name = args[0]
    result = book.show_birthday(name)
    return result


@input_error
def birthdays(args, book) -> str:
    congratulation_data = get_upcoming_birthdays(book)
    
    messages = []
    for data in congratulation_data:
        message = f"Предстоящий день рождения: {data['name']}, дата: {data['congratulation_date']}"
        messages.append(message)
    
    return "\n".join(messages)

def main():
    print("Welcome to the assistant bot!")
    book = AddressBook.load_data("addressbook.pkl")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            AddressBook.save_data(book)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "delete":
            print(delete_contact(args, book))
        elif command == "all":
            show_all(book)
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            result = birthdays(args, book)
            print(result)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()