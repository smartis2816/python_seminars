
# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# new_list = input('Введите числа через пробел: ').split()
# print(new_list)
# new_list = list(map(int, new_list))
# print(new_list)
# print(min(new_list), max(new_list))

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#  1) с помощью математических формул нахождения корней квадратного уравнения
# *2) с помощью дополнительных библиотек Python

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))

# descriminant = (b**2) - (4 * a * c)

# if descriminant < 0:
#     print('корней нет')
# elif descriminant == 0:
#     res = (-b / (2*a))
#     print(f'есть ровно один корень: {res}')
# elif descriminant > 0:
#     res1 = (-b + (descriminant**0.5))/(2 * a)
#     res2 = (-b - (descriminant**0.5))/(2 * a)
#     print(f'корней будет два: {res1, res2}')

# 3. Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.

# Первый вариант решения
# a = 5
# b = 10
# count = a * b
# while a != b: # Выход из цикла при равенстве a и b
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(count / b)

# Второй вариант решения
# import math
# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# print(math.lcm(a, b))

# with open('file.txt', 'w') as f:
#     f.write(str(math.lcm(a, b)))


