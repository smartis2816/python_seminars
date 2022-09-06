
# Задача №1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day_of_week = int(input('Введите номер дня недели от 1 до 7: '))

# while day_of_week > 7 or day_of_week < 1:
#     day_of_week = int(input('Некорректное число. Введите ещё раз: '))

# if day_of_week < 6 and day_of_week > 0:
#     print('Заданный день является будним днём')
# else:
#     print('Заданный день является выходным')


# Задача №2
# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def checking_validity (x, y, z):
#     if not (x or y or z) == (not x and not y and not z):
#         print(f'Выражение ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - истинно')

# checking_validity(0, 0, 0)
# checking_validity(0, 0, 1)
# checking_validity(0, 1, 0)
# checking_validity(0, 1, 1)
# checking_validity(1, 0, 0)
# checking_validity(1, 0, 1)
# checking_validity(1, 1, 0)
# checking_validity(1, 1, 1)

# Задача №3
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = float(input('Введите координату точки по оси x, не равные 0: '))
# y = float(input('Введите координату точки по оси y, не равные 0: '))
# while x == 0:
#     x = int(input('x не должен быть равен 0. Введите корординату ещё раз: '))
# while y == 0:
#     y = int(input('y не должен быть равен 0. Введите корординату ещё раз: '))

# def find_quarter_number(x, y):
#     if x > 0 and y > 0:
#         return 1
#     elif x < 0 and y > 0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     elif x > 0 and y < 0:
#         return 4

# print(f'Номер четверти плоскости по заданным координатам - {find_quarter_number (x, y)}')

# Задача №4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

# def input_and_validation ():
#     num = int(input('Введите номер четверти от 1 до 4: '))
#     while num > 4 or num < 1:
#         num = int(input('Неверный ввод. Номер четверти должен быть от 1 до 4. Введите ещё раз: '))
#     return num

# quarter_number = input_and_validation()

# def coordinate_range (num):
#     if num == 1:
#         print(f'Для четверти {num}:\nx -> от 0 до +∞\ny -> от 0 до +∞')
#     elif num == 2:
#         print(f'Для четверти {num}:\nx -> от 0 до -∞\ny -> от 0 до +∞')
#     elif num == 3:
#         print(f'Для четверти {num}:\nx -> от 0 до -∞\ny -> от 0 до -∞')
#     elif num == 4:
#         print(f'Для четверти {num}:\nx -> от 0 до +∞\ny -> от 0 до -∞')

# coordinate_range(quarter_number)

# Задача №5
# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# xa = float(input('Введите координату первой точки по оси x: '))
# ya = float(input('Введите координату первой точки по оси y: '))
# xb = float(input('Введите координату второй точки по оси x: '))
# yb = float(input('Введите координату второй точки по оси y: '))

# def find_distance (xa, ya, xb, yb):
#     distance = ((xb - xa)**2 + (yb - ya)**2) ** 0.5
#     distance = round (distance, 2)
#     return distance

# print(f'Расстояние между заданными координатами составляет {find_distance (xa, ya, xb, yb)}')