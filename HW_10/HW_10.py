from collections import UserDict
import re


class Field:
    value = None


class Name(Field):
    pass


class Phone(Field):
    pass


class AdressBook(UserDict):
    def add_record(self, name, phone):
        Name.value = name
        Phone.value = phone
        self.data[Record.name.value] = [Record.phone.value]


class Record:
    name = Name()
    phone = Phone()

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def add(self):
        book[self.name].append(self.phone)

    def delete(self):
        book[self.name].remove(self.phone)

    def replace(self):
        book[self.name].clear()
        book[self.name].append(self.phone)


def input_error(func):
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except IndexError:
            print('\nGive me name and/or phone please.\n')

        except KeyError:
            print('\nEnter user name\n')

        except ValueError:
            print('\nGive me name and phone please\n')

    return wrapper


def exit_func(low_client):

    if low_client.strip() in exit_list:
        print('\nGood bye!\n')
        return low_client.strip()

    else:
        return False


def main():
    global book
    book = AdressBook()

    while True:
        client_input = input('Enter command:')
        low_client = client_input.lower()

        if exit_func(low_client):
            break

        elif client_input == '':
            print('\nWrong enter!\nSee README.md for details.\n')
            continue

        elif low_client.split()[0] in command_dict:
            message = command_dict[low_client.split()[0]](client_input)

            if message == None:
               True
            else:
                print(f'\n{message}\n')

        else:
            print('\nWrong enter!\nSee README.md for details.\n')


@input_error
def add_func(client_input):
    pattern = re.search(
        '(?:\+38)?(?:\(0\d{2}\)[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[0-9]{7})', client_input)
    name = client_input.split()[1]
    
    if name in book:
        message = f'Warning: EXISTING name!\nFor updating contact please use "change" command'
        return message

    elif pattern and len(client_input.split()) >= 3:
        phone = pattern.group()
        book.add_record(name, phone)        
        return f"Client {name} is added successfully."

    else:
        return f'Wrong enter!\nSee README.md for details.'


@input_error
def change_func(client_input):
    pattern = re.search('(?:\+38)?(?:\(0\d{2}\)[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[0-9]{7})', client_input)
    name = client_input.split()[1]
    
    if name in book and pattern and len(client_input.split()) >= 3:
        phone = pattern.group()
        Record(name, phone).replace()
        return f"Client {name} is updated successfully."

    elif name not in book:
        return f'Warning: NEW name!\nFor creating contact please use "add" command'

    else:
        return('Wrong enter!\nSee README.md for details.')


@input_error
def add_number(client_input):
    name = client_input.split()[1]
    pattern = re.search('(?:\+38)?(?:\(0\d{2}\)[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[0-9]{7})', client_input)
    
    if name in book and pattern and len(client_input.split()) >= 3:
        phone = pattern.group()
        Record(name, phone).add()
        return f"Client {name} number is added successfully."

    elif name not in book:
        return f'Warning: NEW name!\nFor creating contact please use "add" command'

    else:
        return('Wrong enter!\nSee README.md for details.')

@input_error
def del_number(client_input):
    name = client_input.split()[1]
    pattern = re.search('(?:\+38)?(?:\(0\d{2}\)[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[0-9]{7})', client_input)

    if name in book and pattern and len(client_input.split()) >= 3:
        phone = pattern.group()
        Record(name, phone).delete()
        return f"Client {name} number: {phone} is deleted successfully."

    elif name not in book:
        return f'Warning: entered name doesn\'t exist!\n'

    else:
        return('Wrong enter!\nSee README.md for details.')


@input_error
def phone_func(client_input):
    name = client_input.split()[1]

    if name in book and len(client_input.split()) == 2:
        return book[name]

    elif name in book and len(client_input.split()) != 2:
        return f'Wrong enter!\nSee README.md for details.'

    else:
        return f"{name} name doesn\'t exist.\nPlease recheck name."


def show_all_func(client_input):

    if len(client_input.split()) == 2 and (client_input.split()[0] + ' ' + client_input.split()[1]).lower() == 'show all':

        for key, value in book.items():
            phones = ', '.join(value)
            print(f'\n{key}: {phones}\n')

    else:
        return f'Wrong enter!\nSee README.md for details.'


def hello_func(client_input):

    if len(client_input.split()) == 1:
        return f'How can I help you?'

    else:
        return f'Wrong enter!\nSee README.md for details.'



exit_list = ['good bye', 'close', 'exit']
command_dict = {'add': add_func,
                'change': change_func,
                'add_number': add_number,
                'del_number': del_number,
                'phone': phone_func,
                'show': show_all_func,
                'hello': hello_func}

if __name__ == '__main__':
    main()
