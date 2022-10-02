import input
path_txt = r'сontact_book.txt'

def add_contact(info):
    info = info.split()
    with open (path_txt, 'a', encoding = 'utf-8') as data:
        data.write('\nФамилия: {}\nИмя: {}\nНомер телефона: {}\nОписание: {}\n***'.format(info[0], info[1], info[2], info[3]))


def find_contact(name):
    with open (path_txt, 'r', encoding = 'utf-8') as data:
        new_list = data.read()
        new_list = new_list.split('***')
        new_list = [item.replace('\n', ' ') for item in new_list]
        for item in new_list:
            if name in item:
                print(item)

def find_all():
    with open (path_txt, 'r', encoding = 'utf-8') as data:
        print(data.read())