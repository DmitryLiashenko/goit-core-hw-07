class BaseClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(BaseClass): 
    pass

class Phone(BaseClass):
    def __str__(self):
        return self.value if len(self.value) == 10 else f'{self.value} format must be 0970000000'

class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]

    def add_phone(self, phone):
        if phone not in map(str, self.phones):
            self.phones.append(Phone(phone))
        else:
            return 'Phone already exist in Addressbook'

    def find_phone(self):
        return '; '.join(map(str, self.phones))

    def edit_phones(self, phone):
        self.phones = [Phone(phone)]
        return self.phones

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