
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# text = 'Мы неабв очень любим Питон иабв Джавабв'
# text_find = 'абв'

# list1 = text.split(' ')
# print(list1)

# list2 = [item for item in list1 if text_find not in item]
# print(list2)

# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют
# два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# from ast import Try
# import random

# def initial ():
#     s = ('\nВас приветствует игра "Цифры и котлеты"!\n'
#         'Задача игроков - поочерёдно брать котлеты в количестве от 1 до 28 штук.\n'
#         'Игра заканчивается, когда котлет не останется.\n'
#         'Выигрывает тот, кто последним возьмёт котлеты. Именно он и получит весь стек котлет.\n')
#     print(s)
#     choice = int(input('Напиши цифру 0, если хочешь сыграть против человека, или 1, если - против бота: '))
#     if choice == 0:
#         player_1 = input('Игрок №1, представься: ')
#         player_2 = input('Игрок №2, представься: ')
#     else:
#         player_1 = input('Игрок, представься: ')
#         player_2 = 'smart_bot'
#     toss = random.randint(0,1)
#     if toss == 0:
#         print(f'Первым будет ходить {player_1}')
#         players_list = [player_1, player_2]
#     else:
#         print(f'Первым будет ходить {player_2}')
#         players_list = [player_2, player_1]
#     return players_list

# def human_or_bot(players_list):
#     if not 'smart_bot' in players_list:
#         return 0
#     else:
#         return 1

# def game_human (players_list, sum, rate):
#     while sum > 0:
#         print(f'\nТвой ход, {players_list[0]}!')
#         turn = int(input('Напиши, сколько котлет ты возмёшь: '))
#         while (turn < 1) or (turn > rate):
#             turn = int(input(f'В свой ход можно брать от 1 до {rate} котлет. Попробуй ещё раз: '))
#         sum -= turn
#         print(f'Оставшееся количество котлет - {sum}')
#         if sum == 0:
#             count_1, count_2 = 1, 0
#             return [count_1, count_2]

#         print(f'\nТвой ход, {players_list[1]}!')
#         turn = int(input('Напиши, сколько котлет ты возмёшь: '))
#         while (turn < 1) or (turn > rate):
#             turn = int(input(f'В свой ход можно брать от 1 до {rate} котлет. Попробуй ещё раз: '))
#         sum -= turn
#         print(f'Оставшееся количество котлет - {sum}')
#         if sum == 0:
#             count_1, count_2 = 0, 1
#             return [count_1, count_2]

# def game_bot (players_list, sum, rate):
#     while sum > 0:
#         if 'smart_bot' in players_list[0]:
#             print('Ходит бот.')
#             turn = (sum%(rate + 1))
#             sum -= turn
#             print(f'Количество взятых ботом котлет - {turn}')
#             print(f'Оставшееся количество котлет - {sum}')
#             if sum == 0:
#                 count_1, count_2 = 1, 0
#                 return [count_1, count_2]
#             print(f'Твой ход, {players_list[1]}!')
#             turn = int(input())
#             while (turn < 1) or (turn > rate):
#                 turn = int(input(f'В свой ход можно брать от 1 до {rate} котлет. Попробуй ещё раз: '))
#             sum -= turn
#             print(f'Оставшееся количество котлет - {sum}')
#             if sum == 0:
#                 count_1, count_2 = 0, 1
#                 return [count_1, count_2]
#         else:
#             print(f'Твой ход, {players_list[0]}!')
#             turn = int(input('Напиши, сколько котлет ты возмёшь: '))
#             while (turn < 1) or (turn > rate):
#                 turn = int(input(f'В свой ход можно брать от 1 до {rate} котлет. Попробуй ещё раз: '))
#             sum -= turn
#             print(f'Оставшееся количество котлет - {sum}')
#             if sum == 0:
#                 count_1, count_2 = 1, 0
#                 return [count_1, count_2]
#             print('Ходит бот.')
#             turn = (sum%(rate + 1))
#             sum -= turn
#             print(f'Количество взятых ботом котлет - {turn}')
#             print(f'Оставшееся количество котлет - {sum}')
#             if sum == 0:
#                 count_1, count_2 = 0, 1
#                 return [count_1, count_2]

# def winner(result, players_list):
#     if result[0] == 1:
#         print(f'Победитель - {players_list[0]}!')
#     else:
#         print(f'Победитель - {players_list[1]}!')

# sum = 2021
# rate = 28
# players_list = initial()
# human_or_bot(players_list)
# if human_or_bot(players_list) == 0:
#     result = game_human(players_list, sum, rate)
# else:
#     result = game_bot (players_list, sum, rate)
# winner(result, players_list)

# 3. Создайте программу для игры в "Крестики-нолики".

# import random
    
# def print_matrix(matrix):
#         print('\n---------')
#         for i in matrix[:3]:
#             print(f'|{i}', end = '|')
#         print('\n---------')
#         for i in matrix[3:6]:
#             print(f'|{i}', end = '|')
#         print('\n---------')
#         for i in matrix[6:]:
#             print(f'|{i}', end = '|')
#         print('\n---------\n')

# def initial ():
#     print('\nВас приветствует игра "Крестики-нолики"!\n')
#     player_1 = input('Игрок №1, представься: ')
#     player_2 = input('Игрок №2, представься: ')
#     toss = random.randint(0,1)
#     if toss == 0:
#         print(f'Первым будет ходить {player_1}')
#         players_list = [player_1, player_2]
#     else:
#         print(f'Первым будет ходить {player_2}')
#         players_list = [player_2, player_1]
#     return players_list

# def check_winner(matrix):
#     if matrix[0] == matrix[1] == matrix[2]:
#         return True
#     elif matrix[3] == matrix[4] == matrix[5]:
#         return True
#     elif matrix[6] == matrix[7] == matrix[8]:
#         return True
#     elif matrix[0] == matrix[3] == matrix[6]:
#         return True
#     elif matrix[1] == matrix[4] == matrix[7]:
#         return True
#     elif matrix[2] == matrix[5] == matrix[8]:
#         return True
#     elif matrix[0] == matrix[4] == matrix[8]:
#         return True
#     elif matrix[2] == matrix[4] == matrix[6]:
#         return True
#     else:
#         return False


# def new_game(matrix, players_list):
#     while check_winner(matrix) == False:
#         print(f'\nТвой ход, {players_list[0]}!')
#         turn = int(input('Напиши от 1 до 9, где ставим крестик: '))
#         while (turn < 1) or (turn > 9):
#             turn = int(input(f'Нужно ввести число от 1 до 9. Попробуй ещё раз: '))
#         matrix[turn - 1] = 'X'
#         print_matrix(matrix)
#         if check_winner(matrix) == True:
#             count_1, count_2 = 1, 0
#             return [count_1, count_2]
#         print(f'\nТвой ход, {players_list[1]}!')
#         turn = int(input('Напиши от 1 до 9, где ставим нолик: '))
#         while (turn < 1) or (turn > 9):
#             turn = int(input(f'Нужно ввести число от 1 до 9. Попробуй ещё раз: '))
#         matrix[turn - 1] = '0'
#         print_matrix(matrix)
#         if check_winner(matrix) == True:
#             count_1, count_2 = 0, 1
#             return [count_1, count_2]

# def winner(result, players_list):
#     if result[0] == 1:
#         print(f'Победитель - {players_list[0]}!')
#     else:
#         print(f'Победитель - {players_list[1]}!')

# matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print_matrix(matrix)
# players_list = initial()
# result = new_game(matrix, players_list)
# winner(result, players_list)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def compression(new_str):
#     result = ''
#     current = ''
#     count = 1
#     for item in new_str:
#         if item != current:
#             if current:
#                 result += str(count) + current
#             count = 1
#             current = item
#         else:
#             count += 1
#     return result

# def decompression(compress_file):
#     count = 1
#     result = ''
#     for item in compress_file:
#         if item.isdigit():
#             count = int(item) 
#         else:
#             result += item * int(count)
#             count = ''
#     return result

# with open('rle_file.txt', 'r') as f:
#     f.seek(0)
#     new_str = f.read()
# print(new_str)

# compress_file = compression(new_str)
# print(compress_file)
# decompress_file = decompression(compress_file)
# print(decompress_file)

# with open('rle_decompress.txt', 'w') as f:
#     f.write(decompress_file)