import csv
import os
import input

path_csv = r'сontact_book.csv'

def csv_check():
    if os.stat(path_csv).st_size == 0:
        with open (path_csv, 'a', encoding = 'utf-8') as data:
            file_writer = csv.writer(data, delimiter = ";", lineterminator="\r")
            file_writer.writerow(["Фамилия", "Имя", "Номер телефона", "Описание"])

def add_contact(info):
    new_list = info.split()
    with open (path_csv, 'a', encoding = 'utf-8') as data:
        file_writer = csv.writer(data, delimiter = ";", lineterminator="\r")
        file_writer.writerow([new_list[0], new_list[1], new_list[2], new_list[3]])

def find_contact(name):
    with open (path_csv, 'r', encoding = 'utf-8') as data:
        file_reader = csv.reader(data, delimiter = ";", lineterminator="\r")
        for row in file_reader:
            if name in row:
                print('\nФамилия: {}\nИмя: {}\nНомер телефона: {}\nОписание: {}\n'.format(row[0], row[1], row[2], row[3]))

def find_all():
    with open (path_csv, 'r', encoding = 'utf-8') as data:
        file_reader = csv.reader(data, delimiter = ";", lineterminator="\r")
        for row in file_reader:
            print('{:<15} {:<15} {:<15} {:<15}'.format(*row))

def delete_contact(name):
    new_list = []
    with open (path_csv, 'r', encoding = 'utf-8') as data:
        file_reader = csv.reader(data, delimiter = ";", lineterminator="\r")
        for row in file_reader:
            new_list.append(row)
    for item in new_list:
        if name in item:
            new_list.remove(item)
    with open (path_csv, 'w', encoding = 'utf-8') as data:
        file_writer = csv.writer(data, delimiter = ";", lineterminator="\r")
        file_writer.writerows(new_list)