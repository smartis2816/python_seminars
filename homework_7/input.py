
def choose_ext():
    return int(input("""Выберите формат, с которым будем работать.
    1) txt
    2) csv
    """))

def input_menu_csv():
    return input("""Введите номер требующегося действия.
    1) Добавить контакт
    2) Найти контакт
    3) Удалить контакт
    4) Показать все контакты
    5) Завершить программу
    """)

def input_menu_txt():
    return input("""Введите номер требующегося действия.
    1) Добавить контакт
    2) Найти контакт
    3) Показать все контакты
    4) Завершить программу
    """)

def input_contact():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    description = input('Введите описание контакта: ')
    info = second_name + ' ' + first_name + ' ' + phone_number + ' ' + description
    return info

def name_contact():
    return input('Введите имя контакта: ')
