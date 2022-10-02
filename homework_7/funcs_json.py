import json
import input
path_json = r'сontact_book.json'

def add_contact(info):
    info = info.split()
    dictionary = [{"info": [{
    "Фамилия": info[0],
    "Имя": info[1],
    "Номер телефона": info[2],
    "Описание": info[3]
    }]}]
    with open(path_json,'r') as data:
        a = json.load(data)
    with open(path_json,'w') as data:
        b = a[0]('info')
        user_info = {'Фамилия': info[0], 'Имя': info[1], 'Номер телефона': info[2], 'Описание': info[3]}
        b.append(user_info)
        json.dump(a, data, indent=4)

    # data = json.load(open(path_json))
    # if type(data) is dict:
    #     data = [data]
    # data.append(dictionary)
    # print(data)
    # with open (path_json, 'w') as data:
    #     json.dump(dictionary, data)

def find_all():
    with open (path_json, 'r') as data:
        json_object = json.load(data)
        print(json_object)


add_contact(input.input_contact())
# find_all()

