import csv
import os
path_csv = r'сontact_book.csv'
path_txt = r'сontact_book.txt'

def csv_check():
    if os.stat(path_csv).st_size == 0:
        with open (path_csv, 'a', encoding = 'utf-8') as data:
            file_writer = csv.writer(data, delimiter = ";", lineterminator="\r")
            file_writer.writerow(["Фамилия", "Имя", "Номер телефона", "Описание"])

def add_info_csv(info):
    info = info.split()
    with open (path_csv, 'a', encoding = 'utf-8') as data:
        file_writer = csv.writer(data, delimiter = ";", lineterminator="\r")
        file_writer.writerow([info[0], info[1], info[2], info[3]])

def add_info_txt(info):
    info = info.split()
    with open (path_txt, 'a', encoding = 'utf-8') as data:
        data.write('\n\nФамилия: {}\nИмя: {}\nНомер телефона: {}\nОписание: {}\n'.format(info[0], info[1], info[2], info[3]))