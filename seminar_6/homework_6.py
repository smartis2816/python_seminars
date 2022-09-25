
# Задача №1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# num = input('Введите вещественное число: ').split('.')
# num = map(int, num[0] + num[1])
# res = sum([item for item in num])
# print(f'Сумма цифр введённого ччисла - {res}')

# Задача №2
# Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

# def fill_list():
#     new_list = input('Введите несколько чисел через пробел: ').split()
#     new_list = list(map(int, new_list))
#     return new_list

# def find_sum(new_list):
#     res = sum(new_list[i] for i in range(1, len(new_list), 2))
#     return res

# new_list = fill_list()
# print(find_sum(new_list))

# Задача №3
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def fill_list_2():
#     my_list = [int(item) for item in (input('Введите числа через пробел: ').split())]
#     print(my_list)
#     return my_list

# def product_of_numbers(list):
#     result = [(list[i] * list[(i + 1) * (-1)]) for i in range((len(list) // 2) + (len(list) % 2))]
#     print(result)

# new_list = fill_list_2()
# product_of_numbers(new_list)

# Задача №4
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# def fill_list_3():
#     my_list = [float(item) for item in (input('Введите дробные числа через пробел: ').split())]
#     print(f'Оригинальный список - {my_list}')
#     return my_list

# def select_fractional_part (list):
#     list = [round((list[i] % 1), 2) for i in range(0, len(list))]
#     print(f'Список с выделенными дробными частями - {list}')
#     return list

# def difference_max_min (list):
#     list.sort()
#     res = list[-1] - list[0]
#     print(f'Разница между максимальным и минимальным значением дробной части - {res}')
#     return res

# original_list = fill_list_3()
# original_list = select_fractional_part(original_list)
# difference_max_min(original_list)

# Задача №5
# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму

# import math
# k = int(input('Введите число k: '))
# sum = math.fsum([((1 + 1/i) ** i) for i in range(1, k + 1)])
# print(f'Сумма чисел последовательности: {round(sum, 2)}')