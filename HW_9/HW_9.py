import re


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
    pattern = re.search('(?:\+38)?(?:\(0\d{2}\)[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[0-9]{7})', client_input)
    if client_input.split()[1] in phone_book:
        message = f'Warning: EXISTING name!\nFor updating contact please use "change" command'
        return message
    elif pattern and len(client_input.split()) >= 3:
        phone_book[client_input.split()[1]] = pattern.group()
        return f"Client {client_input.split()[1]} is added successfully."
    else:
        return f'Wrong enter!\nSee README.md for details.'

@input_error
def change_func(client_input):
    pattern = re.search('(?:\+38)?(?:\(0\d{2}\)[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[ .-]?[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}|0\d{2}[0-9]{7})', client_input)
    if client_input.split()[1] in phone_book and pattern and len(client_input.split()) >= 3:
        phone_book[client_input.split()[1]] = pattern.group()
        return f"Client {client_input.split()[1]} is updated successfully."
    elif client_input.split()[1] not in phone_book:
        return f'Warning: NEW name!\nFor creating contact please use "add" command'
    else:
        return('Wrong enter!\nSee README.md for details.')


@input_error
def phone_func(client_input):
    if client_input.split()[1] in phone_book and len(client_input.split()) == 2:
        return phone_book[client_input.split()[1]]
    elif client_input.split()[1] in phone_book and len(client_input.split()) != 2:
        return f'Wrong enter!\nSee README.md for details.'
    else:
        return f"{client_input.split()[1]} name doesn\'t exist.\nPlease recheck name."


def show_all_func(client_input):
    if len(client_input.split()) == 2 and (client_input.split()[0] + ' ' + client_input.split()[1]).lower() == 'show all':
        for key, value in phone_book.items():
            print(f'\n{key}: {value}\n')
    else:
        return f'Wrong enter!\nSee README.md for details.'

        
def hello_func(client_input):
    if len(client_input.split()) == 1:
        return f'How can I help you?'
    else:
        return f'Wrong enter!\nSee README.md for details.'



phone_book = {}
exit_list = ['good bye', 'close', 'exit']
command_dict = {'add': add_func,
                'change': change_func, 
                'phone': phone_func, 
                'show': show_all_func,
                'hello': hello_func}


main()
