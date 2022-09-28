
def input_data():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    description = input('Введите описание контакта: ')
    info = second_name + ' ' + first_name + ' ' + phone_number + ' ' + description
    return info