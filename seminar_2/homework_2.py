
# Задача №1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# num = input('Введите вещественное число: ')
# new_list = num.split('.')
# print(f'Список строк после разделения строки по "." - {new_list}')
# new_list = list(map(int, new_list))
# print(f'Список чисел после преобразования строк в числа - {new_list}')
# a = new_list[0]
# b = new_list[1]
# if a < 0:
#     a *= (-1)

# sum = 0
# while a != 0:
#     sum += (a % 10)
#     a //= 10
# while b != 0:
#     sum += (b % 10)
#     b //= 10
# print(f'Суума цифр введённого числа равна {sum}')

# Задача №2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def set_of_products (n):
#     count = 1
#     result = 1
#     new_list = list()
#     while count <= N:
#         new_list.append(result)
#         result *= (count + 1)
#         count += 1
#     print(new_list)

# N = int(input('Введите целое число: '))    
# set_of_products(N)

# Задача №3
# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму

# k = int(input('Введите число k: '))
# sum = 0
# new_list = list()

# for i in range(1, k + 1):
#     result = ((1 + 1/i) ** i)
#     new_list.append(result)

# print(f'Список чисел, полученных в ходе итераций: {new_list}')

# for i in new_list:
#     sum += float(i)

# print(f'Сумма чисел последовательности: {round(sum, 2)}')

# Задача №4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# N = int(input('Введите число N: '))
# new_list = []
# count = 0
# import random
# while count != N:
#     new_list.append(random.randint(-N, N))
#     count += 1
# print(f'Список рандомных чисел в диапазоне от -N до N - {new_list}')

# positions = input('Введите через пробел номера позиций элементов для нахождения произведения: ')
# positions_list = positions.split(' ')
# positions_list = list(map(int, positions_list))
# print(f'Список позиций - {positions_list}')
# product_of_numbers = 1
# for i in range(0, len(positions_list)):
#     for j in range(0, len(new_list)):
#         if positions_list[i] == j:
#             product_of_numbers *= new_list[j]

# print(f'Произведение - {product_of_numbers}')

# Задача №5
# Реализуйте алгоритм перемешивания списка.

# new_list = input('Введите список данных через пробел: ').split()
# print(f'Оригинальный список - {new_list}')
# temp = 0
# import random

# for i in range(0, len(new_list)):
#     j = random.randint(0, len(new_list) - 1)
#     temp = new_list[i]
#     new_list[i] = new_list[j]
#     new_list[j] = temp

# print(f'Перемешанный список - {new_list}')
