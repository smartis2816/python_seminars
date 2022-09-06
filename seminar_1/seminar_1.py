# Задача №1
# Принять на вход 2 числа и проверить, является ли одно число квадратом другого.

# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# Первый вариант решения (более длинный)
# print(type(num_1))
# if num_2 == (num_1 * num_1): # или такая запись if num_2 == (num_1 ** 2):
#     print(True)
# elif num_1 == (num_2 * num_2):
#     print(True)
# else:   # Блок else не обязателен
#     print(False)

# Второй вариант решения (короткий)
# if (num_2 == (num_1 ** 2)) or (num_1 == (num_2 ** 2)):
#     print(True)
# else:
#     print(False)

# Задача №2
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# range(5) -> [0, 1, 2, 3, 4]
# range(5, 16) -> [5, 6, 7, ... 16]
# range(1, 11, 2) -> [1, 3, 4, 7, 9]
# my_list = [] # или my_list = list()
# for i in range(5):
#     num = int(input('--> '))
#     my_list.append(num)
# print(my_list)

# Нахождение максимального в списке
# my_list = [3, 5, 1, 2, 8]
# maxx = my_list[0]
# for item in my_list[1:]:
#     if item > maxx:
#         maxx = item

# print(maxx)

# Нахождение индекса максимального числа в списке
# my_list = [3, 5, 1, 2, 8]
# maxx = my_list[0]
# for i in range(1, len(my_list)):
#     if my_list[i] > maxx:
#         maxx = i

# print(maxx)

# Задача №3
# Напишите программу, которая будет на вход принимать число N и 
# выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input('Введите число N: '))

# for i in range(-N, N + 1):
    # print(i, end = ' ') # или print(f'* {i} *')

# Задача №4
# Напишите программу, которая будет принимать на вход дробь и 
# показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# Решение через строки
# num = input('Введите дробное число: ')
# print(num.split('.')[1][0])

# Решение через числа
# num = input('Введите дробное число: ')
# num *= 10
# num = int(num)
# print(num % 10)

# Задача №5
# Напишите программу, которая принимает на вход число и 
# проверяет, кратно ли оно (5 и 10) или (15, но не 30)

# num = int(input('Введите целое число: '))

# if num % 5 == 0 and num % 10 == 0:
#     print(True)
# elif num % 15 == 0 and num % 30 != 0:
#     print(True)
# else:
#     print(False)